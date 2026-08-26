#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Udesk 知识库自动同步：检测 md 文件变更，上传新增/修改，删除已删除。

用法：
  python sync_udesk.py                    # git diff 自动检测变更
  python sync_udesk.py --site zh          # 只同步中文
  python sync_udesk.py --site en          # 只同步英文
  python sync_udesk.py --file path/to.md  # 同步指定文件
  python sync_udesk.py --diff HEAD~1 HEAD # 指定 diff 范围
"""

import argparse
import base64
import hashlib
import hmac
import json
import os
import re
import shutil
import subprocess
import sys
import time
import uuid
from pathlib import Path

import requests

# ========== 硬编码配置 ==========
SITES = {
    "zh": {
        "kb_id": "14333",
        "category_id": 82404,
        "docs_dir": "docs/zh",
        "site_base_url": "https://www.inhand.com.cn/manuals/",
        "lang_code": "ZH-CN",
    },
    "en": {
        "kb_id": "14769",
        "category_id": 87810,
        "docs_dir": "docs/en",
        "site_base_url": "https://www.inhand.com/manuals/",
        "lang_code": "EN",
    },
}

SKIP_FILES = {"certifications.md", "drawings.md", "EOL Products.md", "README.md", "index.md"}

# ========== 环境变量 ==========
API_BASE = os.environ.get("UDESK_API_BASE", "https://knowledgeservice.s2.udesk.cn")
APP_ID = os.environ.get("UDESK_APP_ID", "")
USER_ID = os.environ.get("UDESK_USER_ID", "")

REPO_ROOT = Path(__file__).resolve().parent.parent.parent


def log(msg):
    print(f"[SYNC] {msg}", flush=True)


# ========== Udesk API ==========

def get_token():
    resp = requests.get(
        f"{API_BASE}/api/auth/open/token",
        params={"appId": APP_ID, "userId": USER_ID},
        timeout=10,
    )
    resp.raise_for_status()
    token = resp.json()["data"]["token"]
    return token


def get_headers(token, content_type="application/json"):
    h = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    if content_type:
        h["Content-Type"] = content_type
    return h


def upload_file(file_path, token, kb_id, category_id, lang_code):
    """OSS 三步上传单个文件"""
    filename = file_path.name
    file_data = file_path.read_bytes()
    file_size = len(file_data)
    headers = get_headers(token)

    # 第一步：OSS 签名
    resp = requests.get(
        f"{API_BASE}/api/oss/efficiency",
        headers=headers,
        params={"knowledgeBaseId": kb_id, "dataType": "document", "filename": filename, "verify": 1},
        timeout=15,
    )
    if resp.status_code != 200 or not resp.json().get("succeed"):
        return False, f"OSS 签名失败: {resp.status_code}"
    oss = resp.json()["data"]
    host, key = oss["host"], oss["key"]
    access_key_id = oss["temporaryId"]
    access_key_secret = oss["policy"]
    security_token = oss["signature"]

    # 第二步：上传
    policy_json = json.dumps({
        "expiration": "2026-12-31T23:59:59.000Z",
        "conditions": [{"bucket": oss["bucket"]}, ["starts-with", "$key", "Data/"]],
    })
    base64_policy = base64.b64encode(policy_json.encode()).decode()
    signature = base64.b64encode(
        hmac.new(access_key_secret.encode(), base64_policy.encode(), hashlib.sha1).digest()
    ).decode()

    resp2 = requests.post(
        host,
        data={
            "key": key,
            "policy": base64_policy,
            "OSSAccessKeyId": access_key_id,
            "Signature": signature,
            "x-oss-security-token": security_token,
            "success_action_status": "200",
        },
        files={"file": (filename, file_data, "application/octet-stream")},
        timeout=60,
    )
    if resp2.status_code != 200:
        return False, f"OSS 上传失败: {resp2.status_code}"

    # 第三步：保存到知识库
    file_uid = str(uuid.uuid4())
    save_data = {
        "materials": [{
            "key": key,
            "url": f"{host}/{key}",
            "name": filename,
            "percent": 100,
            "size": file_size,
            "status": 1,
            "uid": file_uid,
        }],
        "knowledgeBaseId": kb_id,
        "categoryIdList": [category_id],
        "langCode": lang_code,
        "tags": [],
        "accessLevel": 0,
        "availableTimeType": 0,
    }
    resp3 = requests.post(
        f"{API_BASE}/api/sdk/knowledgeBases/{kb_id}/materialRepositorys/batchSave",
        headers={**headers, "Content-Type": "application/json"},
        params={"knowledgeBaseId": kb_id},
        json=save_data,
        timeout=30,
    )
    result = resp3.json()
    if result.get("succeed"):
        return True, file_uid
    return False, json.dumps(result, ensure_ascii=False)[:200]


def list_kb_files(token, kb_id):
    """分页获取知识库所有文件"""
    headers = get_headers(token)
    all_files = []
    page = 1
    while True:
        resp = requests.get(
            f"{API_BASE}/api/sdk/knowledgeBases/{kb_id}/materialRepositorys",
            headers=headers,
            params={"knowledgeBaseId": kb_id, "pageSize": 100, "pageNum": page},
            timeout=15,
        )
        if resp.status_code != 200 or not resp.json().get("succeed"):
            break
        data = resp.json().get("data", [])
        if not data:
            break
        all_files.extend(data)
        if len(data) < 100:
            break
        page += 1
        time.sleep(0.3)
    return all_files


def delete_kb_file(token, kb_id, file_id):
    """删除知识库文件"""
    headers = get_headers(token)
    resp = requests.delete(
        f"{API_BASE}/api/sdk/knowledgeBases/{kb_id}/materialRepositorys/{file_id}",
        headers=headers,
        timeout=15,
    )
    return resp.status_code in (200, 204)


# ========== MD 处理 ==========

def fix_md_images(content, md_rel_path, site_key):
    """将 md 中的相对图片路径转为绝对 URL，清理 MkDocs 自定义语法"""
    site = SITES[site_key]
    docs_dir = REPO_ROOT / site["docs_dir"]
    md_file = docs_dir / md_rel_path
    md_dir_url = site["site_base_url"] + str(md_file.parent.relative_to(docs_dir)).replace("\\", "/") + "/"

    def fix_img(m):
        alt, src = m.group(1), m.group(2)
        if src.startswith("http"):
            return m.group(0)
        abs_url = md_dir_url + src.lstrip("./")
        return f"![{alt}]({abs_url})"

    content = re.sub(r"!\[(.*?)\]\((.*?)\)", fix_img, content)
    content = re.sub(r":::.*?\n", "", content)
    content = re.sub(r"\n{3,}", "\n\n", content)
    return content


# ========== Git Diff ==========

def get_changed_files(ref_from, ref_to):
    """获取变更的 md 文件列表，返回 {zh: {added:[], modified:[], deleted:[]}, en: {...}}"""
    cmd = ["git", "diff", "--name-status", "--diff-filter=ACDMR", ref_from, ref_to]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True, cwd=str(REPO_ROOT))

    changes = {"zh": {"added": [], "modified": [], "deleted": []},
               "en": {"added": [], "modified": [], "deleted": []}}

    for line in result.stdout.strip().split("\n"):
        if not line.strip():
            continue
        parts = line.split("\t", 1)
        if len(parts) != 2:
            continue
        status, filepath = parts[0], parts[1]

        # 只处理 docs/{zh,en} 下的 md 文件
        if not filepath.startswith("docs/"):
            continue
        if not filepath.endswith(".md"):
            continue

        parts2 = filepath.split("/")
        if len(parts2) < 3:
            continue
        lang = parts2[1]
        if lang not in ("zh", "en"):
            continue

        filename = Path(filepath).name
        if filename in SKIP_FILES:
            continue

        rel_path = "/".join(parts2[2:])  # 产品路径部分

        if status in ("A", "M"):
            if status == "A":
                changes[lang]["added"].append(rel_path)
            else:
                changes[lang]["modified"].append(rel_path)
        elif status == "D":
            changes[lang]["deleted"].append(rel_path)

    return changes


# ========== 主逻辑 ==========

def sync_upload(files, site_key, token, temp_dir):
    """上传文件到 Udesk"""
    site = SITES[site_key]
    kb_id = site["kb_id"]
    category_id = site["category_id"]
    lang_code = site["lang_code"]
    docs_dir = REPO_ROOT / site["docs_dir"]

    success = 0
    failed = 0
    for rel_path in files:
        md_file = docs_dir / rel_path
        if not md_file.exists():
            log(f"  文件不存在，跳过: {rel_path}")
            continue

        log(f"  上传: {rel_path}")
        try:
            content = md_file.read_text(encoding="utf-8")

            # 图片路径转换
            has_images = bool(re.search(r"!\[.*?\]\((?!http)", content))
            if has_images:
                content = fix_md_images(content, rel_path, site_key)

            # 写入临时文件
            tmp_file = temp_dir / md_file.name
            tmp_file.write_text(content, encoding="utf-8")

            # 上传
            ok, info = upload_file(tmp_file, token, kb_id, category_id, lang_code)
            if ok:
                success += 1
                log(f"    OK")
            else:
                failed += 1
                log(f"    FAIL: {info}")

            time.sleep(0.3)
        except Exception as e:
            failed += 1
            log(f"    ERROR: {e}")

    return success, failed


def sync_delete(files, site_key, token):
    """从 Udesk 删除文件"""
    site = SITES[site_key]
    kb_id = site["kb_id"]

    # 获取知识库现有文件
    log(f"  查询 KB {kb_id} 文件列表...")
    all_kb_files = list_kb_files(token, kb_id)
    log(f"  共 {len(all_kb_files)} 个文件")

    # 按文件名匹配
    delete_names = {Path(f).name for f in files}
    matched = [kf for kf in all_kb_files if kf.get("name", "") in delete_names]

    log(f"  匹配到 {len(matched)} 个需删除")

    success = 0
    failed = 0
    for kf in matched:
        ok = delete_kb_file(token, kb_id, kf["id"])
        if ok:
            success += 1
            log(f"  已删除: {kf['name']}")
        else:
            failed += 1
            log(f"  删除失败: {kf['name']} (ID={kf['id']})")
        time.sleep(0.3)

    return success, failed


def main():
    parser = argparse.ArgumentParser(description="Udesk 知识库自动同步")
    parser.add_argument("--site", choices=["zh", "en", "all"], default="all", help="同步站点")
    parser.add_argument("--file", help="同步指定文件（相对于仓库根）")
    parser.add_argument("--diff-from", default="HEAD~1", help="git diff 起点")
    parser.add_argument("--diff-to", default="HEAD", help="git diff 终点")
    args = parser.parse_args()

    log("=== Udesk 知识库自动同步 ===")
    log(f"API: {API_BASE}")

    if not APP_ID or not USER_ID:
        log("ERROR: UDESK_APP_ID 和 UDESK_USER_ID 必须设置")
        sys.exit(1)

    # 获取 token
    token = get_token()
    log("Token 获取成功")

    # 确定变更文件
    if args.file:
        # 指定文件模式
        filepath = args.file
        if not filepath.startswith("docs/"):
            log(f"文件不在 docs/ 下: {filepath}")
            sys.exit(1)
        parts = filepath.split("/")
        lang = parts[1]
        rel_path = "/".join(parts[2:])
        changes = {"zh": {"added": [], "modified": [], "deleted": []},
                   "en": {"added": [], "modified": [], "deleted": []}}
        changes[lang]["modified"].append(rel_path)
    else:
        # git diff 模式
        log(f"检测变更: {args.diff_from}..{args.diff_to}")
        changes = get_changed_files(args.diff_from, args.diff_to)

    # 过滤站点
    sites_to_sync = ["zh", "en"] if args.site == "all" else [args.site]

    # 创建临时目录
    temp_dir = REPO_ROOT / "tmp_udesk_sync"
    if temp_dir.exists():
        shutil.rmtree(temp_dir)
    temp_dir.mkdir(parents=True, exist_ok=True)

    results = {}

    try:
        for site_key in sites_to_sync:
            site_changes = changes[site_key]
            to_upload = site_changes["added"] + site_changes["modified"]
            to_delete = site_changes["deleted"]

            if not to_upload and not to_delete:
                log(f"\n{site_key.upper()}: 无变更")
                continue

            log(f"\n{site_key.upper()}: 上传 {len(to_upload)} 个, 删除 {len(to_delete)} 个")

            upload_ok, upload_fail = 0, 0
            if to_upload:
                upload_ok, upload_fail = sync_upload(to_upload, site_key, token, temp_dir)

            delete_ok, delete_fail = 0, 0
            if to_delete:
                delete_ok, delete_fail = sync_delete(to_delete, site_key, token)

            results[site_key] = {
                "uploaded": upload_ok, "upload_failed": upload_fail,
                "deleted": delete_ok, "delete_failed": delete_fail,
            }
    finally:
        # 清理临时目录
        shutil.rmtree(temp_dir, ignore_errors=True)

    # 输出汇总
    log("\n=== 同步完成 ===")
    total_ok = 0
    total_fail = 0
    for site_key, r in results.items():
        log(f"{site_key.upper()}: 上传 {r['uploaded']} 成功 / {r['upload_failed']} 失败, "
            f"删除 {r['deleted']} 成功 / {r['delete_failed']} 失败")
        total_ok += r["uploaded"] + r["deleted"]
        total_fail += r["upload_failed"] + r["delete_failed"]

    # 保存结果
    result_file = REPO_ROOT / "sync_result.json"
    with open(result_file, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    log(f"结果已保存: {result_file}")

    if total_fail > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
