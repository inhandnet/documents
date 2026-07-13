#!/usr/bin/env python3
"""Generate llms.txt index files for the documentation site.

Produces one machine-readable index per language:
  docs/en/llms.txt
  docs/zh/llms.txt

Following the llms.txt convention (https://llmstxt.org/): a curated, grouped
list of `- [title](path): description` entries so LLMs / RAG pipelines can
discover every document without crawling the whole tree.

Design notes
------------
- Standard library only.  No new dependency, no change to requirements.txt,
  so it cannot affect the existing CI build environment.
- Fully derived from repo content; never hand-edited.  Re-running is
  idempotent and deterministic (sorted output → minimal diffs).
- Per-document metadata resolution order:
    title       : frontmatter `title` -> first H1 -> filename
    description : frontmatter `description` -> synthesized "{Product} {DocType}"
  (The first paragraph is intentionally NOT used: it is usually copyright /
  "Declaration" boilerplate.  A good description should be authored in the
  source repo's frontmatter; this script fills a clean fallback until then.)
- Links are paths relative to the language root (i.e. relative to the
  generated llms.txt itself), so they resolve for a repo reader.  Pass
  --base-url to emit absolute web URLs instead.

Usage
-----
    python scripts/generate_llms_txt.py                 # writes both langs
    python scripts/generate_llms_txt.py --lang en
    python scripts/generate_llms_txt.py --check         # non-zero exit if stale
    python scripts/generate_llms_txt.py --base-url https://inhand.com/en/
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import quote

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = REPO_ROOT / "docs"

LANG_TITLES = {
    "en": "InHand Product Documentation",
    "zh": "映翰通产品文档",
}
LANG_INTRO = {
    "en": (
        "Machine-readable index of InHand Networks product documentation, "
        "grouped by product. Each entry links to a document with a one-line "
        "description. Generated automatically from docs/en — do not edit by hand."
    ),
    "zh": (
        "映翰通产品文档的机器可读索引，按产品分组。每条指向一篇文档并附一句话描述。"
        "由 docs/zh 自动生成，请勿手工编辑。"
    ),
}

# Category display order (anything else sorts alphabetically after these).
CATEGORY_ORDER = [
    "Manuals",
    "Developer Documentation",
    "Solutions",
    "Datasheets",
]

# Files that are not real content documents.
SKIP_FILENAMES = {"index.md"}


def split_frontmatter(text: str) -> tuple[dict, str]:
    """Return (frontmatter_dict, body). Only simple `key: value` pairs parsed."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    block = text[3:end]
    rest_start = text.find("\n", end + 1)
    body = text[rest_start + 1:] if rest_start != -1 else ""
    fm: dict = {}
    for line in block.splitlines():
        if ":" not in line or line.lstrip().startswith("#"):
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and value:
            fm[key] = value
    return fm, body


def first_h1(body: str) -> str | None:
    for line in body.splitlines():
        m = re.match(r"^#\s+(.*\S)\s*$", line)
        if m:
            return m.group(1).strip()
    return None


def clean_oneline(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)          # strip HTML tags
    text = re.sub(r"\s+", " ", text).strip()
    return text


# Generic section headings that are NOT usable document titles.
_GENERIC_TITLES = {
    "product overview", "overview", "introduction", "declaration",
    "产品概述", "概述", "简介", "声明", "目录",
}


def looks_like_section_heading(title: str) -> bool:
    """True if the H1 is a numbered/generic section, not a document title."""
    if re.match(r"^\d+(\.\d+)*[.、\s]", title):   # "1. ...", "1.2 ...", "1、..."
        return True
    return title.strip().lower() in _GENERIC_TITLES


# Subcategory names that carry no type information ("General" folders).
_GENERIC_SUBCATEGORIES = {"general", "通用"}

# Category directory names are English even in the zh tree — localize the
# fallback label for zh readers.
_ZH_CATEGORY_LABELS = {
    "Manuals": "手册",
    "Datasheets": "规格书",
    "Developer Documentation": "开发文档",
    "Solutions": "解决方案",
}


