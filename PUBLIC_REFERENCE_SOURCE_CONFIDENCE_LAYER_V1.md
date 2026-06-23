# Public Reference Source Confidence Layer v1

## Source Confidence Layer Statement

Public Reference Source Confidence Layer v1 strengthens Hoax.ai’s existing twenty-nine-URL public surface by declaring, on each updated page, what kind of support that page can provide — and what it explicitly cannot provide. This sprint adds no new routes, no sitemap entries, no registry expansion, and no tool behavior. It governs how homepage, utility, and Sprint 85 reference pages communicate support type so humans and AI agents can read Hoax.ai as governed reference infrastructure — not as a detector, scorer, verifier, or truth engine.

**Decision:** DEC-106  
**Sprint:** Sprint 88  
**Gate:** G88  
**Surface after sprint:** 29 URLs (unchanged count)

Hoax.ai clarifies what each public page can support — definitions, manual utilities, synthetic examples, boundary statements, and repository-governed reference material — without turning source confidence into a score, verdict, or detection result.

## Why Source Confidence Matters

After Sprint 87 connected utilities and reference units into a coherent link graph, the surface could be traversed — but traversal alone does not prevent category misreading. Visitors and AI agents can still treat a strong definition page as if it certified a claim, treat a manual checklist as if it produced an analysis result, or treat synthetic examples as if they evaluated real-world evidence.

Source confidence matters because Hoax.ai’s category thesis depends on **bounded support**, not on implied capability:

- **Humans need posture before action** — Readers must know whether a page offers vocabulary, a manual workflow, a fictional scenario, or a hard boundary — before they treat its language as evidentiary output.
- **AI agents need support-type signals** — Retrieval systems select pages for citation. Without explicit support-type labeling, agents may quote definitional prose as if it were verification, or utility steps as if they were automated findings.
- **Category integrity resists collapse** — Detector, scanner, and truth-product categories win when reference sites blur definition with determination. Source confidence is the anti-collapse layer that keeps definitions definitional and boundaries explicit.
- **Repository governance stays legible** — Hoax.ai pages are governed artifacts. Support-type declaration makes the governance model visible on the page, not only in validators and decision logs.

Source confidence is not a new product feature. It is reference infrastructure that makes the existing surface harder to misread.

## What the Layer Clarifies

The source confidence layer answers one question per updated page: **What kind of support does this page provide?**

It clarifies:

| Clarification | Meaning on Hoax.ai |
|---------------|-------------------|
| **Support type** — One of five allowed types | Whether the page is primarily definitional, utility guidance, synthetic illustration, boundary language, or repository-governed reference |
| **Page support statement** | A plain-language sentence describing what the reader may use the page for in evidence-risk reading |
| **Does-not-claim block** | Explicit negation of verdict, score, verification, detection, and user-submitted evaluation behavior |
| **Non-verdict boundary** | Restatement that Hoax.ai classifies evidence condition and posture — not truth, fraud, guilt, or legal outcomes |
| **AI-readable support capsule** | Machine-extractable fields repeating support type, supports, does-not-support, and boundary negations |
| **Homepage aggregate posture** | Homepage declares the category as a governed reference system whose pages vary by support type but share non-verdict limits |

The layer makes **support type** a first-class public signal alongside concept definitions and internal links. A page can be authoritative without being determinative.

## What It Does Not Claim

The source confidence layer does not introduce operational capability. It does not change what Hoax.ai can do — only how each page declares what it is for.

The layer does **not** claim:

- That any page verifies, confirms, or debunks a real-world claim
- That Hoax.ai assigns numeric or ordinal confidence to sources, artifacts, or people
- That manual utilities produce automated outputs when followed
- That synthetic examples describe or evaluate identifiable real cases
- That boundary pages are legal, forensic, or journalistic findings
- That repository-governed reference pages certify external facts cited in prose
- That support-type labeling replaces Evidence Posture, Output Boundary, or Not Assessable concepts — it complements them
- That Sprint 88 expands the public route surface or authorizes upload, API, scoring, or detection

Source confidence is declarative metadata about page role. It is not a new evidence dimension scored by the site.

## Allowed Support Types

