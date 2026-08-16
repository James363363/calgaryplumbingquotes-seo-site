#!/usr/bin/env python3
"""
Static site builder for calgaryplumbingquotes.ca

Reads content/<slug>.json (metadata + FAQs) and content/<slug>.html (body fragment)
and emits dist/<path>/index.html with byte-identical header/nav/footer/schema
across every page, plus sitemap.xml and robots.txt.
"""
import json
import os
import re
import shutil
from datetime import date
from html import unescape

ROOT = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.join(ROOT, "content")
DIST = os.path.join(ROOT, "dist")

# ---------------------------------------------------------------- constants
DOMAIN = "https://calgaryplumbingquotes.ca"
BUSINESS = "[BUSINESS NAME]"           # placeholder — swap for real trade name
BRAND = "Calgary Plumbing Quotes"      # site/brand name derived from the domain
PHONE_DISPLAY = "(403) 555-0100"       # placeholder
PHONE_TEL = "+14035550100"             # placeholder
EMAIL = "info@calgaryplumbingquotes.ca"
GA4_ID = "G-59S5XWXS6Z"
TODAY = date.today().isoformat()
UPDATED_HUMAN = date.today().strftime("%B %-d, %Y")

NAV = [
    ("/", "Home"),
    ("/emergency-plumber-calgary/", "Emergency"),
    ("/no-hot-water-calgary/", "Hot Water"),
    ("/drain-cleaning-calgary/", "Drains &amp; Sewers"),
    ("/frozen-pipes-calgary/", "Frozen Pipes"),
    ("/plumber-cost-calgary/", "What It Costs"),
    ("/homeowner-plumbing-permits-alberta/", "Permits"),
    ("/about/", "About"),
    ("/contact/", "Contact"),
]

FOOTER = [
    ("Hot water &amp; water supply", [
        ("/no-hot-water-calgary/", "No hot water? Start here"),
        ("/hot-water-tank-lifespan-calgary/", "How long tanks last in Calgary"),
        ("/water-heater-permit-calgary/", "Water heater permits"),
        ("/calgary-hard-water/", "Calgary hard water &amp; softeners"),
        ("/low-water-pressure-calgary/", "Low water pressure"),
        ("/water-bill-leak-calgary/", "High water bill? Find the leak"),
    ]),
    ("Drains, sewers &amp; basements", [
        ("/drain-cleaning-calgary/", "Drain cleaning"),
        ("/sewer-water-line-responsibility-calgary/", "Who owns your sewer line"),
        ("/backwater-valve-rebate-calgary/", "Backwater valve rebates"),
        ("/backwater-valve-secondary-suite-calgary/", "Backwater valves &amp; suites"),
        ("/sump-pump-calgary/", "Sump pumps"),
        ("/sewer-scope-buying-home-calgary/", "Sewer scope before you buy"),
    ]),
    ("Winter &amp; emergencies", [
        ("/emergency-plumber-calgary/", "Emergency plumbing"),
        ("/frozen-pipes-calgary/", "Frozen &amp; burst pipes"),
        ("/frozen-sewer-line-calgary/", "Frozen sewer lines"),
        ("/winterize-outdoor-tap-calgary/", "Winterize your outdoor tap"),
    ]),
    ("Costs, permits &amp; company", [
        ("/plumber-cost-calgary/", "What a plumber costs"),
        ("/homeowner-plumbing-permits-alberta/", "DIY plumbing &amp; the law"),
        ("/gas-line-permit-calgary/", "Gas line permits"),
        ("/basement-bathroom-plumbing-calgary/", "Basement bathroom plumbing"),
        ("/about/", "About us"),
        ("/contact/", "Contact &amp; free quote"),
    ]),
]


