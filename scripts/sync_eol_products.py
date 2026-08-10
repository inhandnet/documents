#!/usr/bin/env python3
"""把 data/eol-products.{zh,en}.md 里的表格同步到官网的 WordPress EOL REST API。

数据源是两份 Markdown 文件（中英文各一份，内容本来就不一样，各自独立维护），
官网 EOL 页面是下游。脚本按「停产产品系列」做增量对账，全自动双向同步：
本地有远端没有 → POST，两边都有但字段不同 → PUT，
远端有本地没有 → DELETE（数据文件删一行 = 官网删一条）。
重复跑是幂等的。加 --no-delete 可临时只增改不删（比如演练时）。

接口约定（见 WordPress 后台 EOL 管理 → API Token 页面）：
    GET    {base}/products?page=&per_page=
    POST   {base}/products
    PUT    {base}/products/{id}
    DELETE {base}/products/{id}
均需 HTTP 头 X-EOL-Token。

配置按站点从环境变量读，缺 URL 或 TOKEN 则跳过该站点（不报错）：
    EOL_API_ZH_URL / EOL_API_ZH_TOKEN
    EOL_API_EN_URL / EOL_API_EN_TOKEN
URL 填到 /wp-json/eol/v1 为止，例如 https://<host>/wp-json/eol/v1
（测试站和正式站只是 URL 不同，切换时改仓库变量即可，脚本里不写死域名。）

用法：
    python scripts/sync_eol_products.py --site zh --dry-run   # 只打印计划
    python scripts/sync_eol_products.py --site zh             # 执行新增/更新/删除
    python scripts/sync_eol_products.py --site zh --no-delete # 只增改，不删
    python scripts/sync_eol_products.py --site all
"""

import argparse
import os
import sys
from pathlib import Path
from typing import Dict, List, Tuple

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
from eol_data import (  # noqa: E402
    FIELDS,
    SITES,
    EolDataError,
    data_file,
    load_entries,
    match_key,
)

TIMEOUT = 30
PER_PAGE = 100


class EolApi:
    def __init__(self, base_url: str, token: str):
        self.base = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({"X-EOL-Token": token})

    def _request(self, method: str, path: str, **kwargs) -> dict:
        resp = self.session.request(method, f"{self.base}{path}", timeout=TIMEOUT, **kwargs)
        try:
            body = resp.json()
        except ValueError:
            body = {}
        if resp.status_code >= 400 or body.get("success") is False:
            message = body.get("message") or resp.text[:200]
            raise RuntimeError(f"{method} {path} 失败：HTTP {resp.status_code} {message}")
        return body

    def list_all(self) -> List[dict]:
        items: List[dict] = []
        page = 1
        while True:
            body = self._request("GET", f"/products?page={page}&per_page={PER_PAGE}")
            data = body.get("data") or []
            items.extend(data)
            total = int(body.get("total") or len(items))
            if len(data) < PER_PAGE or len(items) >= total:
                break
            page += 1
        return items

    def create(self, entry: dict) -> dict:
        return self._request("POST", "/products", json=entry)

    def update(self, item_id, changes: dict) -> dict:
        return self._request("PUT", f"/products/{item_id}", json=changes)

    def delete(self, item_id) -> dict:
        return self._request("DELETE", f"/products/{item_id}")


def diff(
    entries: List[dict], remote: List[dict]
) -> Tuple[List[dict], List[Tuple[dict, dict, dict]], List[dict]]:
    """返回 (要新增, 要更新[(远端记录, 目标, 变更字段)], 要删除)。"""
    by_key: Dict[str, dict] = {}
    extra: List[dict] = []
    for item in remote:
        key = match_key(item.get("discontinued_series") or "")
        if key in by_key:
            extra.append(item)  # 远端重复记录，按多余处理
        else:
            by_key[key] = item

    to_create, to_update = [], []
    for entry in entries:
        item = by_key.pop(match_key(entry["discontinued_series"]), None)
        if item is None:
            to_create.append(entry)
            continue
        changes = {f: entry[f] for f in FIELDS if (entry.get(f) or "") != str(item.get(f) or "")}
        if changes:
            to_update.append((item, entry, changes))

    return to_create, to_update, extra + list(by_key.values())


def sync_site(site: str, dry_run: bool, do_delete: bool) -> int:
    base_url = os.environ.get(f"EOL_API_{site.upper()}_URL", "").strip()
    token = os.environ.get(f"EOL_API_{site.upper()}_TOKEN", "").strip()
    if not base_url or not token:
        print(f"[跳过] {site}：未配置 EOL_API_{site.upper()}_URL / _TOKEN")
        return 0

    entries = load_entries(site)
    api = EolApi(base_url, token)
    remote = api.list_all()
    to_create, to_update, to_delete = diff(entries, remote)

    print(f"\n=== {site}（{data_file(site).name} → {base_url}）===")
    print(
        f"本地 {len(entries)} 条，远端 {len(remote)} 条 → 新增 {len(to_create)}，"
        f"更新 {len(to_update)}，{'删除' if do_delete else '多余（未删）'} {len(to_delete)}"
    )
    for entry in to_create:
        print(f"  + {entry['discontinued_series']}")
    for item, entry, changes in to_update:
        detail = ", ".join(f"{f}: {item.get(f) or '(空)'} → {changes[f] or '(空)'}" for f in changes)
        print(f"  ~ {entry['discontinued_series']}  [{detail}]")
    for item in to_delete:
        print(f"  {'-' if do_delete else '!'} {item.get('discontinued_series')} (id={item.get('id')})")
    if not (to_create or to_update or to_delete):
        print("  已一致，无需变更")

    if dry_run:
        print("  (--dry-run，未写入)")
        return 0

    failures = 0
    for entry in to_create:
        try:
            api.create(entry)
            print(f"  已新增 {entry['discontinued_series']}")
        except RuntimeError as exc:
            failures += 1
            print(f"  [失败] 新增 {entry['discontinued_series']}：{exc}", file=sys.stderr)
    for item, entry, changes in to_update:
        try:
            api.update(item["id"], changes)
            print(f"  已更新 {entry['discontinued_series']}")
        except RuntimeError as exc:
            failures += 1
            print(f"  [失败] 更新 {entry['discontinued_series']}：{exc}", file=sys.stderr)
    if do_delete:
        for item in to_delete:
            try:
                api.delete(item["id"])
                print(f"  已删除 {item.get('discontinued_series')}")
            except RuntimeError as exc:
                failures += 1
                print(f"  [失败] 删除 {item.get('discontinued_series')}：{exc}", file=sys.stderr)
    elif to_delete:
        print("  提示：--no-delete 生效，远端记录未删除")

    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="同步 EOL 产品清单到官网 API")
    parser.add_argument("--site", choices=[*SITES, "all"], default="all")
    parser.add_argument("--dry-run", action="store_true", help="只打印计划，不写入")
    parser.add_argument(
        "--no-delete", action="store_true", help="只新增/更新，不删除远端多余记录"
    )
    args = parser.parse_args()

    sites = SITES if args.site == "all" else (args.site,)
    try:
        failures = sum(sync_site(s, args.dry_run, not args.no_delete) for s in sites)
    except EolDataError as exc:
        print(f"[错误] {exc}", file=sys.stderr)
        return 2
    if failures:
        print(f"\n共 {failures} 个操作失败", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
