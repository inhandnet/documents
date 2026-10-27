#!/usr/bin/env python3
"""Merge case-variant duplicate product folders into the catalog-canonical case.

Upstream syncs (user-manual etc.) may spell a product folder differently from
docs/product-catalog.json (e.g. IG502-lite vs IG502-LITE). On the case-sensitive
CI filesystem both folders then exist, which the MCP catalog refuses to index
and the validator reports as an unmapped folder.

This script merges every case-variant group into the spelling that
docs/product-catalog.json lists in source_folders (falling back to the
most recently committed name when the catalog lists none of them). When both
variants hold a file at the same relative path with different content, the
variant folder wins -- it is the copy the latest upstream sync just wrote.

Standard library only; never fails the workflow (unexpected shapes are
reported and skipped).
"""

import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CATALOG = REPO_ROOT / "docs" / "product-catalog.json"
LANG_ROOTS = [REPO_ROOT / "docs" / "zh", REPO_ROOT / "docs" / "en"]


def catalog_folder_case() -> dict:
    """casefold(name) -> exact folder name as listed in the catalog."""
    mapping = {}
    try:
        data = json.loads(CATALOG.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"[WARN] cannot read {CATALOG}: {exc}")
        return mapping
    for product in data.get("products", []):
        for folder in product.get("source_folders", []):
            mapping.setdefault(folder.casefold(), folder)
    return mapping


def last_commit_ts(path: Path) -> int:
    out = subprocess.run(
        ["git", "log", "-1", "--format=%ct", "--", str(path.relative_to(REPO_ROOT))],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )
    return int(out.stdout.strip()) if out.stdout.strip().isdigit() else 0


def pick_canonical(names: list[str], known: dict) -> str | None:
    listed = [n for n in names if known.get(n.casefold()) == n]
    if len(listed) == 1:
        return listed[0]
    if len(listed) > 1:
        print(f"[WARN] catalog lists several spellings {listed}; skipping group")
        return None
    return max(names, key=lambda n: (last_commit_ts(_root / n), n))


def merge_dir(variant: Path, canonical: Path) -> tuple[int, int]:
    """Move variant's files under canonical; returns (moved, replaced)."""
    moved = replaced = 0
    for src in sorted(variant.rglob("*")):
        if src.is_dir():
            continue
        dst = canonical / src.relative_to(variant)
        dst.parent.mkdir(parents=True, exist_ok=True)
        if dst.exists():
            if src.read_bytes() == dst.read_bytes():
                src.unlink()
                continue
            src.replace(dst)  # variant (freshest sync copy) wins
            replaced += 1
        else:
            src.replace(dst)
            moved += 1
    for p in sorted(variant.rglob("*"), reverse=True):
        if p.is_dir():
            try:
                p.rmdir()
            except OSError:
                pass
    try:
        variant.rmdir()
    except OSError as exc:
        print(f"[WARN] could not remove {variant}: {exc}")
    return moved, replaced


def main() -> int:
    global _root
    known = catalog_folder_case()
    acted = False
    for _root in LANG_ROOTS:
        if not _root.is_dir():
            continue
        groups: dict[str, list[str]] = {}
        for child in _root.iterdir():
            if child.is_dir():
                groups.setdefault(child.name.casefold(), []).append(child.name)
        for key, names in sorted(groups.items()):
            if len(names) < 2:
                continue
            canonical_name = pick_canonical(names, known)
            if canonical_name is None:
                continue
            canonical = _root / canonical_name
            print(f"[CASE] merging {names} -> {canonical_name} (in {_root.name}/)")
            for name in names:
                if name == canonical_name:
                    continue
                moved, replaced = merge_dir(_root / name, canonical)
                print(f"       {name}: {moved} moved, {replaced} replaced by fresher copy")
                acted = True
    if not acted:
        print("No case-variant product folders.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
