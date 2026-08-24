# Content backlog — calgaryplumbingquotes.ca

Single source of truth for what gets published, in what order, and what has already
shipped. **Read this before writing a page. Update it in the same commit as the page.**

This file was created on **2026-08-24**. It did not previously exist — two earlier
scheduled runs (the 2026-08-22 Saturday refresh, and this one) each looked for it and
had to reconstruct the queue from `claude/calgaryplumbingquotes-6month-roadmap.html`
in the Claude project. The queues below are that reconstruction. Keep this file in the
repo so no future run has to guess.

Editorial standard lives in `BRIEF.md`. Nothing here overrides it.

---

## The weekly rhythm

| Day | Asset | Length | Queue |
|---|---|---|---|
| Monday | service / commercial page | 1,200–2,000 w | MONDAY QUEUE |
| Wednesday | homeowner guide | 1,500–2,200 w | WEDNESDAY QUEUE |
| Friday | real case study | 600–1,000 w | **BLOCKED — see below** |
| Saturday | refresh one existing page | — | SATURDAY QUEUE |

---

## MONDAY QUEUE — service / commercial pages

Take the top unpublished item. Respect the note attached to it.

1. **Leak detection Calgary** — `new`. Roadmap Wk 4.
   *Note: the existing `/water-bill-leak-calgary/` page already owns the leak-cost
   arithmetic and the meter/dye-test method. **Verify distinct search intent before
   building.** If the SERP for "leak detection Calgary" is served by the existing page's
   intent, do not build a second URL — strengthen the existing page instead and record
   that here.*
2. **Water softener installation Calgary** — `new`. Roadmap Wk 8.
   *Note: `/calgary-hard-water/` owns the hardness data and the "do you need one"
   question. This page must be the install/commercial half only — sizing, salt vs
   salt-free, drain and bypass requirements, what the job involves. Verify intent split
   before building. Use the verified Bearspaw/Glenmore figures, show the ÷17.1 conversion.*
3. **Tankless water heater installation Calgary** — `new`. Roadmap Wk 5.
   *Note: heavily defended — 8 Calgary competitors, most 2026-dated. Angle on cold
   Calgary inlet temperatures, gas-sizing and venting permit triggers, and hard-water
   descaling as an ongoing cost. Expect 6–12 months to rank; do not read early flatness
   as failure.*
4. **Sewer line repair Calgary** — `new`. Roadmap Wk 10. Trenchless vs conventional.
   *Note: `/sewer-water-line-responsibility-calgary/` owns who-pays. This is the repair
   job itself. The City gives no cost figures — say so.*
5. **Backwater valve installation Calgary** — `new`. Roadmap Wk 11.
   *Note: **two** pages already exist (`/backwater-valve-rebate-calgary/` and
   `/backwater-valve-secondary-suite-calgary/`). Consolidate, do not duplicate. Verify
   there is genuine install-intent demand distinct from those two before building.*
6. **Sewer-line inspection / camera Calgary** — `new`. Roadmap Wk 9.
   *Note: `/sewer-scope-buying-home-calgary/` owns the pre-purchase angle and no plumber
   competes there. Verify distinct intent — this would be the general diagnostic-camera
   service, not the buyer's inspection. If the intent is not distinct, skip it.*

### Deferred from the Monday queue (reasoned, not skipped silently)

- **Emergency plumber Calgary — REBUILD (roadmap Wk 1).** Deferred 2026-08-24.
  The roadmap marked this `rebuild` on 16 Aug because the planner was reconciling a
  publishing plan against a site that already existed; the marker exists to stop anyone
  creating a duplicate URL, not to mandate rewriting a fresh page. `/emergency-plumber-calgary/`
  was built to the current `BRIEF.md` standard on 2026-08-16, runs 2,030 words (in spec),
  and carries its citations. There is no material rebuild work available eight days later.
  **Revisit as a Saturday refresh, or once real after-hours coverage and real reviews
  exist to replace the placeholders.**
- **Drain cleaning Calgary — REBUILD (roadmap Wk 2).** Deferred 2026-08-24, same reason.
  `/drain-cleaning-calgary/` was built 2026-08-16 and runs 2,373 words — **over the
  1,200–2,000 spec**. The real work here is a trim, not a rebuild. **Queued as a Saturday
  refresh instead** (see SATURDAY QUEUE).
