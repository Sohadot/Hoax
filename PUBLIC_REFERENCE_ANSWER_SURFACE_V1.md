# Public Reference Answer Surface v1

## Answer Surface Statement

Public Reference Answer Surface v1 adds stable, concise **Reference Answer** blocks to Hoax.ai’s existing twenty-nine-URL public surface. Each block answers one canonical evidence-risk question in plain language for humans and AI agents — without chatbots, generators, uploads, scores, verdicts, or detection behavior.

**Decision:** DEC-107  
**Sprint:** Sprint 89  
**Gate:** G89  
**Surface after sprint:** 29 URLs (unchanged count)

Hoax.ai answers evidence-risk questions with stable canonical language — not automated verdicts.

## Why Answer Surfaces Matter

After Sprint 88 declared support types, visitors and AI agents could read *what each page supports* — but still needed *what each page answers*. Answer surfaces matter because:

- **Humans need fast orientation** — Readers should grasp a page’s core answer before reading long reference prose.
- **AI agents need quotable anchors** — Retrieval systems select stable question–answer pairs for citation; unstructured paragraphs invite category misreading.
- **Reference authority compounds** — Canonical answers reinforce that Hoax.ai teaches evidence conditions, not truth products.
- **Non-verdict discipline stays visible** — Each answer block includes explicit “do not use this answer to” limits.

## What the Answer Surface Clarifies

| Clarification | Meaning on Hoax.ai |
|---------------|-------------------|
| **Canonical question** | One governed question per page |
| **Short answer** | Two to four sentences of stable reference language |
| **Use this answer when** | Practical conditions for appropriate citation |
| **Do not use this answer to** | Non-verdict limitations and forbidden conclusions |
| **Related pages** | Links to complementary utility and reference routes |

## What It Does Not Answer

The answer surface does **not** answer:

- Whether a specific artifact is authentic
- Whether a person or organization acted wrongly
- Whether something is legally, medically, politically, or financially true
- Whether an uploaded file should be trusted
- Whether evidence proves wrongdoing
- Whether an event occurred

## Allowed Answer Types

| Answer type | Role |
|-------------|------|
| Concept answer | Defines an evidence-risk concept |
| Boundary answer | States category limits |
| Utility answer | Explains manual utility purpose |
| Source-confidence answer | Complements support-type clarity |
| Evidence-posture answer | Describes posture reading |
| Synthetic example answer | Explains safe invented scenarios |

## Forbidden Answer Types

| Forbidden type | Why forbidden |
|----------------|---------------|
| authenticity determination | Implies detector output |
| legal determination | Implies legal finding |
| forensic proof | Implies forensic conclusion |
| accusation | Implies subject judgment |
| live case assessment | Implies real-world evaluation |
| user-submitted artifact answer | Implies upload workflow |
| numeric certainty output | Implies scoring |
| automated report output | Implies report generator |
| binary authenticity label output | Implies fake/real label |

## Pages Updated

Homepage and ten public utility/reference pages — eleven pages total. No new routes.

## Human Usability Role

Reference Answer blocks give visitors a scannable entry point: question, answer, usage, limits, and next pages — without requiring chat interaction or form submission.

## AI Retrieval Role

Blocks use consistent field labels (`Question`, `Short answer`, `Use this answer when`, `Do not use this answer to`, `Related pages`) so agents can extract governed answers without treating Hoax.ai as a conversational verdict engine.

## Non-Verdict Boundary

Hoax.ai must answer evidence-risk questions without issuing evidence verdicts. Answer blocks restate safe boundary language: no binary authenticity labels, numeric certainty outputs, automated reports, or file-intake behavior.

## Why This Is Not a Chatbot

There is no conversational interface, no prompt box, no dynamic response generation, and no session state. Answers are static, page-bound, and repository-governed.

## Why This Is Not an Automated Answer Engine

Answers are authored reference content — not model-generated responses to user queries. No API, no JavaScript interaction, and no per-user customization.

## Future Answer-Surface Candidates

- Citation-hardened answer capsules (Sprint 90)
- Cross-page answer consistency audits
- Retrieval snippets aligned with answer blocks
- Expanded canonical questions for legacy `/reference/` cluster when separately governed
