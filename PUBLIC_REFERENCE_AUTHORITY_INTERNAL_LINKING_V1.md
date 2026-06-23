# Public Reference Authority Internal Linking v1

## Internal Linking Statement

Public Reference Authority Internal Linking v1 strengthens Hoax.ai’s existing twenty-nine-URL public surface by connecting utilities, reference units, and boundary pages into a coherent human-readable and AI-readable evidence-risk concept graph. This sprint adds no new routes, no sitemap entries, no registry expansion, and no tool behavior. It governs how already-live pages link to one another so the category reads as integrated reference infrastructure — not as isolated pages or SEO filler.

**Decision:** DEC-105  
**Sprint:** Sprint 87  
**Gate:** G87  
**Surface after sprint:** 29 URLs (unchanged count)

## Why Internal Links Create Authority

Reference authority on Hoax.ai is produced by governed substance, conceptual coherence, and retrievable structure — not by page volume alone. After Sprint 84 created four public utilities and Sprint 85 added six public reference routes, the surface had depth but uneven traversal. Visitors and AI agents could land on a single strong page without discovering the utility layer, sibling concepts, or category boundary.

Internal links create authority by:

- **Making concepts discoverable** — Each reference unit becomes a node in a graph, not a dead end.
- **Encoding relationships** — Provenance risk, context collapse, claim drift, and traceability gap are linked as sibling evidence-risk concepts, not as keyword-adjacent pages.
- **Binding utilities to definitions** — Manual checklist, posture map, synthetic examples, and guided questions connect to the reference layer they operationalize.
- **Preserving boundary language** — Links route readers toward non-verdict posture reading, not toward detector, scoring, or verdict behavior.
- **Supporting AI retrieval** — Stable labeled link capsules and predictable navigation clusters help agents traverse Hoax.ai without misreading it as a classifier.

Authority linking is category infrastructure. It makes Hoax.ai harder to imitate because the graph embodies the thesis, not merely the sitemap count.

## Human Navigation Role

Humans use internal links to move from definition to practice and from practice to boundary.

- **Homepage** — The **Explore the Evidence-Risk Reference Layer** section and utility cards provide the primary human entry graph.
- **Reference units** — Breadcrumb reference paths, in-body related-concept links, **Use next** guidance, and page-end reference navigation help readers continue reading without hunting the sitemap.
- **Utilities** — Page-end navigation links utilities back to the six Sprint 85 reference routes so manual workflows stay conceptually grounded.
- **Boundary pages** — Links to **Why Hoax.ai Is Not a Detector** and legacy reference pages prevent misreading utilities as product outputs.

Human navigation must feel intentional: short paths, descriptive anchors, and no link farms at page footers.

## AI Retrieval Role

AI systems retrieve Hoax.ai pages as reference units, not as transactional tools. Internal linking supports retrieval by:

- Repeating canonical concept names in anchor text and capsule fields
- Exposing **Related concepts** and **Public utility routes** inside AI-readable reference capsules
- Maintaining consistent route paths across all ten updated production pages
- Providing labeled navigation clusters (`iface-reference-nav`, `iface-utility-nav`) that survive HTML-to-text extraction
- Keeping homepage reference graph links stable for crawl and citation selection

AI retrieval benefits when every Sprint 85 reference page and every Sprint 84 utility page exposes the same graph endpoints. Inconsistency causes agents to treat pages as unrelated assets.

## Utility Layer

The utility layer contains four manual, non-operational public routes introduced in Sprint 84:

| Route | Role in link graph |
|-------|-------------------|
| `/manual-evidence-checklist/` | Stepwise manual reading workflow |
| `/evidence-posture-map/` | Visual layer map for posture thinking |
| `/synthetic-examples/` | Safe fictional scenarios for evidence-risk reading |
| `/evidence-risk-questions/` | Guided question flow before action |

**Link graph obligations for utilities:**

- Each utility links to all six Sprint 85 reference routes in page-end reference navigation
- Each utility links to sibling utilities in page-end utility navigation
- Each utility links contextually to the most relevant reference unit in body prose where natural
- No utility links to upload, scoring, API, or automated-report behavior (none exists)

Utilities are the practice layer. Reference units are the definition layer. Authority linking connects them bidirectionally.

## Concept Reference Layer

The concept reference layer contains six Sprint 85 top-level reference routes:

| Route | Concept contribution |
|-------|---------------------|
| `/evidence-risk/` | Umbrella evidence-risk frame |
| `/provenance-risk/` | Origin and custody continuity risk |
| `/context-collapse/` | Loss of situational framing |
| `/claim-drift/` | Distance between artifact and circulating claim |
| `/traceability-gap/` | Broken chain from artifact to public claim |
| `/why-hoax-ai-is-not-a-detector/` | Category boundary and non-detector thesis |

**Link graph obligations for reference units:**

- Breadcrumb **reference path** (Home → concept)
- In-body links to at least two sibling reference routes
- Links to all four utility routes in AI capsule and page-end utility navigation
- Full six-route listing in page-end reference navigation
- **Use next** block recommending the most logical following read
- **Related concepts** expressed in prose, lists, and capsule fields

The six routes form a closed sibling cluster. They do not replace the twelve legacy `/reference/` pages or the language layer; they deepen the public evidence-risk category at the utility boundary.

## Boundary/Thesis Layer

