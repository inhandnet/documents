#!/usr/bin/env python3
"""Generate per-product index.md files with cross-links to QA, specs, config, and brochures.

This script scans `docs/{lang}/{Category}/{Chipset}/{Model}/` and generates an
`index.md` for each product model.  The index aggregates:
  - Manual pages found under docs/
  - QA articles found under qa/
  - Spec sheets found under specs/
  - Configuration files found under config/
  - Brochures (single-page) found under brochures/

Generated files are written *in-place* inside docs/ so MkDocs can pick them up
via `navigation.indexes`.  They are intended to be generated during CI only
(not committed to Git).
"""

import argparse
import os
from pathlib import Path

# Content-type directories that mirror docs/ path structure.
# Each entry: (dir_name, label_zh, label_en, file_extensions)
CONTENT_TYPES = [
    ("qa", "QA", "QA", {".md"}),
    ("specs", "Specs", "Specs", {".pdf", ".docx", ".doc", ".xlsx"}),
    ("brochures", "Brochures", "Brochures", {".pdf", ".docx", ".doc"}),
]

# configurations/ uses a different structure: {lang}/{Model}/{CaseName}/
# Matched by model name only (not Category/Chipset path).
CONFIGURATIONS_EXTENSIONS = {".md", ".cfg", ".conf", ".json", ".yaml", ".yml", ".xml", ".ini", ".txt", ".zip"}

# deployment/ lives inside docs/{lang}/{Category}/{Chipset}/{Model}/deployment/
DEPLOYMENT_EXTENSIONS = {".md", ".cfg", ".conf", ".json", ".yaml", ".yml", ".xml", ".ini", ".txt", ".zip"}

SKIP_DIRS = {"assets", "images", "stylesheets", "javascripts", "_redirects", "deployment"}
SKIP_FILES = {"index.md", ".gitkeep"}


def find_product_dirs(docs_root: Path):
    """Yield (category, chipset, model, model_path) for every product directory.

    Expected layout: docs_root / Category / Chipset / Model /
    """
    if not docs_root.is_dir():
        return
    for category in sorted(docs_root.iterdir()):
        if not category.is_dir() or category.name in SKIP_DIRS:
            continue
        for chipset in sorted(category.iterdir()):
            if not chipset.is_dir() or chipset.name in SKIP_DIRS:
                continue
            for model in sorted(chipset.iterdir()):
                if not model.is_dir() or model.name in SKIP_DIRS:
                    continue
                yield category.name, chipset.name, model.name, model


def collect_manual_files(model_path: Path):
    """Return list of .md files in the model directory (excluding index.md)."""
    files = []
    for f in sorted(model_path.iterdir()):
        if f.is_file() and f.suffix == ".md" and f.name.lower() not in SKIP_FILES:
            files.append(f)
    return files


def collect_deployment_cases(model_path: Path):
    """Return list of .md files under model_path/deployment/ (deployment case docs)."""
    deployment_dir = model_path / "deployment"
    if not deployment_dir.is_dir():
        return []
    files = []
    for f in sorted(deployment_dir.rglob("*")):
        if f.is_file() and f.name.lower() not in SKIP_FILES:
            if f.suffix.lower() in DEPLOYMENT_EXTENSIONS:
                files.append(f)
    return files


def collect_cross_content(repo_root: Path, lang: str, category: str,
                          chipset: str, model: str):
    """Return dict of {content_type: [file_paths]} for QA/specs/configurations/brochures."""
    result = {}

    # Mirror-path content types (qa, specs, brochures)
    for dir_name, _, _, extensions in CONTENT_TYPES:
        content_dir = repo_root / dir_name / lang / category / chipset / model
        if not content_dir.is_dir():
            continue
        files = []
        for f in sorted(content_dir.rglob("*")):
            if f.is_file() and f.name.lower() not in SKIP_FILES:
                if extensions and f.suffix.lower() not in extensions:
                    continue
                files.append(f)
        if files:
            result[dir_name] = files

    # configurations/ uses {lang}/{Model}/{CaseName}/ — match by model name only
    config_dir = repo_root / "configurations" / lang / model
    if config_dir.is_dir():
        files = []
        for f in sorted(config_dir.rglob("*")):
            if f.is_file() and f.name.lower() not in SKIP_FILES:
                if CONFIGURATIONS_EXTENSIONS and f.suffix.lower() not in CONFIGURATIONS_EXTENSIONS:
                    continue
                files.append(f)
        if files:
            result["configurations"] = files

    return result


