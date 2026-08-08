#!/usr/bin/env python3
"""解析 data/eol-products.{zh,en}.md 里人手维护的 EOL 表格。

被两个脚本共用：
  - sync_eol_products.py  同步到官网 WordPress EOL API
  - generate_eol_pages.py 生成文档站的 EOL 页面（进 llms.txt）

只用标准库，generate-llms.yml 里不装任何依赖也能跑。
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Dict, List

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"

SITES = ("zh", "en")
DATE_FIELDS = ("order_stop_date", "production_stop_date", "support_stop_date")
FIELDS = ("discontinued_series", "replacement_series") + DATE_FIELDS

# 表头 → 字段。中英文两套写法都认，大小写和空格不敏感。
HEADER_ALIASES = {
    "discontinued_series": ("停产产品系列", "停产产品", "eol product", "eol products", "discontinued"),
    "replacement_series": ("替代产品系列", "替代产品", "replacement", "replacement product"),
    "order_stop_date": ("停止订购日期", "停止订购", "end of ordering", "last order date"),
    "production_stop_date": ("停止生产日期", "停止生产", "end of production"),
    "support_stop_date": ("停止支持日期", "停止支持", "end of support"),
}

# 生成文档页时用的列名
COLUMN_TITLES = {
    "zh": ("停产产品系列", "替代产品系列", "停止订购日期", "停止生产日期", "停止支持日期"),
    "en": ("EOL Product", "Replacement", "End of Ordering", "End of Production", "End of Support"),
}


class EolDataError(Exception):
    """数据文件写错了（格式、日期、重复行等），带可定位的行号信息。"""


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
            raise EolDataError(f"{where} 日期格式无法识别：{value!r}（请写成 YYYY-MM-DD）")
        m, d, y = us.groups()
    if not (1 <= int(m) <= 12 and 1 <= int(d) <= 31):
        raise EolDataError(f"{where} 日期不合法：{value!r}")
    return f"{int(y):04d}-{int(m):02d}-{int(d):02d}"


def match_key(text: str) -> str:
    """匹配用的归一化键：忽略空格与大小写差异。"""
    return re.sub(r"\s+", "", str(text)).strip().lower()


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
        cells = [c.strip() for c in stripped.strip("|").split("|")]

        if not in_table:
            mapped = [normalize_header(c) for c in cells]
            if mapped.count("discontinued_series") == 1 and mapped.count("replacement_series") == 1:
                columns = mapped
                in_table = True
            continue

        if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
            continue  # 分隔行

        if len(cells) != len(columns):
            raise EolDataError(
                f"{path.name}:{lineno} 有 {len(cells)} 列，表头是 {len(columns)} 列：{stripped}"
            )

        record = {f: "" for f in FIELDS}
        for field, cell in zip(columns, cells):
            if not field:
                continue
            value = clean_cell(cell)
            record[field] = (
                parse_date(value, f"{path.name}:{lineno}") if field in DATE_FIELDS else value
            )
        if not record["discontinued_series"]:
            raise EolDataError(f"{path.name}:{lineno} 缺少停产产品系列")
        rows.append(record)

    if not in_table:
        raise EolDataError(f"{path} 里没找到 EOL 表格（表头需含「停产产品系列 / EOL Product」列）")
    if not rows:
        raise EolDataError(f"{path} 的表格是空的")
    return rows


def load_entries(site: str) -> List[Dict[str, str]]:
    path = data_file(site)
    if not path.exists():
        raise EolDataError(f"找不到数据文件 {path}")
    rows = parse_markdown_table(path)
    seen: Dict[str, int] = {}
    for i, row in enumerate(rows, 1):
        key = match_key(row["discontinued_series"])
        if key in seen:
            raise EolDataError(
                f"{path.name} 里 {row['discontinued_series']} 重复（第 {seen[key]} 行和第 {i} 行）"
            )
        seen[key] = i
    return rows
