# `data/` — build-time data

This directory holds **structured source data**: not site content, but
input for builds and sync jobs.

Site content lives in `docs/zh` and `docs/en` (the `docs_dir` of the two
mkdocs configs). `data/` sits outside the site sources and is **never
published** to the docs site.

## Current contents

| File | Purpose |
| --- | --- |
| `eol-products.zh.md` | EOL list for the Chinese site; data source of the corporate-site EOL page |
| `eol-products.en.md` | EOL list for the English site; same as above |

Both files are **mirrors**, synced automatically from `eol-products/` in
the internal `device-hw-docs` repo. Edits made here are overwritten by
the next sync — see the note at the top of each file.

This repo uses them for two things:

- `scripts/generate_eol_pages.py` → renders the docs-site EOL pages (also feeds `llms.txt`)
- `scripts/sync_eol_products.py` → incremental sync to the corporate WordPress EOL API (triggered by `sync-eol.yml`)

## Conventions for adding a new dataset

### 1. Naming: `<dataset>.<lang>.md`, stay flat at first

The filename prefix is the grouping; with two or three files there is no
need for a subdirectory. For example:

```
data/eol-products.zh.md
data/product-matrix.zh.md
```

Introduce a `data/<dataset>/` subdirectory only when one of these holds:

- a single dataset exceeds 3 files
- two datasets want the same filename
- a dataset needs attachments (images, CSV, …)

When you do split into a directory, update everything together:
`DATA_DIR` in `scripts/eol_data.py`, the path filters of the workflows,
and `--out-dir` in the upstream `eol-sync-to-documents.yml` of
`device-hw-docs`.

### 2. Path filters must name the files — **never use `data/**`**

All four existing workflows trigger on an exact glob:

```yaml
paths:
  - "data/eol-products.*.md"
```

When adding a dataset, **add another line** just like it; do not widen
the filter to `data/**` for convenience.

Reason: `sync-eol.yml` calls the corporate-site API and writes data.
With a directory-wide glob, a change to any dataset would trigger the
EOL sync and produce pointless writes and noise.

### 3. Read files by name, never scan the directory

Existing scripts fetch files through a single entry point — no `glob` /
`iterdir`:

```python
def data_file(site: str) -> Path:
    return DATA_DIR / f"eol-products.{site}.md"
```

Keep that habit so new files are never mistakenly parsed as EOL data by
other scripts.

### 4. Data synced from upstream must be configured on both ends

If a new dataset is also maintained in `device-hw-docs` and synced over,
configure the rendering and push in the upstream
`eol-sync-to-documents.yml` in addition to this repo's path filters.

⚠️ A misaligned cross-repo sync **fails silently** — validation passes,
yet the files never arrive, with no error raised. After wiring it up,
make a real data change and confirm the file actually lands; do not
trust a green pipeline alone.
