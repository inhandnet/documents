#!/usr/bin/env python3
"""Keep docs/product-catalog.json in sync with the docs/{en,zh} folder tree.

The Documents MCP indexer treats docs/product-catalog.json as the single
source of truth for product identity. Its real validation rule (see
inhand-docs-mcp's commit_builder.py / catalog.py) is:

  * "represented folders" are derived ONLY from folders that contain at
    least one Markdown file (`list_markdown_paths`, keyed by the top-level
    docs/{lang}/<folder> segment). A folder with no Markdown at all is
    never required to be registered.
  * PDF assets are resolved independently via `catalog.for_asset(folder,
    filename)`: if the folder itself is registered, the PDF belongs to that
    product; otherwise the PDF is matched by filename against every public
    product's id/aliases/display names. A folder that is nothing but PDFs
    (a pure spec-sheet/certificate aggregation folder, e.g. shared between
    several discontinued sub-models) is legitimately never listed in
    source_folders, and registering it would be a real regression: any PDF
    inside it that happens to filename-match a *different* registered
    product would then resolve to the wrong product, because the (now
    registered-but-wrong) folder short-circuits the filename fallback.
  * There is no requirement that a registered source_folder still exist on
    disk -- content can be "represented" purely through PDF filename
    matching even when the folder that originally held it has been
    renamed/removed. Disk existence of a registered folder is therefore not
    a meaningful signal for this script; it is deliberately NOT checked.

So this script only automates the one case that both requires action and is
mechanically safe:

  * A new top-level folder appears under docs/en/ and/or docs/zh/ AND
    contains at least one Markdown file -> a new catalog entry is appended
    automatically (kind "model", public, no aliases -- those still need a
    human).
  * A new top-level folder appears but contains no Markdown (pure PDF
    aggregation, etc.) -> silently skipped. It needs no catalog entry; MCP's
    own build validation will loudly fail if a PDF genuinely can't be
    resolved, which is a content problem for a human, not something this
    script can or should guess at.
  * A new folder's name is not ASCII (id cannot be safely derived) -> the
    script refuses to guess and exits non-zero so a human registers it.

It leaves existing catalog entries byte-for-byte untouched -- kind, public,
expected_languages and display_names are human-authored -- with exactly one
exception, "alias hand-off":

  * A sub-model with no documentation of its own (e.g. ISE2003D-P) is
    registered as an *alias* of the bare model (ISE2003D). Once the content
    team gives it its own Markdown folder, it must become an independent
    product -- and the alias MUST disappear in the same catalog change,
    because MCP's catalog loader puts ids, display names, aliases and source
    folders into one global lookup table and refuses to load the catalog at
    all on a duplicate ("duplicate lookup name ..."), which silently freezes
    every index update. So when a new folder's derived id normalizes to an
    existing entry's alias, that alias is removed from that entry and the new
    independent entry is registered in the same run.

Any *other* collision (an existing entry's id, one of its display_names, or
one of its source_folders) is never auto-resolved: the script reports it and
exits non-zero so a human decides.

New entries are spliced into the JSON text immediately before the closing of
the "products" array so that a diff only ever shows pure additions plus, at
most, the one-line alias removal -- no reformatting noise.

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


def discover_markdown_folders() -> dict[str, set[str]]:
    """Return {lang: {top-level folder names containing >=1 .md file}}.

    Mirrors the MCP indexer's own notion of "represented folder": only
    folders with Markdown content need a catalog entry. Pure-PDF folders are
    excluded here on purpose (see module docstring).
    """
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
                if any(entry.rglob("*.md")):
                    found.add(entry.name)
        folders[lang] = found
    return folders


def _normalize(value: str) -> str:
    """Byte-for-byte the same normalization MCP's catalog loader uses.

    Kept identical to `_normalize` in inhand-docs-mcp's
    src/inhand_docs_mcp/catalog.py -- if these two ever diverge this script
    will happily write a catalog that MCP then refuses to load.
    """
    return " ".join(value.split()).casefold()


def build_lookup(catalog: dict) -> dict[str, list[tuple[str, str, str]]]:
    """Mirror MCP's global lookup table: normalized name -> owners.

    Each owner is (product_id, field, original_name) where field is one of
    "id", "display_name", "alias", "source_folder".
    """
    lookup: dict[str, list[tuple[str, str, str]]] = {}
    for product in catalog["products"]:
        named: list[tuple[str, str]] = [("id", product["id"])]
        named += [("display_name", value) for value in product["display_names"].values()]
        named += [("alias", alias) for alias in product["aliases"]]
        named += [("source_folder", folder) for folder in product["source_folders"]]
        for field, name in named:
            lookup.setdefault(_normalize(name), []).append((product["id"], field, name))
    return lookup


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


_FIELD_LABELS = {
    "id": "id",
    "display_name": "display_names value",
    "source_folder": "source_folders entry",
}


def build_new_entry(
    folder_name: str,
    langs_present: list[str],
    lookup: dict[str, list[tuple[str, str, str]]],
) -> tuple[dict, list[tuple[str, str]]]:
    """Plan the entry for a new folder.

    Returns (entry, alias_removals) where alias_removals is a list of
    (owner_product_id, alias) pairs that must be deleted from existing
    entries so the new entry does not collide in MCP's global lookup table.
    Raises SyncError for any collision that is not a plain alias hand-off.
    """
    if not folder_name.isascii():
        raise SyncError(
            f"folder {folder_name!r} is not ASCII; a catalog id cannot be "
            "auto-derived. Register it manually in docs/product-catalog.json "
            "(id, kind, display_names, expected_languages, aliases as needed)."
        )
    product_id = derive_id(folder_name)

    alias_removals: list[tuple[str, str]] = []
    seen_keys: set[str] = set()
    for own_field, name in (
        ("id", product_id),
        ("display_names", folder_name),
        ("source_folders", folder_name),
    ):
        key = _normalize(name)
        if key in seen_keys:
            continue
        seen_keys.add(key)
        owners = lookup.get(key, [])
        hard = [owner for owner in owners if owner[1] != "alias"]
        if hard:
            owner_id, owner_field, owner_name = hard[0]
            raise SyncError(
                f"new folder {folder_name!r} would register {own_field} "
                f"{name!r}, which collides with the {_FIELD_LABELS[owner_field]} "
                f"{owner_name!r} of existing catalog entry {owner_id!r}. MCP "
                "would refuse to load the catalog (duplicate lookup name), so "
                "this is not auto-resolved: either add this folder to "
                f"{owner_id!r}'s source_folders, or register it manually with "
                "an explicit, non-colliding id/display_names."
            )
        for owner_id, _field, alias in owners:
            if (owner_id, alias) not in alias_removals:
                alias_removals.append((owner_id, alias))

    entry = {
        "id": product_id,
        "kind": "model",
        "display_names": {lang: folder_name for lang in langs_present},
        "aliases": [],
        "source_folders": [folder_name],
        "expected_languages": list(langs_present),
        "public": True,
    }
    return entry, alias_removals


def format_entry(entry: dict) -> str:
    """Render one catalog entry matching the file's existing indent style."""
    rendered = json.dumps(entry, indent=2, ensure_ascii=False)
    return "\n".join("    " + line if line else line for line in rendered.split("\n"))


