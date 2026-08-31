#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
用户手册永久链接跳转页生成器

在 mkdocs build 之后运行，扫描构建产物，为每个有用户手册的产品生成
一个固定 URL 的跳转页（user-manual.html），指向当前版本的手册页面。

用法：
  python scripts/generate_manual_redirects.py --site-dir site-zh --lang zh
  python scripts/generate_manual_redirects.py --site-dir site-en --lang en

URL 规则：
  英文: https://www.inhand.com/manuals/{Product}/user-manual.html
  中文: https://www.inhand.com.cn/manuals/{Product}/user-manual.html
"""

import argparse
import sys
import urllib.parse
from pathlib import Path

sys.stdout = __import__("io").TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# 语言 → 用户手册子目录名
MANUALS_SUBDIR = {
    "zh": "用户手册",
    "en": "User manual",
}


def log(msg):
    print(f"[REDIRECT] {msg}", flush=True)


def find_html_files(manual_dir: Path) -> list:
    """找到目录下所有 .html 文件"""
    return sorted(manual_dir.glob("*.html"))


def generate_redirect(site_dir: Path, product: str, manuals_subdir: str, target_html: str) -> Path:
    """生成跳转页"""
    redirect_path = site_dir / product / "user-manual.html"
    # URL encode 相对路径
    encoded = urllib.parse.quote(target_html)
    html = f"""<!DOCTYPE html>
<html><head>
<meta charset="utf-8">
<meta http-equiv="refresh" content="0;url={encoded}">
<title>Redirecting...</title>
</head>
<body>
<p>Redirecting to user manual... <a href="{encoded}">Click here</a></p>
</body></html>
"""
    redirect_path.write_text(html, encoding="utf-8")
    return redirect_path


def main():
    parser = argparse.ArgumentParser(description="生成用户手册永久链接跳转页")
    parser.add_argument("--site-dir", required=True, help="mkdocs build 输出目录")
    parser.add_argument("--lang", required=True, choices=["zh", "en"], help="语言")
    args = parser.parse_args()

    site_dir = Path(args.site_dir)
    lang = args.lang
    manuals_subdir = MANUALS_SUBDIR[lang]

    if not site_dir.exists():
        log(f"ERROR: site 目录不存在: {site_dir}")
        sys.exit(1)

    log(f"=== 生成用户手册跳转页 ===")
    log(f"site 目录: {site_dir}")
    log(f"语言: {lang}, 手册子目录: {manuals_subdir}")

    generated = 0
    skipped = []
    details = []

    # 扫描 site_dir 下所有产品目录
    for product_dir in sorted(site_dir.iterdir()):
        if not product_dir.is_dir():
            continue
        # 跳过 assets、javascripts、stylesheets 等非产品目录
        if product_dir.name in ("assets", "javascripts", "stylesheets", "search", "css", "js", "img", "fonts"):
            continue

        manual_dir = product_dir / "Manuals" / manuals_subdir
        if not manual_dir.exists():
            continue

        html_files = find_html_files(manual_dir)
        if not html_files:
            skipped.append((product_dir.name, "目录里没有 .html 文件"))
            continue

        if len(html_files) == 1:
            target = html_files[0]
        else:
            # 多文件时警告，取第一个（按文件名排序）
            names = [f.name for f in html_files]
            log(f"  WARNING: {product_dir.name} 有 {len(html_files)} 个文件: {names}，使用第一个")
            target = html_files[0]

        # 计算相对路径（从 product/user-manual.html 到 Manuals/xxx/xxx.html）
        relative_target = f"Manuals/{manuals_subdir}/{target.name}"

        redirect_path = generate_redirect(site_dir, product_dir.name, manuals_subdir, relative_target)
        generated += 1
        details.append((product_dir.name, target.name))

    # 输出报告
    log(f"\n=== {lang.upper()} Redirect Report ===")
    for product, target in details:
        log(f"  ✅ {product:25s} → {target}")
    for product, reason in skipped:
        log(f"  ❌ {product:25s} → {reason}")
    log(f"Total: {generated} generated, {len(skipped)} skipped")

    if generated == 0:
        log("WARNING: 没有生成任何跳转页！")


if __name__ == "__main__":
    main()
