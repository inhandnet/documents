#!/usr/bin/env python3
"""把一份「EOL 产品变更申请」Issue 表单的内容应用到 data/eol-products.*.md。

配合 .github/ISSUE_TEMPLATE/eol-change.yml 和 .github/workflows/eol-issue-to-pr.yml：
产品/市场同事填表单 → 本脚本改表格 → 机器人开 PR → 维护人合并 → 官网自动更新。
填表人不接触 Markdown，也不需要 Git 知识。

Issue 表单提交后的正文长这样（每个字段一个三级标题）：

    ### 操作类型

    新增

    ### 停产产品系列

    IR999-XX系列

用法：
    ISSUE_BODY="$(cat issue.md)" python scripts/apply_eol_issue.py
    python scripts/apply_eol_issue.py --body-file issue.md

出错时以非零码退出，并把面向填表人的中文说明打到 stderr，
由工作流回帖到 Issue 里——所以错误信息要让非技术同事看得懂。
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional

sys.path.insert(0, str(Path(__file__).resolve().parent))
from eol_data import (  # noqa: E402
    DATE_FIELDS,
    EolDataError,
    clean_cell,
    data_file,
    load_entries,
    match_key,
    normalize_header,
    parse_date,
)

# Issue 表单里的标题 → 内部字段名
FORM_LABELS = {
    "操作类型": "action",
    "适用站点": "site",
    "停产产品系列": "discontinued_series",
    "替代产品系列": "replacement_series",
    "停止订购日期": "order_stop_date",
    "停止生产日期": "production_stop_date",
    "停止支持日期": "support_stop_date",
}

SITE_CHOICES = {
    "中文站": ["zh"],
    "英文站": ["en"],
    "两个站都要": ["zh", "en"],
}

ACTIONS = ("新增", "修改", "删除")

# GitHub 表单里未填的字段会渲染成这个
NO_RESPONSE = "_No response_"


class FormError(Exception):
    """填表人能看懂的错误。"""


def parse_issue_form(body: str) -> Dict[str, str]:
    """把 Issue 表单正文解析成 {字段: 值}。"""
    fields: Dict[str, str] = {}
    current: Optional[str] = None
    buffer: List[str] = []

    def flush() -> None:
        if current is None:
            return
        value = "\n".join(buffer).strip()
        if value == NO_RESPONSE:
            value = ""
        fields[current] = value

    for line in body.replace("\r\n", "\n").split("\n"):
        heading = re.fullmatch(r"#{2,4}\s*(.+?)\s*", line)
        if heading:
            flush()
            label = heading.group(1).strip()
            current = FORM_LABELS.get(label)
            buffer = []
            continue
        if current is not None:
            buffer.append(line)
    flush()

    return {k: v for k, v in fields.items() if k}


DATE_LABELS = {
    "order_stop_date": "停止订购日期",
    "production_stop_date": "停止生产日期",
    "support_stop_date": "停止支持日期",
}


def render_model(text: str, site: str) -> str:
    """按站点统一「系列 / Series」写法。

    选了「两个站都要」时填表人只会写一种写法，这里替他转成另一边的习惯写法，
    免得中文的「系列」被原样写进英文站的表格。
    """
    text = text.strip()
    if not text:
        return text
    if site == "zh":
        return re.sub(r"\s*Series$", "系列", text, flags=re.IGNORECASE)
    return re.sub(r"\s*系列$", " Series", text)


def row_line(entry: Dict[str, str]) -> str:
    cells = [
        entry["discontinued_series"],
        entry["replacement_series"],
        entry["order_stop_date"],
        entry["production_stop_date"],
        entry["support_stop_date"],
    ]
    return "| " + " | ".join(c or "-" for c in cells) + " |"


def family_of(model: str) -> str:
    """型号的字母前缀，用来把新行插进同系列那一段（少制造合并冲突）。"""
    m = re.match(r"[A-Za-z]+", model.strip())
    return m.group(0).upper() if m else ""


def table_bounds(lines: List[str]) -> tuple:
    """返回 (表头行号, 第一条数据行号, 最后一条数据行号+1)。

    只认真正的数据表：表头必须能映射出「停产产品系列」和「替代产品系列」两列。
    说明文字里的围栏代码块（例如冲突示例）会被跳过——那里面也有以 | 开头的行，
    早期版本据此误判过表格位置，把数据写进了代码块里。
    """
    header = separator = None
    fenced = False
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            fenced = not fenced
            continue
        if fenced or not stripped.startswith("|"):
            continue
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        if header is None:
            mapped = [normalize_header(c) for c in cells]
            if (
                mapped.count("discontinued_series") == 1
                and mapped.count("replacement_series") == 1
            ):
                header = i
            continue
        separator = i
        break
    if header is None or separator is None:
        raise FormError("数据文件里找不到 EOL 表格，请联系维护人。")
    end = separator + 1
    while end < len(lines) and lines[end].strip().startswith("|"):
        end += 1
    return header, separator + 1, end


def apply_to_site(site: str, action: str, entry: Dict[str, str]) -> str:
    """对某个站点的数据文件执行一次增/改/删，返回一句变更说明。"""
    path = data_file(site)
    lines = path.read_text(encoding="utf-8").splitlines()
    _, first, end = table_bounds(lines)

    entry = dict(entry)
    for field in ("discontinued_series", "replacement_series"):
        entry[field] = render_model(entry[field], site)
    key = match_key(entry["discontinued_series"])

    found = None
    for i in range(first, end):
        cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
        if cells and match_key(cells[0]) == key:
            found = i
            break

    site_name = "中文站" if site == "zh" else "英文站"

    if action == "新增":
        if found is not None:
            raise FormError(
                f"{site_name}的清单里已经有「{entry['discontinued_series']}」了"
                f"（第 {found - first + 1} 条）。如果是要改它，请把操作类型选成「修改」。"
            )
        insert_at = end
        family = family_of(entry["discontinued_series"])
        for i in range(first, end):
            cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
            if cells and family and family_of(cells[0]) == family:
                insert_at = i + 1
        lines.insert(insert_at, row_line(entry))
        summary = f"{site_name}：新增「{entry['discontinued_series']}」"

    elif action == "修改":
        if found is None:
            raise FormError(
                f"{site_name}的清单里没有「{entry['discontinued_series']}」，改不了。"
                f"请确认型号写法是否和清单里一致；如果本来就要加，请把操作类型选成「新增」。"
            )
        old = [c.strip() for c in lines[found].strip().strip("|").split("|")]
        merged = {
            "discontinued_series": entry["discontinued_series"],
            "replacement_series": entry["replacement_series"] or (old[1] if len(old) > 1 else ""),
            "order_stop_date": entry["order_stop_date"] or (old[2] if len(old) > 2 else ""),
            "production_stop_date": entry["production_stop_date"] or (old[3] if len(old) > 3 else ""),
            "support_stop_date": entry["support_stop_date"] or (old[4] if len(old) > 4 else ""),
        }
        merged = {k: ("" if v == "-" else v) for k, v in merged.items()}
        if row_line(merged) == lines[found]:
            raise FormError(
                f"{site_name}的「{entry['discontinued_series']}」内容和现在完全一样，没有需要改的。"
            )
        lines[found] = row_line(merged)
        summary = f"{site_name}：修改「{entry['discontinued_series']}」"

    else:  # 删除
        if found is None:
            raise FormError(
                f"{site_name}的清单里没有「{entry['discontinued_series']}」，无需删除。"
            )
        lines.pop(found)
        summary = f"{site_name}：删除「{entry['discontinued_series']}」（合并后官网上的这条也会被删除）"

    path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description="把 EOL 变更申请应用到数据文件")
    parser.add_argument("--body-file", help="Issue 正文文件；默认读环境变量 ISSUE_BODY")
    args = parser.parse_args()

    if args.body_file:
        body = Path(args.body_file).read_text(encoding="utf-8")
    else:
        body = os.environ.get("ISSUE_BODY", "")
    if not body.strip():
        print("[错误] 没有拿到 Issue 正文。", file=sys.stderr)
        return 2

    try:
        form = parse_issue_form(body)

        action = form.get("action", "").strip()
        if action not in ACTIONS:
            raise FormError(f"「操作类型」要选 {' / '.join(ACTIONS)} 之一，现在是「{action or '空'}」。")

        sites = SITE_CHOICES.get(form.get("site", "").strip())
        if not sites:
            raise FormError(
                f"「适用站点」要选 {' / '.join(SITE_CHOICES)} 之一，"
                f"现在是「{form.get('site') or '空'}」。"
            )

        discontinued = clean_cell(form.get("discontinued_series", ""))
        if not discontinued:
            raise FormError("「停产产品系列」是必填的。")

        entry = {
            "discontinued_series": discontinued,
            "replacement_series": clean_cell(form.get("replacement_series", "")),
        }
        for field in DATE_FIELDS:
            raw = form.get(field, "").strip()
            try:
                entry[field] = parse_date(raw, DATE_LABELS[field]) if raw else ""
            except EolDataError as exc:
                raise FormError(str(exc)) from exc

        if action == "新增":
            missing = [f for f in DATE_FIELDS if not entry[f]]
            if missing:
                raise FormError(
                    "新增记录时三个日期都要填，缺了："
                    + "、".join(DATE_LABELS[f] for f in missing)
                )
            if not entry["replacement_series"]:
                raise FormError("新增记录时「替代产品系列」要填，客户需要知道改用哪个型号。")

        summaries = [apply_to_site(site, action, entry) for site in sites]

        # 改完再整体校验一遍，避免写出后续同步会报错的数据
        for site in sites:
            load_entries(site)

    except FormError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    except EolDataError as exc:
        print(f"数据文件校验没通过：{exc}", file=sys.stderr)
        return 1

    summary = "；".join(summaries)
    print(summary)

    out = os.environ.get("GITHUB_OUTPUT")
    if out:
        slug = re.sub(r"[^A-Za-z0-9]+", "-", discontinued).strip("-").lower()[:40]
        with open(out, "a", encoding="utf-8") as fh:
            fh.write(f"summary={summary}\n")
            fh.write(f"action={action}\n")
            fh.write(f"slug={slug or 'change'}\n")
            fh.write(f"sites={','.join(sites)}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
