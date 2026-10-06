"""MkDocs hook: lazy-load the badge images on the list page.

The list page renders about 2,700 shields.io badges. Without this, every
browser requests all of them on load and shields.io rate-limits some of them.
With loading="lazy" the browser fetches only the ones near the viewport.
"""

import re

_IMG = re.compile(r"<img(?![^>]*\bloading=)")


def on_page_content(html, page, config, files):
    if page.file.src_uri != "list.md":
        return html
    return _IMG.sub('<img loading="lazy" decoding="async"', html)
