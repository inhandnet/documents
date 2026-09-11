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

# 本地配置加载（优先环境变量，其次 config.json）
LOCAL_CONFIG = {}
_config_path = Path(__file__).resolve().parent / "config.json"
if _config_path.exists():
    try:
        LOCAL_CONFIG = json.loads(_config_path.read_text(encoding="utf-8"))
    except Exception:
        pass

# 项目路径
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
SPECS_PKG = REPO_ROOT / "auto-import" / "onboarding" / "specs-import"

# LLM 配置（用于 AI 审查产品匹配）
LLM_API_URL = os.environ.get("LLM_API_URL", "") or LOCAL_CONFIG.get("llm", {}).get("api_url", "")
LLM_API_KEY = os.environ.get("LLM_API_KEY", "") or LOCAL_CONFIG.get("llm", {}).get("api_key", "")
LLM_MODEL = os.environ.get("LLM_MODEL", "") or LOCAL_CONFIG.get("llm", {}).get("model", "deepseek-v4-flash")

# 站点配置（从环境变量或 config.json 读取）
_sites_config = LOCAL_CONFIG.get("sites", {})
SITES = {
    "zh": {
        "wp_url": os.environ.get("WP_ZH_URL", "") or _sites_config.get("zh", {}).get("wp_url", ""),
        "icon_url": os.environ.get("WP_ZH_ICON_URL", ""),
        "template_id": int(os.environ.get("WP_ZH_TEMPLATE_ID", "0")),
    },
    "en": {
        "wp_url": os.environ.get("WP_EN_URL", "") or _sites_config.get("en", {}).get("wp_url", ""),
        "icon_url": os.environ.get("WP_EN_ICON_URL", ""),
        "template_id": int(os.environ.get("WP_EN_TEMPLATE_ID", "0")),
    },
}

# Datasheets 目录名的中英文变体
DATASHEET_DIRS = {"datasheets", "specifications", "specs", "规格书"}

# Poweris API 配置（中英文站分开）
POWERIS_ZH_BASE = os.environ.get("POWERIS_ZH_BASE", "")
POWERIS_ZH_KEY = os.environ.get("POWERIS_ZH_KEY", "")
POWERIS_EN_BASE = os.environ.get("POWERIS_EN_BASE", "")
POWERIS_EN_KEY = os.environ.get("POWERIS_EN_KEY", "")


def log(msg):
    print(f"[SYNC] {msg}", flush=True)


def decode_git_path(path: str) -> str:
    """解码 git 输出的八进制转义路径（如 \\351\\200\\236 → 通用）"""
    parts = re.split(r'(\\[0-9]{3})', path)
    result = []
    for part in parts:
        if part.startswith('\\') and len(part) == 4:
            result.append(bytes([int(part[1:], 8)]))
        else:
            result.append(part.encode('utf-8'))
    return b''.join(result).decode('utf-8')


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
        all_files = [decode_git_path(f.strip().strip('"')) for f in result.stdout.strip().split("\n") if f.strip()]
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
    """从 md 路径提取产品型号、语言和子目录
    例：docs/zh/CPE02/Datasheets/通用/CPE02规格书_V1.0.md
    → {'site': 'zh', 'product': 'CPE02', 'subdir': '通用', 'path': '...'}
    """
    parts = file_path.split("/")
    if len(parts) < 4 or parts[0] != "docs":
        return None

    site = parts[1]
    product = parts[2]
    # 子目录名（Datasheets 下的一级目录，如 通用、General、Rail、Road）
    subdir = parts[4] if len(parts) > 4 else ""

    if site not in ("zh", "en"):
        return None

    return {
        "site": site,
        "product": product,
        "subdir": subdir,
        "path": file_path,
    }


def basic_auth(username: str, password: str) -> str:
    return "Basic " + base64.b64encode(f"{username}:{password}".encode()).decode()