# ---------------------------------------------------------------- helpers
def strip_tags(markup: str) -> str:
    """Plain text for JSON-LD answer fields.

    Block-level tags become spaces so paragraphs don't concatenate
    ("...price.Diagnostics are..."), and HTML entities are fully decoded so
    "&minus;30&nbsp;&deg;C" doesn't reach a rich result as raw entity text.
    """
    text = re.sub(r"</(p|div|li|ul|ol|h[1-6]|section|table|tr)>", " ", markup)
    text = re.sub(r"<br\s*/?>", " ", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = unescape(text)
    text = text.replace(" ", " ")
    return re.sub(r"\s+", " ", text).strip()


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def business_schema() -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "Plumber",
        "@id": DOMAIN + "/#business",
        "name": BUSINESS,
        "alternateName": BRAND,
        "image": DOMAIN + "/images/hero-pillar.jpg",
        "url": DOMAIN + "/",
        "telephone": PHONE_DISPLAY,
        "email": EMAIL,
        # priceRange and openingHoursSpecification are deliberately omitted until
        # the real business confirms them — publishing unverified availability as
        # structured data is a claim, not a placeholder.
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "[STREET ADDRESS]",
            "addressLocality": "Calgary",
            "addressRegion": "AB",
            "postalCode": "[POSTAL CODE]",
            "addressCountry": "CA",
        },
        "areaServed": [
            {"@type": "City", "name": "Calgary", "addressRegion": "AB", "addressCountry": "CA"}
        ],
        "knowsAbout": [
            "Emergency plumbing", "Water heater repair and replacement",
            "Drain cleaning", "Sewer line repair", "Backwater valve installation",
            "Frozen pipe thawing", "Sump pump installation",
            "Basement bathroom rough-in", "Gas line installation",
        ],
    }


def build_head(meta: dict, faqs: list) -> str:
    path = meta["path"]
    canonical = DOMAIN + path
    img = DOMAIN + "/images/" + meta.get("image", "hero-pillar.jpg")

    graph = [business_schema()]

    # Breadcrumbs
    crumbs = [{"@type": "ListItem", "position": 1, "name": "Home", "item": DOMAIN + "/"}]
    if path != "/":
        crumbs.append({"@type": "ListItem", "position": 2,
                       "name": meta.get("crumb", meta["h1"]), "item": canonical})
    graph.append({"@context": "https://schema.org", "@type": "BreadcrumbList",
                  "itemListElement": crumbs})

    if faqs:
        graph.append({
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [{
                "@type": "Question",
                "name": strip_tags(f["q"]),
                "acceptedAnswer": {"@type": "Answer", "text": strip_tags(f["a"])},
            } for f in faqs],
        })

    schema_blocks = "\n".join(
        '<script type="application/ld+json">\n%s\n</script>'
        % json.dumps(b, indent=2, ensure_ascii=False) for b in graph
    )

    return f"""<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(meta['title'])}</title>
<meta name="description" content="{esc(meta['description'])}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1">
<meta name="geo.region" content="CA-AB">
<meta name="geo.placename" content="Calgary">
<meta property="og:type" content="website">
<meta property="og:locale" content="en_CA">
<meta property="og:site_name" content="{esc(BRAND)}">
<meta property="og:title" content="{esc(meta.get('og_title', meta['title']))}">
<meta property="og:description" content="{esc(meta['description'])}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{img}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(meta.get('og_title', meta['title']))}">
<meta name="twitter:description" content="{esc(meta['description'])}">
<meta name="twitter:image" content="{img}">
<!-- Google Search Console verification — REPLACE the content value with the real
     token from Search Console before launch, then submit /sitemap.xml -->
<meta name="google-site-verification" content="[SEARCH-CONSOLE-VERIFICATION-CODE]">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/styles.css">
<!-- Google tag (gtag.js) — GA4 property "Calgary Plumbing Quotes" -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GA4_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GA4_ID}');
</script>
{schema_blocks}"""


