#!/usr/bin/env python3
"""WordPress 资源条目同步脚本（可选 Phase 5）。

通过 WordPress REST API 自动创建/更新资源条目（WP Job Manager），
使资源中心前端能自动展示新上传的规格书和下载文件。

使用 WordPress Application Password 进行鉴权。
"""

import base64
import json
import os
import subprocess
import sys
from pathlib import Path

import requests

WP_API_URL = os.getenv("WP_API_URL", "").rstrip("/")
WP_API_USER = os.getenv("WP_API_USER", "")
WP_API_TOKEN = os.getenv("WP_API_TOKEN", "")

# 资源在 WordPress 服务器上的 URL 前缀
WP_RESOURCE_URL_BASE = os.getenv("WP_RESOURCE_URL_BASE", "/wp-content/uploads/resources")


def get_auth_headers():
    """生成 WordPress Application Password 鉴权头"""
    credentials = base64.b64encode(f"{WP_API_USER}:{WP_API_TOKEN}".encode()).decode()
    return {
        "Authorization": f"Basic {credentials}",
        "Content-Type": "application/json",
    }


def get_changed_files(base_dir):
    """获取指定目录下本次提交变更的文件"""
    try:
        cmd = ["git", "diff", "--name-only", "HEAD~1", "HEAD"]
        output = subprocess.check_output(cmd).decode("utf-8")
        files = output.splitlines()
        return [f for f in files if f.startswith(base_dir) and os.path.exists(f)]
    except Exception as e:
        print(f"⚠️ Git 获取差异失败: {e}")
        return []


def find_existing_listing(title):
    """查找 WordPress 中是否已有同名资源条目"""
    resp = requests.get(
        f"{WP_API_URL}/wp/v2/job-listings",
        params={"search": title, "per_page": 5},
        headers=get_auth_headers(),
        timeout=30,
    )
    resp.raise_for_status()
    listings = resp.json()
    for listing in listings:
        if listing.get("title", {}).get("rendered", "").strip() == title:
            return listing["id"]
    return None


def create_or_update_listing(title, download_url, description="", listing_id=None):
    """创建或更新 WordPress 资源条目"""
    payload = {
        "title": title,
        "status": "publish",
        "content": description,
        "meta": {
            "_download_url": download_url,
        },
    }

    if listing_id:
        resp = requests.put(
            f"{WP_API_URL}/wp/v2/job-listings/{listing_id}",
            json=payload,
            headers=get_auth_headers(),
            timeout=30,
        )
        action = "更新"
    else:
        resp = requests.post(
            f"{WP_API_URL}/wp/v2/job-listings",
            json=payload,
            headers=get_auth_headers(),
            timeout=30,
        )
        action = "创建"

    resp.raise_for_status()
    print(f"  ✅ {action}成功: {title} (ID: {resp.json().get('id')})")
    return resp.json().get("id")


def sync_resources(resource_type):
    """同步指定类型的资源到 WordPress

    Args:
        resource_type: "specs" 或 "downloads"
    """
    if not WP_API_URL or not WP_API_TOKEN:
        print(f"⚠️ WordPress API 配置缺失，跳过 {resource_type} 资源同步。")
        return

    # 对于 specs，已构建的 PDF 在 dist/specs/；对于 downloads，原始文件在 downloads/
    if resource_type == "specs":
        base_dir = "dist/specs"
        url_prefix = f"{WP_RESOURCE_URL_BASE}/specs"
    else:
        base_dir = "downloads"
        url_prefix = f"{WP_RESOURCE_URL_BASE}/downloads"

    changed_files = get_changed_files(
        "specs/" if resource_type == "specs" else "downloads/"
    )

    if not changed_files:
        print(f"✅ 本次提交未涉及 {resource_type} 变更，无需同步。")
        return

    print(f"=== 同步 {resource_type} 资源到 WordPress ===\n")

    for filepath in changed_files:
        filename = os.path.basename(filepath)
        # 从路径提取产品名（倒数第二级目录）
        parts = Path(filepath).parts
        product_name = parts[-2] if len(parts) >= 3 else filename

        title = f"{product_name} - {filename}"
        rel_path = filepath.replace("specs/", "").replace("downloads/", "")
        download_url = f"{url_prefix}/{rel_path}"

        print(f"处理: {filepath}")

        try:
            existing_id = find_existing_listing(title)
            create_or_update_listing(title, download_url, listing_id=existing_id)
        except requests.RequestException as e:
            print(f"  ❌ 同步失败: {e}")

    print(f"\n🎉 {resource_type} 资源同步完成！")


def main():
    if len(sys.argv) < 2:
        print("用法: python wp_sync.py <specs|downloads>")
        sys.exit(1)

    resource_type = sys.argv[1]
    if resource_type not in ("specs", "downloads"):
        print(f"❌ 不支持的资源类型: {resource_type}")
        sys.exit(1)

    sync_resources(resource_type)


if __name__ == "__main__":
    main()
