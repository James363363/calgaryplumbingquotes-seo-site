# Writing brief — calgaryplumbingquotes.ca

You are writing pages for a Calgary residential plumbing site. Read this whole file
before writing anything.

## Read these first (mandatory)

1. `/root/.claude/plugins/synced/calgary-seo-site-builder/skills/build-seo-site/references/copywriting-guide.md`
2. `/root/calgaryplumbingquotes/content/index.html` and `index.json` — the pillar page.
   **This is the exemplar.** Match its voice, density, HTML component usage and honesty
   level exactly. Do not invent new CSS classes; only use the ones it uses.

## Output format — exactly two files per page

### `content/<slug>.json`

```json
{
  "path": "/url-path/",
  "priority": "0.8",
  "crumb": "Short breadcrumb label",
  "title": "Under 60 chars, keyword-relevant, unique",
  "og_title": "Optional, more human framing",
  "description": "Under 155 chars, benefit-led, unique",
  "h1": "Matches page topic, not identical to title",
  "image": "hero-xxx.jpg",
  "image_alt": "Specific descriptive alt text, not keyword stuffing",
  "sidebar_links": [["/other-page/", "Link text"], ["/another/", "Link text"]],
  "faqs": [
    {"q": "Question in the words a homeowner would use", "a": "<p>HTML answer.</p><p>Second para.</p>"}
  ]
}
```

- 4–6 FAQs per page. Answers 2–3 paragraphs, wrapped in `<p>` tags.
- **FAQ voice is non-negotiable**: a Calgary homeowner explaining it to a neighbour over the
  fence. Plain language. Local reality (winter, housing stock era, City rules). Never
  marketing copy. Read the pillar page's FAQs — match that register.
- `title` MUST be under 60 characters. `description` MUST be under 155 characters. Count them.

### `content/<slug>.html`

The `<article>` body fragment only. **Do not** include `<h1>`, `<head>`, header, footer,
sidebar, the FAQ section, or the hero `<figure>` — the build script adds all of those.
Start directly with content. Wrap major sections in `<section>`.

## Available HTML components (use these, invent nothing)

- `<div class="answer"><p><strong>Short answer:</strong> ...</p></div>` — the direct answer,
  near the top. Use on every informational page.
- `<div class="callout">` — warning / "don't do this" / time-sensitive.
- `<div class="note">` — caveat, methodology note, or a marked placeholder.
- `<p class="source">Source: <a href="URL" rel="nofollow">Name</a></p>` — after any cited fact.
- `<div class="tablewrap"><table>…</table></div>` — all tables must be wrapped.
- `<ul class="checks">` — benefit/checklist lists.
- `<ol class="steps"><li><strong>Do this.</strong> Explanation.</li></ol>` — sequential steps.
- `<div class="cards">` + `<div class="card"><h3>…</h3><p>…</p></div>` — benefit grids.
  Add `cards-3` to the wrapper for a 3-up grid.
- `<div class="cta"><h2>…</h2><p>…</p><div class="btn-row"><a class="btn btn-primary" href="tel:+14035550100">Call (403) 555-0100</a> <a class="btn btn-ghost" href="/contact/">…</a></div></div>`
- `<div class="related"><h2>…</h2><ul>…</ul></div>` — internal links, near the end.
- `<span class="placeholder">[LABEL]</span>` — for anything not yet real.

## Non-negotiable content rules

1. **Reader-first opening.** First sentence is about the reader's situation, never the
   business. No "We are Calgary's leading…". Ever.
2. **Match structure to intent** (stated per page below):
   - *Informational* → direct answer in the first two sentences (`.answer` block), then
     explanation, then a soft CTA.
   - *Commercial-investigation* → lead with the honest answer including ranges and
     tradeoffs; build trust through transparency; medium CTA.
   - *Local-transactional* → service + area + speed up top, strong CTA early, trust
     signals nearby.
3. **Feature → benefit, always.** Never state a feature without the homeowner benefit.
   Formula: [Feature] means [what it does] so [what the homeowner actually gets].
   If a sentence names a feature with no stated benefit, rewrite it.
