#!/usr/bin/env python3
"""批量在产品目录下的子分类目录中创建 .pages 文件（hide: true）。"""

from pathlib import Path

PAGES_CONTENT = "hide: true\n"

# 合法的子分类目录名（中文 + 英文）
SUB_CATEGORIES = {
    "通用", "4G版", "5G版", "1G版", "Road", "Rail",
    "General", "4G Version", "5G Version", "1G Version",
    "Python SDK", "Docker SDK", "Greengrass SDK",
    "Device Supervisor Agent", "FlexAPI",
    "用户手册", "安装指南", "快速用户手册",
    "User manual", "Installation Guide", "Quick user manual",
}


def create_pages_files(docs_root: Path):
    """在 docs/zh/ 和 docs/en/ 下的子分类目录中创建 .pages 文件。"""
    for lang in ["zh", "en"]:
        lang_path = docs_root / lang
        if not lang_path.exists():
            continue
        for product_dir in lang_path.iterdir():
            if not product_dir.is_dir() or product_dir.name in {"assets", "javascripts", "stylesheets"}:
                continue
            for sub_dir in product_dir.iterdir():
                if not sub_dir.is_dir():
                    continue
                # 如果是合法的子分类目录，创建 .pages
                if sub_dir.name in SUB_CATEGORIES:
                    pages_file = sub_dir / ".pages"
                    if not pages_file.exists():
                        pages_file.write_text(PAGES_CONTENT, encoding="utf-8")
                        print(f"Created: {pages_file}")


if __name__ == "__main__":
    docs = Path("docs")
    create_pages_files(docs)
    print("Done.")