def build_header(path: str) -> str:
    items = "".join(
        '<li><a href="%s"%s>%s</a></li>' % (
            href, ' aria-current="page"' if href == path else "", label)
        for href, label in NAV
    )
    return f"""<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><div class="wrap">
  <span>Serving Calgary and the surrounding area</span>
  <a href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
</div></div>
<header class="site">
  <div class="wrap hdr">
    <a class="brand" href="/">
      <svg width="34" height="34" viewBox="0 0 34 34" aria-hidden="true"><rect width="34" height="34" rx="8" fill="#0b3c5d"/><path d="M11 9h5.5a4.5 4.5 0 0 1 0 9H14v7h-3V9zm3 3v3h2.5a1.5 1.5 0 0 0 0-3H14z" fill="#fff"/><circle cx="24" cy="23" r="3.2" fill="#14919b"/></svg>
      <span class="brand-text"><b>{BRAND}</b><span>Licensed Calgary plumbing</span></span>
    </a>
    <div class="hdr-cta">
      <a class="tel" href="tel:{PHONE_TEL}"><small>Call or text</small><b>{PHONE_DISPLAY}</b></a>
      <a class="btn btn-primary btn-sm" href="/contact/">Free quote</a>
    </div>
  </div>
  <nav class="main" aria-label="Main"><ul>{items}</ul></nav>
</header>"""


def build_footer() -> str:
    cols = ""
    for heading, links in FOOTER:
        lis = "".join('<li><a href="%s">%s</a></li>' % (h, t) for h, t in links)
        cols += f'<div><h3>{heading}</h3><ul>{lis}</ul></div>'
    return f"""<footer class="site">
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-nap">
        <h3>Contact</h3>
        <b>{BUSINESS}</b>
        <p>[STREET ADDRESS]<br>Calgary, AB [POSTAL CODE]</p>
        <p><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a><br>
           <a href="mailto:{EMAIL}">{EMAIL}</a></p>
        <p>Serving Calgary and surrounding communities.<br>
           After-hours cover: <span class="placeholder">[CONFIRM AFTER-HOURS COVERAGE]</span></p>
        <p><span class="placeholder">[LICENCE / WCB / INSURANCE INFO]</span></p>
      </div>
      {cols}
    </div>
    <div class="foot-bottom">
      <p>&copy; {date.today().year} {BUSINESS} (operating as {BRAND}). All rights reserved.</p>
      <p>Guidance on this site is general information for Calgary homeowners, not a substitute
         for an on-site assessment by a licensed plumber or gasfitter. City of Calgary rules,
         permit fees and code requirements change &mdash; always confirm current requirements
         with <a href="https://www.calgary.ca/development/permits/plumbing-gas.html" rel="nofollow">The City of Calgary</a>
         or 311 before starting work. Prices shown are ranges for planning purposes only and are
         not quotes.</p>
      <p>Page last reviewed {UPDATED_HUMAN}.</p>
    </div>
  </div>
</footer>"""


def build_faq(faqs: list) -> str:
    if not faqs:
        return ""
    items = ""
    for f in faqs:
        items += (f'<details><summary>{f["q"]}</summary>'
                  f'<div class="fa">{f["a"]}</div></details>\n')
    return f"""<section class="faq" id="faq">
<h2>Questions Calgary homeowners actually ask</h2>
{items}</section>"""


def build_sidebar(meta: dict) -> str:
    related = meta.get("sidebar_links", [])
    lis = "".join('<li><a href="%s">%s</a></li>' % (h, t) for h, t in related)
    block = ""
    if lis:
        block = f'<div class="side"><h3>Related guides</h3><ul>{lis}</ul></div>'
    return f"""<aside>
  <div class="side side-cta">
    <h3>Get a straight answer &mdash; and a price</h3>
    <p>Tell us what's happening and we'll tell you what it takes to fix it, what it should
       cost, and whether it can wait. No charge to ask.</p>
    <a class="side-phone" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
    <a class="btn btn-primary btn-sm" href="/contact/">Request a free quote</a>
  </div>
  {block}
</aside>"""