4. **Semantic coverage.** Cover the surrounding field naturally — related parts, brands,
   symptoms, synonyms, the obvious follow-up question. Do not keyword-stuff. Do not
   leave an obvious adjacent subtopic uncovered.
5. **Cite every hard fact** with `<p class="source">` immediately after it. Only use facts
   from the verified list below, or facts you verify yourself with WebSearch/WebFetch
   during writing.
6. **Never fabricate.** No invented reviews, no invented credentials, no invented
   statistics, no invented City programs. If you want a fact that isn't in the verified
   list, either verify it live or write around it.
7. **Prices**: only present as ranges, always labelled as planning estimates and not
   quotes, and where a figure came from a competitor's self-reported page, say so
   ("plumbers around the city publish rates in the range of…"). There is no authoritative
   public source for Calgary plumber rates — be honest about that, it's a differentiator.
8. **Length**: 1,200–2,000 words of body content. Substance over padding. Every paragraph
   must earn its place — if it could appear on a plumbing site in any city, cut it or
   localize it.
9. **Internal links**: 4–8 contextual in-body links to other pages on the site (use the
   URL list below), plus a `.related` block. Every page links back to `/` (the pillar) at
   least once in the body, naturally.
10. **Date-stamp claims about rules and programs** ("As of August 2026, …") so the page
    ages honestly.

## Placeholders (use exactly these)

- Business name: `[BUSINESS NAME]` — the brand is "Calgary Plumbing Quotes"
- Phone: `(403) 555-0100`, tel link `tel:+14035550100`
- Email: `info@calgaryplumbingquotes.ca`
- Licence/insurance: `<span class="placeholder">[LICENCE / WCB / INSURANCE INFO]</span>`
- Reviews: `<span class="placeholder">[ADD REAL REVIEWS HERE]</span>`

## VERIFIED FACTS — safe to state and cite

**City of Calgary — water/sewer responsibility**
- City owns from the water main to the property line; homeowner owns from the property line
  to the house. Homeowner pays "all repair costs to the service on private property (with
  the exception of the water meter)." The property line typically ends "a few metres from
  the edge of the curb or sidewalk." The water service valve (curb stop) sits very close to
  the property line but **The City owns it** — homeowners and plumbers cannot legally operate it.
  Source: https://www.calgary.ca/water/customer-service/water-service-lines-calgary.html
- Sewer: "Builders or homeowners are responsible for providing the water and sewer service
  connections from the property line to the residential or commercial plumbing system."
  Source: https://www.calgary.ca/development/home-building/water-sewer-connections.html
- Sewer backup procedure: call 311. The agent determines whether it's internal plumbing or
  possibly City infrastructure. "City crews will not move furniture, pull back carpet, remove
  toilets or make holes in drywall to identify the source of the backup." If the blockage is
  on private property the customer is advised to call a plumber.
  Source: https://www.calgary.ca/water/wastewater/sewage-backup.html
- Water service line leaks: under the Water Utility Bylaw an owner must repair a confirmed
  service line leak **within 15 days** or the City may issue a remedial order. Repair methods:
  trenchless service pull, excavation, or hydrovac spot repair. The City gives no cost figures.
  Source: https://www.calgary.ca/water/customer-service/water-service-line-leaks-calgary.html

**City of Calgary — permits and fees**
- Homeowner's plumbing permit: **$112 permit fee + $4.50 Safety Codes Council fee = $116.50**,
  $0 processing fee. Fees increase annually on January 1.
