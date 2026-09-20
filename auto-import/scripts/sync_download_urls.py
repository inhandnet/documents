#!/usr/bin/env python3
"""
产品下载页 URL 同步到 Udesk 知识库。

从 poweris API 获取所有产品行业→分类→系列结构，
生成下载页 URL md 文件，上传到 Udesk KCS。

用法：
    python auto-import/scripts/sync_download_urls.py                # 生成+上传
    python auto-import/scripts/sync_download_urls.py --dry-run      # 只生成不上传
    python auto-import/scripts/sync_download_urls.py --site zh      # 只处理中文
"""
import argparse
import base64
import hashlib
import hmac
import json
import os
import sys
import time
import uuid
from pathlib import Path

import requests

# Poweris API
POWERIS_ZH_BASE = os.environ.get("POWERIS_ZH_BASE", "https://poweris.inhand.online")
POWERIS_ZH_KEY = os.environ.get("POWERIS_ZH_KEY", "16caeb02-2b12-4181-8253-203298038161")
POWERIS_EN_BASE = os.environ.get("POWERIS_EN_BASE", "https://poweris.inhandnetworks.com")
POWERIS_EN_KEY = os.environ.get("POWERIS_EN_KEY", "b4ae9d11-dd4d-40e5-931f-3480e8c20c63")

# 下载页 URL 模板
URL_TEMPLATES = {
    "zh": "https://www.inhand.com.cn/resources-center/#/{industry}/{category}/{series}",
    "en": "https://www.inhand.com/en/resources-center/#/{industry}/{category}/{series}",
}

# 文件名和标题（多语言）
TITLES = {
    "zh": {
        "filename": "产品资源页面汇总_zh.md",
        "title": "映翰通产品资源页面汇总（{site}）",
        "intro": "本页汇总映翰通所有产品的资源入口页面，包含用户手册、规格书、固件、认证证书、图纸、FAQ 等资料的下载入口。",
        "link_text": "进入",
        "col_header": "资源页面",
    },
    "en": {
        "filename": "产品资源页面汇总_en.md",
        "title": "InHand Product Resource Pages ({site})",
        "intro": "This page lists the resource entry pages for all InHand products, including user manuals, datasheets, firmware, certifications, drawings, FAQs, and more.",
        "link_text": "Open",
        "col_header": "Resource Page",
    },
}

# Udesk API
UDESK_BASE = os.environ.get("UDESK_API_BASE", "https://knowledgeservice.s2.udesk.cn")
UDESK_APP_ID = os.environ.get("UDESK_APP_ID", "9b1b1ba1-4ecf-4a79-70f9-9e0ee93d0252")
UDESK_USER_ID = os.environ.get("UDESK_USER_ID", "10002618")
UDESK_KB_ID_ZH = "14333"
UDESK_KB_ID_EN = "14769"
UDESK_CAT_ID = 82404


def log(msg):
    print(f"[SYNC] {msg}", flush=True)


def fetch_poweris_data(base_url, api_key):
    """从 poweris 获取所有行业→分类→系列"""
    s = requests.Session()
    h = {"x-api-key": api_key}

    r = s.get(f"{base_url}/api/plm/product/category-groups",
              params={"locale": "zh"}, headers=h, timeout=15)
    industries = r.json().get("result", [])
    log(f"  {len(industries)} industries")

    all_data = []
    for ind in industries:
        ind_id = ind["id"]
        r2 = s.get(f"{base_url}/api/plm/product/category-groups/{ind_id}",
                    params={"locale": "zh"}, headers=h, timeout=15)
        try:
            cats = r2.json().get("result", {}).get("product_categories", [])
        except Exception:
            cats = []
        for cat in cats:
            cat_id = cat["id"]
            for series in cat.get("product_series", []):
                all_data.append({
                    "industry": ind_id,
                    "industry_name": ind.get("name", {}).get("cn", ind_id),
                    "category": cat_id,
                    "category_name": cat.get("name", {}).get("cn", cat_id),
                    "series": series.get("id", ""),
                    "series_name": series.get("name", ""),
                })
    return all_data


def generate_md(data, url_template, title_config):
    """生成 md 内容"""
    t = title_config
    lines = []
    lines.append(f"# {t['title']}")
    lines.append("")
    lines.append(f"> {t['intro']}")
    lines.append("")
    lines.append("> 自动生成，数据来源：poweris 系统")

    by_industry = {}
    for item in data:
        key = f"{item['industry']}（{item['industry_name']}）"
        by_industry.setdefault(key, []).append(item)

    for ind_key in sorted(by_industry.keys()):
        lines.append(f"\n### {ind_key}")
        lines.append("")
        lines.append(f"| 产品系列 | {t['col_header']} |")
        lines.append("|---------|---------|")
        for item in by_industry[ind_key]:
            url = url_template.format(**item)
            lines.append(f"| {item['series_name']} | [{t['link_text']}]({url}) |")
        lines.append("")

    return "\n".join(lines)


