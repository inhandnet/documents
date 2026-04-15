#!/usr/bin/env python3
"""上传文件到 PowerIS 云存储 API。

在本地构建后运行，将生成的文件上传到云存储。
支持上传 PDF、压缩包、文档等（排除 .md 源文件和图片文件）

用法：
    python scripts/upload_specs_to_cloud.py              # 上传 dist/specs/ 下所有文件
    python scripts/upload_specs_to_cloud.py --file path  # 上传指定文件
"""

import argparse
import mimetypes
import os
import subprocess
import sys
from pathlib import Path
from typing import List, Optional

import requests

# API 配置
API_BASE_URL = "https://cloud-dev.poweris.inhand.online"
API_ENDPOINT = "/api/common/github/application/files"
API_KEY = "5bfcc5c90c2c4ff485838773e9cc9c05"

# 默认查询参数
DEFAULT_PARAMS = {
    "source": "test",
    "security_level": "0"
}

# 构建输出目录
DIST_DIR = Path("dist/specs")

# 排除的文件类型
EXCLUDED_EXTENSIONS = {
    ".md",      # Markdown 源文件
    ".png",     # 图片
    ".jpg",
    ".jpeg",
    ".gif",
    ".svg",
    ".webp",
    ".bmp",
    ".ico",
    ".js",      # 前端资源
    ".css",
    ".html",
    ".htm",
    ".json",
    ".xml",
    ".yaml",
    ".yml",
}


def get_git_commit_id() -> Optional[str]:
    """获取当前 git commit ID（短格式）。"""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
            cwd=Path(__file__).parent.parent  # 在仓库根目录执行
        )
        return result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def normalize_upload_path(file_path: Path, base_dir: Path = DIST_DIR) -> str:
    """标准化上传路径，去掉头部目录（如 dist/specs/zh/）。

    例如:
        dist/specs/zh/AI Edge Computers/Rockchip/EC954/datasheet.pdf
        → AI Edge Computers/Rockchip/EC954/datasheet.pdf

        dist/specs/en/IG502/Manual/ig502_manual.pdf
        → IG502/Manual/ig502_manual.pdf
    """
    try:
        # 获取相对于 base_dir 的路径
        rel_path = file_path.relative_to(base_dir)
    except ValueError:
        # 如果不在 base_dir 下，使用完整路径
        rel_path = file_path

    parts = list(rel_path.parts)

    # 去掉语言前缀 zh/ 或 en/
    if parts and parts[0] in ("zh", "en"):
        parts = parts[1:]

    # 用 / 连接
    return "/".join(parts)