def format_aliases(aliases: list[str], *, multiline: bool, ensure_ascii: bool) -> str:
    """Render an aliases array in the style the edited entry already uses.

    docs/product-catalog.json is not uniformly formatted: most entries are
    `json.dumps(indent=2, ensure_ascii=False)` output shifted by 4 spaces
    (fields at indent 6, array items at indent 8), while an older block of
    entries keeps each array on one line with \\uXXXX escapes. The style of
    the array being edited is detected and reproduced so the diff shows only
    the removed alias -- no reformatting noise.
    """
    if not multiline:
        return json.dumps(aliases, ensure_ascii=ensure_ascii)
    rendered = json.dumps(aliases, indent=2, ensure_ascii=ensure_ascii)
    return "\n".join(
        ("      " + line if index else line)
        for index, line in enumerate(rendered.split("\n"))
    )


def find_array_span(raw_text: str, start: int, key: str) -> tuple[int, int] | None:
    """Return (open_bracket, end) of the array value of `key` after `start`."""
    key_at = raw_text.find(f'"{key}":', start)
    if key_at == -1:
        return None
    open_at = raw_text.find("[", key_at)
    if open_at == -1:
        return None
    index = open_at + 1
    in_string = False
    escaped = False
    while index < len(raw_text):
        char = raw_text[index]
        if in_string:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                in_string = False
        elif char == '"':
            in_string = True
        elif char == "]":
            return open_at, index + 1
        index += 1
    return None


