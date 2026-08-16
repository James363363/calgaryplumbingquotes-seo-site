# calgaryplumbingquotes.ca

Static local-SEO site for a Calgary residential plumbing business. No framework, no
build dependencies beyond the Python standard library.

**Live:** https://calgaryplumbingquotes.ca
**GA4 Measurement ID:** `G-59S5XWXS6Z` (property "Calgary Plumbing Quotes")

---

## How it works

`build.py` reads a pair of files per page from `content/` and emits `dist/`:

- `content/<slug>.json` — page metadata (title, description, H1, hero image, sidebar
  links, FAQ list)
- `content/<slug>.html` — the `<article>` body fragment only

The build script supplies everything shared: `<head>`, GA4 tag, canonical, Open Graph,
`Plumber` + `BreadcrumbList` + `FAQPage` JSON-LD, header, nav, sidebar, FAQ accordion,
and footer. That keeps the boilerplate byte-identical across all pages, which is the
whole reason for the split — a static site with no templating engine otherwise drifts.

```bash
python3 build.py     # writes dist/
python3 verify.py    # pre-launch checks, exits non-zero on failure
```

Pushing to `main` runs both in CI and deploys `dist/` to GitHub Pages
(`.github/workflows/deploy.yml`). A failing `verify.py` blocks the deploy.

## What verify.py checks

HTML tag balance, JSON-LD validity, presence of `Plumber` schema on every page, the GA4
tag, viewport, Search Console placeholder, exactly one `<h1>` per page, canonical
correctness, title/description uniqueness and length, NAP consistency across all pages,
every internal link resolving to a real built page, every referenced image existing,
`alt` on every `<img>`, sitemap/page-set agreement, and orphan pages with no inbound
internal links.

## Adding a page

1. Create `content/<slug>.json` and `content/<slug>.html`. Copy the shape of an
   existing pair — `content/index.json` is the exemplar.
2. Add it to the `FOOTER` (and optionally `NAV`) lists near the top of `build.py` so it
   gets inbound links. `verify.py` fails the build on orphan pages, by design.
3. Add contextual in-body links to it from related existing pages.
4. Commit. CI rebuilds and redeploys.

`BRIEF.md` holds the editorial standard — voice, the component set, and the verified
facts with their primary sources. **Read it before writing a page.** It also lists the
facts that could not be verified and must not be published.

## Content rules that are not negotiable

- Every hard fact carries a `<p class="source">` citation to a primary source.
- Anything unverified is stated as unverified on the page, not quietly filled in.
- No fabricated reviews, credentials, statistics or prices. Prices are ranges labelled
  as planning estimates; where a figure came from a competitor's page, the page says so.
- Content production is AI-assisted and `/about/` discloses that openly.

## Before going live

See the "replace before launch" checklist in `BRIEF.md`. In short: real business name,
address, phone, licence/WCB/insurance details, founder bio, real reviews, the Search
Console verification token, and a real form handler for the contact form (currently a
`mailto:` stopgap).

## Structure

```
build.py                 site generator
verify.py                pre-launch checks (runs in CI)
styles.css               single shared stylesheet
BRIEF.md                 editorial standard + verified facts
CNAME                    custom domain for Pages
content/                 46 files — one .json + .html pair per page
images/                  23 hero images
.github/workflows/       build + deploy to Pages
```
