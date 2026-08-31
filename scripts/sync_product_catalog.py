#!/usr/bin/env python3
"""Keep docs/product-catalog.json in sync with the docs/{en,zh} folder tree.

The Documents MCP indexer treats docs/product-catalog.json as the single
source of truth for product identity, and refuses to build an index unless
every top-level docs/{en,zh}/<folder> is registered there (and vice versa).
Historically that registration was a manual step that people forgot, which
silently blocked new content from ever reaching the index.

This script closes that gap for the common case:

  * A new top-level folder appears under docs/en/ and/or docs/zh/  ->  a new
    catalog entry is appended automatically (kind "model", public, no
    aliases -- those still need a human).
  * A folder that used to be registered has disappeared               -> the
    script refuses to guess (that is a de-listing decision) and exits
    non-zero so a human deals with it.
  * A new folder name is not ASCII (id cannot be safely derived)       -> the
    script refuses to guess and exits non-zero so a human registers it.

It NEVER modifies or removes an existing catalog entry: aliases, kind,
public, expected_languages and display_names are human-authored and are
left byte-for-byte untouched. New entries are spliced into the JSON text
immediately before the closing of the "products" array so that a diff only
ever shows pure additions -- no reformatting noise.

Design notes
------------
- Standard library only.
- Idempotent: running twice in a row produces zero further changes.

Usage
-----
    python scripts/sync_product_catalog.py            # write new entries
    python scripts/sync_product_catalog.py --check     # report only, exit
                                                        # non-zero if a write
                                                        # would be needed
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = REPO_ROOT / "docs"
CATALOG_PATH = DOCS_DIR / "product-catalog.json"

LANGUAGES = ("en", "zh")

# Template/infrastructure directories under docs/{lang}/ that are not
# products. Kept in sync with scripts/validate_docs.py's EXCLUDED_DIRS.
EXCLUDED_DIRS = {"assets", "javascripts", "stylesheets"}

_PRODUCT_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")

TAIL = "\n  ]\n}\n"


class SyncError(Exception):
    """A situation the script deliberately refuses to auto-resolve."""


def discover_folders() -> dict[str, set[str]]:
    """Return {lang: {top-level product folder names}} for docs/{lang}/."""
    folders: dict[str, set[str]] = {}
    for lang in LANGUAGES:
        lang_root = DOCS_DIR / lang
        found = set()
        if lang_root.is_dir():
            for entry in lang_root.iterdir():
                if not entry.is_dir():
                    continue
                if entry.name.startswith("."):
                    continue
                if entry.name in EXCLUDED_DIRS:
                    continue
                found.add(entry.name)
        folders[lang] = found
    return folders


def registered_source_folders(catalog: dict) -> set[str]:
    registered: set[str] = set()
    for product in catalog["products"]:
        registered.update(product["source_folders"])
    return registered


def derive_id(folder_name: str) -> str:
    """Derive a URL-safe catalog id from a folder name.

    Rule (per project policy): collapse whitespace runs to a single hyphen,
    preserve case. Anything that still doesn't satisfy the MCP's URL-safe id
    regex is rejected -- that folder needs a human-chosen id.
    """
    candidate = re.sub(r"\s+", "-", folder_name.strip())
    if not _PRODUCT_ID.fullmatch(candidate):
        raise SyncError(
            f"cannot derive a URL-safe id from folder {folder_name!r} "
            f"(derived {candidate!r} does not match {_PRODUCT_ID.pattern!r})"
        )
    return candidate


def build_new_entry(folder_name: str, langs_present: list[str], existing_ids: set[str]) -> dict:
    if not folder_name.isascii():
        raise SyncError(
            f"folder {folder_name!r} is not ASCII; a catalog id cannot be "
            "auto-derived. Register it manually in docs/product-catalog.json "
            "(id, kind, display_names, expected_languages, aliases as needed)."
        )
    product_id = derive_id(folder_name)
    if product_id in existing_ids:
        raise SyncError(
            f"derived id {product_id!r} for new folder {folder_name!r} "
            "collides with an existing catalog id; register this folder "
            "manually with an explicit, non-colliding id."
        )
    return {
        "id": product_id,
        "kind": "model",
        "display_names": {lang: folder_name for lang in langs_present},
        "aliases": [],
        "source_folders": [folder_name],
        "expected_languages": list(langs_present),
        "public": True,
    }


def format_entry(entry: dict) -> str:
    """Render one catalog entry matching the file's existing indent style."""
    rendered = json.dumps(entry, indent=2, ensure_ascii=False)
    return "\n".join("    " + line if line else line for line in rendered.split("\n"))