def derive_doc_type(category: str, subcategory: str, filename: str,
                    lang: str = "en") -> str:
    """Human-ish document type label from path segments."""
    if subcategory and subcategory.lower() not in _GENERIC_SUBCATEGORIES:
        return subcategory
    if category:
        if lang == "zh" and category in _ZH_CATEGORY_LABELS:
            return _ZH_CATEGORY_LABELS[category]
        return category.rstrip("s") if category.endswith("s") else category
    return "Document" if lang == "en" else "文档"


def parse_version(filename: str) -> str | None:
    m = re.search(r"[_\-]?[Vv](\d+(?:\.\d+)*)", filename)
    return m.group(1) if m else None


# --- Body-derived description fallback (until source frontmatter arrives) ---

# Lines that mark copyright / declaration boilerplate, not real content.
_BOILERPLATE_RE = re.compile(
    r"声明|版权|保留一切权利|保留所有权利|商标|著作权|恕不提前通知"
    r"|更改权|解释权|不承担|争议"
    r"|declaration|copyright|all rights reserved|trademark|disclaimer",
    re.IGNORECASE,
)

# Description may only be taken from an intro-like section (or text before
# any heading).  A keyword blocklist alone is whack-a-mole: legal boilerplate
# is endlessly creative.
_INTRO_HEADINGS_RE = re.compile(
    r"^(产品概述|概述|简介|产品简介|产品介绍|功能特点"
    r"|overview|introduction|product overview|about)\s*$",
    re.IGNORECASE,
)


def first_meaningful_paragraph(body: str, max_len: int = 120) -> str | None:
    """First substantive prose paragraph from an intro-like section.

    Whitelist strategy: only text appearing before any heading, or under a
    heading like 概述/简介/Overview/Introduction, qualifies. Returns None
    when the document has no such prose (caller falls back to a synthesized
    description) — a missing description beats a wrong one.
    """
    in_intro = True  # text before the first heading counts as intro
    checked = 0
    for raw in body.splitlines():
        line = raw.strip()
        if not line:
            continue
        m = re.match(r"^#{1,6}\s+(.*\S)\s*$", line)
        if m:
            heading = re.sub(r"^\d+(\.\d+)*[.、\s]+", "", clean_oneline(m.group(1)))
            in_intro = bool(_INTRO_HEADINGS_RE.match(heading))
            continue
        if not in_intro:
            continue
        checked += 1
        if checked > 40:  # don't fish for prose deep inside the document
            return None
        if line.startswith(("|", ">", "!", "<", "-", "*", "```", "[")):
            continue
        text = clean_oneline(line)
        if len(text) < 20 or _BOILERPLATE_RE.search(text):
            continue
        return text[:max_len].rstrip() + ("…" if len(text) > max_len else "")
    return None


# --- Section deep links for long documents (llms.txt §6.5 plan B) ---

SECTION_BODY_THRESHOLD = 50_000   # only documents larger than this get anchors
SECTION_MAX = 15                  # cap per document to keep the index lean

# H2 headings that are boilerplate, not navigable content chapters.
_SECTION_SKIP_RE = re.compile(
    r"^(声明|版权.*|技术支持|图形界面约定|如何使用本手册|前置信息|目录|前言|修订历史"
    r"|declaration|copyright.*|technical support|conventions?"
    r"|revision history|preface|table of contents)\s*$",
    re.IGNORECASE,
)


def slugify(text: str) -> str:
    """Approximation of pymdownx uslugify (mkdocs toc anchors): lowercase,
    punctuation dropped, whitespace to dashes, CJK preserved."""
    t = text.strip().lower()
    t = re.sub(r"[^\w一-鿿\- ]", "", t, flags=re.UNICODE)
    return re.sub(r"\s+", "-", t).strip("-")


def extract_sections(body: str) -> list[tuple[str, str]]:
    """(heading, anchor) pairs for content H2 headings of a long document."""
    if len(body) < SECTION_BODY_THRESHOLD:
        return []
    sections: list[tuple[str, str]] = []
    for m in re.finditer(r"^##\s+(.+?)\s*$", body, flags=re.MULTILINE):
        heading = clean_oneline(m.group(1))
        if not heading or _SECTION_SKIP_RE.match(heading):
            continue
        sections.append((heading, slugify(heading)))
        if len(sections) >= SECTION_MAX:
            break
    return sections


