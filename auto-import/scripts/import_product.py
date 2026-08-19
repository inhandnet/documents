#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
新产品自动导入：从 GitHub 仓库的规格书 md 一键生成 WordPress 产品页草稿。

流程：
  1. 从 GitHub 拉取 md 内容
  2. 调 Claude API 提取闪光点（含选图标）
  3. 生成 products_{lang}/{model}.json
  4. 调用 node clone_highlights.js 克隆产品，得到新 ID
  5. 从 md 提取规格属性
  6. 调用 upload_specs.py 上传规格

用法：
  python import_product.py --md-path docs/zh/IG532/Datasheets/通用/IG532规格书_V1.0.md \
                           --site zh \
                           --product IG532
"""

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

# 依赖
import requests

# LLM 配置（OpenAI 兼容格式，支持阿里云 DeepSeek 等）
LLM_API_URL = os.environ.get("LLM_API_URL", "https://llm-tg3jkhnwwk1q7xif.cn-beijing.maas.aliyuncs.com/compatible-mode/v1/chat/completions")
LLM_API_KEY = os.environ.get("LLM_API_KEY", "")
LLM_MODEL = os.environ.get("LLM_MODEL", "deepseek-v4-flash")

# 项目根目录（自动导入产品/）
REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = REPO_ROOT / "scripts"
ONBOARDING_DIR = REPO_ROOT / "onboarding"
HIGHLIGHTS_PKG = ONBOARDING_DIR / "highlights-import"
SPECS_PKG = ONBOARDING_DIR / "specs-import"

# GitHub 配置
GITHUB_RAW_BASE = os.environ.get("GITHUB_RAW_BASE", "https://raw.githubusercontent.com/inhandnet/documents/master/")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

# 站点配置（全部从环境变量读取，不硬编码域名）
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


def log(msg):
    print(f"\n[IMPORT] {msg}", flush=True)


def fetch_md_from_github(md_path: str) -> str:
    """读取 md 内容（优先本地路径，否则从 GitHub raw 拉取）"""
    local_path = Path(md_path)
    if local_path.exists():
        log(f"读取本地 md: {local_path}")
        content = local_path.read_text(encoding="utf-8")
        log(f"读取成功，长度 {len(content)} 字符")
        return content

    # 本地没有则从 GitHub raw 拉（兼容非 checkout 场景）
    url = GITHUB_RAW_BASE + md_path
    headers = {}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"

    log(f"从 GitHub 拉取 md: {url}")
    r = requests.get(url, headers=headers, timeout=60)
    if r.status_code != 200:
        raise RuntimeError(f"拉取 md 失败: HTTP {r.status_code}\n{r.text}")

    content = r.text
    log(f"拉取成功，长度 {len(content)} 字符")
    return content


def extract_highlights_with_claude(md_content: str, product: str, site: str) -> dict:
    """调 LLM（OpenAI 兼容 API）从 md 提取闪光点 + 选图标"""
    llm_key = LLM_API_KEY
    if not llm_key:
        raise RuntimeError("LLM_API_KEY 环境变量未设置")

    # 读取可用图标列表
    icons_file = SCRIPTS_DIR / "core-product-icons.json"
    with open(icons_file, "r", encoding="utf-8") as f:
        icon_list = json.load(f)
    icon_names = [i["name"] for i in icon_list]

    lang_hint = "中文" if site == "zh" else "English"
    title_example = f'"{product} 系列边缘网关"' if site == "zh" else f'"{product} Series Edge Gateway"'
    section_example = "产品类型 / 核心场景，不超过 25 字" if site == "zh" else "Product Type / Core Scenario, ≤25 chars"
    oneliner_example = "一句话卖点，不超过 30 字" if site == "zh" else "One-line pitch, ≤30 chars"
    overview_hint = "200-400 字" if site == "zh" else "200-400 words"
    card_title_hint = "4-8 字" if site == "zh" else "3-6 words"
    card_desc_hint = "30-80 字" if site == "zh" else "30-80 words"

    prompt = f"""你是一位专业的产品文案专家。请从下面的规格书 markdown 中提取以下信息，用于生成 WordPress 产品落地页。

产品型号：{product}
目标语言：{lang_hint}（所有文案必须使用此语言输出）

要求：
1. productName：产品型号（如 IG532）
2. title：产品标题（如 {title_example}）
3. sectionTitle：分类/场景标题，格式"{section_example}"
4. oneLiner：{oneliner_example}
5. overview：产品概述段落（{overview_hint}）
6. cards：5 张特性卡片，每张包含：
   - title：特性标题（{card_title_hint}）
   - desc：详细描述（{card_desc_hint}）
   - icon：从下方"可用图标"中选择一个最匹配的 SVG 文件名
   - 5 张卡片的 icon 必须互不相同

可用图标（从中选择）：
{json.dumps(icon_names, ensure_ascii=False, indent=2)}

选择图标时：
- 优先匹配标题或描述的关键词（如"多串口"→MultiDevice.svg，"协议"→Protocol.svg）
- 5 张卡片覆盖不同维度（网络、计算、安全、可靠性、管理等）

