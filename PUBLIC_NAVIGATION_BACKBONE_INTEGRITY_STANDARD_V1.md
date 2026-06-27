# Public Navigation Backbone Integrity Standard v1

Sprint 111 — Public Reference Navigation Backbone Integrity Audit v1  
**Decision:** DEC-129

## Navigation Backbone Integrity Standard Statement

The public navigation backbone must remain a static, citation-safe traversal layer across the 83-route public surface. Integrity audits inspect route counts, files, metadata, internal links, route-group connectivity, page-end navigation, AI retrieval navigation, boundaries, and prohibited drift without creating new routes or operational tools.

## Navigation-backbone route-count requirements

- Sitemap must remain exactly 83 URLs unless an approved route sprint changes count.
- Route registry must remain exactly 83 entries.
- Public-file-registry must stay aligned if used.
- Visible public copy describing current release surface must not use stale 58/63/68/73/78 route counts.

## Navigation-backbone role clarity requirements

The backbone must function as a public route-group navigation layer and structural orientation layer — not a dashboard, graph tool, scorecard, rating system, due-diligence room, pitch deck, sales page, private data room, downloadable report, transaction surface, legal or financial representation, verdict system, or operational review tool.

## Route-group connectivity requirements

Major route groups must remain reachable from homepage, system map, and review layers through grouped navigation — not exhaustive 83-link dumps on every page.

## Page-end navigation requirements

Page-end navigation must remain grouped and concise where present, without stale route-group omissions.

## AI retrieval navigation requirements

Retrieval capsules must preserve coherent upstream/downstream route roles without implying judgments or operational assessments.

## Metadata requirements

Exactly one H1, canonical URL, title, meta description, Open Graph title, and Open Graph description on every public HTML page.

## Link integrity requirements

No broken internal links among public HTML routes.

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

After publisher-status allowlist updates, run `py -3 -m compileall validators` before `validate_all.py`. Prefer precise tuple and constant edits over broad regex replacement.

## Forbidden regression patterns

Do not bulk-edit `policy.get(...)` or `pub.get(...)` calls without manual review. Do not introduce positive forbidden phrases in public HTML without safe negation.

## Future navigation-backbone audit rules

Future integrity audits must preserve homepage Navigation Backbone Integrity Snapshot and `/system-map/` Navigation Backbone Integrity Note unless superseded by an approved sprint with visible production contact.

## Validator protection

`validators/validate_public_reference_navigation_backbone_integrity_audit_v1.py` enforces this standard after visible production changes exist.
