#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
规格文档自动同步：检测 docs/ 下变更的 Datasheets md，自动更新 WordPress 产品规格属性。

流程：
  1. git diff 检查变更的 Datasheets md 文件
  2. 从路径提取产品型号和语言
  3. WP API 搜索产品名 → 得到产品 ID
  4. parse_tables 提取规格属性
  5. upload_specs 更新 WooCommerce 属性

用法：
  python sync_specs.py                         # 自动检测变更
  python sync_specs.py --md-path docs/zh/CPE02/Datasheets/通用/CPE02规格书_V1.0.md  # 指定文件
"""

import argparse
import base64
import json
import os
import re
import subprocess
import sys
from pathlib import Path

import requests

# 项目路径
REPO_ROOT = Path(__file__).resolve().parent.parent
SPECS_PKG = REPO_ROOT / "onboarding" / "specs-import"

# LLM 配置（用于 AI 审查产品匹配）
LLM_API_URL = os.environ.get("LLM_API_URL", "")
LLM_API_KEY = os.environ.get("LLM_API_KEY", "")

# 站点配置（从环境变量读取）
SITES = {
    "zh": {
        "wp_url": os.environ.get("WP_ZH_URL", ""),
        "icon_url": os.environ.get("WP_ZH_ICON_URL", ""),
        "template_id": int(os.environ.get("WP_ZH_TEMPLATE_ID", "0")),
    },
    "en": {
        "wp_url": os.environ.get("WP_EN_URL", ""),
        "icon_url": os.environ.get("WP_EN_ICON_URL", ""),
        "template_id": int(os.environ.get("WP_EN_TEMPLATE_ID", "0")),
    },
}

# Datasheets 目录名的中英文变体
DATASHEET_DIRS = {"datasheets", "specifications", "specs", "规格书"}


def log(msg):
    print(f"[SYNC] {msg}", flush=True)


def get_changed_datasheet_files() -> list:
    """从 git diff 获取变更的 Datasheets md 文件"""
    # 支持 push（HEAD~1..HEAD）和手动指定 sha
    before = os.environ.get("GITHUB_EVENT_BEFORE", "")
    after = os.environ.get("GITHUB_SHA", "HEAD")

    if before:
        cmd = ["git", "diff", "--name-only", "--diff-filter=ACMRT", before, after]
    else:
        cmd = ["git", "diff", "--name-only", "--diff-filter=ACMRT", "HEAD~1", "HEAD"]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        all_files = [f.strip() for f in result.stdout.strip().split("\n") if f.strip()]
    except subprocess.CalledProcessError:
        log("git diff 失败，尝试从环境变量获取")
        return []

    # 过滤：docs/{zh|en}/{Product}/Datasheets/**/*.md
    datasheet_files = []
    for f in all_files:
        parts = f.split("/")
        if len(parts) < 5:
            continue
        if parts[0] != "docs" or parts[1] not in ("zh", "en"):
            continue
        # 检查是否在 Datasheets 目录下
        if parts[3].lower() in DATASHEET_DIRS or "datasheet" in parts[3].lower():
            if f.endswith(".md"):
                datasheet_files.append(f)

    return datasheet_files


def parse_path(file_path: str) -> dict:
    """从 md 路径提取产品型号和语言
    例：docs/zh/CPE02/Datasheets/通用/CPE02规格书_V1.0.md
    → {'site': 'zh', 'product': 'CPE02', 'path': '...'}
    """
    parts = file_path.split("/")
    if len(parts) < 4 or parts[0] != "docs":
        return None

    site = parts[1]
    product = parts[2]

    if site not in ("zh", "en"):
        return None

    return {
        "site": site,
        "product": product,
        "path": file_path,
    }


def basic_auth(username: str, password: str) -> str:
    return "Basic " + base64.b64encode(f"{username}:{password}".encode()).decode()


def ai_review_match(product_name: str, candidates: list) -> dict:
    """用 LLM 审查多个候选产品，返回最匹配的 {id, name}"""
    if not LLM_API_URL or not LLM_API_KEY:
        log("LLM API 未配置，跳过 AI 审查")
        return None

    # 构建候选列表
    candidate_list = "\n".join([f"- ID={c['id']}, name=\"{c['name']}\"" for c in candidates])

    prompt = f"""产品型号 "{product_name}" 需要匹配到 WordPress 产品。

候选产品列表：
{candidate_list}

