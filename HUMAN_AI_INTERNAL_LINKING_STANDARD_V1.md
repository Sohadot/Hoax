# Human and AI Internal Linking Standard v1

## Internal Linking Standard Statement

A Hoax.ai public page that participates in the authority link graph must expose internal links that work for both human readers and AI retrieval systems. Links are governed reference infrastructure: they name relationships, enable traversal, and preserve non-verdict category boundaries. They are not navigation decoration, SEO filler, or implied product capability.

This standard applies to Sprint 87 updated pages: homepage, four utility routes, and six Sprint 85 reference routes. It does not authorize new routes, JavaScript behavior, forms, upload, scoring, verdicts, or detector claims.

**Decision:** DEC-105  
**Sprint:** Sprint 87  
**Companion policy:** PUBLIC_REFERENCE_AUTHORITY_INTERNAL_LINKING_V1.md

## Human-Readable Linking Requirements

Human-readable links must be scannable, purposeful, and concept-named.

**Required on every updated reference and utility page:**

1. **Reference path** — Breadcrumb navigation (`Home / Concept Name`) at page open
2. **Contextual body links** — At least one in-prose link to a sibling concept or legacy reference page where analytically appropriate
3. **Use next** — A labeled section recommending the single best following read with one sentence of rationale
4. **Related concepts** — A visible list or prose block naming governed sibling or parent concepts with links
5. **Page-end reference navigation** — Labeled cluster listing all six Sprint 85 reference routes
6. **Page-end utility navigation** — Labeled cluster listing all four Sprint 84 utility routes
7. **Homepage return** — Footer or boundary area link back to `/`

**Human readability quality bar:**

- Anchor text must read as a concept title or governed phrase, not as a call-to-action slogan
- Link clusters use semantic headings or `aria-labelledby` labels so screen-reader users hear purpose, not undifferentiated lists
- Link order follows evidence-risk logic (umbrella → sibling → utility), not alphabetical convenience
- No more than two consecutive link-only paragraphs without explanatory prose

## AI-Readable Linking Requirements

AI-readable linking makes relationships extractable from static HTML without JavaScript execution.

**Required on every Sprint 85 reference page:**

1. **AI-readable reference capsule** — `<dl class="ai-capsule">` with labeled fields:
   - Concept
   - Definition
   - Use
   - Not
   - Related concepts (comma-separated canonical names; link where repeated in field)
   - Public utility routes (linked list of four utilities)
2. **Stable route strings** — Identical path spelling across capsule, navigation clusters, and homepage graph
3. **Labeled navigation regions** — `iface-reference-nav` and `iface-utility-nav` with explicit label elements
4. **Canonical terminology** — Repeat governed terms (Evidence Risk, Provenance Risk, Context Collapse, Claim Drift, Traceability Gap, Evidence Posture, non-verdict) consistently in anchors and capsule text
5. **Homepage graph exposure** — Homepage sections must contain plain `<a href>` links to all ten child routes so crawlers and agents discover the full cluster from `/`

**Required on every Sprint 84 utility page:**

1. Page-end reference navigation listing all six reference routes
2. Page-end utility navigation listing all four utilities
3. At least one contextual link in body prose to the most relevant reference unit
4. Boundary strip restating non-verdict posture (no verdict, score, upload, or binary authenticity label)

AI readability fails when capsules omit utility routes, when related concepts use informal synonyms, or when navigation clusters differ between pages.

## Link Capsule Standard

The link capsule is the machine-retrievable summary of a reference unit’s graph position.

**Structure:**

```html
<section class="reference-section reference-capsule-section" aria-labelledby="ai-capsule">
  <h2 id="ai-capsule">AI-Readable Reference Capsule</h2>
  <dl class="ai-capsule">
    <dt>Concept:</dt><dd>…</dd>
    <dt>Definition:</dt><dd>…</dd>
    <dt>Use:</dt><dd>…</dd>
    <dt>Not:</dt><dd>…</dd>
    <dt>Related concepts:</dt><dd>…</dd>
    <dt>Public utility routes:</dt><dd>…linked utilities…</dd>
  </dl>
</section>
```

**Capsule rules:**

- **Concept** — Matches H1 and canonical concept name exactly
- **Definition** — One sentence; no verdict or detector language
- **Use** — Describes evidence-reading purpose
- **Not** — Explicit negation of fake/real verdict, score, or detection output
- **Related concepts** — Minimum three sibling or parent concepts by canonical name
- **Public utility routes** — All four utilities linked; order: Checklist, Posture Map, Synthetic Examples, Evidence-Risk Questions

Utilities do not require full capsules but must not contradict capsule terminology on linked reference pages.

## Related Concepts Standard

The **Related concepts** block names analytical neighbors — not every page on the site.

**Reference page requirements:**

- Minimum three related concepts named
- At least two must link to other Sprint 85 reference routes
- At least one may link to a legacy `/reference/` page or Evidence Posture where posture relationship is discussed
- Names use title case governed vocabulary
- Order reflects dependency (umbrella concepts before specialized siblings where applicable)

**Presentation options (one or more per page):**

- Bulleted list with descriptive anchors in a `related-concepts` section
- Prose paragraph with inline links
- Capsule `Related concepts` field mirroring the same set

**Prohibited:**

