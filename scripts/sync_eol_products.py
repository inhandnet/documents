#!/usr/bin/env python3
"""把 data/eol-products.{zh,en}.md 里的表格同步到官网的 WordPress EOL REST API。

数据源是两份 Markdown 文件（中英文各一份，内容本来就不一样，各自独立维护），
官网 EOL 页面是下游。脚本按「停产产品系列」做增量对账：
本地有远端没有 → POST，两边都有但字段不同 → PUT，
远端有本地没有 → 默认只报告，加 --prune 才 DELETE。重复跑是幂等的。

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
    python scripts/sync_eol_products.py --site zh             # 执行新增/更新
    python scripts/sync_eol_products.py --site zh --prune     # 同时删除远端多余记录
    python scripts/sync_eol_products.py --site all
"""

import argparse
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

import requests

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"

SITES = ("zh", "en")
DATE_FIELDS = ("order_stop_date", "production_stop_date", "support_stop_date")
API_FIELDS = ("discontinued_series", "replacement_series") + DATE_FIELDS

# 表头 → API 字段。中英文两套写法都认，大小写和空格不敏感。
HEADER_ALIASES = {
    "discontinued_series": ("停产产品系列", "停产产品", "eol product", "eol products", "discontinued"),
    "replacement_series": ("替代产品系列", "替代产品", "replacement", "replacement product"),
    "order_stop_date": ("停止订购日期", "停止订购", "end of ordering", "last order date"),
    "production_stop_date": ("停止生产日期", "停止生产", "end of production"),
    "support_stop_date": ("停止支持日期", "停止支持", "end of support"),
}

TIMEOUT = 30
PER_PAGE = 100


# --------------------------------------------------------------------------
# 解析 Markdown 表格
# --------------------------------------------------------------------------

def data_file(site: str) -> Path:
    return DATA_DIR / f"eol-products.{site}.md"


def normalize_header(cell: str) -> str:
    text = re.sub(r"[\s*`|]+", "", cell).strip().lower()
    text = text.replace("（", "(").replace("）", ")")
    for field, aliases in HEADER_ALIASES.items():
        for alias in aliases:
            if text == re.sub(r"\s+", "", alias).lower():
                return field
    return ""


def clean_cell(cell: str) -> str:
    """去掉 Markdown 强调符号和多余空白，中文「系列」前不留空格。"""
    text = cell.replace(" ", " ").strip()
    text = re.sub(r"^\*\*(.*)\*\*$", r"\1", text).strip()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\s*系列$", "系列", text)
    return text


def parse_date(value: str, where: str) -> str:
    """接受 YYYY-MM-DD 和官网上的 M/D/YYYY，统一输出 ISO 8601。"""
    text = value.strip()
    if not text or text in {"-", "—", "TBD", "待定"}:
        return ""
    iso = re.fullmatch(r"(\d{4})-(\d{1,2})-(\d{1,2})", text)
    if iso:
        y, m, d = iso.groups()
    else:
        us = re.fullmatch(r"(\d{1,2})/(\d{1,2})/(\d{4})", text)
        if not us:
            raise SystemExit(f"[错误] {where} 日期格式无法识别：{value!r}（用 YYYY-MM-DD）")
        m, d, y = us.groups()
    if not (1 <= int(m) <= 12 and 1 <= int(d) <= 31):
        raise SystemExit(f"[错误] {where} 日期不合法：{value!r}")
    return f"{int(y):04d}-{int(m):02d}-{int(d):02d}"