- Homeowner eligibility, all three required: own the home; live in it or intend to reside in
  it (not a rental); do the work yourself (cannot pull a permit on a contractor's behalf).
  Not available for apartment-style condos; individually owned rowhouse/townhouse units need
  condo board authorization.
- A plumbing permit **is** required when a plumbing system is constructed, extended or
  altered, and when water and sewer lines in or around the home are replaced.
- A plumbing permit is **not** required to: repair a leak in a water distribution or drainage
  system; replace existing faucets and fixtures; remove a blockage in the drainage.
- Homeowners **cannot** pull a gas permit unless they hold Alberta first- or second-class
  gasfitter certification, reside (or intend to reside) at the address, and apply in person
  with proof of qualifications. Otherwise a licensed contractor must pull it.
- Exception: a homeowner may pull a gas fireplace permit to install the insert themselves,
  but a licensed gas fitter must make the gas line connection.
- Homeowners cannot do HVAC/mechanical work.
- Rough-in and final inspections required; someone 18+ must be present. Inspections booked
  via 311 or VISTA; next-day requests by 2 p.m.
  Sources: https://www.calgary.ca/development/home-building/trades-permits.html
           https://www.calgary.ca/development/permits/plumbing-gas.html
- Contractor trade permit: $112 processing + $9.79 per $1,000 of construction value; SCC fee
  4% of permit fee ($4.50 min / $560 max); $116.50 minimum.
  Source: https://www.calgary.ca/content/dam/www/pda/pd/documents/fees/building-and-trade-permit-fee-schedule.pdf

**Alberta trade licensing**
- Plumber is a **compulsory certification trade** in Alberta — you must hold a journeyperson
  certificate, a recognized trade certificate, or be a registered apprentice to perform the
  restricted activities. Apprenticeship is 4 periods, each 1,560 hours of work experience +
  8 weeks classroom. Red Seal endorsement requires passing **both** the Plumber and the
  Gasfitter Class B interprovincial exams. Gasfitting is a separate ticket from plumbing.
  Source: https://tradesecrets.alberta.ca/trades-in-alberta/profiles/006/
- **Owner exemption**: the restricted activities may be performed by "any individual who is
  performing the restricted activity in respect of any property that the individual owns, has
  possession of or control over, and intends only for personal and not-for-profit use by the
  individual." The "not-for-profit use" wording strongly implies the exemption does NOT cover
  work in a rental unit or a suite you intend to rent — present that as a reasonable reading,
  clearly flagged as such, NOT as settled law, and tell readers to confirm with Alberta
  Apprenticeship and Industry Training or a lawyer.
  Source: https://tradesecrets.alberta.ca/trades-in-alberta/profiles/006/classes-of-individuals/

**Backwater valves**
- "A plumbing permit is required to install a back-flow prevention device."
  Source: https://www.calgary.ca/environment/resources/climate-ready-measures-drainage-and-water-management.html
- City of Calgary plumbing advisory (dated Oct 4, 2022): National Plumbing Code 2020 requires
  fixtures located below the level of the adjoining street and subject to backflow to be
  protected (NPC 2020 s. 2.4.6.4). A normally-open backwater valve **may only serve one
  dwelling unit**; because a secondary suite is a separate dwelling unit, one valve cannot
  protect both. Existing shared installations may need to "remove, reconfigure, or install
  backwater protection to meet the minimum requirements." **The advisory itself states it has
  no legal status and cannot serve as official code interpretation — say so on the page.**
  Source: https://www.calgary.ca/content/dam/www/pda/pd/documents/building/advisories/plumbing-advisory-secondary-suites-backwater-valves-and-protection-from-backflow.pdf
- **As of August 2026 there is no City of Calgary rebate, subsidy or grant for residential
  backwater valves or sump pumps.** The Climate Ready page discusses both devices and offers
  no financial incentive. Calgary's only stormwater incentive is a developer program (3+
  primary housing units, up to $50,000) that does not cover backwater valves or sump pumps.
  Source: https://www.calgary.ca/development/home-building/stormwater-incentive-program.html
  For contrast: **EPCOR offers Edmonton homeowners up to $800** for interior or exterior
  backwater valve installation (homes built before 1989 or with prior sanitary backup history,
  first-come first-served).
  Source: https://www.epcor.com/ca/en/ab/edmonton/safety/home/flood-prevention-at-home/backwater-valve-subsidy.html
  Frame this as "as of August 2026" and tell readers to re-check calgary.ca — absence of
  evidence is strong here but not absolute.

