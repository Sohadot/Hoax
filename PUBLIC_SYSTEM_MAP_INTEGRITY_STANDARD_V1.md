# Public System Map Integrity Standard v1

Sprint 109 — Public Reference System Map Integrity Audit v1  
**Decision:** DEC-127

## System Map Integrity Standard Statement

The public system map must remain a static, citation-safe route-structure organizer across the 83-route public surface. Integrity audits inspect route counts, metadata, links, components, boundaries, and prohibited drift without creating new routes or operational tools.

## System-map route-count requirements

- Sitemap must remain exactly 83 URLs unless an approved route sprint changes count.
- Route registry must remain exactly 83 entries.
- Public-file-registry must stay aligned if used.
- Visible public copy describing current release surface must not use stale 58/63/68/73/78 route counts.

## System-map component preservation requirements

Every system-map page must preserve Reference summary, Map purpose, System map path, What this map supports, What this map does not claim, Reference Answer, Source Confidence, Cite This Reference, Retrieval Capsule, Boundary reminder, Non-transactional review boundary, and page-end reference navigation.

## System-map metadata requirements

Exactly one H1, canonical URL, title, meta description, Open Graph title, and Open Graph description on every public HTML page.

## System-map link requirements

Each system-map page links to `/system-map/`, at least three strategic review layer routes, at least five reference/utility/pathway routes, and at least two sibling system-map routes. No broken internal links.

## System-map role clarity requirements

Maps must state they organize public route structure — not dashboards, graph tools, scorecards, rating systems, due-diligence rooms, pitch decks, sales pages, private data rooms, downloadable reports, or transaction surfaces.

## Non-verdict requirements

No verdict, detector, upload, or automated report capability claims.

## Non-transactional requirements

No pricing, transaction, acquisition term, representative mandate, legal, or financial representation claims.

## Dashboard prohibition

No dashboard behavior or dashboard framing as capability.

## Graph-tool prohibition

No graph-tool behavior or interactive graph framing as capability.

## Scorecard prohibition

No scorecard behavior.

## Rating-system prohibition

No rating-system behavior.

## Due-diligence-room prohibition

No due-diligence-room or private diligence-room access claims.

## Pitch-deck prohibition

No pitch-deck behavior.

## Sales-page prohibition

No sales-page behavior.

## Private data-room prohibition

No private data-room access claims.

## Downloadable report prohibition

No downloadable report behavior.

## Publisher-status syntax safety rule

When adding publisher-status constants to validator allowlists, use precise tuple edits. Run `py -3 -m compileall validators` before `validate_all.py`. Do not bulk-insert status constants inside `policy.get(...)` call arguments.

## Forbidden regression patterns

- Bulk regex replacement across validators damaging Python syntax.
- Inserting status constants inside `policy.get("current_publisher_status"` argument lists.
- Rewriting historical governance docs to satisfy current public copy rules.
- Adding new public routes during integrity audit sprints without expansion gate approval.

## Future system-map audit rules

Each system-map integrity audit must add or refresh a visible integrity snapshot on `/system-map/`, inspect all five system-map routes, verify 83-route counts unless changed by approved sprint, and document repairs in a repair log with `total_repairs_made >= 1`.