输出严格的 JSON 格式，不要包含 markdown 代码块标记：

{{"productName": "...", "title": "...", "sectionTitle": "...", "oneLiner": "...", "overview": "...", "cards": [{{"icon": "...svg", "title": "...", "desc": "..."}}]}}

规格书内容：
---
{md_content}
---
"""

    log("调 LLM API 提取闪光点 + 选图标...")
    payload = {
        "model": LLM_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 8192,
    }
    headers = {
        "Authorization": f"Bearer {llm_key}",
        "Content-Type": "application/json",
    }
    r = requests.post(LLM_API_URL, json=payload, headers=headers, timeout=300)
    if r.status_code != 200:
        raise RuntimeError(f"LLM API 失败: HTTP {r.status_code}\n{r.text[:500]}")
    result = r.json()

    # 解析响应（OpenAI 兼容格式：choices[0].message.content）
    raw = result.get("choices", [{}])[0].get("message", {}).get("content", "").strip()
    # 去掉可能的 markdown 代码块标记
    raw = re.sub(r"^```(?:json)?\s*", "", raw)
    raw = re.sub(r"\s*```$", "", raw)

    try:
        result = json.loads(raw)
    except json.JSONDecodeError as e:
        # 容错：截断的 JSON 通常在最后一个完整 } 处断开，尝试修复
        last_brace = raw.rfind('}')
        if last_brace > 0:
            trimmed = raw[:last_brace + 1]
            log(f"JSON 截断，尝试从 {last_brace} 位置截断修复...")
            try:
                result = json.loads(trimmed)
                log("JSON 截断修复成功")
            except json.JSONDecodeError:
                log(f"JSON 修复失败，原始输出：\n{raw[:500]}")
                raise
        else:
            log(f"JSON 解析失败: {e}")
            log(f"原始输出：\n{raw[:500]}")
            raise

    # 校验
    required = ["productName", "title", "sectionTitle", "oneLiner", "overview", "cards"]
    for k in required:
        if k not in result:
            raise RuntimeError(f"Claude 输出缺少字段: {k}")
    if len(result["cards"]) != 5:
        log(f"警告：卡片数 {len(result['cards'])} != 5，可能需要调整 prompt")

    # 校验图标互不相同
    icons_used = [c.get("icon") for c in result["cards"]]
    if len(set(icons_used)) != len(icons_used):
        raise RuntimeError(f"图标重复: {icons_used}")

    # 校验图标在可用列表里
    for icon in icons_used:
        if icon not in icon_names:
            raise RuntimeError(f"图标不在可用列表: {icon}")

    log("Claude 提取成功")
    log(f"  产品: {result['productName']}")
    log(f"  标题: {result['title']}")
    log(f"  一句话: {result['oneLiner']}")
    log(f"  卡片: {[c['title'] for c in result['cards']]}")
    log(f"  图标: {icons_used}")

    return result


def ensure_clone_config(site: str):
    """从环境变量动态生成 clone_highlights.js 需要的 config.json（避免明文密码提交到 git）"""
    cfg_file = HIGHLIGHTS_PKG / "config.json"
    env_map = {"zh": "WP_ZH_APP_PASSWORD", "en": "WP_EN_APP_PASSWORD"}

    pw = os.environ.get(env_map.get(site, ""))
    if not pw:
        log(f"警告：环境变量 {env_map[site]} 未设置，跳过 config.json 重写（使用现有文件）")
        return

    cfg = {
        "zh": {
            "wpUrl": SITES["zh"]["wp_url"],
            "username": "admin",
            "appPassword": os.environ.get("WP_ZH_APP_PASSWORD", ""),
            "iconUrl": SITES["zh"]["icon_url"],
            "templateProductId": SITES["zh"]["template_id"],
        },
        "en": {
            "wpUrl": SITES["en"]["wp_url"],
            "username": "admin",
            "appPassword": os.environ.get("WP_EN_APP_PASSWORD", ""),
            "iconUrl": SITES["en"]["icon_url"],
            "templateProductId": SITES["en"]["template_id"],
        },
    }
    with open(cfg_file, "w", encoding="utf-8") as f:
        json.dump(cfg, f, ensure_ascii=False, indent=2)
    log(f"已动态生成 config.json:")
    log(f"  zh wpUrl={cfg['zh']['wpUrl']!r}")
    log(f"  zh templateProductId={cfg['zh']['templateProductId']!r}")
    log(f"  en wpUrl={cfg['en']['wpUrl']!r}")


def save_product_config(highlights: dict, site: str, product: str) -> Path:
    """保存产品配置 JSON 到闪光点导入技能包/products_{site}/"""
    out_dir = HIGHLIGHTS_PKG / f"products_{site}"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / f"{product}.json"

    # clone_highlights.js 需要的字段
    config = {
        "name": product,
        "title": highlights["title"],
        "sectionTitle": highlights["sectionTitle"],
        "oneLiner": highlights["oneLiner"],
        "cards": highlights["cards"],
    }

    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)

    log(f"产品配置已保存: {out_file}")
    return out_file


def run_clone_highlights(config_file: Path, site: str) -> int:
    """调用 clone_highlights.js 克隆产品，返回新产品 ID"""
    log(f"调用 clone_highlights.js (site={site})")

    # 先从环境变量生成 config.json（避免明文密码）
    ensure_clone_config(site)

    cmd = [
        "node",
        str(HIGHLIGHTS_PKG / "clone_highlights.js"),
        f"--site={site}",
        f"--config={config_file}",
    ]

    result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")

    log(f"stdout:\n{result.stdout}")
    if result.stderr:
        log(f"stderr:\n{result.stderr}")

    if result.returncode != 0:
        raise RuntimeError(f"clone_highlights.js 失败: exit {result.returncode}")

    # 从输出中解析新 ID（格式："新ID: 1215466 (草稿)"）
    match = re.search(r"新ID:\s*(\d+)", result.stdout)
    if not match:
        log("警告：未找到新 ID，请检查输出")
        raise RuntimeError("未从 clone_highlights.js 输出中解析到新 ID")

    new_id = int(match.group(1))
    log(f"克隆成功，新 ID: {new_id}")
    return new_id


def extract_specs_from_md(md_content: str) -> list:
    """从 md 提取规格属性（复用 batch_extract.py）"""
    log("提取规格属性...")

    # 导入规格提取模块
    sys.path.insert(0, str(SPECS_PKG))
    from batch_extract import parse_tables

    attrs = parse_tables(md_content)
    log(f"提取到 {len(attrs)} 个规格属性组")
    return attrs


def upload_specs(product_id: int, attrs: list, site: str):
    """调用 upload_specs.py 上传规格"""
    log(f"上传规格到产品 {product_id} (site={site})")

    # 先保存为临时 JSON
    tmp_file = REPO_ROOT / f"tmp_specs_{product_id}.json"
    with open(tmp_file, "w", encoding="utf-8") as f:
        json.dump(attrs, f, ensure_ascii=False, indent=2)

    try:
        # 调用 upload_specs.py
        cmd = [
            sys.executable,
            str(SPECS_PKG / "upload_specs.py"),
            str(product_id),
            str(tmp_file),
        ]
        env = os.environ.copy()
        env["WP_SITE"] = site
        env["WP_URL"] = SITES[site]["wp_url"]
        env["WP_USER"] = "admin"
        env["WP_APP_PASSWORD"] = os.environ.get(f"WP_{site.upper()}_APP_PASSWORD", "")
        env["PYTHONIOENCODING"] = "utf-8"  # 强制 Python 子进程用 UTF-8
        result = subprocess.run(
            cmd, capture_output=True,
            text=True, encoding="utf-8", errors="replace",
            env=env,
        )

        log(f"stdout:\n{result.stdout}")
        if result.stderr:
            log(f"stderr:\n{result.stderr}")

        if result.returncode != 0:
            raise RuntimeError(f"upload_specs.py 失败: exit {result.returncode}")

        log("规格上传成功")
    finally:
        if tmp_file.exists():
            tmp_file.unlink()


def main():
    parser = argparse.ArgumentParser(description="新产品自动导入")
    parser.add_argument("--md-path", required=True, help="规格书 md 路径（相对仓库根）")
    parser.add_argument("--site", required=True, choices=["zh", "en"], help="站点")
    parser.add_argument("--product", required=True, help="产品型号")
    args = parser.parse_args()

    log(f"=== 开始导入产品 {args.product} 到 {args.site} 站 ===")
    log(f"规格书路径: {args.md_path}")

    # 1. 拉 md
    md_content = fetch_md_from_github(args.md_path)

    # 2. Claude 提取闪光点 + 选图标
    highlights = extract_highlights_with_claude(md_content, args.product, args.site)

    # 3. 保存产品配置
    config_file = save_product_config(highlights, args.site, args.product)

    # 4. 克隆产品，得到新 ID
    new_id = run_clone_highlights(config_file, args.site)

    # 5. 提取规格
    attrs = extract_specs_from_md(md_content)

    # 6. 上传规格
    if attrs:
        upload_specs(new_id, attrs, args.site)
    else:
        log("无规格属性可上传")

    log(f"\n=== 导入完成 ===")
    log(f"新产品 ID: {new_id}")
    log(f"状态: 草稿 (draft)")
    log(f"请人工审核：{SITES[args.site]['wp_url']}/wp-admin/post.php?post={new_id}&action=edit")

    # 输出结果 JSON（便于 GitHub Actions 使用）
    result = {
        "success": True,
        "product": args.product,
        "site": args.site,
        "new_id": new_id,
        "edit_url": f"{SITES[args.site]['wp_url']}/wp-admin/post.php?post={new_id}&action=edit",
        "highlights": highlights,
    }
    result_file = REPO_ROOT / f"import_result_{args.product}.json"
    with open(result_file, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    log(f"结果已保存: {result_file}")

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        log(f"ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