- Listing unrelated legacy pages for graph density
- Naming concepts without registered routes
- Using related-concept blocks as sitemap dumps

## Use-Next Standard

**Use next** answers: “After reading this page, what is the disciplined following read?”

**Structure:**

```html
<section class="use-next-section" aria-labelledby="use-next">
  <h2 id="use-next">Use Next</h2>
  <p>…one sentence rationale…</p>
  <p><a href="…">…concept-named anchor…</a></p>
</section>
```

**Rules:**

- Exactly one primary **Use next** target per page (one anchor)
- Rationale must state analytical reason, not marketing encouragement
- Target must be a registered route within the twenty-nine-URL surface
- Reference pages should prefer sibling or utility targets that deepen the same evidence layer
- Utility pages should prefer the reference unit that best grounds the workflow just described
- **Why Hoax.ai Is Not a Detector** may recommend a utility as the “what to do instead” read

**Examples of valid rationale:**

- “Read provenance risk next when origin weakness is the primary structural concern.”
- “Use the Manual Evidence Checklist next to apply these questions in order.”

**Invalid rationale:**

- “Learn more about our tools.”
- “See why we’re the best resource.”

## Footer/Reference Navigation Standard

Page-end navigation uses two labeled clusters plus footer return.

**Reference navigation cluster (`iface-reference-nav`):**

- Label: “Evidence-risk reference layer”
- Links: all six Sprint 85 routes in evidence-risk logical order:
  1. Evidence Risk
  2. Provenance Risk
  3. Context Collapse
  4. Claim Drift
  5. Traceability Gap
  6. Why Hoax.ai Is Not a Detector

**Utility navigation cluster (`iface-utility-nav`):**

- Label: “Public utilities”
- Links: all four Sprint 84 utilities in workflow order:
  1. Manual Evidence Checklist
  2. Evidence Posture Map
  3. Synthetic Examples
  4. Evidence-Risk Questions

**Footer:**

- Restate non-verdict boundary in one line
- Link to homepage

Clusters appear after boundary strip and before `</article>`. Homepage uses section cards instead of iface clusters but must expose the same route set.

## Anchor Text Rules

| Rule | Requirement |
|------|-------------|
| Concept naming | Use canonical concept title as anchor text |
| Utility naming | Use official utility page title |
| Path stability | `href` must match registry path including trailing slash policy |
| No truncation | Do not abbreviate governed terms (“Prov. Risk”) |
| No keyword stuffing | One concept per anchor; no “evidence risk provenance fake detector” chains |
| Sentence integration | Body links sit inside grammatical sentences |
| Self-link clarity | Current page may appear in reference nav list but contextual links should prefer other targets |
| Case consistency | Title case for concept names in anchors |

## Non-Verdict Linking Language

Links must preserve artifact-first, non-accusatory posture.

**Allowed framing:**

- “Read evidence condition before conclusions”
- “Connect to Evidence Posture language”
- “Classify structural risk without performing the verdict”
- “Manual reference utility — no upload, no score”

**Link context must not imply:**

- Truth or falsity outcomes from following the link
- Detection, scanning, or authenticity certification
- User file submission or automated analysis
- Confidence percentages or numeric certainty
- Subject accusation or deception proof

When linking to **Why Hoax.ai Is Not a Detector**, anchor text must name the boundary concept, not “why we’re not fake news” or similar colloquial frames.

## Forbidden Anchor Text

Do not use these as anchor text on public pages:

- click here
- read more
- learn more
- here
- this page
- our tool
- detect fake / detect deepfake / AI detector
- verify truth / prove real / prove fake
- submit / upload / analyze your file
- confidence score / authenticity score / % likely fake
- real or fake
- scam / fraud / guilty / deceptive (as link labels)
- free scan / check now

Forbidden anchors fail both human trust and AI misread prevention.

## Thin-Link Prevention Rules

Thin linking is high link count with low analytical value.

**Prevention rules:**

1. **No link-only sections** — Every navigation cluster must have a visible label; contextual sections need prose
2. **Cap redundant anchors** — The same target may appear in capsule, related concepts, and page-end nav, but body prose must not repeat identical anchor text more than twice outside navigation clusters
3. **No alphabetical sitemap blocks** — Navigation order follows evidence-risk model, not A–Z
4. **Minimum contextual depth** — At least one in-argument link per updated page beyond page-end clusters
5. **Sibling discipline** — Reference pages link to ≥2 siblings in body or related-concepts areas, not only in footer
6. **Utility grounding** — Each utility links contextually to ≥1 reference unit in prose
7. **Homepage proportionality** — Homepage links utilities and reference layer in dedicated sections, not repeated ad hoc through body copy
8. **Validator enforcement** — `validators/validate_public_reference_authority_internal_linking_v1.py` fails thin or missing graph obligations

Thin links inflate HTML without strengthening category authority. Prefer fewer, truer relationships.

## Compliance Checklist

- [ ] Reference path present on reference and utility pages
- [ ] AI capsule present on all six reference routes
- [ ] Related concepts ≥3 with valid targets
- [ ] Use next present with one primary target and rationale
- [ ] Page-end reference nav — all six routes
- [ ] Page-end utility nav — all four utilities
- [ ] Homepage graph — all ten child routes
- [ ] No forbidden anchor text
- [ ] No links to unregistered routes
- [ ] Non-verdict language in boundary strip and link context