class Doc:
    __slots__ = ("product", "category", "subcategory", "title",
                 "description", "link", "sections", "body")

    def __init__(self, product, category, subcategory, title, description,
                 link, sections=None, body=""):
        self.product = product
        self.category = category
        self.subcategory = subcategory
        self.title = title
        self.description = description
        self.link = link
        self.sections = sections or []
        self.body = body


def list_markdown_files(lang_root: Path) -> list[Path]:
    """Enumerate *.md via the git index, falling back to the filesystem.

    The git index is the source of truth for paths: the repo contains
    directories differing only by case (e.g. "MO 62A" vs "Mo 62A"), which a
    case-insensitive filesystem (Windows) merges into one folder.  Scanning
    the filesystem there yields paths that do not exist in the repo / on the
    Linux-built site.
    """
    rel_root = lang_root.relative_to(REPO_ROOT).as_posix()
    try:
        # --others --exclude-standard: also include freshly generated,
        # not-yet-committed pages (e.g. asset registry pages in CI),
        # while still honoring .gitignore.
        out = subprocess.run(
            ["git", "-C", str(REPO_ROOT), "ls-files", "-z", "--cached",
             "--others", "--exclude-standard", "--", f"{rel_root}/**/*.md"],
            capture_output=True, check=True,
        ).stdout.decode("utf-8")
        paths = [REPO_ROOT / p for p in out.split("\0") if p]
        if paths:
            # Sort by posix string: Windows Path comparison is
            # case-insensitive and would order case-variant dirs
            # differently than CI (Linux).
            return sorted(paths, key=Path.as_posix)
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass
    return sorted(lang_root.rglob("*.md"), key=Path.as_posix)


def collect(lang: str, base_url: str | None) -> list[Doc]:
    lang_root = DOCS_DIR / lang
    docs: list[Doc] = []
    for md in list_markdown_files(lang_root):
        if md.name in SKIP_FILENAMES:
            continue
        rel = md.relative_to(lang_root)
        parts = rel.parts  # e.g. (Product, Category, Subcategory, file.md)
        if len(parts) < 2:
            continue  # top-level stray file, not a product doc
        product = parts[0]
        category = parts[1] if len(parts) >= 3 else ""
        subcategory = parts[2] if len(parts) >= 4 else ""

        try:
            text = md.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            text = md.read_text(encoding="utf-8", errors="replace")
        fm, body = split_frontmatter(text)

        doc_type = fm.get("doc_type") or derive_doc_type(category, subcategory,
                                                         md.name, lang)
        version = fm.get("version") or parse_version(md.name)

        synthesized = f"{product} {doc_type}"
        if version:
            synthesized += f" v{version}"

        if fm.get("title"):
            title = clean_oneline(fm["title"])
        else:
            h1 = first_h1(body)
            h1 = clean_oneline(h1) if h1 else None
            # A numbered/generic section heading is not a real title -> synthesize.
            title = h1 if (h1 and not looks_like_section_heading(h1)) else synthesized

        # description: frontmatter > first substantive paragraph > synthesized
        if fm.get("description"):
            description = clean_oneline(fm["description"])
        else:
            paragraph = first_meaningful_paragraph(body)
            description = f"{synthesized} — {paragraph}" if paragraph else synthesized

        rel_posix = rel.as_posix()
        link = (base_url.rstrip("/") + "/" + rel_posix) if base_url else rel_posix

        docs.append(Doc(product, category, subcategory, title, description,
                        link, sections=extract_sections(body), body=body))
    return docs


def category_rank(category: str) -> int:
    try:
        return CATEGORY_ORDER.index(category)
    except ValueError:
        return len(CATEGORY_ORDER)


