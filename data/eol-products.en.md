# EOL Product List (English site)

Single source of truth for the table on <https://www.inhand.com/en/support/eol-products>.
**The Chinese and English lists are intentionally different** — each site has its own
file. See [eol-products.zh.md](eol-products.zh.md) for the Chinese site.

## How to edit

**The easy way: don't edit this file — file a change request instead.**
On the repository's Issues tab choose New issue → "EOL 产品变更申请", fill in the
form (operation, model, dates) and submit. A bot edits this table for you and
opens a PR for a maintainer to review. No Markdown, no Git needed.

Editing the file directly, for maintainers comfortable with Git:

1. Edit the table below: add / change / remove a row, keep the five columns.
2. Write dates as `YYYY-MM-DD` (the `7/24/2026` style used on the website is
   accepted too and converted automatically).
3. Open a PR. CI runs a dry-run and prints exactly which rows would be created,
   updated or deleted on the website — merge to `master` once that looks right,
   and the site updates itself. No WordPress admin work needed.
4. **Removing a row here deletes the matching record on the website too**, on the
   next merge — deletion is permanent and cannot be undone, so double-check before
   removing a model. Preview the effect with `--no-delete` first if unsure.

This table also feeds the documentation site: CI renders
`docs/en/EOL Products/EOL Products.md` from it, published with the manuals and
indexed in `llms.txt` (so AI assistants and crawlers can answer EOL questions).
That page is generated — never edit it by hand, edit this table.

Local preview: `python scripts/sync_eol_products.py --site en --dry-run`

## Editing alongside others

Each row is an independent product, so **edits to different rows merge cleanly** —
Git handles them automatically. Only two situations actually collide: two people
both **appending to the end of the table**, or two people editing **the same row**.

Two habits that avoid most collisions:

- **Insert a new row inside its product group** (an IR model among the IR rows, an
  ER model among the ER rows) instead of everyone appending at the bottom.
- **Sync before you edit** (`git pull`, or reopen the file on the web) and open the
  PR promptly — long-lived branches collide more.

**If Git reports a conflict, don't worry — two new rows is the easiest kind to fix**,
because both sides are correct and you simply keep both. The file will show three
marker lines:

```
<<<<<<< HEAD
| IR999-XX Series | IR315-FF39 Series | 2027-01-01 | 2027-03-01 | 2030-01-01 |
=======
| ER888-YY | ER815-NRQ1 | 2027-02-01 | 2027-04-01 | 2030-02-01 |
>>>>>>> their branch
```

Fix it by **deleting the `<<<<<<<`, `=======` and `>>>>>>>` marker lines and keeping
both product rows**, then commit. GitHub's "Resolve conflicts" button lets you do this
in the browser — no command line needed. If the conflict is on the *same* row with
different values, check with the other person instead of picking one yourself.

The PR dry-run prints the final result, so you can verify before merging.

## List

| EOL Product | Replacement | End of Ordering | End of Production | End of Support |
| --------------------- | --------------------- | ----------------- | ------------------- | ---------------- |
| VG814-FS59-W-G-V | VG814-F09-W-G-V | 2026-07-24 | 2026-09-24 | 2030-07-24 |
| VG814-FQ59-W-G-V | VG814-F09-W-G-V | 2026-07-24 | 2026-09-24 | 2030-07-24 |
| VG814-FS59-W-G-R | VG814-F09-W-G-R | 2026-07-24 | 2026-09-24 | 2030-07-24 |
| VG814-FQ59-W-G-R | VG814-F09-W-G-R | 2026-07-24 | 2026-09-24 | 2030-07-24 |
| IR915L-FQ39 Series | IR315-FF39 Series | 2024-08-23 | 2024-10-23 | 2028-08-23 |
| IR912L-FQ39 | IR315-FF39 Series | 2024-08-23 | 2024-10-23 | 2028-08-23 |
| IR615-S-FQ88 Series | IR315-FQ88 Series | 2024-01-05 | 2024-03-05 | 2029-01-05 |
| IR615-S-FS39 Series | IR315-FF39 Series | 2024-01-05 | 2024-03-05 | 2029-01-05 |
| IR305-FQ33 Series | IR315-FF39 Series | 2025-07-31 | 2025-10-31 | 2027-05-07 |
| IR305-FQ39 Series | IR315-FF39 Series | 2024-08-23 | 2024-10-23 | 2029-08-23 |
| IR302-FQ02 Series | IR302-FQ33-S Series | 2024-12-15 | 2024-12-31 | 2029-12-15 |
| IR301 | IR302 | 2024-12-15 | 2024-12-31 | 2029-12-15 |
| IR611-S | IR302/IR315 | 2021-04-01 | 2021-12-01 | 2026-04-01 |