def split_row(line: str) -> List[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def parse_markdown_table(path: Path) -> List[Dict[str, str]]:
    """取文件里第一张能认出表头的 Markdown 表格。"""
    lines = path.read_text(encoding="utf-8").splitlines()
    columns: List[str] = []
    rows: List[Dict[str, str]] = []
    in_table = False

    for lineno, line in enumerate(lines, 1):
        stripped = line.strip()
        if not stripped.startswith("|"):
            if in_table:
                break  # 表格结束
            continue
        cells = split_row(stripped)

        if not in_table:
            mapped = [normalize_header(c) for c in cells]
            if mapped.count("discontinued_series") == 1 and mapped.count("replacement_series") == 1:
                columns = mapped
                in_table = True
            continue

        if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
            continue  # 分隔行

        if len(cells) != len(columns):
            raise SystemExit(
                f"[错误] {path.name}:{lineno} 有 {len(cells)} 列，表头是 {len(columns)} 列：{stripped}"
            )

        record = {f: "" for f in API_FIELDS}
        for field, cell in zip(columns, cells):
            if not field:
                continue
            value = clean_cell(cell)
            record[field] = (
                parse_date(value, f"{path.name}:{lineno}") if field in DATE_FIELDS else value
            )
        if not record["discontinued_series"]:
            raise SystemExit(f"[错误] {path.name}:{lineno} 缺少停产产品系列")
        rows.append(record)

    if not in_table:
        raise SystemExit(f"[错误] {path} 里没找到 EOL 表格（表头需含「停产产品系列/EOL Product」列）")
    if not rows:
        raise SystemExit(f"[错误] {path} 的表格是空的")
    return rows


def match_key(text: str) -> str:
    """匹配用的归一化键：忽略空格与大小写差异。"""
    return re.sub(r"\s+", "", str(text)).strip().lower()


def load_entries(site: str) -> List[Dict[str, str]]:
    path = data_file(site)
    if not path.exists():
        raise SystemExit(f"[错误] 找不到数据文件 {path}")
    rows = parse_markdown_table(path)
    seen: Dict[str, int] = {}
    for i, row in enumerate(rows, 1):
        key = match_key(row["discontinued_series"])
        if key in seen:
            raise SystemExit(
                f"[错误] {path.name} 里 {row['discontinued_series']} 重复"
                f"（第 {seen[key]} 行和第 {i} 行）"
            )
        seen[key] = i
    return rows


# --------------------------------------------------------------------------
# 远端 API
# --------------------------------------------------------------------------

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


# --------------------------------------------------------------------------
# 对账
# --------------------------------------------------------------------------

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
        changes = {
            f: entry[f] for f in API_FIELDS if (entry.get(f) or "") != str(item.get(f) or "")
        }
        if changes:
            to_update.append((item, entry, changes))

    return to_create, to_update, extra + list(by_key.values())


def sync_site(site: str, dry_run: bool, prune: bool) -> int:
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
        f"更新 {len(to_update)}，{'删除' if prune else '多余（未删）'} {len(to_delete)}"
    )
    for entry in to_create:
        print(f"  + {entry['discontinued_series']}")
    for item, entry, changes in to_update:
        detail = ", ".join(f"{f}: {item.get(f) or '(空)'} → {changes[f] or '(空)'}" for f in changes)
        print(f"  ~ {entry['discontinued_series']}  [{detail}]")
    for item in to_delete:
        print(f"  {'-' if prune else '!'} {item.get('discontinued_series')} (id={item.get('id')})")
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
    if prune:
        for item in to_delete:
            try:
                api.delete(item["id"])
                print(f"  已删除 {item.get('discontinued_series')}")
            except RuntimeError as exc:
                failures += 1
                print(f"  [失败] 删除 {item.get('discontinued_series')}：{exc}", file=sys.stderr)
    elif to_delete:
        print("  提示：远端多余记录未处理，确认无误后加 --prune 删除（不可恢复）")

    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="同步 EOL 产品清单到官网 API")
    parser.add_argument("--site", choices=[*SITES, "all"], default="all")
    parser.add_argument("--dry-run", action="store_true", help="只打印计划，不写入")
    parser.add_argument("--prune", action="store_true", help="删除远端多余记录（永久删除）")
    args = parser.parse_args()

    sites = SITES if args.site == "all" else (args.site,)
    failures = sum(sync_site(s, args.dry_run, args.prune) for s in sites)
    if failures:
        print(f"\n共 {failures} 个操作失败", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