def render(lang: str, docs: list[Doc]) -> str:
    lines: list[str] = []
    lines.append(f"# {LANG_TITLES.get(lang, lang)}")
    lines.append("")
    lines.append(f"> {LANG_INTRO.get(lang, '')}")
    lines.append("")

    products = sorted({d.product for d in docs})
    for product in products:
        group = [d for d in docs if d.product == product]
        group.sort(key=lambda d: (category_rank(d.category), d.category,
                                   d.subcategory, d.title))
        lines.append(f"## {product}")
        lines.append("")
        for d in group:
            # Percent-encode: spaces/CJK in raw paths break CommonMark
            # link parsing (the destination ends at the first space).
            # ":" is kept for absolute --base-url links.
            link = quote(d.link, safe="/:")
            lines.append(f"- [{d.title}]({link}): {d.description}")
            # Section deep links let an agent fetch only the chapter it
            # needs instead of a whole multi-hundred-KB manual.
            for heading, anchor in d.sections:
                lines.append(f"  - [{heading}]({link}#{quote(anchor, safe='')})")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


# --- llms-full.txt: whole corpus in one file --------------------------------

_IMG_MD_RE = re.compile(r"!\[([^\]]*)\]\([^)]*\)")
_IMG_TAG_RE = re.compile(r"<img\b[^>]*?\balt=[\"']([^\"']*)[\"'][^>]*>|<img\b[^>]*>",
                         re.IGNORECASE)


def clean_body_for_full(body: str) -> str:
    """Strip images (keep alt text) — image URLs are dead weight for LLMs."""
    body = _IMG_MD_RE.sub(lambda m: f"[图片: {m.group(1)}]" if m.group(1) else "", body)
    body = _IMG_TAG_RE.sub(lambda m: f"[图片: {m.group(1)}]" if m.group(1) else "", body)
    return body.strip()


def render_full(lang: str, docs: list[Doc]) -> str:
    """Concatenate every document body, with attribution separators, in the
    same product order as llms.txt."""
    sep = "=" * 78
    parts = [f"# {LANG_TITLES.get(lang, lang)} — full text",
             "",
             f"> {LANG_INTRO.get(lang, '')}",
             ""]
    products = sorted({d.product for d in docs})
    for product in products:
        group = [d for d in docs if d.product == product]
        group.sort(key=lambda d: (category_rank(d.category), d.category,
                                   d.subcategory, d.title))
        for d in group:
            parts.append(sep)
            parts.append(f"# {d.title}")
            parts.append(f"Source: {quote(d.link, safe='/:')}")
            parts.append(sep)
            parts.append("")
            parts.append(clean_body_for_full(d.body))
            parts.append("")
    return "\n".join(parts).rstrip() + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description="Generate llms.txt index files.")
    ap.add_argument("--lang", choices=["en", "zh"], action="append",
                    help="Limit to given language(s); default both.")
    ap.add_argument("--base-url", default=None,
                    help="Emit absolute web URLs under this base instead of "
                         "language-root-relative paths.")
    ap.add_argument("--check", action="store_true",
                    help="Do not write; exit non-zero if any llms.txt is stale.")
    ap.add_argument("--full", action="store_true",
                    help="Also write llms-full.txt (whole corpus in one file; "
                         "deploy-time artifact, not committed).")
    args = ap.parse_args()

    langs = args.lang or ["en", "zh"]
    stale = False
    for lang in langs:
        lang_root = DOCS_DIR / lang
        if not lang_root.is_dir():
            print(f"skip {lang}: {lang_root} not found", file=sys.stderr)
            continue
        docs = collect(lang, args.base_url)
        content = render(lang, docs)
        out = lang_root / "llms.txt"
        if args.check:
            existing = out.read_text(encoding="utf-8") if out.exists() else ""
            if existing != content:
                stale = True
                print(f"STALE: {out.relative_to(REPO_ROOT).as_posix()}")
            continue
        # newline="\n": identical output on Windows and CI (Linux)
        out.write_text(content, encoding="utf-8", newline="\n")
        print(f"wrote {out.relative_to(REPO_ROOT).as_posix()} "
              f"({len(docs)} docs)")
        if args.full:
            # llms-full.txt is a deploy-time artifact (gitignored): 6+ MB
            # per language would bloat git history if committed.
            full_out = lang_root / "llms-full.txt"
            full_content = render_full(lang, docs)
            full_out.write_text(full_content, encoding="utf-8", newline="\n")
            print(f"wrote {full_out.relative_to(REPO_ROOT).as_posix()} "
                  f"({len(full_content) // 1024} KB)")

    if args.check and stale:
        print("llms.txt is out of date; run scripts/generate_llms_txt.py",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