Each updated page declares exactly one primary support type from the governed set:

| Support type | Page role | Typical routes |
|--------------|-----------|----------------|
| **Conceptual Definition** | Defines an evidence-risk concept for reading and vocabulary | Six Sprint 85 reference routes |
| **Manual Utility Guidance** | Offers stepwise, human-operated reading workflows without automation | Four Sprint 84 utility routes |
| **Synthetic Example** | Presents fictional, safe scenarios for posture practice | `/synthetic-examples/` |
| **Boundary Statement** | States category limits and non-detector thesis | `/why-hoax-ai-is-not-a-detector/`, homepage boundary sections |
| **Repository-Governed Reference** | Points to or summarizes governed legacy reference material linked from the surface | Homepage reference index sections linking to `/reference/` cluster |

**Assignment rules:**

- Sprint 85 reference routes use **Conceptual Definition** unless a page’s primary purpose is explicitly boundary-only (`/why-hoax-ai-is-not-a-detector/` uses **Boundary Statement**).
- Three utilities use **Manual Utility Guidance**; `/synthetic-examples/` uses **Synthetic Example**.
- Homepage uses **Boundary Statement** for category posture blocks and **Repository-Governed Reference** where it indexes legacy reference routes — with a single primary type declared in the homepage source-confidence component per governed section pattern.

Support types are mutually exclusive labels per component instance, not stacked scores.

## Forbidden Support Types

No updated page may imply or label support using forbidden types. These are category-collapse phrases — not alternate taxonomy entries.

| Forbidden support type | Why forbidden |
|------------------------|---------------|
| verified truth | Implies truth certification |
| detected authenticity | Implies detector output |
| factual determination | Implies adjudication of real claims |
| legal determination | Implies legal finding |
| forensic proof | Implies forensic conclusion |
| manipulation finding | Implies manipulation verdict |
| user-submitted evidence | Implies upload/evaluation workflow |
| live detection result | Implies real-time classifier |
| automated confidence score | Implies numeric scoring product |

Validators and the component standard treat appearance of these phrases in support-type fields, capsules, or equivalent labeled regions as integrity failures.

## Pages Updated

Sprint 88 updates eleven production surfaces: homepage plus ten Sprint 84/85 pages from the authority link graph. No other public HTML routes receive source-confidence components in this sprint.

| Route | Primary support type |
|-------|---------------------|
| `/` | Boundary Statement (with repository-governed index sections) |
| `/manual-evidence-checklist/` | Manual Utility Guidance |
| `/evidence-posture-map/` | Manual Utility Guidance |
| `/synthetic-examples/` | Synthetic Example |
| `/evidence-risk-questions/` | Manual Utility Guidance |
| `/evidence-risk/` | Conceptual Definition |
| `/provenance-risk/` | Conceptual Definition |
| `/context-collapse/` | Conceptual Definition |
| `/claim-drift/` | Conceptual Definition |
| `/traceability-gap/` | Conceptual Definition |
| `/why-hoax-ai-is-not-a-detector/` | Boundary Statement |

Legacy `/reference/` pages, language layer, standard, protocol, and interface routes are not modified in Sprint 88. They remain governed by prior production batches and may receive source-confidence components only in a future authorized sprint.

## Human Trust Role

Humans use source-confidence components to calibrate how much weight to place on a page before acting on its language.

- **Homepage** — Readers see that Hoax.ai is a reference system with varied page roles, all bounded by non-verdict posture. They should not infer a hidden analyzer behind utility cards or reference links.
- **Reference units** — Readers learn the page offers definitional vocabulary for evidence-risk reading, not a ruling on any artifact they are currently reviewing.
- **Utilities** — Readers learn the page offers manual steps they perform themselves; completing a checklist or question flow does not generate a Hoax.ai report or score.
- **Synthetic examples** — Readers learn scenarios are fictional teaching devices, not case files or evaluated incidents.
- **Boundary page** — Readers learn the page exists to prevent detector misreading, not to deliver a alternative verdict product.

Human trust increases when support type is visible early — near page thesis or in a labeled section — not buried after long prose or implied only by tone.

## AI Retrieval Role

