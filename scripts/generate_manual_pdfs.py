#!/usr/bin/env python3
"""Pre-generate downloadable PDFs for manual pages from a built mkdocs site.

Renders each Manuals page through Chromium's print pipeline (honours the
site's @media print rules), then post-processes and quality-checks the result:

  render (eager images, footer w/ page numbers) -> rewrite localhost links ->
  set metadata -> image recompression (300dpi cap) -> quality gate ->
  write X.pdf next to X.html + update pdf-manifest.json

Incremental: a fingerprint of (source md + sibling images listing + print CSS
+ this script) is stored in the manifest; unchanged pages whose PDF already
exists are skipped.

Usage:
    python scripts/generate_manual_pdfs.py --site-dir site --lang zh \
        [--only ER805] [--channel msedge]

Deps: playwright (chromium or msedge channel), pymupdf.
"""
from __future__ import annotations

import argparse
import datetime
import hashlib
from html import escape as html_escape
import http.server
import json
import socket
import sys
import threading
import urllib.parse
import urllib.request
from pathlib import Path

import fitz  # pymupdf
from playwright.sync_api import sync_playwright

SCRIPT_VERSION = "3"  # bump to force full regeneration on behavior changes

SIZE_MIN = 50 * 1024
SIZE_MAX = 30 * 1024 * 1024

PROD_BASES = {
    "zh": "https://www.inhand.com.cn/manuals/",
    "en": "https://www.inhand.com/manuals/",
}

FOOTER = (
    '<div style="width:100%;font-size:8px;color:#888;'
    'padding:0 10mm;display:flex;justify-content:space-between;">'
    "<span>{title}</span>"
    "<span>© InHand Networks · {site} · {date}</span>"
    '<span><span class="pageNumber"></span> / <span class="totalPages"></span></span>'
    "</div>"
)

EAGER_IMAGES_JS = """
async () => {
  const imgs = Array.from(document.images);
  imgs.forEach(i => { i.loading = 'eager'; });
  await Promise.all(imgs.map(i => i.complete ? null :
    new Promise(r => { i.onload = i.onerror = r; })));
  return imgs.length;
}
"""


def log(msg: str) -> None:
    print(msg, flush=True)


def find_manual_pages(site_dir: Path, only: str | None) -> list[Path]:
    pages = sorted(
        p for p in site_dir.rglob("*.html")
        if "/Manuals/" in p.relative_to(site_dir).as_posix()
        # generated product-index navigation stubs are not manuals
        and p.name.lower() != "index.html"
    )
    if only:
        needle = only.lower()
        pages = [p for p in pages if needle in p.relative_to(site_dir).as_posix().lower()]
    return pages


def fingerprint(site_dir: Path, page: Path, docs_dir: Path, extra: list[Path]) -> str:
    """Hash of the page's markdown source, sibling images and shared assets."""
    h = hashlib.sha256()
    h.update(SCRIPT_VERSION.encode())
    rel = page.relative_to(site_dir).with_suffix(".md")
    src = docs_dir / rel
    if src.is_file():
        h.update(src.read_bytes())
    img_dir = src.parent / "images"
    if img_dir.is_dir():
        for f in sorted(img_dir.iterdir()):
            h.update(f.name.encode())
            h.update(str(f.stat().st_size).encode())
    for f in extra:
        if f.is_file():
            h.update(f.read_bytes())
    return h.hexdigest()


def serve(site_dir: Path) -> tuple[http.server.ThreadingHTTPServer, int]:
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        port = s.getsockname()[1]
    handler = lambda *a, **kw: http.server.SimpleHTTPRequestHandler(  # noqa: E731
        *a, directory=str(site_dir), **kw)
    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", port), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd, port


def rewrite_links_and_meta(pdf_path: Path, local_base: str, prod_base: str,
                           title: str) -> None:
    """Rewrite localhost URI links to the production URL and set metadata.

    Note: same-document anchor links need no handling — tagged PDF generation
    already emits them as internal named destinations (verified: they jump
    within the PDF). Only cross-document/external links are URI actions.
    """
    doc = fitz.open(pdf_path)
    for pno in range(doc.page_count):
        page = doc[pno]
        for link in page.get_links():
            uri = link.get("uri") or ""
            if uri.startswith(local_base):
                link["uri"] = uri.replace(local_base, prod_base, 1)
                page.update_link(link)
    doc.set_metadata({"title": title, "author": "InHand Networks",
                      "producer": "InHand docs pipeline"})
    tmp = pdf_path.with_suffix(".tmp.pdf")
    doc.save(tmp, garbage=2, deflate=True)
    doc.close()
    tmp.replace(pdf_path)


def compress(pdf_path: Path) -> None:
    """Re-encode embedded images (JPEG q85, ~300dpi cap) to shrink the file.

    Replaces the earlier ghostscript /ebook pass: its 150dpi downsampling
    made small text in full-width UI screenshots illegible. pymupdf keeps
    the effective resolution while roughly halving the size.
    """
    tmp = pdf_path.with_suffix(".cmp.pdf")
    try:
        doc = fitz.open(pdf_path)
        doc.rewrite_images(dpi_threshold=301, dpi_target=300, quality=85)
        doc.save(tmp, garbage=2, deflate=True)
        doc.close()
    except Exception as exc:  # noqa: BLE001 - keep the uncompressed original
        log(f"  [compress] skipped ({exc.__class__.__name__}: {exc})")
        tmp.unlink(missing_ok=True)
        return
    if tmp.is_file() and 0 < tmp.stat().st_size < pdf_path.stat().st_size:
        tmp.replace(pdf_path)
    else:
        tmp.unlink(missing_ok=True)


