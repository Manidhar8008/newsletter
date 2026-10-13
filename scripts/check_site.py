#!/usr/bin/env python3
"""Validate generated Jekyll output and newsletter post conventions."""
from __future__ import annotations

import argparse
import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


class PageAudit(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.title_depth = 0
        self.title = ""
        self.description = None
        self.links: list[str] = []
        self.image_missing_alt: list[str] = []

    def handle_starttag(self, tag: str, attrs) -> None:
        values = dict(attrs)
        if tag == "title":
            self.title_depth = 1
        elif tag == "meta" and values.get("name", "").lower() == "description":
            self.description = values.get("content", "")
        elif tag in ("a", "link") and values.get("href"):
            self.links.append(values["href"])
        elif tag == "img" and "alt" not in values:
            self.image_missing_alt.append(values.get("src", "(image without src)"))

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.title_depth = 0

    def handle_data(self, data: str) -> None:
        if self.title_depth:
            self.title += data


def front_matter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise ValueError("missing YAML front matter")
    end = text.find("\n---", 3)
    if end < 0:
        raise ValueError("unterminated YAML front matter")
    values: dict[str, str] = {}
    for line in text[3:end].splitlines():
        match = re.match(r"^([A-Za-z_][\w-]*):\s*(.*?)\s*$", line)
        if match:
            values[match.group(1)] = match.group(2).strip().strip('"').strip("'")
    return values


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site", default="_site")
    parser.add_argument("--baseurl", default="")
    args = parser.parse_args()
    site = Path(args.site)
    errors: list[str] = []

    if not site.is_dir():
        print(f"ERROR: generated site directory not found: {site}", file=sys.stderr)
        return 2

    posts = sorted(Path("_posts").glob("*.md"))
    titles: Counter[str] = Counter()
    permalinks: Counter[str] = Counter()
    naming = re.compile(r"^\d{4}-\d{2}-\d{2}-.+\.md$")
    for post in posts:
        if not naming.match(post.name):
            errors.append(f"{post}: expected YYYY-MM-DD-title.md")
        try:
            meta = front_matter(post)
            title = meta.get("title", "").strip()
            date = meta.get("date", "").strip()
            if not title:
                errors.append(f"{post}: missing title in front matter")
            if not re.match(r"^\d{4}-\d{2}-\d{2}$", date):
                errors.append(f"{post}: date must use YYYY-MM-DD")
            if title:
                titles[title.casefold()] += 1
            if meta.get("permalink"):
                permalinks[meta["permalink"]] += 1
        except (OSError, ValueError) as exc:
            errors.append(f"{post}: {exc}")

    for title, count in titles.items():
        if count > 1:
            errors.append(f"duplicate post title ({count}): {title}")
    for permalink, count in permalinks.items():
        if count > 1:
            errors.append(f"duplicate permalink ({count}): {permalink}")

    html_files = sorted(site.rglob("*.html"))
    if not html_files:
        errors.append("no generated HTML pages found")

    checked_links = 0
    for html in html_files:
        audit = PageAudit()
        try:
            audit.feed(html.read_text(encoding="utf-8"))
        except (OSError, UnicodeError) as exc:
            errors.append(f"{html}: cannot read HTML: {exc}")
            continue
        rel = html.relative_to(site)
        if not audit.title.strip():
            errors.append(f"{rel}: missing <title>")
        if audit.description is None or not audit.description.strip():
            errors.append(f"{rel}: missing meta description")
        elif len(audit.description.strip()) >= 160:
            errors.append(f"{rel}: meta description must be under 160 characters (got {len(audit.description.strip())})")
        for src in audit.image_missing_alt:
            errors.append(f"{rel}: image missing alt attribute: {src}")

        for raw in audit.links:
            parsed = urlparse(raw)
            if parsed.scheme or parsed.netloc or raw.startswith(("mailto:", "tel:", "data:", "javascript:")):
                continue
            path = unquote(parsed.path)
            if not path:
                continue
            if args.baseurl and (path == args.baseurl or path.startswith(args.baseurl.rstrip("/") + "/")):
                path = path[len(args.baseurl):] or "/"
            if path.startswith("/"):
                target = site / path.lstrip("/")
            else:
                target = html.parent / path
            candidates = [target]
            if not target.suffix:
                candidates.extend([target / "index.html", target.with_suffix(".html")])
            if not any(p.is_file() for p in candidates):
                errors.append(f"{rel}: broken internal link: {raw}")
            checked_links += 1

    feed_candidates = [site / "feed.xml", site / "atom.xml"]
    feed = next((p for p in feed_candidates if p.is_file()), None)
    if feed:
        try:
            ET.parse(feed)
        except ET.ParseError as exc:
            errors.append(f"{feed.relative_to(site)}: invalid XML: {exc}")
    else:
        errors.append("RSS/Atom feed not generated (expected feed.xml or atom.xml)")

    total_bytes = sum(p.stat().st_size for p in site.rglob("*") if p.is_file())
    print(f"Audited {len(posts)} posts, {len(html_files)} HTML pages, {checked_links} internal links.")
    print(f"Generated site size: {total_bytes / 1024:.1f} KiB")
    if errors:
        print(f"FAILED: {len(errors)} issue(s)")
        for error in errors:
            print(f" - {error}")
        return 1
    print("PASS: newsletter content, HTML metadata, image alt attributes, internal links, and feed XML.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