def remove_alias(raw_text: str, catalog: dict, product_id: str, alias: str) -> str:
    """Delete one alias from one existing entry, in place, in the raw text."""
    marker = f'\n      "id": "{product_id}",\n'
    start_of_entry = raw_text.find(marker)
    if start_of_entry == -1 or raw_text.find(marker, start_of_entry + 1) != -1:
        raise SyncError(
            f"could not locate exactly one catalog entry with id {product_id!r} "
            "in docs/product-catalog.json; refusing to edit its aliases "
            f"automatically. Remove the alias {alias!r} by hand."
        )
    products = [item for item in catalog["products"] if item["id"] == product_id]
    if len(products) != 1:
        raise SyncError(f"catalog has {len(products)} entries with id {product_id!r}")
    remaining = [
        item for item in products[0]["aliases"] if _normalize(item) != _normalize(alias)
    ]

    span = find_array_span(raw_text, start_of_entry, "aliases")
    if span is None:
        raise SyncError(
            f"could not locate the aliases array of catalog entry {product_id!r}; "
            f"remove the alias {alias!r} by hand."
        )
    open_at, end_at = span
    current = raw_text[open_at:end_at]
    try:
        current_aliases = json.loads(current)
    except json.JSONDecodeError:
        current_aliases = None
    if current_aliases != products[0]["aliases"]:
        raise SyncError(
            f"the aliases array of catalog entry {product_id!r} does not read back "
            f"as expected; remove the alias {alias!r} by hand."
        )
    # Keep the parsed catalog in step so a second removal on the same entry
    # still validates against what the text now holds.
    products[0]["aliases"] = remaining
    replacement = format_aliases(
        remaining,
        multiline="\n" in current,
        ensure_ascii="\\u" in current,
    )
    return raw_text[:open_at] + replacement + raw_text[end_at:]


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

    folders_by_lang = discover_markdown_folders()
    all_discovered = folders_by_lang["en"] | folders_by_lang["zh"]
    registered = registered_source_folders(catalog)

    # Only Markdown-bearing folders are ever "new" candidates here -- see
    # module docstring for why pure-PDF folders and disk non-existence of a
    # registered folder are both deliberately not checked.
    new_folders = sorted(all_discovered - registered)

    problems: list[str] = []
    lookup = build_lookup(catalog)
    new_entries: list[dict] = []
    alias_removals: list[tuple[str, str]] = []
    for folder_name in new_folders:
        langs_present = sorted(
            (lang for lang in LANGUAGES if folder_name in folders_by_lang[lang]),
            key=LANGUAGES.index,
        )
        try:
            entry, removals = build_new_entry(folder_name, langs_present, lookup)
        except SyncError as error:
            problems.append(str(error))
            continue
        # Keep the lookup table in step with what this run will write, so a
        # second new folder colliding with the first (or with an alias this
        # run already hands off) is still caught.
        for owner_id, alias in removals:
            key = _normalize(alias)
            lookup[key] = [owner for owner in lookup.get(key, []) if owner[1] != "alias"]
            if (owner_id, alias) not in alias_removals:
                alias_removals.append((owner_id, alias))
        for field, name in (
            ("id", entry["id"]),
            ("display_name", folder_name),
            ("source_folder", folder_name),
        ):
            lookup.setdefault(_normalize(name), []).append((entry["id"], field, name))
        new_entries.append(entry)

    # New, cleanly-derivable folders are registered even if some other new
    # folder in the same run needs a human (non-ASCII name, or a derived id
    # that collides with an existing one) -- automatic registration of
    # legitimate new content must not be held hostage by an unrelated
    # manual-registration item. Such problems still make the run exit
    # non-zero so a human sees them.
    if new_entries:
        print(f"sync_product_catalog: {len(new_entries)} new product(s) to register:")
        for entry in new_entries:
            print(f"  - {entry['id']} (source_folders={entry['source_folders']!r})")

    def report_alias_removals(verb: str) -> None:
        for owner_id, alias in alias_removals:
            print(
                f"sync_product_catalog: alias {alias!r} {verb} from {owner_id!r} "
                "(folder now has independent docs)"
            )

    if args.check:
        report_alias_removals("will be removed")
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
        new_text = raw_text
        try:
            for owner_id, alias in alias_removals:
                new_text = remove_alias(new_text, catalog, owner_id, alias)
        except SyncError as error:
            # An alias hand-off that cannot be applied must abort the whole
            # write: registering the new entry without dropping the alias is
            # exactly the duplicate-lookup-name failure that freezes indexing.
            print("sync_product_catalog: manual action required:", file=sys.stderr)
            print(f"  - {error}", file=sys.stderr)
            for problem in problems:
                print(f"  - {problem}", file=sys.stderr)
            return 1
        new_text = splice_entries(new_text, new_entries)
        CATALOG_PATH.write_text(new_text, encoding="utf-8", newline="\n")
        report_alias_removals("removed")
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
