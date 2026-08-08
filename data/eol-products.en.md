# EOL Product List (English site)

Single source of truth for the table on <https://www.inhand.com/en/support/eol-products>.
**The Chinese and English lists are intentionally different** — each site has its own
file. See [eol-products.zh.md](eol-products.zh.md) for the Chinese site.

## How to edit

1. Edit the table below: add / change / remove a row, keep the five columns.
2. Write dates as `YYYY-MM-DD` (the `7/24/2026` style used on the website is
   accepted too and converted automatically).
3. Open a PR. CI runs a dry-run and prints exactly which rows would be created,
   updated or deleted on the website — merge to `master` once that looks right,
   and the site updates itself. No WordPress admin work needed.
4. Removing a row here does **not** delete it on the website (guard against
   accidents); it is only reported. To really delete, dispatch the workflow with
   `prune` checked.

This table also feeds the documentation site: CI renders
`docs/en/EOL Products/EOL Products.md` from it, published with the manuals and
indexed in `llms.txt` (so AI assistants and crawlers can answer EOL questions).
That page is generated — never edit it by hand, edit this table.

Local preview: `python scripts/sync_eol_products.py --site en --dry-run`

## List

| EOL Product         | Replacement         | End of Ordering | End of Production | End of Support |
|---------------------|---------------------|-----------------|-------------------|----------------|
| VG814-FS59-W-G-V    | VG814-F09-W-G-V     | 2026-07-24      | 2026-09-24        | 2030-07-24     |
| VG814-FQ59-W-G-V    | VG814-F09-W-G-V     | 2026-07-24      | 2026-09-24        | 2030-07-24     |
| VG814-FS59-W-G-R    | VG814-F09-W-G-R     | 2026-07-24      | 2026-09-24        | 2030-07-24     |
| VG814-FQ59-W-G-R    | VG814-F09-W-G-R     | 2026-07-24      | 2026-09-24        | 2030-07-24     |
| IR915L-FQ39 Series  | IR315-FF39 Series   | 2024-08-23      | 2024-10-23        | 2028-08-23     |
| IR912L-FQ39         | IR315-FF39 Series   | 2024-08-23      | 2024-10-23        | 2028-08-23     |
| IR615-S-FQ88 Series | IR315-FQ88 Series   | 2024-01-05      | 2024-03-05        | 2029-01-05     |
| IR615-S-FS39 Series | IR315-FF39 Series   | 2024-01-05      | 2024-03-05        | 2029-01-05     |
| IR305-FQ33 Series   | IR315-FF39 Series   | 2025-07-31      | 2025-10-31        | 2027-05-07     |
| IR305-FQ39 Series   | IR315-FF39 Series   | 2024-08-23      | 2024-10-23        | 2029-08-23     |
| IR302-FQ02 Series   | IR302-FQ33-S Series | 2024-12-15      | 2024-12-31        | 2029-12-15     |
| IR301               | IR302               | 2024-12-15      | 2024-12-31        | 2029-12-15     |
| IR611-S             | IR302/IR315         | 2021-04-01      | 2021-12-01        | 2026-04-01     |