def build_index_content(lang: str, category: str, chipset: str, model: str,
                        manuals: list, cross_content: dict,
                        deployment_cases: list = None):
    """Build the markdown content for a product index page."""
    is_zh = lang == "zh"

    title = model
    lines = [
        f"---",
        f"title: {title}",
        f"---",
        f"",
        f"# {title}",
        f"",
    ]

    # Breadcrumb-style info
    info_label = "Product Info" if not is_zh else "Product Info"
    lines.append(f"**{category}** / **{chipset}** / **{model}**")
    lines.append("")

    # Manuals section
    if manuals:
        section_title = "User Manual" if not is_zh else "User Manual"
        lines.append(f"## :material-book-open-variant: {section_title}")
        lines.append("")
        for f in manuals:
            name = f.stem.replace("_", " ")
            lines.append(f"- [{name}]({f.name})")
        lines.append("")

    # Deployment cases section (files live under model_path/deployment/)
    if deployment_cases:
        deploy_title = "部署案例" if is_zh else "Deployment Cases"
        lines.append(f"## :material-rocket-launch-outline: {deploy_title}")
        lines.append("")
        for f in deployment_cases:
            name = f.stem.replace("_", " ").replace("-", " ")
            # Link is relative to model dir — use deployment/subpath
            # deployment_cases are collected from model_path/deployment/
            # so relative_to(model_path.parent / model_path.name) would be deployment/...
            # but we can just find the "deployment" boundary in the path
            rel = "/".join(f.parts[f.parts.index("deployment"):])
            if f.suffix == ".md":
                rel = rel.rsplit(".", 1)[0] + ".html"
            lines.append(f"- [{name}]({rel})")
        lines.append("")

    # Cross-content sections
    icon_map = {
        "qa": ":material-frequently-asked-questions:",
        "specs": ":material-file-document-outline:",
        "configurations": ":material-cog-outline:",
        "brochures": ":material-file-chart-outline:",
        "deployment": ":material-rocket-launch-outline:",
    }

    # All cross-content types including configurations
    all_cross_types = list(CONTENT_TYPES) + [
        ("configurations", "Configurations", "Configurations", CONFIGURATIONS_EXTENSIONS),
    ]

    for dir_name, label_zh, label_en, _ in all_cross_types:
        if dir_name not in cross_content:
            continue
        files = cross_content[dir_name]
        label = label_zh if is_zh else label_en
        icon = icon_map.get(dir_name, "")

        # Build the relative URL to the other site's content
        lines.append(f"## {icon} {label}")
        lines.append("")

        for f in files:
            name = f.stem.replace("_", " ")
            # For QA (MkDocs site at /kb/), link to the built page
            if dir_name == "qa" and f.suffix == ".md":
                rel = f"{category}/{chipset}/{model}/{f.stem}.html"
                if is_zh:
                    url = f"/kb/{rel}"
                else:
                    url = f"/kb/en/{rel}"
                lines.append(f"- [{name}]({url})")
            elif dir_name == "configurations":
                # configurations/ uses {lang}/{Model}/... structure
                # Build path relative to configurations/ root
                try:
                    rel = f.relative_to(repo_root / "configurations")
                except ValueError:
                    rel = f.name
                lines.append(f"- [{f.name}](/configurations/{rel})")
            else:
                # For specs/brochures, link to the raw file path
                rel = f"{dir_name}/{lang}/{category}/{chipset}/{model}/{f.name}"
                lines.append(f"- [{f.name}](/{rel})")
        lines.append("")

    # If nothing found at all, add a placeholder
    if not manuals and not cross_content:
        if is_zh:
            lines.append("*This product currently has no documents.*")
        else:
            lines.append("*This product currently has no documents.*")
        lines.append("")

    return "\n".join(lines)