def upload_file(file_path: Path, dry_run: bool = False, commit_id: Optional[str] = None,
                base_dir: Path = DIST_DIR) -> bool:
    """上传单个文件到云存储 API。

    Args:
        file_path: 文件路径
        dry_run: 如果为 True，只打印不实际上传
        commit_id: Git commit ID（可选）
        base_dir: 基础目录，用于计算相对路径

    Returns:
        上传成功返回 True，失败返回 False
    """
    if not file_path.exists():
        print(f"  [FAIL] 文件不存在: {file_path}")
        return False

    # 从路径提取产品名（倒数第二级目录）
    parts = file_path.parts
    product_name = parts[-2] if len(parts) >= 2 else file_path.stem

    # 标准化路径（去掉 dist/specs/zh/ 等前缀）
    normalized_path = normalize_upload_path(file_path, base_dir)

    # 构建完整 URL
    url = f"{API_BASE_URL}{API_ENDPOINT}"
    params = DEFAULT_PARAMS.copy()

    # 添加路径参数
    params["path"] = normalized_path

    # 添加 commitId 参数（如果提供）
    if commit_id:
        params["commitId"] = commit_id

    # 准备请求头
    headers = {
        "x-api-key": API_KEY
    }

    # 自动检测 MIME 类型
    mime_type, _ = mimetypes.guess_type(str(file_path))
    if mime_type is None:
        mime_type = "application/octet-stream"

    # 准备表单数据
    files = {
        "file": (file_path.name, open(file_path, "rb"), mime_type)
    }

    print(f"  上传: {file_path.name}")
    print(f"    产品: {product_name}")
    print(f"    路径: {normalized_path}")
    print(f"    URL: {url}")
    print(f"    Params: {params}")

    if dry_run:
        print(f"  [DRY RUN] 跳过实际上传")
        return True

    try:
        response = requests.post(
            url,
            headers=headers,
            params=params,
            files=files,
            timeout=60
        )
        response.raise_for_status()

        result = response.json()

        # 检查是否有错误
        if 'error' in result:
            print(f"  [FAIL] 上传失败: {result.get('error')}")
            print(f"  完整响应: {result}")
            return False

        print(f"  [OK] 上传成功")
        print(f"  完整响应: {result}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"  [FAIL] 上传失败: {e}")
        if hasattr(e.response, 'text'):
            print(f"     响应: {e.response.text}")
        return False
    finally:
        files["file"][1].close()


def find_upload_files(directory: Path) -> List[Path]:
    """递归查找目录下所有需要上传的文件（只处理 zh/ 和 en/ 子目录）。

    规则：
    - 只处理 zh/ 和 en/ 子目录下的文件
    - 排除 .md 文件（Markdown 是源文件）
    - 排除图片文件（.png, .jpg, .jpeg, .gif, .svg, .webp 等）
    - 只上传 PDF、压缩包、文档等非图片文件
    """
    if not directory.exists():
        return []

    upload_files = []

    # 只处理 zh/ 和 en/ 子目录，跳过 redirects 目录
    for lang_dir in ["zh", "en"]:
        lang_path = directory / lang_dir
        if lang_path.exists():
            for file_path in lang_path.rglob("*"):
                # 跳过 redirects 目录
                if "redirects" in file_path.parts:
                    continue
                if file_path.is_file():
                    ext = file_path.suffix.lower()
                    if ext not in EXCLUDED_EXTENSIONS:
                        upload_files.append(file_path)

    return upload_files


def main():
    parser = argparse.ArgumentParser(
        description="上传文件到 PowerIS 云存储（排除 .md 和图片文件）"
    )
    parser.add_argument(
        "--file",
        type=Path,
        help="指定要上传的单个文件（默认上传 dist/specs/ 下所有非 .md 非图片文件）"
    )
    parser.add_argument(
        "--dist-dir",
        type=Path,
        default=DIST_DIR,
        help=f"文件输出目录（默认: {DIST_DIR}）"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="预览模式，只打印不上传"
    )
    args = parser.parse_args()

    # 确定要上传的文件列表
    if args.file:
        upload_files_list = [args.file]
    else:
        upload_files_list = find_upload_files(args.dist_dir)

    if not upload_files_list:
        print(f"[INFO] 没有找到可上传的文件: {args.dist_dir}")
        print("跳过上传步骤")
        sys.exit(0)

    # 获取 Git commit ID
    commit_id = get_git_commit_id()
    if commit_id:
        print(f"Git Commit ID: {commit_id}")
    else:
        print("警告: 无法获取 Git commit ID")

    print(f"=== 准备上传 {len(upload_files_list)} 个文件 ===\n")

    # 上传文件
    success_count = 0
    fail_count = 0

    for upload_file_path in upload_files_list:
        if upload_file(upload_file_path, dry_run=args.dry_run, commit_id=commit_id,
                      base_dir=args.dist_dir):
            success_count += 1
        else:
            fail_count += 1
        print()

    # 汇总
    print("=" * 50)
    if args.dry_run:
        print(f"[DRY RUN] 预览完成，实际将上传: {success_count} 个文件（排除 .md 和图片）")
    else:
        print(f"上传完成: {success_count} 成功, {fail_count} 失败")
    print("=" * 50)

    if fail_count > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
