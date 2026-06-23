# Public Source Confidence Component Standard v1

## Component Statement

A Hoax.ai public page that participates in the Source Confidence Layer v1 must expose a **source-confidence component**: a paired human-readable block and AI-readable capsule that declare the page’s primary support type, what the page supports, and what it does not support. The component is governed reference infrastructure. It is not a widget, badge score, trust seal, or verification stamp.

This standard applies to Sprint 88 updated pages: homepage, four utility routes, and six Sprint 85 reference routes (including the non-detector boundary page). It does not authorize new routes, JavaScript behavior, forms, upload, scoring, verdicts, or detector claims.

**Decision:** DEC-106  
**Sprint:** Sprint 88  
**Companion policy:** PUBLIC_REFERENCE_SOURCE_CONFIDENCE_LAYER_V1.md

## Required Fields

Every source-confidence component on an updated page must include all required fields below in both human-visible and AI-extractable form.

### Human-visible block

Labeled section (recommended heading: **What this page supports** or equivalent governed title) containing:

| Field | Requirement |
|-------|-------------|
| **Support type** | Exactly one primary label from the five allowed support types |
| **Page support statement** | One to two sentences: what a reader may use this page for in evidence-risk reading |
| **Does not support** | Bullet list or short prose negating verdict, score, verification, detection, upload, and automated report outputs |
| **Non-verdict reminder** | One sentence restating artifact/posture framing — not truth, fraud, or legal adjudication |

### AI-readable capsule

`<dl class="ai-capsule ai-source-confidence-capsule">` (or equivalent governed class) inside a labeled section (`iface-source-confidence`, `aria-labelledby="source-confidence-capsule"`):

| Field | Requirement |
|-------|-------------|
| **Support type:** | Canonical enum string — `Conceptual Definition`, `Manual Utility Guidance`, `Synthetic Example`, `Boundary Statement`, or `Repository-Governed Reference` |
| **Supports:** | One sentence aligned with page support statement |
| **Does not support:** | Comma-separated or listed forbidden outputs; must include score, verdict, and verification negations |
| **Not a score:** | `true` stated explicitly — e.g., “This is not a confidence score.” |
| **Not verification:** | `true` stated explicitly — e.g., “This is not source or claim verification.” |
| **Route:** | Canonical path matching `data/route-registry.json` |

### Structural requirements

- Component appears after page thesis or definition open — before long ancillary sections where possible
- No JavaScript required to read component content
- Component coexists with Sprint 87 link-graph elements without contradicting them
- Homepage may use one governed component per major section if sections differ in support role; each instance still satisfies required fields

## Allowed Support Types

Use exact enum strings in both human and AI fields:

| Support type | Human label usage | Supports field may say |
|--------------|-------------------|------------------------|
| **Conceptual Definition** | “This page defines …” | “Defines [concept] for evidence-risk reading and vocabulary.” |
| **Manual Utility Guidance** | “This page guides manual …” | “Guides manual, human-operated evidence reading steps.” |
| **Synthetic Example** | “This page provides fictional …” | “Provides fictional scenarios for safe posture practice.” |
| **Boundary Statement** | “This page states boundaries …” | “States category boundaries and non-detector limits.” |
| **Repository-Governed Reference** | “This page indexes governed reference …” | “Indexes repository-governed reference material on Hoax.ai.” |

Do not invent sub-types, hybrid labels, or informal synonyms in capsule **Support type** fields.

## Page-Specific Usage Rules

### Homepage (`/`)

- Primary component support type: **Boundary Statement** for category posture
- Repository index blocks linking to `/reference/` may repeat **Repository-Governed Reference** in section-level components if governed by validator
- Must negate detector, upload, score, and verification in **Does not support**
- Must not imply utilities auto-run or return results when clicked

### Sprint 85 reference routes (5 conceptual + 1 boundary)

| Route | Support type | Additional rules |
|-------|--------------|------------------|
| `/evidence-risk/` through `/traceability-gap/` | Conceptual Definition | **Supports** names the concept; **Does not support** negates ruling on reader’s artifact |
| `/why-hoax-ai-is-not-a-detector/` | Boundary Statement | **Supports** emphasizes misreading prevention; must not offer “alternative detection” |

Reference pages retain Sprint 87 AI link capsules; source-confidence capsule is a separate labeled block.

### Sprint 84 utility routes

| Route | Support type | Additional rules |
|-------|--------------|------------------|
| `/manual-evidence-checklist/` | Manual Utility Guidance | State checklist is self-applied; no submission endpoint |
| `/evidence-posture-map/` | Manual Utility Guidance | Map is illustrative posture aid, not computed output |
| `/evidence-risk-questions/` | Manual Utility Guidance | Questions prompt human judgment; no scored result |
| `/synthetic-examples/` | Synthetic Example | Must state fiction explicitly in **Supports** and human block |

Utilities must repeat automation negation even if obvious to human readers — AI agents need explicit **Does not support** text.

## Safe Language Rules

Safe language describes page role and reader action without implying system determination.

**Prefer:**

- “supports,” “defines,” “guides,” “illustrates,” “states boundaries,” “helps you read,” “manual,” “fictional,” “reference vocabulary,” “evidence-risk framing,” “non-verdict,” “posture reading”