def generate_completeness_report(repo_root: Path, all_products: dict):
    """Print a completeness report to stdout and optionally to GitHub Actions Job Summary."""
    check = "\u2705"
    cross = "\u274c"

    # --- stdout plain text ---
    print("\n" + "=" * 70)
    print("Product Documentation Completeness Report")
    print("=" * 70)

    content_keys = ["manuals", "deployment", "qa", "specs", "configurations", "brochures"]
    col_labels = ["Manual", "Deploy", "QA", "Specs", "Configurations", "Brochures"]

    header = f"{'Product':<30} " + " ".join(f"{c:^10}" for c in col_labels)
    print(header)
    print("-" * 82)

    total = 0
    complete = 0
    for key in sorted(all_products.keys()):
        info = all_products[key]
        lang, cat, chip, model = key
        flags = ["Y" if info.get(k) else "-" for k in content_keys]
        label = f"[{lang}] {model}"
        print(f"{label:<30} " + " ".join(f"{f:^10}" for f in flags))
        total += 1
        if all(info.get(k) for k in content_keys):
            complete += 1

    print("-" * 82)
    pct = (complete / total * 100) if total else 0
    print(f"Total: {total} products, {complete} fully documented ({pct:.0f}%)")
    print("=" * 82)

    # --- GitHub Actions Job Summary (Markdown table) ---
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if not summary_path:
        return

    md_lines = [
        "## Product Documentation Completeness Report",
        "",
        f"> **{total}** products total, **{complete}** fully documented (**{pct:.0f}%**)",
        "",
        "| Product | " + " | ".join(col_labels) + " |",
        "|---------|" + "|".join(":---:" for _ in col_labels) + "|",
    ]
    for key in sorted(all_products.keys()):
        info = all_products[key]
        lang, cat, chip, model = key
        row = [f"`[{lang}]` {model}"] + [
            check if info.get(k) else cross for k in content_keys
        ]
        md_lines.append("| " + " | ".join(row) + " |")
    md_lines.append("")

    with open(summary_path, "a", encoding="utf-8") as f:
        f.write("\n".join(md_lines) + "\n")


def main():
    parser = argparse.ArgumentParser(
        description="Generate per-product index.md with cross-links"
    )
    parser.add_argument(
        "--repo-root", type=Path, default=Path("."),
        help="Repository root directory (default: current directory)"
    )
    parser.add_argument(
        "--langs", nargs="+", default=["zh", "en"],
        help="Languages to process (default: zh en)"
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Print generated content without writing files"
    )
    parser.add_argument(
        "--report", action="store_true",
        help="Print completeness report"
    )
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    generated = 0
    all_products = {}

    for lang in args.langs:
        docs_root = repo_root / "docs" / lang

        for category, chipset, model, model_path in find_product_dirs(docs_root):
            manuals = collect_manual_files(model_path)
            cross = collect_cross_content(repo_root, lang, category, chipset, model)
            deployment = collect_deployment_cases(model_path)

            # Track for report
            product_key = (lang, category, chipset, model)
            all_products[product_key] = {
                "manuals": manuals,
                "deployment": deployment,
                **{k: v for k, v in cross.items()},
            }

            content = build_index_content(
                lang, category, chipset, model, manuals, cross,
                deployment_cases=deployment,
            )

            index_path = model_path / "index.md"
            if args.dry_run:
                print(f"\n--- {index_path.relative_to(repo_root)} ---")
                print(content)
            else:
                index_path.write_text(content, encoding="utf-8")
                generated += 1
                print(f"  Generated: {index_path.relative_to(repo_root)}")

    if not args.dry_run:
        print(f"\nGenerated {generated} index.md file(s).")

    if args.report:
        generate_completeness_report(repo_root, all_products)


if __name__ == "__main__":
    main()