The boundary/thesis layer prevents category collapse into detector, scanner, or verdict products.

Anchor nodes:

- **Homepage** — States governed evidence-risk reference system posture; links utilities and reference layer
- **`/why-hoax-ai-is-not-a-detector/`** — Explicit non-detector boundary reference unit
- **Legacy reference pages** — Evidence Posture, Artifact-Subject Separation, Output Boundary, and related `/reference/` routes remain link targets where conceptually appropriate
- **Standard, protocol, interface surfaces** — Link when posture, protocol, or interface embodiment context is required

Boundary links must use non-accusatory, non-verdict language. They classify evidence condition; they do not perform the verdict.

## Link Graph Rules

1. **Registry alignment** — Every `href` on the updated public pages must resolve to a route in `data/route-registry.json`.
2. **Sitemap alignment** — No link target may point outside the twenty-nine-URL sitemap set.
3. **No new routes** — Sprint 87 does not authorize route inflation, candidate paths, or placeholder URLs.
4. **No orphan utilities** — All four utilities must link into the six-route reference cluster.
5. **No orphan reference units** — All six reference routes must link to utilities and siblings.
6. **Homepage graph completeness** — Homepage must link to all four utilities and all six reference routes in governed sections.
7. **Bidirectional discoverability** — Reference ↔ utility links must work in both directions via page-end navigation.
8. **Single canonical path** — Use registered paths only; no duplicate slug variants or unregistered aliases.
9. **Fragment integrity** — In-page anchors must target existing element IDs.
10. **No external dependency links** — Authority linking stays on-domain within the governed public surface.

## Contextual Link Requirements

Contextual links appear inside reference-grade prose where the relationship is analytically true — not only in footer navigation.

**Required contextual patterns:**

- Reference units link to **Evidence Posture** (`/reference/evidence-posture/`) when discussing posture relationship
- Reference units link to siblings when defining overlapping or dependent concepts (e.g., evidence risk → provenance risk, traceability gap)
- Utilities link to the reference unit that best matches the workflow step being described
- Boundary page links outward to utilities and siblings to show what Hoax.ai offers instead of detection

**Contextual link quality rules:**

- Anchor text must name the governed concept, not generic “click here” or “learn more”
- Links must appear in sentences that explain why the target matters
- At least one contextual sibling link per Sprint 85 reference page
- No contextual link may imply unsupported capability

## Forbidden Link Patterns

| Pattern | Why forbidden |
|---------|---------------|
| Links to unregistered or planned routes | Violates link-route integrity |
| Links to candidate paths from SEO authority map | Candidate-only until governed |
| Links to upload, score, API, or report endpoints | Capability not authorized |
| Footer link stuffing (> governed clusters) | Thin-link and SEO-spam pattern |
| Generic anchor text (“here”, “more”, “read this”) | Fails human and AI readability |
| Cross-linking every page to every page | Decoration, not concept graph |
| Links that imply fake/real verdict outputs | Violates non-verdict boundary |
| JavaScript-dependent navigation | Not authorized on public surface |
| External monetization or analytics destinations | Not authorized |
| Broken, empty, or placeholder `href` values | Integrity failure |

## Why This Is Not SEO-Only Linking

SEO-only linking optimizes for crawl funnels and keyword adjacency without improving comprehension. Hoax.ai authority linking optimizes for **category coherence**:

- Links express real conceptual dependencies (risk → posture, utility → definition)
- Anchor text uses governed terminology, not keyword variants
- Graph density is bounded by the evidence-risk model, not by arbitrary PageRank tactics
- No sitemap expansion accompanies this sprint — proof that linking serves structure, not index inflation
- Validators check graph obligations and forbidden behavior, not keyword placement

If a link does not help a human or agent understand evidence-risk reading better, it does not belong in this graph.

## Why This Is Not Decoration

Decorative links repeat navigation without analytical purpose — sibling lists copied verbatim with no prose relationship, “related” blocks that name random pages, or footer walls of blue text.

Hoax.ai authority linking is functional:

- **Use next** recommends the disciplined following read
- **Related concepts** name actual conceptual neighbors
- **AI-readable capsules** encode machine-retrievable relationships
- **Page-end navigation** mirrors the same graph on every updated page for predictable traversal
- Body links appear where the argument requires them

Decoration adds HTML noise. Authority linking adds traversable meaning.

## Future Link Authority Candidates

Candidate-only until separate registration, production, and gate approval:

- **Interpretation risk bridge** — Stronger cross-links between `/reference/interpretation-risk/` and Sprint 85 top-level reference cluster
- **Evidence sufficiency reference unit** — Candidate path from SEO authority map; no link until registered
- **Source corroboration reference unit** — Candidate-only
- **Posture state cluster wiring** — Deeper links between `/reference/not-assessable/`, posture standard, and utility layer
- **Language layer traversal** — Governed bidirectional links between `/language/` terms and Sprint 85 reference routes
- **Standard/protocol/interface embodiment chain** — Sequential “read next” path across authority-layer surfaces

None of these candidates are authorized by Sprint 87. No new `href` targets may be added for them until a future sprint passes route registry, sitemap, and expansion gate requirements.

## Governance Note

Production first. Governance second. DEC-105 exists because ten public pages and the homepage were updated with a coherent authority link graph across the unchanged twenty-nine-URL surface. Validators protect graph integrity without replacing user-facing reference value.
