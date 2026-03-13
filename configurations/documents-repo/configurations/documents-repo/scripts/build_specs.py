#!/usr/bin/env python3
"""规格书构建脚本：将 specs/ 下的 Markdown 文件转换为 PDF。

逻辑：
1. 遍历 specs/ 下所有 .md 文件
2. 如果同目录已有同名 .pdf，跳过（说明是现成 PDF，无需构建）
3. 否则用 Pandoc 转换为 PDF
4. 输出到 dist/specs/ 保持目录结构
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

SPECS_DIR = Path("specs")
DIST_DIR = Path("dist/specs")


def find_md_specs():
    """找到所有需要构建的 .md 规格书文件"""
    md_files = []
    for md_path in SPECS_DIR.rglob("*.md"):
        # 跳过 index.md
        if md_path.name.lower() == "index.md":
            continue
        # 如果同目录已有同名 PDF，跳过
        pdf_sibling = md_path.with_suffix(".pdf")
        if pdf_sibling.exists():
            print(f"  [SKIP] {md_path} (已有同名 PDF)")
            continue
        md_files.append(md_path)
    return md_files


def build_pdf(md_path: Path):
    """使用 Pandoc 将 Markdown 转换为 PDF"""
    rel_path = md_path.relative_to(SPECS_DIR)
    out_path = DIST_DIR / rel_path.with_suffix(".pdf")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"  [BUILD] {md_path} -> {out_path}")

    cmd = [
        "pandoc",
        str(md_path),
        "-o", str(out_path),
        "--pdf-engine=weasyprint",
        "--metadata", f"title={md_path.stem}",
    ]

    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"  [ERROR] 构建失败: {md_path}")
        print(f"    stderr: {e.stderr}")
        return False


def copy_existing_pdfs():
    """将已有的 PDF 文件复制到 dist 目录"""
    for pdf_path in SPECS_DIR.rglob("*.pdf"):
        rel_path = pdf_path.relative_to(SPECS_DIR)
        out_path = DIST_DIR / rel_path
        out_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(pdf_path, out_path)
        print(f"  [COPY] {pdf_path} -> {out_path}")


def main():
    if not SPECS_DIR.exists():
        print("specs/ 目录不存在，无需构建。")
        return

    print("=== 规格书构建开始 ===\n")

    # 清理输出目录
    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    DIST_DIR.mkdir(parents=True, exist_ok=True)

    # 复制已有 PDF
    print("1. 复制已有 PDF 文件...")
    copy_existing_pdfs()

    # 构建 Markdown → PDF
    print("\n2. 构建 Markdown 规格书...")
    md_files = find_md_specs()
    if not md_files:
        print("  没有需要构建的 Markdown 规格书。")
    else:
        failures = []
        for md_path in md_files:
            if not build_pdf(md_path):
                failures.append(md_path)

        if failures:
            print(f"\n❌ {len(failures)} 个文件构建失败:")
            for f in failures:
                print(f"  - {f}")
            sys.exit(1)

    print("\n=== 规格书构建完成 ===")


if __name__ == "__main__":
    main()
