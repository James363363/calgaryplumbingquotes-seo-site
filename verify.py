#!/usr/bin/env python3
"""Pre-launch verification for the built site in dist/."""
import json
import os
import re
import sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, "dist")
DOMAIN = "https://calgaryplumbingquotes.ca"
GA4 = "G-59S5XWXS6Z"
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr"}

errors, warnings = [], []


class Balance(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.bad = []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack:
            self.bad.append("closing </%s> with empty stack" % tag)
        elif self.stack[-1] == tag:
            self.stack.pop()
        elif tag in self.stack:
            while self.stack and self.stack[-1] != tag:
                self.bad.append("unclosed <%s> before </%s>" % (self.stack.pop(), tag))
            if self.stack:
                self.stack.pop()
        else:
            self.bad.append("stray </%s>" % tag)


pages = {}
for dirpath, _, files in os.walk(DIST):
    if "index.html" in files:
        rel = os.path.relpath(dirpath, DIST)
        url = "/" if rel == "." else "/" + rel.replace(os.sep, "/") + "/"
        with open(os.path.join(dirpath, "index.html"), encoding="utf-8") as fh:
            pages[url] = fh.read()

print("Found %d built pages\n" % len(pages))

titles, descs, canons = {}, {}, {}
total_faqs = 0

for url, html in sorted(pages.items()):
    p = "[%s]" % url

    # --- tag balance
    b = Balance()
    b.feed(html)
    if b.bad:
        errors.append("%s HTML imbalance: %s" % (p, "; ".join(b.bad[:4])))
    if b.stack:
        errors.append("%s unclosed at EOF: %s" % (p, b.stack))

    # --- JSON-LD
    blocks = re.findall(
        r'<script type="application/ld\+json">\s*(.*?)\s*</script>', html, re.S)
    if not blocks:
        errors.append("%s no JSON-LD" % p)
    types = []
    for blk in blocks:
        try:
            obj = json.loads(blk)
            types.append(obj.get("@type"))
            if obj.get("@type") == "FAQPage":
                n = len(obj.get("mainEntity", []))
                total_faqs += n
                for q in obj["mainEntity"]:
                    if "<" in q["acceptedAnswer"]["text"]:
                        errors.append("%s FAQ answer contains raw HTML in schema" % p)
                    if not q["acceptedAnswer"]["text"].strip():
                        errors.append("%s empty FAQ answer in schema" % p)
        except json.JSONDecodeError as e:
            errors.append("%s invalid JSON-LD: %s" % (p, e))
    # FAQ markup must correspond to FAQ content the visitor can actually see,
    # or it is invisible-content structured data (policy violation).
    has_faq_schema = "FAQPage" in types
    has_faq_visible = 'class="faq"' in html
    if has_faq_schema and not has_faq_visible:
        errors.append("%s FAQPage schema but no visible FAQ section" % p)
    if has_faq_visible and not has_faq_schema:
        warnings.append("%s visible FAQ but no FAQPage schema" % p)

    if "Plumber" not in types:
        errors.append("%s missing LocalBusiness/Plumber schema" % p)
    if "BreadcrumbList" not in types:
        warnings.append("%s missing BreadcrumbList" % p)

    # --- head essentials
    if GA4 not in html:
        errors.append("%s missing GA4 tag" % p)
    if 'name="viewport"' not in html:
        errors.append("%s missing viewport" % p)
    if "google-site-verification" not in html:
        errors.append("%s missing Search Console placeholder" % p)

    m = re.search(r"<title>(.*?)</title>", html, re.S)
    if not m:
        errors.append("%s no <title>" % p)
    else:
        t = m.group(1)
        titles.setdefault(t, []).append(url)
        if len(t) > 62:
            warnings.append("%s title %d chars: %s" % (p, len(t), t[:66]))

    m = re.search(r'<meta name="description" content="(.*?)">', html, re.S)
    if not m:
        errors.append("%s no meta description" % p)
    else:
        d = m.group(1)
        descs.setdefault(d, []).append(url)
        if len(d) > 158:
            warnings.append("%s description %d chars" % (p, len(d)))

    m = re.search(r'<link rel="canonical" href="(.*?)">', html)
    if not m:
        errors.append("%s no canonical" % p)
    else:
        canons.setdefault(m.group(1), []).append(url)
        if m.group(1) != DOMAIN + url:
            errors.append("%s canonical mismatch: %s" % (p, m.group(1)))

    if len(re.findall(r"<h1[ >]", html)) != 1:
        errors.append("%s does not have exactly one <h1>" % p)

    # --- NAP consistency
    for token in ["(403) 555-0100", "info@calgaryplumbingquotes.ca", "Calgary, AB"]:
        if token not in html:
            errors.append("%s NAP token missing: %s" % (p, token))

    # --- internal links resolve
    for href in set(re.findall(r'href="(/[^"#?]*)"', html)):
        target = href if href.endswith("/") else href + "/"
        if href in ("/styles.css", "/favicon.svg", "/sitemap.xml", "/robots.txt"):
            if not os.path.exists(os.path.join(DIST, href.lstrip("/"))):
                errors.append("%s missing asset %s" % (p, href))
            continue
        if target not in pages:
            errors.append("%s broken internal link -> %s" % (p, href))

    # --- images exist + have alt
    for src in set(re.findall(r'<img [^>]*src="(/[^"]+)"', html)):
        if not os.path.exists(os.path.join(DIST, src.lstrip("/"))):
            errors.append("%s missing image %s" % (p, src))
    for tag in re.findall(r"<img [^>]*>", html):
        if 'alt="' not in tag:
            errors.append("%s <img> without alt" % p)

    # --- leftover template artifacts
    for bad in ["DOMAIN/PATH", "BUSINESS_NAME", "IMAGE_URL", "None", "{{", "}}"]:
        if bad in html:
            warnings.append("%s contains suspicious token %r" % (p, bad))

# --- duplicates
for label, d in (("title", titles), ("description", descs), ("canonical", canons)):
    for val, urls in d.items():
        if len(urls) > 1:
            errors.append("duplicate %s across %s: %s" % (label, urls, val[:60]))

# --- sitemap
sm = open(os.path.join(DIST, "sitemap.xml"), encoding="utf-8").read()
locs = set(re.findall(r"<loc>(.*?)</loc>", sm))
expected = {DOMAIN + u for u in pages}
if locs != expected:
    errors.append("sitemap mismatch: missing %s / extra %s"
                  % (expected - locs, locs - expected))

rb = open(os.path.join(DIST, "robots.txt"), encoding="utf-8").read()
if "Sitemap: %s/sitemap.xml" % DOMAIN not in rb:
    errors.append("robots.txt missing sitemap reference")

# --- orphan check (every page linked from at least one other page)
linked = set()
for url, html in pages.items():
    for href in re.findall(r'href="(/[^"#?]*)"', html):
        t = href if href.endswith("/") else href + "/"
        if t != url:
            linked.add(t)
orphans = [u for u in pages if u not in linked and u != "/"]
if orphans:
    errors.append("orphan pages (no inbound internal links): %s" % orphans)

# --- report
print("FAQ questions in schema across site: %d" % total_faqs)
print("Unique titles: %d / %d" % (len(titles), len(pages)))
print()
if warnings:
    print("WARNINGS (%d)" % len(warnings))
    for w in warnings:
        print("  ! " + w)
    print()
if errors:
    print("ERRORS (%d)" % len(errors))
    for e in errors:
        print("  X " + e)
    sys.exit(1)
print("All checks passed.")