请判断哪个产品最匹配 "{product_name}"。只返回最匹配产品的 ID 数字，不匹配则返回 0。
例如：123"""

    try:
        headers = {
            "Authorization": f"Bearer {LLM_API_KEY}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": os.environ.get("LLM_MODEL", "deepseek-v4-flash"),
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 100,
        }
        r = requests.post(LLM_API_URL, json=payload, headers=headers, timeout=30)
        if r.status_code != 200:
            log(f"LLM API 失败: HTTP {r.status_code}")
            return None

        result = r.json()
        text = result.get("choices", [{}])[0].get("message", {}).get("content", "").strip()

        # 提取数字
        match = re.search(r"\d+", text)
        if match:
            selected_id = int(match.group())
            if selected_id == 0:
                log(f"AI 审查：无匹配产品")
                return None
            for c in candidates:
                if c["id"] == selected_id:
                    log(f"AI 审查：选择 {c['name']} (ID={selected_id})")
                    return c
            log(f"AI 审查：返回 ID {selected_id} 不在候选列表中")
            return None

        log(f"AI 审查：无法解析返回值: {text}")
        return None

    except Exception as e:
        log(f"AI 审查异常: {e}")
        return None


def find_product_by_name(product_name: str, site: str) -> dict:
    """调 WP API 搜索产品，返回 {id, name} 或 None"""
    wp_url = SITES[site].get("wp_url", "")
    if not wp_url:
        log(f"警告：{site} 站点 WP_URL 未配置")
        return None

    # 从环境变量获取认证
    env_map = {"zh": ("WP_ZH_URL", "WP_ZH_APP_PASSWORD"), "en": ("WP_EN_URL", "WP_EN_APP_PASSWORD")}
    pw = os.environ.get(env_map[site][1], "")
    if not pw:
        log(f"警告：{env_map[site][1]} 未配置")
        return None

    auth = basic_auth("admin", pw)
    headers = {"Authorization": auth, "Accept": "application/json"}

    # 搜索产品
    try:
        r = requests.get(
            f"{wp_url}/wp-json/wc/v3/products",
            headers=headers,
            params={"search": product_name, "per_page": 20, "status": "publish,draft"},
            timeout=30,
        )
        if r.status_code != 200:
            log(f"WP API 搜索失败: HTTP {r.status_code}")
            return None

        products = r.json()
        if not products:
            log(f"未找到产品：{product_name}")
            return None

        # 精确匹配（不区分大小写）
        name_lower = product_name.lower()
        exact = [p for p in products if p["name"].lower() == name_lower]
        if len(exact) == 1:
            return {"id": exact[0]["id"], "name": exact[0]["name"]}

        # 包含匹配
        contains = [p for p in products if name_lower in p["name"].lower()]
        if len(contains) == 1:
            return {"id": contains[0]["id"], "name": contains[0]["name"]}

        # 多个候选 → AI 审查
        if len(contains) > 1:
            log(f"找到 {len(contains)} 个候选产品，调 AI 审查...")
            candidates = [{"id": p["id"], "name": p["name"]} for p in contains]
            return ai_review_match(product_name, candidates)

        log(f"未精确匹配产品：{product_name}（搜索到 {len(products)} 个，但都不匹配）")
        return None

    except Exception as e:
        log(f"WP API 搜索异常: {e}")
        return None


def extract_specs(md_path: str) -> list:
    """从 md 文件提取规格属性"""
    file_path = Path(md_path)
    if not file_path.exists():
        log(f"文件不存在: {md_path}")
        return []

    content = file_path.read_text(encoding="utf-8")

    # 动态导入 batch_extract
    sys.path.insert(0, str(SPECS_PKG))
    from batch_extract import parse_tables

    attrs = parse_tables(content)
    log(f"提取到 {len(attrs)} 个规格属性组")
    return attrs


def upload_specs(product_id: int, attrs: list, site: str):
    """调用 upload_specs.py 上传规格属性"""
    if not attrs:
        log("无规格属性可上传")
        return

    # 保存临时 JSON
    tmp_file = REPO_ROOT / f"tmp_specs_{product_id}.json"
    with open(tmp_file, "w", encoding="utf-8") as f:
        json.dump(attrs, f, ensure_ascii=False, indent=2)

    try:
        env = os.environ.copy()
        env["WP_SITE"] = site
        env["WP_URL"] = SITES[site]["wp_url"]
        env["WP_USER"] = "admin"
        env["WP_APP_PASSWORD"] = os.environ.get(f"WP_{site.upper()}_APP_PASSWORD", "")
        env["PYTHONIOENCODING"] = "utf-8"

        cmd = [sys.executable, str(SPECS_PKG / "upload_specs.py"), str(product_id), str(tmp_file)]
        result = subprocess.run(
            cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", env=env
        )

        log(f"stdout:\n{result.stdout}")
        if result.stderr:
            log(f"stderr:\n{result.stderr}")

        if result.returncode != 0:
            log(f"upload_specs.py 失败: exit {result.returncode}")

    finally:
        if tmp_file.exists():
            tmp_file.unlink()


def sync_file(file_path: str):
    """同步单个 md 文件的规格到 WordPress"""
    info = parse_path(file_path)
    if not info:
        log(f"无法解析路径: {file_path}")
        return

    site = info["site"]
    product_name = info["product"]

    log(f"处理: {file_path} (site={site}, product={product_name})")

    # 搜索产品
    product = find_product_by_name(product_name, site)
    if not product:
        log(f"跳过: 未找到 {product_name} 在 {site} 站点")
        return

    product_id = product["id"]
    log(f"匹配产品: {product['name']} (ID={product_id})")

    # 提取规格
    attrs = extract_specs(file_path)
    if not attrs:
        log(f"跳过: {file_path} 未提取到规格属性")
        return

    # 上传
    upload_specs(product_id, attrs, site)
    log(f"完成: {product_name} 规格已更新")


def main():
    parser = argparse.ArgumentParser(description="规格文档自动同步到 WordPress")
    parser.add_argument("--md-path", help="指定单个 md 文件路径（跳过 git diff）")
    args = parser.parse_args()

    log("=== 规格文档自动同步 ===")

    if args.md_path:
        files = [args.md_path]
    else:
        files = get_changed_datasheet_files()

    if not files:
        log("没有变更的 Datasheets md 文件")
        return

    log(f"检测到 {len(files)} 个变更文件:")
    for f in files:
        log(f"  - {f}")

    success = 0
    failed = 0
    skipped = 0

    for f in files:
        try:
            info = parse_path(f)
            if not info:
                log(f"跳过: 无法解析路径 {f}")
                skipped += 1
                continue

            product = find_product_by_name(info["product"], info["site"])
            if not product:
                skipped += 1
                continue

            attrs = extract_specs(f)
            if not attrs:
                skipped += 1
                continue

            upload_specs(product["id"], attrs, info["site"])
            success += 1
        except Exception as e:
            log(f"错误: {f} - {e}")
            failed += 1

    log(f"\n=== 同步完成 ===")
    log(f"成功: {success}, 失败: {failed}, 跳过: {skipped}")


if __name__ == "__main__":
    main()
