#!/usr/bin/env python3
"""本地构建规格书并上传到云存储（一体化脚本）。

用法：
    python scripts/build_and_upload.py              # 构建并上传所有
    python scripts/build_and_upload.py --dry-run    # 预览模式
    python scripts/build_and_upload.py --skip-build # 只上传（不重新构建）
"""

import argparse
import subprocess
import sys
from pathlib import Path

# 导入上传功能
from upload_specs_to_cloud import upload_file, find_pdfs, DIST_DIR


def build_specs():
    """运行 build_specs.py 构建 PDF。"""
    print("=== 步骤 1: 构建 PDF ===\n")

    build_script = Path(__file__).parent / "build_specs.py"
    result = subprocess.run(
        [sys.executable, str(build_script)],
        capture_output=False,
        text=True
    )

    if result.returncode != 0:
        print("\n❌ PDF 构建失败，停止上传")
        sys.exit(1)

    print("\n✅ PDF 构建完成\n")


def upload_all_pdfs(dry_run: bool = False):
    """上传 dist/specs/ 下所有 PDF。"""
    print("=== 步骤 2: 上传到云存储 ===\n")

    pdf_files = find_pdfs(DIST_DIR)

    if not pdf_files:
        print(f"⚠️ 没有找到 PDF 文件: {DIST_DIR}")
        sys.exit(1)

    print(f"发现 {len(pdf_files)} 个 PDF 文件\n")

    success_count = 0
    fail_count = 0

    for pdf_file in pdf_files:
        if upload_file(pdf_file, dry_run=dry_run):
            success_count += 1
        else:
            fail_count += 1
        print()

    print("=" * 50)
    if dry_run:
        print(f"[DRY RUN] 预览完成")
        print(f"  - 将构建: {len(pdf_files)} 个 PDF")
        print(f"  - 将上传: {len(pdf_files)} 个 PDF")
    else:
        print(f"完成: {success_count} 成功, {fail_count} 失败")
    print("=" * 50)

    return fail_count == 0


def main():
    parser = argparse.ArgumentParser(
        description="构建规格书 PDF 并上传到云存储"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="预览模式，只打印不执行"
    )
    parser.add_argument(
        "--skip-build",
        action="store_true",
        help="跳过构建，只上传已有 PDF"
    )
    args = parser.parse_args()

    # 步骤 1: 构建（可选跳过）
    if not args.skip_build:
        if args.dry_run:
            print("[DRY RUN] 将执行: python scripts/build_specs.py\n")
        else:
            build_specs()

    # 步骤 2: 上传
    success = upload_all_pdfs(dry_run=args.dry_run)

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
