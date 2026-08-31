# InHand Product Documentation

This repository contains the source files for InHand Networks product documentation, built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and deployed automatically.

## Website

- **English**: https://inhand.com
- **Chinese**: https://inhand.com.cn

## Repository Structure

```
├── docs/
│   ├── en/              # English documentation
│   └── zh/              # Chinese documentation
│
├── data/                # Structured data synced to the website (EOL list)
├── scripts/             # Build, validation, EOL sync scripts
│   ├── sync_eol_products.py   # push data/*.md tables to the website API
│   └── generate_eol_pages.py # render the docs-site EOL pages from data/
├── overrides/           # MkDocs theme customizations
├── mkdocs.yml           # Chinese site configuration
└── mkdocs.en.yml        # English site configuration
```

## Product Directory Layout

Documentation is organized by product model:

```
docs/en/
├── CPE02/
│   ├── Manuals/
│   │   ├── CPE02_User_Manual.md
│   │   └── images/
│   ├── Specs/           # Product specifications
│   └── Solutions/       # Solution configurations
├── EC300/
│   └── Manuals/
│       └── ...
└── index.md
```

### Product Catalog Automation

`docs/product-catalog.json` maps documentation folders to a stable product
identity. The Documents MCP indexer only requires a catalog entry for a
top-level `docs/{en,zh}/<folder>` that contains at least one Markdown file
-- that's the folder set it actually resolves chunks from. A folder made up
purely of PDFs (e.g. a shared spec-sheet aggregation folder for several
sub-models) is resolved per-PDF by filename matching instead and does not
need to appear in `source_folders` at all.

When a push adds a new top-level folder under `docs/en/` or `docs/zh/` that
contains Markdown, the `sync-product-catalog` GitHub Actions workflow runs
`scripts/sync_product_catalog.py` and commits a new catalog entry for it
automatically (`kind: model`, `public: true`, no aliases). You do not need to
edit the catalog by hand for a plain new Markdown product folder. A new
pure-PDF folder is left alone by design -- if a PDF in it can't be resolved
to a product, the MCP build itself will fail loudly, which is the correct
signal for a human to look at it.

A human still needs to edit `docs/product-catalog.json` manually for:

- **Aliases** for a product (alternate names it should also resolve under).
- **Adjusting `kind`** (e.g. `family` for a product family, `software` for
  non-hardware products) or `public` (internal-only entries).
- **Merging multiple folders into one product**, e.g. a product that ships
  a differently-named folder per language (`source_folders: ["Eagle Energy
  Management", "白鹰能源管家"]`), or a pure-PDF aggregation folder that should
  be registered under an existing product's `source_folders`.
- **De-listing a product** or reconciling a renamed/removed folder. The sync
  script never deletes or edits an existing catalog entry -- it only appends
  new ones for new Markdown folders. It does not check whether a registered
  folder still exists on disk (disk existence isn't what the MCP build
  actually validates), so it will not warn about that case; rely on the MCP
  build's own validation for that.

## Local Development

### Prerequisites

- Python 3.11+
- pip

### Setup

```bash
pip install -r requirements.txt
```

### Preview

```bash
# Chinese site
python -m mkdocs serve -f mkdocs.yml

# English site
python -m mkdocs serve -f mkdocs.en.yml
```

### Build

```bash
python -m mkdocs build -f mkdocs.yml -d site-zh --clean
python -m mkdocs build -f mkdocs.en.yml -d site-en --clean
```

## EOL Product List

The EOL tables on the corporate site are driven by two hand-editable Markdown
tables — the Chinese and English lists are maintained independently because
their contents legitimately differ:

| File | Website page |
|------|--------------|
| [`data/eol-products.zh.md`](data/eol-products.zh.md) | https://www.inhand.com.cn/support/eol-products |
| [`data/eol-products.en.md`](data/eol-products.en.md) | https://www.inhand.com/en/support/eol-products |

**These two files are mirrors — don't edit them here.** The lists are maintained in
the internal `device-hw-docs` repository (marketing and product staff file a change
request there through an issue form) and synced into this repository automatically;
edits made here are overwritten by the next sync.

When a sync lands, CI prints a dry-run of exactly which rows would be
created, updated or deleted on the website. Merging to `master` syncs the list
to the WordPress EOL REST API via `.github/workflows/sync-eol.yml`. The sync is
incremental, idempotent and fully bidirectional: rows created, changed or removed
in the table are created, updated or deleted on the website.

The same data also feeds the documentation site: `scripts/generate_eol_pages.py`
renders `docs/<lang>/EOL Products/EOL Products.md`, which is published with the
manuals and indexed in `llms.txt` (so the docs QA agent and AI crawlers can
answer EOL questions). Those pages are generated — edit the `data/` files.

If a sync run fails, the workflow opens (or comments on) a GitHub issue labelled
`eol-sync`, because a failure means the repo and the website have drifted. The
sync is idempotent: fix the cause and re-run the workflow.

Endpoints are configured per site as repo variables `EOL_API_ZH_URL` /
`EOL_API_EN_URL` plus secrets `EOL_API_ZH_TOKEN` / `EOL_API_EN_TOKEN`, so moving
from a staging host to production is a variable change, not a code change.

```bash
# local preview
export EOL_API_ZH_URL="https://<host>/wp-json/eol/v1"
export EOL_API_ZH_TOKEN="..."
python scripts/sync_eol_products.py --site zh --dry-run
```

## Contributing

We welcome contributions to improve our documentation. Please submit changes via Pull Requests.

- Create a feature branch from `master`
- Make your changes
- Submit a Pull Request for review

## License

Copyright (c) InHand Networks. All rights reserved.
