# Public Answer Surface Component Standard v1

## Component Statement

The **Reference Answer** component is a static HTML block on each governed public page. It provides one canonical question, a short answer, usage guidance, non-verdict limits, and related page links.

## Required Fields

| Field | Requirement |
|-------|-------------|
| Question | One canonical evidence-risk question |
| Short answer | Two to four sentences; page-specific governed text |
| Use this answer when | Practical usage condition |
| Do not use this answer to | Clear non-verdict limitation |
| Related pages | At least two internal links to utility/reference routes |

## Page-Specific Answer Rules

Each page uses governed question and short-answer text defined in Sprint 89. Utility pages emphasize manual workflow answers. Reference pages emphasize concept answers. `/why-hoax-ai-is-not-a-detector/` uses a boundary answer. Homepage aggregates category posture.

## Safe Answer Language

- Prefer evidence-condition vocabulary: support, limits, boundaries, posture, drift, traceability
- Use negation for forbidden behavior: does not produce, does not issue, does not establish
- Prefer Sprint 86 safe phrasing: binary authenticity label, numeric certainty output, automated report

## Forbidden Answer Types

No answer block may imply authenticity determination, legal determination, forensic proof, accusation, live case assessment, user-submitted artifact answers, numeric certainty outputs, automated report outputs, or binary authenticity label outputs.

## Human Readability Requirements

- Visible `h2` heading: Reference Answer
- Definition list (`dl`) with labeled fields
- Short answer readable in under thirty seconds
- Related pages use descriptive link text

## AI Readability Requirements

- Stable field labels across all eleven pages
- Question text matches canonical governed strings for key reference routes
- No JSON-LD FAQ schema unless separately governed
- Answer block appears in static HTML without JavaScript rendering

## Boundary Language Standard

Each block’s “Do not use this answer to” field must negate verdict, score, detection, upload, and automated report behavior using safe boundary phrasing.

## Thin-Answer Prevention Rules

- Short answer must be at least two sentences
- Must include page-specific governed concepts (not generic filler)
- “Use this answer when” and “Do not use this answer to” must be distinct
- Related pages must link to routes that exist in the twenty-nine-URL sitemap

## Answer Extraction Quality Checklist

- [ ] Reference Answer heading present
- [ ] All five fields present
- [ ] Canonical question matches sprint specification
- [ ] Short answer matches governed content intent
- [ ] No forbidden exact n-grams
- [ ] No chatbot or generator markers
- [ ] Related pages include valid internal links
- [ ] Validator passes for the page