def ai_review_match(product_name: str, candidates: list, md_content: str = None) -> dict:
    """用 LLM 审查多个候选产品，返回最匹配的 {id, name}"""
    if not LLM_API_URL or not LLM_API_KEY:
        log("LLM API 未配置，跳过 AI 审查")
        return None

    # 构建候选列表（简化格式）
    candidate_lines = []
    for c in candidates:
        candidate_lines.append(f"ID={c['id']} name={c['name']}")
    candidate_list = ", ".join(candidate_lines)

    # 如果有 md 内容，传给 AI 参考
    content_hint = ""
    if md_content:
        # 取前 500 字符作为提示
        content_hint = f"\n文档前500字：{md_content[:500]}"

    prompt = f"""文档路径里的产品型号是 "{product_name}"，但文档内容里的产品型号可能不同。
请根据候选列表和文档内容，判断文档实际对应哪个产品。只返回数字ID，不匹配返回0。
候选：{candidate_list}{content_hint}
答案："""

    try:
        headers = {
            "Authorization": f"Bearer {LLM_API_KEY}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": os.environ.get("LLM_MODEL", "deepseek-v4-flash"),
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 500,
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


def ai_extract_product_models(md_content: str) -> list:
    """让 LLM 从 md 内容分析出产品型号列表"""
    if not LLM_API_URL or not LLM_API_KEY:
        return []

    prompt = f"""从下面的规格书内容中，提取所有出现的产品型号/产品名称。
只返回型号列表，每行一个，不要其他内容。
例如：
EC300
EC312
EC5000

规格书内容：
{md_content[:3000]}"""

    try:
        headers = {
            "Authorization": f"Bearer {LLM_API_KEY}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": LLM_MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 200,
        }
        r = requests.post(LLM_API_URL, json=payload, headers=headers, timeout=30)
        if r.status_code != 200:
            return []

        result = r.json()
        text = result.get("choices", [{}])[0].get("message", {}).get("content", "").strip()

        # 每行一个型号
        models = [line.strip() for line in text.split("\n") if line.strip()]
        return models

    except Exception as e:
        log(f"AI 提取型号异常: {e}")
        return []


def find_product_via_poweris(dir_name: str, subdir: str = "", lang: str = "en") -> str:
    """通过 poweris ext-mapping API 查询文档目录名对应的网站产品名。

    中英文站用不同的 poweris API 地址和凭证。
    如果返回多个产品名（如 VG814 → [VG814-Rail, VG814-Road]），
    用子目录名匹配：subdir=Rail 匹配 VG814-Rail（不区分大小写）。
    """
    if lang == "zh":
        api_base, api_key = POWERIS_ZH_BASE, POWERIS_ZH_KEY
    else:
        api_base, api_key = POWERIS_EN_BASE, POWERIS_EN_KEY

    if not api_base or not api_key:
        log(f"警告：poweris {lang} API 未配置")
        return None

    try:
        headers = {"x-api-key": api_key}
        r = requests.get(
            f"{api_base}/api/plm/product/series/ext-mapping/names",
            params={"platform": "website", "name": dir_name},
            headers=headers, timeout=10,
        )
        if r.status_code != 200:
            return None

        data = r.json()
        result = data.get("result", [])
        if not result or not isinstance(result, list):
            return None

        if len(result) == 1:
            website_name = result[0]
            log(f"poweris 映射: {dir_name} → {website_name}")
            return website_name

        # 多个映射 → 用子目录名匹配
        if subdir:
            subdir_lower = subdir.lower()
            for name in result:
                if subdir_lower in name.lower():
                    log(f"poweris 映射(按子目录): {dir_name}/{subdir} → {name}")
                    return name

        log(f"poweris 返回 {len(result)} 个映射但无法确定: {result}")
        return None
    except Exception as e:
        log(f"poweris API 异常: {e}")
        return None


def find_product_by_name(product_name: str, site: str, md_content: str = None, subdir: str = "") -> dict:
    """搜索产品，返回 {id, name} 或 None。

    优先使用 poweris ext-mapping API 查询目录名对应的网站产品名，
    然后用网站产品名搜索 WordPress。如果 poweris 查不到，回退到 WP 搜索 + LLM。
    """
    # 第一步：通过 poweris API 查询目录名对应的网站产品名
    website_name = find_product_via_poweris(product_name, subdir, lang=site)
    if website_name:
        log(f"poweris 映射成功: {product_name} → {website_name}")
        # 用网站产品名搜索 WordPress
        product = search_wp_product(website_name, site)
        if product:
            return product
        log(f"poweris 映射到 {website_name}，但 WP 未找到，尝试回退搜索...")

    # 第二步：回退到原有逻辑（WP 搜索 + LLM）
    log(f"poweris 未映射，回退到 WP 搜索: {product_name}")
    return search_wp_product(product_name, site, md_content)


def search_wp_product(product_name: str, site: str, md_content: str = None) -> dict:
    """在 WordPress 中搜索产品，返回 {id, name} 或 None"""
    wp_url = SITES[site].get("wp_url", "")
    if not wp_url:
        log(f"警告：{site} 站点 WP_URL 未配置")
        return None

    # 从环境变量或 config.json 获取认证
    env_map = {"zh": "WP_ZH_APP_PASSWORD", "en": "WP_EN_APP_PASSWORD"}
    pw = os.environ.get(env_map[site], "") or _sites_config.get(site, {}).get("wp_app_password", "")
    if not pw:
        log(f"警告：{env_map[site]} 未配置")
        return None

    wp_user = _sites_config.get(site, {}).get("wp_user", "admin")
    auth = basic_auth(wp_user, pw)
    headers = {"Authorization": auth, "Accept": "application/json"}

    # 搜索产品（用路径型号作为关键词）
    try:
        # WC API status 参数只接受单个值，用 search 搜索所有状态
        r = requests.get(
            f"{wp_url}/wp-json/wc/v3/products",
            headers=headers,
            params={"search": product_name, "per_page": 20},
            timeout=30,
        )
        if r.status_code != 200:
            log(f"WP API 搜索失败: HTTP {r.status_code}")
            return None

        products = r.json()
        if not products:
            log(f"未搜索到产品：{product_name}")
        else:
            # 精确匹配（不区分大小写）→ 直接用
            name_lower = product_name.lower()
            exact = [p for p in products if p["name"].lower() == name_lower]
            if len(exact) == 1:
                return {"id": exact[0]["id"], "name": exact[0]["name"]}

            # 有搜索结果但不是精确匹配 → AI 审查
            log(f"搜索到 {len(products)} 个产品但无精确匹配，调 AI 审查...")
            candidates = [{"id": p["id"], "name": p["name"]} for p in products]
            result = ai_review_match(product_name, candidates, md_content)
            if result:
                return result

        # 没搜到或 AI 审查无结果 → 读 md 内容，LLM 分析型号
        if md_content and LLM_API_URL and LLM_API_KEY:
            log(f"字符串匹配失败，调 LLM 从 md 内容分析型号...")
            models = ai_extract_product_models(md_content)
            if models:
                log(f"LLM 分析出型号: {models}")
                # 用分析出的型号搜索 WP
                for model in models:
                    r2 = requests.get(
                        f"{wp_url}/wp-json/wc/v3/products",
                        headers=headers,
                        params={"search": model, "per_page": 5},
                        timeout=30,
                    )
                    if r2.status_code == 200:
                        for p in r2.json():
                            if p["name"].lower() == model.lower() or model.lower() in p["name"].lower():
                                log(f"LLM 匹配成功: {p['name']} (ID={p['id']})")
                                return {"id": p["id"], "name": p["name"]}

        log(f"未匹配产品：{product_name}")
        return None

    except Exception as e:
        log(f"WP API 搜索异常: {e}")
        return None


def extract_specs(md_path: str) -> list:
    """从 md 文件提取规格属性（合并相同 slug 的属性组）"""
    file_path = Path(md_path)
    if not file_path.exists():
        log(f"文件不存在: {md_path}")
        return []

    content = file_path.read_text(encoding="utf-8")

    # 动态导入 batch_extract
    sys.path.insert(0, str(SPECS_PKG))
    from batch_extract import parse_tables

    raw_attrs = parse_tables(content)
    log(f"提取到 {len(raw_attrs)} 个规格属性组（原始）")

    # 合并相同 slug 的属性组
    merged = {}
    for a in raw_attrs:
        slug = a["slug"]
        if slug in merged:
            # 合并 options 和 optionValues
            existing = merged[slug]
            existing["options"] = list(set(existing["options"] + a.get("options", [])))
            existing["optionValues"].update(a.get("optionValues", {}))
        else:
            merged[slug] = {
                "name": a.get("name", ""),
                "slug": slug,
                "options": list(a.get("options", [])),
                "optionValues": dict(a.get("optionValues", {})),
                "visible": a.get("visible", True),
                "variation": a.get("variation", False),
                "position": a.get("position", 0),
            }

    result = list(merged.values())
    log(f"合并后 {len(result)} 个规格属性组")
    return result


def get_existing_specs(product_id: int, site: str) -> dict:
    """获取产品现有规格属性"""
    wp_url = SITES[site].get("wp_url", "")
    if not wp_url:
        return {}

    env_map = {"zh": "WP_ZH_APP_PASSWORD", "en": "WP_EN_APP_PASSWORD"}
    pw = os.environ.get(env_map[site], "") or _sites_config.get(site, {}).get("wp_app_password", "")
    if not pw:
        return {}

    auth = basic_auth(_sites_config.get(site, {}).get("wp_user", "admin"), pw)

    try:
        r = requests.get(
            f"{wp_url}/wp-json/wc/v3/products/{product_id}",
            headers={"Authorization": auth, "Accept": "application/json"},
            timeout=30,
        )
        if r.status_code != 200:
            return {}

        product = r.json()
        attrs = product.get("attributes", [])

        # 构建属性字典 {slug: {name, options}}
        existing = {}
        for a in attrs:
            existing[a["slug"]] = {
                "name": a["name"],
                "options": sorted(a.get("options", [])),
            }
        return existing

    except Exception:
        return {}


def normalize_slug(slug: str) -> str:
    """统一 slug 格式：去掉 pa_ 前缀"""
    return slug[3:] if slug.startswith("pa_") else slug


def has_specs_changed(new_attrs: list, existing: dict) -> bool:
    """对比新旧规格，判断是否有变化"""
    if not existing:
        return True  # 现有为空，需要更新

    # 构建新属性字典（统一 slug 格式）
    new_dict = {}
    for a in new_attrs:
        norm_slug = normalize_slug(a["slug"])
        if norm_slug in new_dict:
            # 重复的 slug（如 wi-fi），合并 options
            new_dict[norm_slug]["options"] = sorted(
                set(new_dict[norm_slug]["options"]) | set(a.get("options", []))
            )
        else:
            new_dict[norm_slug] = {
                "name": a.get("name", ""),
                "options": sorted(a.get("options", [])),
            }

    # 构建现有属性字典（统一 slug 格式）
    existing_dict = {}
    for slug, info in existing.items():
        norm_slug = normalize_slug(slug)
        existing_dict[norm_slug] = info

    # 对比
    if set(new_dict.keys()) != set(existing_dict.keys()):
        log(f"属性组数量不同: 新={len(new_dict)}, 现有={len(existing_dict)}")
        return True

    for slug in new_dict:
        if new_dict[slug]["options"] != existing_dict[slug]["options"]:
            log(f"属性组 '{slug}' 选项有变化: 新={len(new_dict[slug]['options'])}, 现有={len(existing_dict[slug]['options'])}")
            return True

    return False


def upload_specs(product_id: int, attrs: list, site: str, force: bool = False):
    """增量上传规格属性（对比现有规格，只在有变化时更新）。
    失败重试 3 次，仍失败则抛出异常。
    """
    if not attrs:
        log("无规格属性可上传")
        return

    # 获取现有规格
    existing = get_existing_specs(product_id, site)
    log(f"现有规格: {len(existing)} 个属性组")

    # 对比
    if not force and not has_specs_changed(attrs, existing):
        log("规格无变化，跳过上传")
        return

    log("检测到规格变化，开始上传...")
    # 保存临时 JSON
    tmp_file = REPO_ROOT / f"tmp_specs_{product_id}.json"
    with open(tmp_file, "w", encoding="utf-8") as f:
        json.dump(attrs, f, ensure_ascii=False, indent=2)

    max_retries = 3
    for attempt in range(1, max_retries + 1):
        try:
            env = os.environ.copy()
            env["WP_SITE"] = site
            env["WP_URL"] = SITES[site]["wp_url"]
            env["WP_USER"] = os.environ.get(f"WP_{site.upper()}_USER", "admin")
            env["WP_APP_PASSWORD"] = os.environ.get(f"WP_{site.upper()}_APP_PASSWORD", "")
            env["PYTHONIOENCODING"] = "utf-8"

            cmd = [sys.executable, str(SPECS_PKG / "upload_specs.py"), str(product_id), str(tmp_file)]
            result = subprocess.run(
                cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", env=env
            )

            log(f"stdout:\n{result.stdout}")
            if result.stderr:
                log(f"stderr:\n{result.stderr}")

            if result.returncode == 0:
                log("上传成功")
                break
            else:
                log(f"upload_specs.py 失败 (attempt {attempt}/{max_retries}): exit {result.returncode}")
                if attempt < max_retries:
                    import time
                    time.sleep(5)
                else:
                    raise RuntimeError(f"upload_specs.py 重试 {max_retries} 次后仍失败")

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

    # 读取 md 内容（用于 LLM 分析型号）
    md_content = ""
    try:
        md_content = Path(file_path).read_text(encoding="utf-8")
    except Exception:
        pass

    # 搜索产品（poweris 映射 → WP 搜索 → LLM 回退）
    product = find_product_by_name(product_name, site, md_content=md_content, subdir=info.get("subdir", ""))
    if not product:
        log(f"跳过: 未匹配到产品（路径: {product_name}）")
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
