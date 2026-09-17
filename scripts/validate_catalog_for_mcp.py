#!/usr/bin/env python3
"""Pre-flight check: would the Documents MCP indexer accept this commit?

WHY THIS EXISTS
---------------
The Documents MCP service (https://docs-mcp.inhand.com) rebuilds its search
index from every push to master. Before it indexes anything it validates
docs/product-catalog.json against the actual docs/{en,zh}/ folder tree
(inhand-docs-mcp: commit_builder.CommitIndexBuilder._catalog_chunks_and_assets).
If that validation raises CatalogValidationError the whole build is abandoned
and the *previously* active index stays live -- silently. Nothing 500s, search
keeps answering, it just answers from a stale commit forever. That has already
happened once for two weeks before anyone noticed.

This script replays that exact validation locally / in CI so a bad commit is
rejected at push time instead of silently freezing the index.

RELATIONSHIP TO inhand-docs-mcp
-------------------------------
Everything between the "BEGIN MIRRORED LOGIC" and "END MIRRORED LOGIC" markers
is a verbatim copy of inhand-docs-mcp source and MUST be kept identical to it:

  * _PRODUCT_ID / _KINDS / _LANGUAGES, _parse_product, _string_list,
    _normalize, _asset_filename_contains, ProductCatalog.__init__ uniqueness
    rules, for_source_folder, for_asset, validate_source_folders
    -> must stay consistent with inhand-docs-mcp
       src/inhand_docs_mcp/catalog.py
  * the md/pdf path filters (indexable_paths)
    -> must stay consistent with inhand-docs-mcp
       src/inhand_docs_mcp/github.py  (GitHubDocsSource.indexable_paths /
       list_pdf_assets)
  * the represented-folders derivation
    -> must stay consistent with inhand-docs-mcp
       src/inhand_docs_mcp/commit_builder.py:71-96

The only intentional behavioural difference: the real indexer raises on the
first problem, while this script collects *every* problem and reports them all
before exiting non-zero, so one CI run is enough to fix everything.

Standard library only -- no pip install, so it cannot break the CI env.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CATALOG_PATH = REPO_ROOT / "docs" / "product-catalog.json"
DOC_ROOTS = ("docs/en/", "docs/zh/")

# --------------------------------------------------------------------------
# BEGIN MIRRORED LOGIC -- keep identical to inhand-docs-mcp catalog.py
# --------------------------------------------------------------------------

_PRODUCT_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")
_KINDS = {"model", "family", "software"}
_LANGUAGES = {"en", "zh"}


class CatalogValidationError(ValueError):
    """The product catalog cannot safely describe one documentation commit."""


@dataclass(frozen=True)
class ProductDefinition:
    """One stable public identity and its source-folder mappings."""

    product_id: str
    kind: str
    display_names: dict[str, str]
    aliases: tuple[str, ...]
    source_folders: tuple[str, ...]
    expected_languages: tuple[str, ...]
    public: bool


def _normalize(value: str) -> str:
    """Must stay consistent with inhand-docs-mcp catalog._normalize."""
    return " ".join(value.split()).casefold()


def _asset_filename_contains(filename: str, product_name: str) -> bool:
    """Must stay consistent with inhand-docs-mcp catalog._asset_filename_contains."""
    token = product_name.strip().casefold()
    if not token:
        return False
    return (
        re.search(
            rf"(?<![a-z0-9]){re.escape(token)}(?![a-z0-9])",
            filename.casefold(),
        )
        is not None
    )


def _string_list(
    value: object, product_id: str, label: str, *, allow_empty: bool
) -> tuple[str, ...]:
    """Must stay consistent with inhand-docs-mcp catalog._string_list."""
    if (
        not isinstance(value, list)
        or (not allow_empty and not value)
        or any(not isinstance(item, str) or not item.strip() for item in value)
    ):
        raise CatalogValidationError(f"product {product_id} has invalid {label} list")
    result = tuple(item.strip() for item in value)
    if len({_normalize(item) for item in result}) != len(result):
        raise CatalogValidationError(f"product {product_id} has duplicate {label} values")
    return result


def _parse_product(item: object) -> ProductDefinition:
    """Must stay consistent with inhand-docs-mcp catalog._parse_product."""
    if not isinstance(item, dict):
        raise CatalogValidationError("each product must be an object")
    product_id = item.get("id")
    if not isinstance(product_id, str) or not _PRODUCT_ID.fullmatch(product_id):
        raise CatalogValidationError("product id must be a non-empty URL-safe identifier")
    kind = item.get("kind")
    if kind not in _KINDS:
        raise CatalogValidationError(f"product {product_id} has invalid kind")
    display_names = item.get("display_names")
    if (
        not isinstance(display_names, dict)
        or not display_names
        or any(
            language not in _LANGUAGES or not isinstance(value, str) or not value.strip()
            for language, value in display_names.items()
        )
    ):
        raise CatalogValidationError(f"product {product_id} has invalid display names")
    aliases = _string_list(item.get("aliases"), product_id, "aliases", allow_empty=True)
    source_folders = _string_list(
        item.get("source_folders"), product_id, "source folder", allow_empty=False
    )
    expected_languages = _string_list(
        item.get("expected_languages"), product_id, "language", allow_empty=False
    )
    if any(language not in _LANGUAGES for language in expected_languages):
        raise CatalogValidationError(f"product {product_id} has invalid language")
    public = item.get("public")
    if not isinstance(public, bool):
        raise CatalogValidationError(f"product {product_id} public must be boolean")
    return ProductDefinition(
        product_id=product_id,
        kind=str(kind),
        display_names={str(key): str(value).strip() for key, value in display_names.items()},
        aliases=aliases,
        source_folders=source_folders,
        expected_languages=expected_languages,
        public=public,
    )


def indexable_markdown(paths: list[str]) -> list[str]:
    """Must stay consistent with inhand-docs-mcp github.indexable_paths."""
    return sorted(
        {
            path
            for path in paths
            if path.startswith(DOC_ROOTS)
            and path.endswith(".md")
            and not path.endswith("/llms.txt")
        }
    )


def indexable_pdfs(paths: list[str]) -> list[str]:
    """Must stay consistent with inhand-docs-mcp github.list_pdf_assets."""
    return sorted(
        {
            path
            for path in paths
            if path.startswith(DOC_ROOTS) and path.casefold().endswith(".pdf")
        }
    )


# --------------------------------------------------------------------------
# END MIRRORED LOGIC
# --------------------------------------------------------------------------


class Report:
    """Collect every problem instead of failing on the first one."""

    def __init__(self) -> None:
        self.errors: list[str] = []

    def add(self, headline: str, *, detail: str = "", fix: str = "") -> None:
        block = [f"ERROR: {headline}"]
        if detail:
            block.extend(f"       {line}" for line in detail.splitlines())
        if fix:
            block.extend(f"  FIX: {line}" for line in fix.splitlines())
        self.errors.append("\n".join(block))

    @property
    def failed(self) -> bool:
        return bool(self.errors)


class Catalog:
    """Lookup indexes over the parsed products, built error-tolerantly.

    Mirrors ProductCatalog.__init__ / for_source_folder / for_asset /
    validate_source_folders from inhand-docs-mcp catalog.py, except that
    index construction records duplicate-name collisions in the report
    instead of raising on the first one.
    """

    def __init__(self, products: list[ProductDefinition], report: Report) -> None:
        self.products = products
        self._report = report
        self._by_lookup: dict[str, ProductDefinition] = {}
        self._by_source_folder: dict[str, ProductDefinition] = {}
        for product in products:
            for name in (
                product.product_id,
                *product.display_names.values(),
                *product.aliases,
                *product.source_folders,
            ):
                key = _normalize(name)
                existing = self._by_lookup.get(key)
                if existing is not None and existing.product_id != product.product_id:
                    report.add(
                        f"duplicate lookup name {name!r} for {existing.product_id} "
                        f"and {product.product_id}",
                        detail=(
                            "A product id, display name, alias or source folder may "
                            "only resolve to one product (case/whitespace-insensitive). "
                            "MCP refuses to load the whole catalog otherwise."
                        ),
                        fix=(
                            f"In docs/product-catalog.json remove {name!r} from one of "
                            f"{existing.product_id} / {product.product_id} -- normally "
                            "from the broader/older entry, because the product that owns "
                            "the docs folder keeps the name."
                        ),
                    )
                    continue
                self._by_lookup[key] = product
            for folder in product.source_folders:
                existing = self._by_source_folder.get(folder)
                if existing is not None:
                    report.add(
                        f"duplicate source folder {folder!r} for {existing.product_id} "
                        f"and {product.product_id}",
                        fix=(
                            "In docs/product-catalog.json keep the folder in exactly one "
                            "entry's source_folders."
                        ),
                    )
                    continue
                self._by_source_folder[folder] = product

    @property
    def public_products(self) -> tuple[ProductDefinition, ...]:
        return tuple(
            sorted(
                (product for product in self.products if product.public),
                key=lambda product: product.product_id.casefold(),
            )
        )

    def for_source_folder(self, folder: str) -> ProductDefinition:
        try:
            return self._by_source_folder[folder]
        except KeyError as error:
            raise KeyError(f"unmapped source folder {folder!r}") from error

    def for_asset(self, folder: str, filename: str) -> ProductDefinition:
        """Resolve a PDF by folder, or by one unambiguous public product name."""
        try:
            return self.for_source_folder(folder)
        except KeyError:
            pass
        candidates = {
            product.product_id: product
            for product in self.public_products
            if any(
                _asset_filename_contains(filename, name)
                for name in (
                    product.product_id,
                    *product.aliases,
                    *product.display_names.values(),
                )
            )
        }
        if len(candidates) != 1:
            matches = ", ".join(sorted(candidates)) or "none"
            raise CatalogValidationError(
                f"cannot map PDF asset {folder}/{filename} to one public product; "
                f"matches: {matches}"
            )
        return next(iter(candidates.values()))

    def check_source_folders(self, folders: set[str], report: Report) -> None:
        """Both directions of validate_source_folders, reported together."""
        mapped = set(self._by_source_folder)
        for folder in sorted(folders - mapped):
            report.add(
                f"unmapped source folder: {folder}",
                detail=(
                    f"docs/en/{folder} or docs/zh/{folder} has content but no catalog "
                    "entry lists it in source_folders."
                ),
                fix=(
                    "Add the folder to an existing product's source_folders in "
                    "docs/product-catalog.json, or add a new product entry. The "
                    "'Sync product catalog' workflow normally does this for you on the "
                    "next push to master."
                ),
            )
        for folder in sorted(mapped - folders):
            owner = self._by_source_folder[folder].product_id
            report.add(
                f"nonexistent source folder: {folder} (product {owner})",
                detail=(
                    f"docs/product-catalog.json maps {owner} to source folder "
                    f"{folder!r}, but neither docs/en/{folder} nor docs/zh/{folder} "
                    "contains any indexable file."
                ),
                fix=(
                    f"Either restore the folder, or remove {folder!r} from {owner}'s "
                    "source_folders (dropping the entry entirely if it has no folders "
                    "left)."
                ),
            )


def git_tracked_doc_files() -> list[str]:
    """Tracked paths under docs/en and docs/zh, exactly as Git stores them.

    -z avoids Git's quoting of non-ASCII path names, which the index sees raw.
    """
    result = subprocess.run(
        ["git", "ls-files", "-z", "--", "docs/en", "docs/zh"],
        cwd=REPO_ROOT,
        capture_output=True,
        check=True,
    )
    raw = result.stdout.decode("utf-8", errors="surrogateescape")
    return [path for path in raw.split("\0") if path]


def load_products(report: Report) -> list[ProductDefinition]:
    """Parse docs/product-catalog.json, reporting every bad entry."""
    try:
        payload = CATALOG_PATH.read_text(encoding="utf-8")
    except OSError as error:
        report.add(
            f"cannot read {CATALOG_PATH.relative_to(REPO_ROOT).as_posix()}: {error}",
            fix="The Documents MCP indexer reads docs/product-catalog.json; it must exist.",
        )
        return []
    try:
        data = json.loads(payload)
    except (json.JSONDecodeError, TypeError) as error:
        report.add(
            f"product catalog must be valid JSON: {error}",
            fix="Fix the JSON syntax in docs/product-catalog.json.",
        )
        return []
    if not isinstance(data, dict) or data.get("schema_version") != 1:
        report.add(
            "product catalog schema_version must be 1",
            fix='Set "schema_version": 1 at the top level of docs/product-catalog.json.',
        )
        return []
    raw_products = data.get("products")
    if not isinstance(raw_products, list):
        report.add(
            "product catalog products must be a list",
            fix='docs/product-catalog.json needs a top-level "products": [...] array.',
        )
        return []

    products: list[ProductDefinition] = []
    for position, item in enumerate(raw_products):
        try:
            products.append(_parse_product(item))
        except CatalogValidationError as error:
            shown = item.get("id") if isinstance(item, dict) else None
            report.add(
                f"invalid product entry #{position} (id={shown!r}): {error}",
                fix=(
                    "Fix the entry in docs/product-catalog.json. Required shape: "
                    'id (URL-safe), kind (model|family|software), display_names '
                    '({"en"/"zh": non-empty}), aliases (list of strings, may be empty), '
                    "source_folders (non-empty), expected_languages (non-empty, en/zh "
                    "only), public (true/false literal, not a string)."
                ),
            )

    ids = [product.product_id for product in products]
    for duplicate in sorted({item for item in ids if ids.count(item) > 1}):
        report.add(
            f"duplicate product ID: {duplicate}",
            fix=f"Merge the two {duplicate!r} entries in docs/product-catalog.json.",
        )
    return products


def main() -> int:
    report = Report()
    products = load_products(report)
    catalog = Catalog(products, report)

    files = git_tracked_doc_files()
    md = indexable_markdown(files)
    pdf = indexable_pdfs(files)

    # Mirrors commit_builder._catalog_chunks_and_assets:71-96.
    represented: set[str] = {
        path.split("/")[2] for path in md if len(path.split("/")) > 3
    }
    for path in pdf:
        parts = path.split("/")
        if len(parts) <= 3:
            continue
        try:
            product = catalog.for_asset(parts[2], parts[-1])
        except CatalogValidationError as error:
            report.add(
                str(error),
                detail=(
                    f"PDF {path} sits in a folder that is not in any entry's "
                    "source_folders, so MCP falls back to matching the file NAME "
                    "against every public product id/alias/display name -- and that "
                    "must hit exactly one product."
                ),
                fix=(
                    f"Either register folder {parts[2]!r} under the owning product's "
                    "source_folders in docs/product-catalog.json, or rename the PDF so "
                    "exactly one public product name appears in it as a whole token, or "
                    "move it under the product's own docs folder."
                ),
            )
            continue
        represented.update(product.source_folders)

    catalog.check_source_folders(represented, report)

    if report.failed:
        print(
            "Documents MCP catalog validation FAILED -- "
            f"{len(report.errors)} problem(s).\n",
            file=sys.stderr,
        )
        for block in report.errors:
            print(block + "\n", file=sys.stderr)
        print(
            "Merging this as-is does not break the docs site, but it makes the "
            "Documents MCP indexer abort every rebuild, so https://docs-mcp.inhand.com "
            "would keep serving a stale commit indefinitely (no error surfaces to "
            "users). Fix docs/product-catalog.json and/or the docs tree above.",
            file=sys.stderr,
        )
        return 1

    print(
        f"catalog OK: {len(products)} products, {len(md)} md, {len(pdf)} pdf, "
        f"{len(represented)} folders"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