def quality_gate(pdf_path: Path) -> list[str]:
    problems: list[str] = []
    size = pdf_path.stat().st_size
    if not SIZE_MIN <= size <= SIZE_MAX:
        problems.append(f"size {size/1048576:.1f}MB outside [{SIZE_MIN//1024}KB, {SIZE_MAX//1048576}MB]")
    doc = fitz.open(pdf_path)
    if doc.page_count == 0:
        problems.append("0 pages")
    for pno in range(doc.page_count):
        page = doc[pno]
        for b in page.get_text("blocks"):
            if b[2] > page.rect.width + 1:
                problems.append(f"page {pno+1}: text overflows right edge ({b[4][:30]!r})")
                break
    # first page must not be blank (cover regression check)
    pix = doc[0].get_pixmap(dpi=36)
    samples = pix.samples
    if len(set(samples[:: max(1, len(samples)//5000)])) <= 2:
        problems.append("first page looks blank")
    doc.close()
    return problems


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--site-dir", required=True, type=Path)
    ap.add_argument("--lang", required=True, choices=("zh", "en"))
    ap.add_argument("--only", help="substring filter on page path")
    ap.add_argument("--channel", default="", help="browser channel, e.g. msedge")
    ap.add_argument("--force", action="store_true", help="ignore manifest, regenerate")
    ap.add_argument("--reuse-base", default="",
                    help="deployed site base URL; unchanged PDFs are downloaded "
                         "from there instead of re-rendered (prod as cache)")
    args = ap.parse_args()

    site_dir = args.site_dir.resolve()
    docs_dir = Path("docs") / args.lang
    prod_base = PROD_BASES[args.lang]
    shared_assets = [
        docs_dir / "stylesheets" / "extra-v2.css",
        Path(__file__),
    ]

    pages = find_manual_pages(site_dir, args.only)
    if not pages:
        log("no manual pages matched")
        return 1
    log(f"{len(pages)} manual page(s) to consider")

    manifest_path = site_dir / "pdf-manifest.json"
    manifest: dict[str, str] = {}
    if manifest_path.is_file():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    reuse_base = args.reuse_base.rstrip("/") + "/" if args.reuse_base else ""
    if reuse_base and not manifest and not args.force:
        try:
            with urllib.request.urlopen(reuse_base + "pdf-manifest.json",
                                        timeout=30) as r:
                manifest = json.loads(r.read().decode("utf-8"))
            log(f"reuse manifest from {reuse_base}: {len(manifest)} entries")
        except Exception as exc:  # noqa: BLE001 - any failure => full generation
            log(f"no reusable manifest ({exc.__class__.__name__}); generating all")

    httpd, port = serve(site_dir)
    local_base = f"http://127.0.0.1:{port}/"
    failures: list[str] = []
    generated = skipped = 0

    with sync_playwright() as p:
        browser = p.chromium.launch(
            channel=args.channel or None, headless=True)
        page = browser.new_page()
        for html in pages:
            rel = html.relative_to(site_dir).as_posix()
            pdf_path = html.with_suffix(".pdf")
            fp = fingerprint(site_dir, html, docs_dir, shared_assets)
            if not args.force and manifest.get(rel) == fp:
                if pdf_path.is_file():
                    skipped += 1
                    continue
                if reuse_base:
                    # fingerprint unchanged: pull the deployed PDF instead of
                    # re-rendering. Magic-byte check guards against the
                    # WordPress 200-HTML fallback for unknown paths.
                    try:
                        with urllib.request.urlopen(
                                reuse_base + urllib.parse.quote(
                                    rel[:-5] + ".pdf"), timeout=60) as r:
                            data = r.read()
                        if data.startswith(b"%PDF"):
                            pdf_path.write_bytes(data)
                            skipped += 1
                            log(f"reuse {rel} ({len(data)/1048576:.1f}MB)")
                            continue
                    except Exception:  # noqa: BLE001 - fall through to render
                        pass
            url = local_base + urllib.parse.quote(rel)
            log(f"render {rel}")
            page.goto(url, wait_until="networkidle", timeout=120_000)
            n_imgs = page.evaluate(EAGER_IMAGES_JS)
            # strip the " - site name" suffix mkdocs appends to <title>
            title = page.title().split(" - ")[0].strip()
            page.pdf(
                path=str(pdf_path), format="A4", print_background=True,
                outline=True, tagged=True,
                display_header_footer=True, header_template="<span></span>",
                footer_template=FOOTER.format(
                    title=html_escape(title),
                    site=prod_base.split("//")[1].rstrip("/"),
                    date=datetime.date.today().isoformat()),
                margin={"top": "14mm", "bottom": "16mm",
                        "left": "10mm", "right": "10mm"},
            )
            rewrite_links_and_meta(pdf_path, local_base, prod_base, title)
            compress(pdf_path)
            problems = quality_gate(pdf_path)
            if problems:
                failures.append(f"{rel}: " + "; ".join(problems))
                log(f"  FAIL {problems}")
                continue
            manifest[rel] = fp
            generated += 1
            log(f"  ok: {pdf_path.stat().st_size/1048576:.1f}MB, images={n_imgs}")
        browser.close()
    httpd.shutdown()

    # prune entries for pages that no longer exist (renamed/removed manuals),
    # otherwise the manifest accumulates stale keys forever
    current = {p.relative_to(site_dir).as_posix() for p in
               find_manual_pages(site_dir, None)}
    manifest = {k: v for k, v in manifest.items() if k in current}
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=1, sort_keys=True),
        encoding="utf-8", newline="\n")
    log(f"done: {generated} generated, {skipped} up-to-date, {len(failures)} failed")
    if failures:
        log("FAILURES:")
        for f in failures:
            log("  " + f)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