- **Hot-water-tank repair & replacement (roadmap Wk 3).** → **Published 2026-08-24** as
  `/hot-water-tank-replacement-calgary/`. Intent verified as distinct from the three
  existing hot-water pages before building — see PUBLISHED below.
- **Poly-B replacement Calgary (roadmap Wk 14).** **Do not build here.**
  `polybreplacementcalgary.com` is a separate owned site targeting exactly this, with its
  own twice-weekly pipeline. Building it here splits the topical signal and competes with
  an owned asset. Cover Poly-B only as an identification section inside the housing-era
  cluster, linking out.

---

## WEDNESDAY QUEUE — homeowner guides

1. What counts as a plumbing emergency (roadmap Wk 1)
2. Why Calgary drains re-block (roadmap Wk 2)
3. Repair vs replace: the decision (roadmap Wk 3) — *check overlap with
   `/hot-water-tank-lifespan-calgary/`, which already has a "Repair or replace" section*
4. Finding a hidden leak (roadmap Wk 4) — *link to `/water-bill-leak-calgary/`, don't repeat the arithmetic*
5. Tank vs tankless operating cost (roadmap Wk 5)
6. Gas vs electric water heater failure modes (roadmap Wk 6)

---

## SATURDAY QUEUE — refresh an existing page

Seasonal order: refresh **ahead of** the season, not during it.

1. **`/drain-cleaning-calgary/`** — trim 2,373 → under 2,000 (over spec), re-verify sources.
   *Promoted here 2026-08-24 from the Monday queue.*
2. `/frozen-pipes-calgary/` — ahead of the freeze window
3. `/frozen-sewer-line-calgary/` — ahead of the freeze window
4. `/no-hot-water-calgary/` — ahead of the winter failure peak
5. `/plumber-cost-calgary/` — trim 2,684 → under 2,000 (over spec)
6. `/sump-pump-calgary/` and `/water-bill-leak-calgary/` — both slightly over spec

**Hard date — 1 January:** City of Calgary permit fees increase annually. The $116.50
homeowner figure and the $9.79-per-$1,000 contractor formula appear on at least five
pages now. A stale fee on a site whose whole pitch is accuracy is the worst possible
error. Diarise it.

---

## FRIDAY LANE — BLOCKED

Case studies require a real completed job, real diagnostic findings, original
photographs and customer consent. **No exceptions — nothing in this lane is written
from imagination.** As of 2026-08-24 there is no operating business and no completed
jobs, so the lane has produced nothing. See
`claude/calgaryplumbingquotes-case-study-capture-log.md` in the Claude project.

---

## PUBLISHED

| Date | URL | Type | Target query | Notes |
|---|---|---|---|---|
| 2026-08-16 | 23 pages — initial build | mixed | — | See `claude/calgaryplumbingquotes-build-summary.md` |
| 2026-08-22 | `/winterize-outdoor-tap-calgary/` | refresh | — | Saturday refresh: re-verified City sources, trimmed to 2,010 w |
| 2026-08-24 | `/hot-water-tank-replacement-calgary/` | service / commercial | hot water tank replacement Calgary | **Intent verified distinct** from `/no-hot-water-calgary/` (symptom), `/hot-water-tank-lifespan-calgary/` (informational) and `/water-heater-permit-calgary/` (permit yes/no) — the SERP for this query is served entirely by commercial install-and-cost pages, and the site had none. Cites calgary.ca trades-permits, the City fee schedule, and the City hardness data; competitor price ranges labelled as self-reported. Corrects the "$100–$300 permit fee" figure published by a ranking competitor against the City's actual $116.50. **Hero image `hero-hotwater.jpg` is reused from `/no-hot-water-calgary/`** — all 23 heroes were already assigned 1:1; replace when original photography lands (roadmap M4). |

---

## Standing rules

- Nothing publishes without inbound internal links — `verify.py` fails on orphans by design.
  Add the page to `FOOTER` (and `NAV` if warranted) in `build.py`, and add contextual
  in-body links from at least two existing pages.
- `python3 build.py && python3 verify.py` must both pass with **zero ERRORS** before commit.
  Warnings about the literal token `None` are known false positives — it is ordinary prose.
- When the Monday queue is exhausted, or down to items whose intent could not be verified
  as distinct, **stop and flag it for fresh keyword research.** Do not invent topics
  unattended.
- Update `content/review-log.json` for any page whose sources you actually opened and
  confirmed. Do not stamp a date you did not earn.
