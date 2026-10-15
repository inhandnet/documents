"""Feed real git revision dates into the sitemap <lastmod>.

mkdocs core initializes page.update_date to the build clock and nothing
overwrites it, so sitemap.xml ends up with one uniform build timestamp
(mkdocs-material issue #6107). git-revision-date-localized already
resolved the true per-file commit date into page.meta -- copy its ISO
value onto update_date; the sitemap template renders afterwards and
reads exactly this attribute.
"""


def on_page_content(html, page, **kwargs):
    iso = page.meta.get("git_revision_date_localized_raw_iso_date")
    if iso:
        page.update_date = iso
    return html
