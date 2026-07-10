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

# API endpoint (same for both zh and en)
API_ENDPOINT = "/api/common/github/application/files"

# 默认查询参数
DEFAULT_PARAMS = {
    "source": "test",
    "security_level": "0"
}

# 构建输出目录
DIST_DIR = Path("dist/specs")


def get_api_config(file_path: Path, base_dir: Path = DIST_DIR) -> dict:
    """根据文件路径的语言前缀获取对应 API 配置。"""
    try:
        rel_path = file_path.relative_to(base_dir)
    except ValueError:
        rel_path = file_path

    parts = list(rel_path.parts)
    lang = parts[0] if parts else ""

    env_url = f"PLM_API_ZHENG_{lang.upper()}_URL"
    env_key = f"PLM_API_ZHENG_{lang.upper()}_KEY"
    env_token = f"PLM_API_ZHENG_{lang.upper()}_TOKEN"

    url = os.environ.get(env_url, "")
    key = os.environ.get(env_token, "")
    token = os.environ.get(env_token, "")

    if not url:
        print(f"[错误] {env_url} 环境变量未设置")
        sys.exit(1)
    if not key:
        print(f"[错误] {env_key} 环境变量未设置")
        sys.exit(1)

    return {"url": url, "key": key, "token": token}

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
                base_dir: Path = DIST_DIR, timeout: int = 60) -> dict:
    """上传单个文件到云存储 API。

    Args:
        file_path: 文件路径
        dry_run: 如果为 True，只打印不实际上传
        commit_id: Git commit ID（可选）
        base_dir: 基础目录，用于计算相对路径
        timeout: 请求超时时间（秒）

    Returns:
        {"success": bool, "error": str}
    """
    result = {"success": False, "error": ""}
    if not file_path.exists():
        print(f"  [FAIL] 文件不存在: {file_path}")
        result["error"] = "文件不存在"
        return result

    # 从路径提取产品名（倒数第二级目录）
    parts = file_path.parts
    product_name = parts[-2] if len(parts) >= 2 else file_path.stem

    # 标准化路径（去掉 dist/specs/zh/ 等前缀）
    normalized_path = normalize_upload_path(file_path, base_dir)

    # 获取对应语言的 API 配置
    config = get_api_config(file_path, base_dir)

    # 构建完整 URL
    url = f"{config['url']}{API_ENDPOINT}"
    params = DEFAULT_PARAMS.copy()

    # 添加路径参数
    params["path"] = normalized_path

    # 添加 commitId 参数（如果提供）
    if commit_id:
        params["commitId"] = commit_id

    # 准备请求头
    headers = {
        "x-api-key": config["key"]
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
        files["file"][1].close()
        result["success"] = True
        return result

    try:
        response = requests.post(
            url,
            headers=headers,
            params=params,
            files=files,
            timeout=timeout
        )
        response.raise_for_status()

        resp_result = response.json()

        # 检查是否有错误
        if 'error' in resp_result:
            print(f"  [FAIL] 上传失败: {resp_result.get('error')}")
            print(f"  完整响应: {resp_result}")
            result["error"] = resp_result.get('error', 'API 返回错误')
            return result

        print(f"  [OK] 上传成功")
        print(f"  完整响应: {resp_result}")
        result["success"] = True
        return result

    except requests.exceptions.RequestException as e:
        print(f"  [FAIL] 上传失败")
        print(f"    Error type: {type(e).__name__}")
        print(f"    Error detail: {e}")
        print(f"    Request URL: {url}")
        print(f"    Request params: {params}")
        print(f"    Request headers: {headers}")
        if hasattr(e.response, 'text'):
            print(f"    Response: {e.response.text}")
        if hasattr(e, 'request') and e.request:
            print(f"    Request method: {e.request.method}")
            print(f"    Request full URL: {e.request.url}")
        result["error"] = f"{type(e).__name__}: {e}"
        return result
    finally:
        files["file"][1].close()


def _should_upload(file_path: Path) -> bool:
    """判断单个文件是否符合上传规则。"""
    if not file_path.is_file():
        return False
    # 跳过 redirects 目录
    if "redirects" in file_path.parts:
        return False
    # 跳过 Developer Documentation 下的 series.txt
    if file_path.name == "series.txt" and "Developer Documentation" in file_path.parts:
        return False
    # 跳过语言根目录下的站点级索引文件（llms.txt 等）：
    # 它们不属于产品文件，PLM API 也不接受产品目录之外的 path
    if file_path.name == "llms.txt":
        return False
    ext = file_path.suffix.lower()
    if ext in EXCLUDED_EXTENSIONS:
        return False
    # 排除 Manuals 目录下的所有文件
    if any(p.lower() == "manuals" for p in file_path.parts):
        return False
    # Datasheets 目录下只保留 PDF
    if any(p.lower() == "datasheets" for p in file_path.parts) and ext != ".pdf":
        return False
    return True


def find_upload_files(directory: Path) -> List[Path]:
    """递归查找目录下所有需要上传的文件（全量，只处理 zh/ 和 en/ 子目录）。"""
    if not directory.exists():
        return []

    upload_files = []
    for lang_dir in ["zh", "en"]:
        lang_path = directory / lang_dir
        if lang_path.exists():
            for file_path in lang_path.rglob("*"):
                if _should_upload(file_path):
                    upload_files.append(file_path)
    return upload_files


def find_changed_files(directory: Path) -> List[Path]:
    """基于 git diff 只获取本次变更的文件（增量）。

    读取 GITHUB_EVENT_BEFORE 环境变量，执行 git diff --name-only。
    如果环境变量不存在，则回退到全量上传。
    """
    before = os.environ.get("GITHUB_EVENT_BEFORE", "").strip()
    if not before:
        print("[INFO] GITHUB_EVENT_BEFORE 未设置，回退到全量上传")
        return find_upload_files(directory)

    try:
        result = subprocess.run(
            ["git", "-c", "core.quotePath=false", "diff", "--name-only", "--diff-filter=ACMRT", before, "HEAD"],
            capture_output=True, text=True, check=True, cwd=directory.parent if directory.exists() else "."
        )
        changed_paths = [p.strip() for p in result.stdout.strip().split("\n") if p.strip()]
    except subprocess.CalledProcessError as e:
        print(f"[WARN] git diff 失败: {e}")
        print("[INFO] 回退到全量上传")
        return find_upload_files(directory)

    # 与全量模式(find_upload_files)保持一致：只处理 {dist_dir}/zh、{dist_dir}/en
    # 下的文件。仓库其他位置的变更（scripts/、workflow 等）没有对应的语言 API。
    lang_prefixes = tuple(f"{directory.as_posix()}/{lang}/" for lang in ("zh", "en"))

    upload_files = []
    for rel_path in changed_paths:
        if not rel_path.replace("\\", "/").startswith(lang_prefixes):
            continue
        file_path = directory.parent / rel_path if directory.exists() else Path(rel_path)
        if file_path.exists() and _should_upload(file_path):
            upload_files.append(file_path)

    if not upload_files:
        print("[INFO] 本次变更中没有需要上传的文件")
    else:
        print(f"[INFO] 本次变更涉及 {len(changed_paths)} 个文件，其中 {len(upload_files)} 个需要上传")
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
    parser.add_argument(
        "--incremental",
        action="store_true",
        help="增量模式，只上传 git diff 中有变更的文件（默认全量）"
    )
    args = parser.parse_args()

    # 确定要上传的文件列表
    if args.file:
        upload_files_list = [args.file]
    elif args.incremental:
        upload_files_list = find_changed_files(args.dist_dir)
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

    # 第一轮上传
    success_count = 0
    failed_first_round = []

    for upload_file_path in upload_files_list:
        result = upload_file(upload_file_path, dry_run=args.dry_run, commit_id=commit_id,
                             base_dir=args.dist_dir, timeout=60)
        if result.get("success"):
            success_count += 1
        else:
            failed_first_round.append(upload_file_path)
        print()

    # 第二轮：重试第一轮失败的，使用更长超时
    failed_second_round = []
    if failed_first_round and not args.dry_run:
        print(f"=== 第二轮重试 {len(failed_first_round)} 个失败文件（超时 180 秒）===\n")
        for upload_file_path in failed_first_round:
            print(f"  [RETRY] {upload_file_path.name}")
            result = upload_file(upload_file_path, dry_run=args.dry_run, commit_id=commit_id,
                                 base_dir=args.dist_dir, timeout=180)
            if result.get("success"):
                success_count += 1
            else:
                failed_second_round.append(upload_file_path)
            print()

    # 汇总
    print("=" * 50)
    if args.dry_run:
        print(f"[DRY RUN] 预览完成，实际将上传: {success_count} 个文件")
    else:
        total_failed = len(failed_second_round)
        print(f"上传完成: {success_count} 成功, {total_failed} 失败")
        print(f"总计处理: {success_count + total_failed}/{len(upload_files_list)}")
        if total_failed > 0:
            print("\n最终失败的文件:")
            for f in failed_second_round:
                print(f"  - {f}")
    print("=" * 50)

    # 只有全部失败才退出报错
    if success_count == 0 and len(upload_files_list) > 0:
        print("[ERROR] 全部上传失败")
        sys.exit(1)


if __name__ == "__main__":
    main()
