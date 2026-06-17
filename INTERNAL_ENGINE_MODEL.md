# Hoax.ai Internal Engine Model

**Version:** v0.1.0  
**Status:** governed_internal_model  
**Maturity:** not_public_tool  
**Decision:** DEC-021

## A. Purpose

This internal engine model defines the permitted logic architecture for a future Hoax.ai evidence-posture engine.

It specifies how a future engine may move from an artifact description through protocol stages into a bounded output shape — without creating an active engine, public classifier, upload workflow, or scoring system.

The engine model defines permitted internal logic; it does not create a public classifier.

## B. Non-Purpose

This model does **not**:

- create a public classifier;
- create a public tool;
- create upload functionality;
- create scoring;
- create automated truth detection;
- determine truth or falsity;
- certify authenticity;
- detect all synthetic media;
- prove fraud;
- establish guilt;
- accuse people or institutions;
- determine whether an event occurred;
- replace human, legal, forensic, journalistic, or institutional review.

## C. Governing Principle

**The engine model defines permitted internal logic; it does not create a public classifier.**

**The model may route evidence posture logic only through adopted taxonomy, standard, protocol, and output boundary schema.**

A future engine may only route through taxonomy, standard, protocol, and output schema. It may not invent outputs.

## D. Dependencies

This model depends on:

- `EVIDENCE_POSTURE_TAXONOMY.md`
- `data/evidence-posture-taxonomy.json`
- `EVIDENCE_POSTURE_STANDARD.md`
- `data/evidence-posture-standard.json`
- `EVIDENCE_POSTURE_CLASSIFICATION_PROTOCOL.md`
- `data/evidence-posture-protocol.json`
- `OUTPUT_BOUNDARY_SCHEMA.md`
- `data/output-boundary-schema.json`
- `GOVERNANCE_BOUNDARY.md`
- `CLAIM_POLICY.md`
- `data/category-language.json`
- `data/ontology-foundation.json`

## E. Engine Input Boundary

### Allowed Internal Input Types

| Input | Purpose |
|-------|---------|
| artifact_description | Bounded description of artifact or evidence chain |
| artifact_type | Type of artifact under review |
| source_record_refs | Optional source record references |
| claim_record_refs | Optional claim record references |
| provenance_notes | Notes on origin, custody, publication path |
| context_notes | Notes on surrounding context |
| coherence_notes | Notes on internal coherence signals |
| corroboration_notes | Notes on supporting or conflicting signals |
| known_limitations | Known gaps or constraints in available information |

### Input Rules

- Inputs must not include personal accusation fields.
- Inputs must not ask whether a person is lying.
- Inputs must not ask whether an institution is guilty.
- Inputs must not request fake/real determination.
- Inputs must not request truth scoring.
- Inputs must not contain upload-handling logic.

## F. Engine Processing Layers

### 1. Input Boundary Check

Checks whether the input is about an artifact or evidence chain, not a subject.

### 2. Artifact Scope Normalization

Bounds the artifact scope and separates it from connected subjects.

### 3. Protocol Stage Mapping

Maps input data to the twelve protocol stages.

### 4. Dimension Finding Assembly

Maps observations to the nine taxonomy/standard dimensions.

### 5. Standard Sufficiency Mapping

Maps dimension findings to standard sufficiency rules.

### 6. Posture State Candidate Selection

Identifies possible posture states using taxonomy and protocol rules.

### 7. Conservative State Resolution

If multiple states are possible, choose the most bounded responsible state. If insufficient data exists, prefer `not_assessable_posture` over speculation.

### 8. Output Boundary Composition

Composes only fields allowed by Output Boundary Schema v1.

### 9. Governance Safety Check

Rejects any output containing verdict, fake/real, accusation, scoring, or subject judgment.

### 10. Internal Output Status Assignment

Marks output as `draft_internal` or `governed_internal` only. No `public_allowed_after_gate` status in this model version.

## G. Internal Engine Non-Scoring Rule

The internal engine model does not use numeric scoring, percentages, grades, risk meters, probability claims, or authenticity scores.

**Allowed:** bounded qualitative posture states, dimension findings, limiting factors, recommended next checks, confidence boundary as qualitative text.

**Prohibited:** truth_score, lie_score, guilt_score, fraud_score, authenticity_score, deception_score, subject_risk_score, probability of fake, risk meter, traffic-light verdict, pass/fail truth result.

## H. Conservative Resolution Rule

**When the available information is incomplete, the engine model must prefer bounded uncertainty over speculative classification.**

## I. Required Internal Output Shape

Any future internal output must conform to `OUTPUT_BOUNDARY_SCHEMA.md` and `data/output-boundary-schema.json`.

Minimum internal output fields: output_id, schema_version, protocol_version, taxonomy_version, standard_version, artifact_scope, artifact_type, posture_state, posture_reason_summary, dimension_findings, limiting_factors, subject_boundary_statement, prohibited_interpretations, confidence_boundary, recommended_next_checks, output_status, generated_by, last_reviewed.

## J. Fixtures Policy

Internal fixtures must use fictional, neutral, non-identifiable examples. Fixtures must not involve real people, real institutions, real brands, real political events, real conflicts, or real accusations. Fixtures exist only to test schema alignment and boundary language.

## K. Engine Maturity

| Field | Value |
|-------|-------|
| Version | v0.1.0 |
| Status | governed_internal_model |
| Maturity | not_public_tool |

## Machine-Readable Sources

- Model: `data/internal-engine-model.json`
- Fixtures: `data/internal-engine-fixtures.json`

## Related Governance

- DEC-017 through DEC-021
- Output Boundary Schema v1 governs all future engine outputs
