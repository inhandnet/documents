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


def derive_doc_type(category: str, subcategory: str, filename: str) -> str:
    """Human-ish document type label from path segments."""
    if subcategory and subcategory.lower() != "general":
        return subcategory
    if category:
        return category.rstrip("s") if category.endswith("s") else category
    return "Document"


def parse_version(filename: str) -> str | None:
    m = re.search(r"[_\-]?[Vv](\d+(?:\.\d+)*)", filename)
    return m.group(1) if m else None


class Doc:
    __slots__ = ("product", "category", "subcategory", "title",
                 "description", "link", "sort_key")

    def __init__(self, product, category, subcategory, title, description, link):
        self.product = product
        self.category = category
        self.subcategory = subcategory
        self.title = title
        self.description = description
        self.link = link


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
        out = subprocess.run(
            ["git", "-C", str(REPO_ROOT), "ls-files", "-z", "--", f"{rel_root}/**/*.md"],
            capture_output=True, check=True,
        ).stdout.decode("utf-8")
        paths = [REPO_ROOT / p for p in out.split("\0") if p]
        if paths:
            return sorted(paths)
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass
    return sorted(lang_root.rglob("*.md"))


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

        doc_type = fm.get("doc_type") or derive_doc_type(category, subcategory, md.name)
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

        description = clean_oneline(fm["description"]) if fm.get("description") else synthesized

        rel_posix = rel.as_posix()
        link = (base_url.rstrip("/") + "/" + rel_posix) if base_url else rel_posix

        docs.append(Doc(product, category, subcategory, title, description, link))
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
            lines.append(f"- [{d.title}]({d.link}): {d.description}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description="Generate llms.txt index files.")
    ap.add_argument("--lang", choices=["en", "zh"], action="append",
                    help="Limit to given language(s); default both.")
    ap.add_argument("--base-url", default=None,
                    help="Emit absolute web URLs under this base instead of "
                         "language-root-relative paths.")
    ap.add_argument("--check", action="store_true",
                    help="Do not write; exit non-zero if any llms.txt is stale.")
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

    if args.check and stale:
        print("llms.txt is out of date; run scripts/generate_llms_txt.py",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