def upload_to_udesk(content, kb_id, category_id, file_name):
    """上传 md 到 Udesk KCS（先删旧文件再上传，避免堆积重复）"""
    s = requests.Session()

    # 获取 token
    r = s.get(f"{UDESK_BASE}/api/auth/open/token",
              params={"appId": UDESK_APP_ID, "userId": UDESK_USER_ID}, timeout=10)
    token = r.json()["data"]["token"]

    h = {"Authorization": f"Bearer {token}", "Accept": "application/json"}

    # 先删除同名旧文件
    page = 1
    while True:
        r_list = s.get(f"{UDESK_BASE}/api/sdk/knowledgeBases/{kb_id}/materialRepositorys",
                       headers=h, params={"knowledgeBaseId": kb_id, "pageSize": 100, "pageNum": page}, timeout=15)
        files = r_list.json().get("data", [])
        if not files:
            break
        for f in files:
            if f.get("name") == file_name:
                r_del = s.delete(f"{UDESK_BASE}/api/sdk/knowledgeBases/{kb_id}/materialRepositorys/{f['id']}",
                                 headers=h, timeout=15)
                if r_del.status_code in (200, 204):
                    log(f"  已删除旧文件: {file_name} (ID={f['id']})")
                else:
                    log(f"  删除旧文件失败: {r_del.status_code}")
        page += 1
        if page > 10:
            break

    # OSS 三步上传
    h = {"Authorization": f"Bearer {token}", "Accept": "application/json"}

    # 第一步
    r1 = s.get(f"{UDESK_BASE}/api/oss/efficiency", headers=h,
               params={"knowledgeBaseId": kb_id, "dataType": "document",
                       "filename": file_name, "verify": 1}, timeout=15)
    oss = r1.json()["data"]

    # 第二步
    policy_json = json.dumps({"expiration": "2026-12-31T23:59:59.000Z",
                              "conditions": [{"bucket": oss["bucket"]}, ["starts-with", "$key", "Data/"]]})
    base64_policy = base64.b64encode(policy_json.encode()).decode()
    signature = base64.b64encode(
        hmac.new(oss["policy"].encode(), base64_policy.encode(), hashlib.sha1).digest()
    ).decode()

    file_data = content.encode("utf-8")
    r2 = s.post(oss["host"], data={
        "key": oss["key"], "policy": base64_policy,
        "OSSAccessKeyId": oss["temporaryId"], "Signature": signature,
        "x-oss-security-token": oss["signature"], "success_action_status": "200",
    }, files={"file": (file_name, file_data, "text/markdown")}, timeout=60)

    # 第三步
    save_data = {
        "materials": [{"key": oss["key"], "url": f'{oss["host"]}/{oss["key"]}',
                        "name": file_name, "percent": 100, "size": len(file_data),
                        "status": 1, "uid": str(__import__("uuid").uuid4())}],
        "knowledgeBaseId": kb_id, "categoryIdList": [category_id],
        "langCode": "ZH-CN" if kb_id == UDESK_KB_ID_ZH else "EN",
        "tags": [], "accessLevel": 0, "availableTimeType": 0,
    }
    r3 = s.post(f"{UDESK_BASE}/api/sdk/knowledgeBases/{kb_id}/materialRepositorys/batchSave",
                headers={**h, "Content-Type": "application/json"},
                params={"knowledgeBaseId": kb_id}, json=save_data, timeout=30)
    return r3.json().get("succeed", False)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--site", choices=["zh", "en", "all"], default="all")
    args = parser.parse_args()

    log("=== 产品资源页 URL 同步 ===")

    sites = {
        "zh": (POWERIS_ZH_BASE, POWERIS_ZH_KEY, {**TITLES["zh"], "title": TITLES["zh"]["title"].format(site="中文站")}),
        "en": (POWERIS_EN_BASE, POWERIS_EN_KEY, {**TITLES["en"], "title": TITLES["en"]["title"].format(site="English")}),
    }
    targets = [args.site] if args.site != "all" else ["zh", "en"]

    for site_key in targets:
        base, key, t = sites[site_key]
        url_template = URL_TEMPLATES[site_key]

        log(f"\n{t['title']}:")
        data = fetch_poweris_data(base, key)
        log(f"  {len(data)} products")

        md_content = generate_md(data, url_template, t)

        out_path = Path(t["filename"])
        out_path.write_text(md_content, encoding="utf-8")
        log(f"  生成: {out_path} ({len(md_content)} 字符)")

        if args.dry_run:
            log("  dry-run，跳过上传")
            continue

        # 上传到 Udesk
        kb_id = UDESK_KB_ID_ZH if site_key == "zh" else UDESK_KB_ID_EN
        log(f"  上传到 Udesk KB {kb_id}...")
        ok = upload_to_udesk(md_content, kb_id, UDESK_CAT_ID, t["filename"])
        log(f"  上传{'成功' if ok else '失败'}")


if __name__ == "__main__":
    main()