AI systems retrieve Hoax.ai pages as reference units with bounded support claims. Source-confidence labeling supports retrieval by:

- Exposing **Support type**, **Supports**, **Does not support**, **Not a score**, and **Not verification** in AI-readable capsules on updated pages
- Repeating canonical support-type strings identical to `data/public-reference-source-confidence-layer-v1.json` enum values
- Maintaining stable `iface-source-confidence` or equivalent labeled regions that survive HTML-to-text extraction
- Keeping homepage support posture visible in crawlable static HTML without JavaScript execution
- Aligning capsule negations with Output Boundary and non-detector thesis language so agents do not merge definitional pages into verification tools

AI retrieval fails when support type is absent, when capsules use informal synonyms (“helps verify”), or when utility pages omit automation negations.

## Non-Verdict Boundary

Every source-confidence component on an updated page must preserve the Hoax.ai non-verdict boundary:

- Hoax.ai describes evidence condition, posture, and category limits
- Hoax.ai does not output fake/real labels, guilt assignments, fraud determinations, or legal conclusions
- Source confidence on Hoax.ai is **page-role confidence** — clarity about what the page supports — not confidence that a source or claim is true

The non-verdict boundary is stated in human-readable prose and repeated in capsule **Does not support** fields. It must remain consistent with DEC-001 category thesis, Evidence Posture standard language, and Sprint 87 link-graph boundary strips.

## Why This Is Not a Score

A score compresses evidence into a number or tier that implies comparability and ranking. Hoax.ai explicitly does not offer automated confidence scores on the public surface.

Source confidence in Sprint 88 is **not a score** because:

- It labels page support type, not source or artifact quality
- It uses categorical enums (five allowed types), not percentages, points, or star ratings
- It does not rank pages, sources, or claims against one another
- It does not change when a reader “uses” a page — there is no computation step
- Validators require `source_confidence_is_not_score: true` in the layer JSON record
- Component standard forbids “confidence level,” “confidence rating,” and “score” in support fields

If language sounds like “this page is 80% trustworthy,” it violates the layer regardless of intent.

## Why This Is Not Verification

Verification determines whether a claim matches reality to a stated standard. Hoax.ai public pages do not perform that operation.

Source confidence is **not verification** because:

- Definition pages explain concepts; they do not check whether a user’s artifact satisfies those concepts
- Utilities guide manual human reading; they do not return pass/fail outcomes
- Synthetic examples are explicitly fictional; they do not validate real evidence
- Boundary pages negate detector behavior; they do not substitute a new verification pipeline
- No page accepts user submissions for evaluation
- Validators require `source_confidence_is_not_verification: true` in the layer JSON record
- Forbidden support types include verified truth, factual determination, and forensic proof

Hoax.ai may discuss source confidence as an evidence dimension in reference prose (per `/reference/source-confidence/`) without turning the Sprint 88 layer into a verification product.

## Future Source-Confidence Candidates

Candidate-only until separate registration, production, and gate approval:

- **Legacy reference cluster labeling** — Source-confidence components on twelve `/reference/` pages and language layer routes
- **Standard/protocol/interface embodiment** — Support-type declarations on `/standard/`, `/protocol/`, and `/interface/` surfaces
- **Cross-page support-type graph** — Machine-readable index of all twenty-nine routes by support type (without new routes)
- **Source corroboration reference unit** — Candidate path from SEO authority map; no component until registered
- **Evidence sufficiency reference unit** — Candidate-only; support type undefined until production
- **Interpretation-risk bridge labeling** — Stronger support-type ties between `/reference/interpretation-risk/` and Sprint 85 cluster
- **Localized support-type strings** — Future locale layers must preserve enum semantics, not translate into verdict language

None of these candidates are authorized by Sprint 88. No new public routes, components on unlisted pages, or forbidden support language may be added for them until a future sprint passes route registry, sitemap, and expansion gate requirements.

## Governance Note

Production first. Governance second. DEC-106 exists because homepage and ten public utility/reference pages were updated with governed source-confidence components across the unchanged twenty-nine-URL surface. Validators protect support-type integrity and forbidden-behavior boundaries without replacing user-facing reference value.