def splice_entries(raw_text: str, entries: list[dict]) -> str:
    if not raw_text.endswith(TAIL):
        raise SyncError(
            "docs/product-catalog.json does not end with the expected "
            f"{TAIL!r} tail; refusing to splice to avoid corrupting the file."
        )
    idx = len(raw_text) - len(TAIL)
    body = ",\n".join(format_entry(entry) for entry in entries)
    return raw_text[:idx] + ",\n" + body + raw_text[idx:]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Report what would change without writing; exit non-zero if so.",
    )
    args = parser.parse_args()

    raw_text = CATALOG_PATH.read_text(encoding="utf-8")
    catalog = json.loads(raw_text)

    folders_by_lang = discover_folders()
    all_discovered = folders_by_lang["en"] | folders_by_lang["zh"]
    registered = registered_source_folders(catalog)

    missing = sorted(registered - all_discovered)
    new_folders = sorted(all_discovered - registered)

    problems: list[str] = []
    if missing:
        problems.append(
            "the following source folders are registered in "
            "docs/product-catalog.json but no longer exist under docs/en or "
            "docs/zh (a human must decide whether to de-list the product or "
            "restore the folder): " + ", ".join(missing)
        )

    existing_ids = {product["id"] for product in catalog["products"]}
    new_entries: list[dict] = []
    for folder_name in new_folders:
        langs_present = sorted(
            (lang for lang in LANGUAGES if folder_name in folders_by_lang[lang]),
            key=LANGUAGES.index,
        )
        try:
            entry = build_new_entry(folder_name, langs_present, existing_ids)
        except SyncError as error:
            problems.append(str(error))
            continue
        existing_ids.add(entry["id"])
        new_entries.append(entry)

    # New, cleanly-derivable folders are registered regardless of unrelated
    # problems elsewhere (e.g. a stale de-listing decision pending for some
    # other product) -- automatic registration of legitimate new content
    # must not be held hostage by an unrelated manual cleanup item. The
    # unrelated problems still make the run exit non-zero so a human sees
    # them.
    if new_entries:
        print(f"sync_product_catalog: {len(new_entries)} new product(s) to register:")
        for entry in new_entries:
            print(f"  - {entry['id']} (source_folders={entry['source_folders']!r})")

    if args.check:
        if problems or new_entries:
            if problems:
                print("sync_product_catalog: manual action required:", file=sys.stderr)
                for problem in problems:
                    print(f"  - {problem}", file=sys.stderr)
            print("sync_product_catalog: --check mode, not writing.")
            return 1
        print("sync_product_catalog: catalog already up to date; nothing to do.")
        return 0

    if new_entries:
        new_text = splice_entries(raw_text, new_entries)
        CATALOG_PATH.write_text(new_text, encoding="utf-8", newline="\n")
        print(f"sync_product_catalog: wrote {CATALOG_PATH.relative_to(REPO_ROOT).as_posix()}")
    elif not problems:
        print("sync_product_catalog: catalog already up to date; nothing to do.")

    if problems:
        print("sync_product_catalog: manual action required:", file=sys.stderr)
        for problem in problems:
            print(f"  - {problem}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
