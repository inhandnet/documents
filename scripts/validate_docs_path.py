#!/usr/bin/env python3
"""校验 docs 文件路径到 PLM 系统。

用法：
    python scripts/validate_docs_path.py                    # 校验所有 docs 文件
    python scripts/validate_docs_path.py --file path.md     # 校验单个文件
    python scripts/validate_docs_path.py --diff             # 只校验 git 变更的文件
"""

import argparse
import subprocess
import sys
from pathlib import Path

import requests

# API 配置
API_URL = "https://cloud-dev.poweris.inhand.online/api/plm/github/product/published-files"
API_TOKEN = "b4ae9d11-dd4d-40e5-931f-3480e8c20c63"

# 支持的文件扩展名
VALID_EXTENSIONS = {".md", ".pdf", ".png", ".jpg", ".jpeg", ".gif", ".svg"}


def get_file_size(file_path: Path) -> int:
    """获取文件大小（字节）"""
    return file_path.stat().st_size


def normalize_path(file_path: Path) -> str:
    """将文件路径转换为 API 所需的格式（去掉 zh/en 前缀）"""
    # 转换为相对路径
    try:
        rel_path = file_path.relative_to(Path("."))
    except ValueError:
        rel_path = file_path

    parts = list(rel_path.parts)

    # 去掉开头的 docs/
    if parts and parts[0] == "docs":
        parts = parts[1:]

    # 去掉语言前缀 zh/ 或 en/
    if parts and parts[0] in ("zh", "en"):
        parts = parts[1:]

    # 用 / 连接
    return "/".join(parts)


def get_git_user_email():
    """获取当前 Git 用户的邮箱"""
    try:
        cmd = ["git", "config", "user.email"]
        output = subprocess.check_output(cmd).decode("utf-8").strip()
        return output
    except Exception:
        return "unknown@inhand.com.cn"


def get_changed_files():
    """获取 git 中变更的文件列表"""
    try:
        cmd = ["git", "diff", "--name-only", "HEAD~1", "HEAD"]
        output = subprocess.check_output(cmd).decode("utf-8")
        files = output.splitlines()
        # 只过滤 docs 目录下的文件
        return [f for f in files if f.startswith("docs/")]
    except Exception as e:
        print(f"[WARN] Git 获取差异失败: {e}")
        return []


def find_all_docs_files():
    """查找所有 docs 目录下的文件"""
    docs_dir = Path("docs")
    if not docs_dir.exists():
        return []

    files = []
    for ext in VALID_EXTENSIONS:
        files.extend(docs_dir.rglob(f"*{ext}"))
    return [str(f) for f in files]


def validate_files(file_list):
    """调用校验接口验证文件路径"""
    if not file_list:
        print("[WARN] 没有需要校验的文件")
        return True

    # 构建请求体
    payload = []
    for filepath in file_list:
        file_path = Path(filepath)
        if not file_path.exists():
            print(f"[SKIP] 文件不存在: {filepath}")
            continue

        # 获取文件大小
        size = get_file_size(file_path)

        # 标准化路径（去掉 zh/en）
        normalized = normalize_path(file_path)

        payload.append({
            "path": normalized,
            "size": size
        })

    if not payload:
        print("[WARN] 没有有效文件需要校验")
        return True

    # 获取 Git 用户邮箱并拼接到 URL
    user_email = get_git_user_email()
    api_url_with_params = f"{API_URL}?email={user_email}"

    # 打印请求信息
    print(f"=== 校验 {len(payload)} 个文件 ===\n")
    for item in payload:
        print(f"  Path: {item['path']}")
        print(f"  Size: {item['size']} bytes")
        print()

    # 调用 API
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }

    print(f"请求 URL: {api_url_with_params}")
    print(f"请求体: {payload}\n")

    try:
        response = requests.post(
            api_url_with_params,
            headers=headers,
            json=payload,
            timeout=30
        )
        response.raise_for_status()

        result = response.json()
        print(f"[OK] 校验成功")
        print(f"响应: {result}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"[FAIL] 校验失败: {e}")
        if hasattr(e.response, 'text'):
            print(f"响应: {e.response.text}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="校验 docs 文件路径到 PLM 系统"
    )
    parser.add_argument(
        "--file",
        type=Path,
        nargs="+",
        help="指定要校验的文件路径"
    )
    parser.add_argument(
        "--diff",
        action="store_true",
        help="只校验 git 变更的文件"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="校验所有 docs 文件"
    )
    args = parser.parse_args()

    # 确定要校验的文件列表
    if args.file:
        file_list = [str(f) for f in args.file]
    elif args.diff:
        file_list = get_changed_files()
    elif args.all:
        file_list = find_all_docs_files()
    else:
        # 默认只校验 git 变更
        file_list = get_changed_files()

    if not file_list:
        print("[INFO] 没有找到需要校验的文件")
        sys.exit(0)

    # 执行校验
    success = validate_files(file_list)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