**Sump pumps / basement flooding**
- "Basement flooding is the responsibility of the homeowner. The City will only assess the
  flooding situation. The City does not pump water out of basements." "It is the homeowners'
  responsibility to maintain the pump."
- Sump discharge may **not** drain to neighbouring properties, lanes, sidewalks, boulevards,
  streets, or into a foundation drain or weeping tile — per the Community Standards Bylaw.
  Source: https://www.calgary.ca/water/flooding/basement-flooding-and-seepage.html
- City guidance: replace sump pumps "every 10 years, or sooner."
  Source: https://www.calgary.ca/environment/resources/climate-ready-measures-drainage-and-water-management.html

**Water hardness (2025 City data, mg/L CaCO3)**
- Bearspaw plant: Jan–Mar 151–200 · Apr–Jun 141–192 · Jul–Sep 151–177 · Oct–Dec 168–197
- Glenmore plant: Jan–Mar 208–274 · Apr–Jun 181–245 · Jul–Sep 191–216 · Oct–Dec 213–248
- Converted at 17.1 mg/L per grain: Bearspaw ≈ 8.2–11.7 gpg, Glenmore ≈ 10.6–16.0 gpg
  ("hard" to "very hard"). The City page does not publish gpg — if you show gpg, state that
  you converted it and show the divisor.
- The City does **not** recommend softeners; it says consumers should "thoroughly research the
  various water softener systems available before deciding," notes salt-based systems "may not
  be suitable for people on sodium-reduced diets," and states there are "no known health
  effects associated with calcium and magnesium minerals in drinking water."
  Source: https://www.calgary.ca/water/drinking-water/water-quality-water-hardness-water-data.html
- **Unknown**: which neighbourhoods are served by which plant. Do not guess. Tell readers to
  ask 311 if they want to know which plant serves them.

**Water rates and leaks (2026)**
- Water $1.7409/m³ + $13.83 per 30 days; wastewater $1.9050/m³ + $23.45 per 30 days;
  stormwater $17.00 per 30 days; typical metered bill $119.21/month. Flat-rate customers pay
  roughly 68% more than metered.
  Source: https://www.calgary.ca/water/water-utility/residential-water-rates-and-billing.html
- City leak benchmark: "A slow leak that takes a minute to fill a 500ml pop bottle can add over
  twenty cubic metres a month." Meter check: shut everything off and watch the flow register.
  Source: https://www.calgary.ca/water/programs/water-leaks-and-basic-repairs.html
- Derived (show your working): 20 m³ × ($1.7409 + $1.9050) = **$72.92/month ≈ $875/year**.
  Label this clearly as a calculation from the City's own figures, not a City-published number.
- The City page makes **no** mention of bill credits or leak forgiveness. Say so honestly
  rather than implying relief exists.

**Frozen pipes**
- Homeowner owns all repair cost on the private-property portion of the service line,
  **including a frozen or damaged water meter**. City advises a minimum indoor temperature of
  **15 °C**, UL-listed heat tape, and disconnecting garden hoses. Report via **311**. The City
  "may send a crew to confirm if your service is frozen," response "may be delayed due to high
  volumes," and the homeowner must sign a **Work Authorization Form** before the City will thaw
  the private portion. At-risk properties receive letters directing them to the City's Frozen
  Pipes Prevention Program.
  Source: https://www.calgary.ca/water/drinking-water/frozen-water-lines.html

**Insurance (Alberta)**
- An Alberta brokerage states most insurers require a vacant home be checked every **24–72
  hours** for burst-pipe damage to be covered, and that clogs and high water pressure are
  treated as maintenance and likely not covered. A **service line endorsement** is the add-on
  covering tree roots, corrosion and shifting earth. Attribute this to the brokerage, not to
  "insurers" generally, and tell readers to read their own policy.
  Source: https://acera.ca/are-burst-pipes-covered-by-home-insurance-in-alberta/

