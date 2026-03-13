#!/usr/bin/env python3
"""Scaffold directory structure for a new product across all content types.

Creates matching directories under docs/, qa/, specs/, configurations/, brochures/
for both zh and en, with template files so authors can start editing immediately.

Usage:
    python scripts/scaffold_product.py --model EC999 --category "AI Edge Computers" --chipset Rockchip
    python scripts/scaffold_product.py --model IR302 --category Routers --chipset "Industrial Routers" --langs zh
"""

import argparse
from pathlib import Path

MANUAL_TEMPLATE_ZH = """\
# {model} 用户手册

> 适用固件版本：V1.0.0 及以上

## 1 产品概述

<!-- 请在此填写产品简介 -->

## 2 安装指南

<!-- 请在此填写安装步骤 -->

## 3 快速配置

<!-- 请在此填写基础配置流程 -->

## 4 常见问题

<!-- 请在此填写 FAQ，或参考 QA 知识库 -->
"""

MANUAL_TEMPLATE_EN = """\
# {model} User Manual

> Applicable firmware version: V1.0.0 and above

## 1 Product Overview

<!-- Fill in product introduction here -->

## 2 Installation Guide

<!-- Fill in installation steps here -->

## 3 Quick Configuration

<!-- Fill in basic configuration steps here -->

## 4 FAQ

<!-- Fill in FAQ here, or refer to the QA knowledge base -->
"""

QA_TEMPLATE_ZH = """\
---
tags:
  - {model}
  - {category}
---

# {model} 常见问题

## Q1: 如何恢复出厂设置？

<!-- 请在此填写回答 -->

## Q2: 如何升级固件？

<!-- 请在此填写回答 -->
"""

QA_TEMPLATE_EN = """\
---
tags:
  - {model}
  - {category}
---

# {model} FAQ

## Q1: How to factory reset?

<!-- Fill in answer here -->

## Q2: How to upgrade firmware?

<!-- Fill in answer here -->
"""


def main():
    parser = argparse.ArgumentParser(
        description="Scaffold a new product across docs/qa/specs/brochures (configurations uses separate case-based structure)"
    )
    parser.add_argument("--model", required=True, help="Product model name (e.g. EC999)")
    parser.add_argument("--category", required=True, help="Product category (e.g. 'AI Edge Computers')")
    parser.add_argument("--chipset", required=True, help="Chipset or sub-category (e.g. Rockchip)")
    parser.add_argument(
        "--langs", nargs="+", default=["zh", "en"],
        help="Languages to scaffold (default: zh en)"
    )
    parser.add_argument(
        "--repo-root", type=Path, default=Path("."),
        help="Repository root directory (default: current directory)"
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Print what would be created without writing files"
    )
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    model = args.model
    category = args.category
    chipset = args.chipset
    product_rel = f"{category}/{chipset}/{model}"

    created_dirs = []
    created_files = []

    for lang in args.langs:
        # --- docs ---
        docs_dir = repo_root / "docs" / lang / product_rel
        manual_name = f"{model}_User_Manual.md"
        template = MANUAL_TEMPLATE_ZH if lang == "zh" else MANUAL_TEMPLATE_EN
        manual_content = template.format(model=model)
        _ensure(docs_dir, manual_name, manual_content, args.dry_run, created_dirs, created_files)

        # images subdirectory
        images_dir = docs_dir / "images"
        _ensure_dir(images_dir, args.dry_run, created_dirs)
        _ensure(images_dir, ".gitkeep", "", args.dry_run, created_dirs, created_files)

        # deployment subdirectory (for deployment cases)
        deployment_dir = docs_dir / "deployment"
        _ensure_dir(deployment_dir, args.dry_run, created_dirs)
        _ensure(deployment_dir, ".gitkeep", "", args.dry_run, created_dirs, created_files)

        # --- qa ---
        qa_dir = repo_root / "qa" / lang / product_rel
        qa_template = QA_TEMPLATE_ZH if lang == "zh" else QA_TEMPLATE_EN
        qa_content = qa_template.format(model=model, category=category)
        _ensure(qa_dir, f"{model}_FAQ.md", qa_content, args.dry_run, created_dirs, created_files)

        # --- specs ---
        specs_dir = repo_root / "specs" / lang / product_rel
        _ensure(specs_dir, ".gitkeep", "", args.dry_run, created_dirs, created_files)

        # --- configurations --- (skipped: uses independent {lang}/{Model}/{CaseName}/ structure)

        # --- brochures ---
        brochures_dir = repo_root / "brochures" / lang / product_rel
        _ensure(brochures_dir, ".gitkeep", "", args.dry_run, created_dirs, created_files)

    # Summary
    prefix = "[DRY RUN] " if args.dry_run else ""
    print(f"\n{prefix}Scaffold complete for {model}:")
    print(f"  Product path: {product_rel}")
    print(f"  Languages:    {', '.join(args.langs)}")
    print(f"  Directories:  {len(created_dirs)} created")
    print(f"  Files:        {len(created_files)} created")

    if created_files:
        print("\nFiles:")
        for f in created_files:
            try:
                print(f"  {f.relative_to(repo_root)}")
            except ValueError:
                print(f"  {f}")


def _ensure_dir(dir_path: Path, dry_run: bool, created_dirs: list):
    if not dir_path.exists():
        if not dry_run:
            dir_path.mkdir(parents=True, exist_ok=True)
        created_dirs.append(dir_path)


def _ensure(dir_path: Path, filename: str, content: str,
            dry_run: bool, created_dirs: list, created_files: list):
    _ensure_dir(dir_path, dry_run, created_dirs)
    file_path = dir_path / filename
    if file_path.exists():
        print(f"  [SKIP] {file_path} (already exists)")
        return
    if not dry_run:
        file_path.write_text(content, encoding="utf-8")
    created_files.append(file_path)


if __name__ == "__main__":
    main()