**Qualify carefully:**

- “confidence” — only as “source-confidence layer” or “page support clarity,” never as numeric reliability
- “evaluate” — only “evaluate your reading process,” never “evaluate this file/claim”
- “assess” — only “assess evidence posture in manual reading,” never automated assessment

**Align with:**

- Evidence Posture standard non-verdict vocabulary
- Output Boundary limits
- Sprint 87 boundary strips on utility pages

## Forbidden Phrasing

Forbidden in source-confidence components, capsule fields, and immediate surrounding labels:

| Category | Forbidden examples |
|----------|-------------------|
| Scoring | confidence score, confidence rating, trust score, reliability percentage, 0–100, high/medium/low confidence tier as page output |
| Verification | verifies, verified, confirmed true, debunked, fact-checked by Hoax.ai, proven false, authenticated |
| Detection | detects, detector result, manipulated, deepfake detected, AI-generated confirmed |
| Verdict | fake, real, guilty, fraudulent, hoax confirmed, verdict, ruling |
| Automation | automatically analyzes, we analyze your, submit for analysis, upload, scan this |
| Legal/forensic | forensic proof, legal determination, admissible in court (as Hoax.ai output) |
| User evaluation | your evidence, your file, your claim evaluated |

Presence in **Does not support** negation lists is allowed when denying the behavior (“does not verify claims”). Presence in **Supports** or **Support type** fields is not allowed.

## Human Readability Requirements

Human-readable source-confidence blocks must be scannable and early-visible.

1. **Labeled section** — Semantic heading; not only a footer disclaimer
2. **Plain sentences** — No jargon stacks; a competent non-expert should understand page role in one read
3. **Visible support type** — Enum label appears as readable text, not hidden metadata
4. **Short does-not-support list** — Three to six bullets maximum; each negates one capability class
5. **Consistent placement** — Same relative position across pages of the same class (reference vs utility)
6. **Accessibility** — Section has `aria-labelledby`; lists are real `<ul>` elements
7. **No visual trust seals** — No badge graphics implying certification, stars, or shields

Human readability fails when support type is implied only by page template or buried below 1,500 words of body copy.

## AI Readability Requirements

AI-readable capsules make support type extractable from static HTML.

1. **Dedicated capsule** — Separate from link-graph AI capsule; both may appear on reference pages
2. **Stable class names** — `ai-source-confidence-capsule`, `iface-source-confidence` for extractor targeting
3. **Enum fidelity** — **Support type** field matches JSON schema enum exactly
4. **Explicit booleans as text** — **Not a score** and **Not verification** stated as sentences, not HTML attributes alone
5. **Route field** — Full canonical path with trailing slash per registry
6. **No contradiction** — Capsule must not negate link capsule concept names or imply different support type
7. **Homepage crawlability** — Homepage capsule fields present in initial HTML response

AI readability fails when support type appears only in `meta` tags without visible paired human block, or when capsules omit **Not a score** / **Not verification**.

## Boundary Language Standard

Boundary language in every component must satisfy all of:

- Hoax.ai classifies evidence **condition** and **posture**, not moral character or legal guilt
- Weak evidence ≠ false; strong appearance ≠ true
- Source confidence on the page = clarity of **page support**, not certification of external sources
- Manual utilities produce **reader judgment**, not Hoax.ai outputs
- Synthetic content is **fictional**, not case evaluation

**Template (adapt per page):**

> This page supports [role]. It does not score, verify, detect, or verdict real-world claims, artifacts, or people. Hoax.ai describes evidence posture — not truth, fraud, or legal outcomes.

Boundary page may strengthen non-detector thesis but must not introduce a new product category claim.

## Thin-Component Prevention Rules

Thin components copy boilerplate without page-specific support statements. They are forbidden.

| Anti-pattern | Requirement to prevent |
|--------------|------------------------|
| Identical **Supports** text on all pages | Each page names its concept or utility in the support statement |
| Generic “reference page” label only | **Support type** enum must be present and correct per route |
| Empty **Does not support** | Minimum three distinct negations |
| Capsule without human block | Both layers required |
| Human block without capsule | Both layers required |
| One-word support type | Full enum string in human and AI fields |
| Footer-only disclaimer replacing component | Component is a governed section, not a copyright footnote |
| Reusing Output Boundary page text verbatim | May align legally; must still name this page’s role |

Validators treat missing required fields, wrong support type for route, or forbidden phrasing as failures.

## Component Quality Checklist

- [ ] Support type matches route assignment table in layer policy  
- [ ] Page support statement is unique to this page’s concept or utility  
- [ ] Does-not-support negates score, verdict, verification, upload, automation  
- [ ] Non-verdict reminder present in human block  
- [ ] AI capsule includes all six required fields  
- [ ] Not a score and Not verification explicit in capsule  
- [ ] No forbidden phrasing in Supports or Support type  
- [ ] Section labeled for humans and machines  
- [ ] Coexists with Sprint 87 link components without contradiction  

## Future Component Rules

New pages receive source-confidence components only after route registry entry, sitemap entry, sprint authorization, validator update, and decision log entry. Candidate routes remain component-free until governed.