**Competitor-reported plumber rates (label as self-reported, not authoritative)**
- Independent plumbers $85–$120/hr; plumbing companies $95–$150/hr; emergency/after-hours
  $150–$250/hr. Source: https://mrmikesplumbing.ca/what-do-plumbers-charge-per-hour-in-calgary/
  (updated Dec 2025). State plainly that no authoritative public source for Calgary plumber
  rates exists and every published figure is a company's self-report.

**Google guidance (for the About page)**
- Google's helpful-content documentation (last updated Dec 10, 2025) uses a "Who / How / Why"
  framework and asks for transparency about how content is produced, including any use of
  automation. Source: https://developers.google.com/search/docs/fundamentals/creating-helpful-content

## DO NOT STATE — unverified, do not publish

- Whether the City charges to thaw a frozen service line, or charges when 311 dispatches
  crews and the blockage turns out to be private-side.
- Whether Calgary has a formal damage-claim/compensation process for City-caused backups.
- Whether discharging a sump pump to the **sanitary** sewer is prohibited in Calgary.
- Whether the City bears liability for boulevard/City-owned tree roots in a private line.
- Any published City of Calgary distribution water-pressure standard in psi.
- The re-inspection fee (the published schedule shows arithmetic that doesn't reconcile).
- Typical Calgary costs for frost-free sillcock replacement or BBQ gas line installation.
- Which neighbourhoods are served by Bearspaw vs Glenmore.
- Permit processes for Airdrie, Cochrane, Okotoks or Chestermere — separate authorities.
- Any specific dollar cost as fact. Ranges only, always labelled as planning estimates.

If you need a fact not on the verified list, verify it live with WebSearch/WebFetch and cite
the primary source, or write around it. When in doubt, say "confirm with 311" — that honesty
is a competitive advantage on this site, not a weakness.

## Full site URL list (for internal linking)

```
/                                              Pillar — Calgary plumber
/emergency-plumber-calgary/                    Emergency plumbing
/no-hot-water-calgary/                         No hot water / tank leaking
/hot-water-tank-lifespan-calgary/              How long tanks last here
/water-heater-permit-calgary/                  Water heater permits
/calgary-hard-water/                           Hard water & softeners
/low-water-pressure-calgary/                   Low water pressure
/water-bill-leak-calgary/                      High water bill / finding leaks
/drain-cleaning-calgary/                       Drain cleaning
/sewer-water-line-responsibility-calgary/      Who owns which pipe
/backwater-valve-rebate-calgary/               Backwater valve rebates
/backwater-valve-secondary-suite-calgary/      Backwater valves & suites
/sump-pump-calgary/                            Sump pumps
/sewer-scope-buying-home-calgary/              Sewer scope before buying
/frozen-pipes-calgary/                         Frozen & burst pipes
/frozen-sewer-line-calgary/                    Frozen sewer lines
/winterize-outdoor-tap-calgary/                Winterize outdoor tap
/plumber-cost-calgary/                         What plumbers charge
/homeowner-plumbing-permits-alberta/           DIY plumbing & the law
/gas-line-permit-calgary/                      Gas line permits
/basement-bathroom-plumbing-calgary/           Basement bathroom plumbing
/about/                                        About / trust
/contact/                                      Contact & free quote
```

## Available hero images (reference by filename)

`hero-pillar.jpg` `hero-emergency.jpg` `hero-hotwater.jpg` `hero-tank-age.jpg`
`hero-permit.jpg` `hero-hardwater.jpg` `hero-pressure.jpg` `hero-waterbill.jpg`
`hero-drain.jpg` `hero-sewer-line.jpg` `hero-backwater.jpg` `hero-suite.jpg`
`hero-sump.jpg` `hero-sewerscope.jpg` `hero-frozen.jpg` `hero-frozen-sewer.jpg`
`hero-hosebib.jpg` `hero-cost.jpg` `hero-diy.jpg` `hero-gasline.jpg`
`hero-basement-bath.jpg` `hero-about.jpg` `hero-contact.jpg`

## Finally

After writing your files, run `cd /root/calgaryplumbingquotes && python3 build.py` to confirm
they compile. Fix any JSON syntax errors. Report which files you created and the word count
of each body.
