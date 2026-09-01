# SEO tracking — calgaryplumbingquotes.ca

Monthly snapshot file. Each run appends a new dated block so the next run has
something to diff against. **Do not rewrite history in this file.** Newest last.

## What this file can and cannot measure right now

**Google Search Console is not connected.** There is no GSC app in the Zapier
catalog for this account, and no SEMrush connection either. That means impressions,
clicks, CTR, average position, and the actual queries people searched are **not
available to any scheduled run**. Everything below is Google Analytics 4 only, which
sees a session *after* the click and never sees the query.

Consequences, stated plainly so no future run pretends otherwise:

- "Which pages gained or lost position" — **not measurable.** GA4 has no position data.
- "Pages with impressions but few clicks" — **not measurable.** GA4 has no impressions.
- "Pages ranking 4–15" — **not measurable.**
- "Queries nobody planned" — **not measurable.** GA4 shows the landing page, never the query.

The `WebSearch` tool available to scheduled runs is US-localised, so it cannot be used
to spot-check Calgary SERPs either — it returns generic national results for Calgary
queries and is worse than useless as a rank proxy. **Do not build a rank table from it.**

**The fix is one task: verify calgaryplumbingquotes.ca in Google Search Console** and
connect it (Zapier has no GSC app — the practical route is the GSC API via a service
account, or manual export). Until that exists, every monthly review is landing-page
counts and nothing more.

---

## 2026-09-01 — baseline (first monthly review)

Site age at snapshot: **17 days** (launched 2026-08-15/16). Everything here is a
baseline to diff against, not a result. Volumes are far too small to carry meaning.

**GA4 property:** Calgary Plumbing Quotes (`properties/550018832`), timezone
America/Edmonton. Window 2026-08-15 → 2026-09-01.

### Sessions by channel

| Channel | Source | Sessions |
|---|---|---|
| Direct | (direct) | 87 |
| Organic Search | google | 13 |
| Organic Search | bing | 6 |
| **Total** | | **106** |

The 87 direct sessions are **not readers**. 71 of them land on `/` and they track the
cadence of the scheduled runs' own live-site checks. Treat direct as instrumentation
noise until there is a reason not to.

### Organic sessions by landing page — the only real signal

| Landing page | Organic sessions |
|---|---|
| `/backwater-valve-rebate-calgary/` | 7 |
| `/basement-bathroom-plumbing-calgary/` | 7 |
| `/` | 2 |
| `/gas-line-permit-calgary/` | 2 |
| `/water-heater-permit-calgary/` | 1 |
| **Total** | **19** |

**19 organic sessions over 17 days. This is noise.** It is recorded as a baseline, not
read as a finding. Nineteen sessions cannot distinguish a good page from a lucky one.

The one thing worth *watching* (not acting on): all five pages that drew any organic at
all are permit-, rebate- or regulation-shaped — the pages built on cited City of Calgary
primary sources. None of them is a commercial service page. That is consistent with the
site's stated edge, and it is also exactly what you would expect from five data points
of random variation. **Re-check at the next snapshot before treating it as real.**

### Pages with zero traffic

The three most recently published pages — `/hot-water-tank-replacement-calgary/`
(2026-08-24), `/tank-vs-tankless-operating-cost-calgary/` (2026-08-26) and
`/leak-detection-calgary/` (2026-08-31) — have **zero** pageviews. Expected. A new URL
on a 2-week-old domain with no inbound links has nothing to draw on yet. Not a defect,
not a deploy failure, and **not a reason to touch those pages.**

### Staleness

**Nothing is stale.** Oldest `review-log.json` entries are 2026-08-15/16 — 17 days. The
90-day staleness threshold is not reachable until mid-November. No refresh work is
justified by age this month; the Saturday queue should keep running on seasonal order
instead.

### Deploy verification — NOT completed this run

`WebFetch` requires interactive approval that an unattended scheduled run cannot obtain,
so **the live site was not fetched this run.** Deployment status is therefore
*inferred*, not verified:

- 19 organic sessions arrived on five different pages during this window. The site is
  live, indexed and serving. That much is certain.
- Whether the newest commits (through `282283d`, 2026-08-31) reached the edge is
  **unconfirmed.** Zero traffic on those pages is not evidence either way.

Per the 2026-08-24 correction in the Monday log: do **not** infer deploy failure from
the repo. There is no `.github/workflows/` because this site deploys via **Cloudflare
Pages, Git-connected**. An attended run should fetch `/leak-detection-calgary/` and
confirm the H1 renders.
