# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

InHand Networks unified document asset management platform. Manages user manuals, QA knowledge base, product specs, solution configurations, and brochures — bilingual (zh/en), built with MkDocs Material theme, deployed via GitHub Actions.

## Architecture

```
documents/
├── docs/                          # User manuals (MkDocs site source)
│   ├── zh/                        #   Chinese manuals
│   │   └── {Category}/{Chipset}/{Model}/
│   │       ├── index.md           #   [CI auto-generated] product index with cross-links
│   │       ├── User_Manual.md     #   Manual content
│   │       └── images/            #   Manual images
│   └── en/                        #   English manuals (mirrors zh/ structure)
│
├── qa/                            # QA knowledge base (FAQ articles)
│   ├── zh/                        #   Same path structure as docs/
│   └── en/
│
├── specs/                         # Product datasheets (PDF or Markdown→PDF)
│   ├── zh/
│   └── en/
│
├── configurations/                # Solution configs (independent structure)
│   ├── zh/{Model}/{CaseName}/
│   └── en/{Model}/{CaseName}/
│
├── brochures/                     # Product brochures (PDF)
│   ├── zh/
│   └── en/
│
├── scripts/                       # Build & sync scripts (Python)
├── .github/workflows/             # CI/CD pipelines
├── mkdocs.yml                     # Chinese manual site config
├── mkdocs.en.yml                  # English manual site config
├── mkdocs.qa.zh.yml               # Chinese QA site config
├── mkdocs.qa.en.yml               # English QA site config
└── validate_products.py           # Product name whitelist validation
```

**Content types share the same product directory path** (`{Category}/{Chipset}/{Model}`) across docs/, qa/, specs/, brochures/. Only configurations/ uses an independent structure (`{Model}/{CaseName}/`).

## Common Commands

### Local Preview

```bash
# Install dependencies
pip install -r requirements.txt

# Generate product index pages (dry-run)
python scripts/generate_product_index.py --dry-run

# Generate index pages with coverage report
python scripts/generate_product_index.py --report

# Serve Chinese manual site
python -m mkdocs serve -f mkdocs.yml

# Serve English manual site
python -m mkdocs serve -f mkdocs.en.yml

# Serve Chinese QA site
python -m mkdocs serve -f mkdocs.qa.zh.yml
```

### Build

```bash
# Build Chinese manual → site/
python -m mkdocs build -f mkdocs.yml -d site --clean

# Build English manual → site/en/
python -m mkdocs build -f mkdocs.en.yml -d site/en

# Build specs (Markdown → PDF)
python scripts/build_specs.py
```

### Validation

```bash
# Validate manual directories (default)
python validate_products.py

# Validate specific content paths
python validate_products.py --paths qa/zh qa/en
python validate_products.py --paths specs/zh specs/en
```

### Scaffold New Product

```bash
# Create full scaffold (zh + en) for a new product
python scripts/scaffold_product.py \
  --model EC999 \
  --category "AI Edge Computers" \
  --chipset Rockchip

# Preview only (dry-run)
python scripts/scaffold_product.py \
  --model EC999 \
  --category "AI Edge Computers" \
  --chipset Rockchip \
  --dry-run
```

## CI/CD Pipelines

| Workflow | Trigger Paths | Output | Deploy Target |
|----------|--------------|--------|---------------|
| `deploy-manuals.yml` | `docs/**`, `mkdocs*.yml` | MkDocs static site | Overseas + Domestic servers + GitHub Pages |
| `deploy-qa.yml` | `qa/**` | MkDocs static site | Overseas + Domestic servers + Discourse |
| `deploy-specs.yml` | `specs/**` | PDF files | WordPress server |
| `deploy-downloads.yml` | `downloads/**` | Raw files | WordPress server |

All pipelines trigger on `master` branch push only. Manual trigger via `workflow_dispatch` is also supported.

## Key Scripts

| Script | Purpose |
|--------|---------|
| `scripts/generate_product_index.py` | Auto-generates `index.md` per product with cross-links to QA/specs/configs/brochures |
| `scripts/scaffold_product.py` | Creates directory structure and templates across docs/qa/specs/brochures for a new product |
| `scripts/build_specs.py` | Converts Markdown specs to PDF via Pandoc + WeasyPrint |
| `scripts/discourse_sync.py` | Syncs QA articles to Discourse forum (create/update posts) |
| `scripts/wp_sync.py` | Syncs specs/configs/brochures info to WordPress resource center |
| `validate_products.py` | Validates product directory names against official website API whitelist |

## Directory Naming Rules

- Folder names **must match the official website product names** exactly
- Maximum 3 levels deep: `{Category}/{Chipset}/{Model}/`
- When no sub-category needed, use 2 levels: `{Category}/{Model}/`
- Product index pages (`index.md`) are auto-generated by CI — do not create manually (they are in `.gitignore`)

## Git Workflow

- **Never commit directly to master** — use feature branches + Pull Requests
- Branch naming: `docs-{product-or-team}` (e.g., `docs-Vehicles-teams`)
- CI runs `validate_products.py` before building to check directory names
- PDF files in `specs/` and `brochures/` are managed by Git LFS (see `.gitattributes`)

## Key Dependencies

- **Python 3.11+**: MkDocs build, validation scripts, sync scripts
- **MkDocs Material**: Documentation site theme
- **Pandoc + WeasyPrint**: Markdown-to-PDF conversion for specs
- **GitHub Actions**: CI/CD automation

## Environment Variables (CI Secrets)

| Secret | Purpose |
|--------|---------|
| `CN_API_KEY` / `CN_XK_TOKEN` | Chinese site product API auth |
| `GLOBAL_API_KEY` / `GLOBAL_XK_TOKEN` | Global site product API auth |
| `OVERSEAS_HOST/USER/PASS` | Overseas server deploy credentials |
| `CN_OVERSEAS_HOST/USER/PASS` | Domestic server deploy credentials |
| `OVERSEAS_TARGET` | Server deploy target path |