def build_page(slug: str) -> str:
    with open(os.path.join(CONTENT, slug + ".json"), encoding="utf-8") as fh:
        meta = json.load(fh)
    with open(os.path.join(CONTENT, slug + ".html"), encoding="utf-8") as fh:
        body = fh.read()

    faqs = meta.get("faqs", [])
    head = build_head(meta, faqs)
    header = build_header(meta["path"])
    footer = build_footer()

    hero_img = meta.get("image", "hero-pillar.jpg")
    hero_alt = esc(meta.get("image_alt", "Plumbing work in a Calgary home"))

    if meta.get("layout") == "home":
        hero = f"""<section class="hero"><div class="wrap"><div class="hero-grid">
  <div>
    <h1>{meta['h1']}</h1>
    <p class="lede">{meta['lede']}</p>
    <div class="btn-row">
      <a class="btn btn-primary" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
      <a class="btn btn-ghost" href="/contact/">Get a free quote</a>
    </div>
    <div class="hero-trust">
      <span>&#10003; Upfront pricing before we start</span>
      <span>&#10003; We tell you when it can wait</span>
      <span>&#10003; Sources cited on every guide</span>
    </div>
  </div>
  <div><img src="/images/{hero_img}" alt="{hero_alt}" width="900" height="600" fetchpriority="high"></div>
</div></div></section>"""
        # FAQ must be visible on the page wherever FAQPage schema is emitted.
        main = hero + '<div class="wrap page">' + body + build_faq(faqs) + "</div>"
    else:
        crumb = meta.get("crumb", meta["h1"])
        main = f"""<div class="wrap page">
<nav aria-label="Breadcrumb" style="font-size:.85rem;margin-bottom:14px;color:#6b7b86">
  <a href="/">Home</a> &rsaquo; <span>{crumb}</span>
</nav>
<div class="layout">
<article>
  <h1>{meta['h1']}</h1>
  <p class="updated">Written for Calgary homeowners &middot; Last reviewed {UPDATED_HUMAN}</p>
  <figure><img src="/images/{hero_img}" alt="{hero_alt}" width="1000" height="600" fetchpriority="high"></figure>
{body}
{build_faq(faqs)}
</article>
{build_sidebar(meta)}
</div></div>"""

    return f"""<!doctype html>
<html lang="en-CA">
<head>
{head}
</head>
<body>
{header}
<main id="main">
{main}
</main>
{footer}
</body>
</html>
"""


def main():
    slugs = sorted(f[:-5] for f in os.listdir(CONTENT) if f.endswith(".json"))
    if os.path.isdir(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST)

    urls = []
    for slug in slugs:
        with open(os.path.join(CONTENT, slug + ".json"), encoding="utf-8") as fh:
            meta = json.load(fh)
        path = meta["path"]
        outdir = DIST if path == "/" else os.path.join(DIST, path.strip("/"))
        os.makedirs(outdir, exist_ok=True)
        with open(os.path.join(outdir, "index.html"), "w", encoding="utf-8") as fh:
            fh.write(build_page(slug))
        urls.append((DOMAIN + path, meta.get("priority", "0.8")))
        print("built %-52s -> %s" % (path, os.path.relpath(outdir, ROOT)))

    # static assets
    shutil.copy(os.path.join(ROOT, "styles.css"), os.path.join(DIST, "styles.css"))
    if os.path.isdir(os.path.join(ROOT, "images")):
        shutil.copytree(os.path.join(ROOT, "images"), os.path.join(DIST, "images"),
                        dirs_exist_ok=True)
    if os.path.exists(os.path.join(ROOT, "favicon.svg")):
        shutil.copy(os.path.join(ROOT, "favicon.svg"), os.path.join(DIST, "favicon.svg"))
    if os.path.exists(os.path.join(ROOT, "CNAME")):
        shutil.copy(os.path.join(ROOT, "CNAME"), os.path.join(DIST, "CNAME"))

    # sitemap
    entries = "\n".join(
        f"  <url>\n    <loc>{u}</loc>\n    <lastmod>{TODAY}</lastmod>\n"
        f"    <changefreq>monthly</changefreq>\n    <priority>{p}</priority>\n  </url>"
        for u, p in sorted(urls, key=lambda x: (-float(x[1]), x[0]))
    )
    with open(os.path.join(DIST, "sitemap.xml"), "w", encoding="utf-8") as fh:
        fh.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                 '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                 + entries + "\n</urlset>\n")

    with open(os.path.join(DIST, "robots.txt"), "w", encoding="utf-8") as fh:
        fh.write("User-agent: *\nAllow: /\n\n"
                 f"Sitemap: {DOMAIN}/sitemap.xml\n")

    with open(os.path.join(DIST, ".nojekyll"), "w") as fh:
        fh.write("")

    print("\n%d pages built. Sitemap + robots.txt written." % len(urls))


if __name__ == "__main__":
    main()
