# Hoax.ai Evidence Posture Standard

**Version:** v1.0.0  
**Status:** governed_internal_standard  
**Decision:** DEC-018

## A. Purpose

This standard defines the minimum conditions for using evidence posture language responsibly.

It specifies what counts as sufficient, limited, unstable, high-risk, or not assessable evidence posture on an evidence artifact or evidence chain — so that future protocols, tools, and reference outputs do not assign posture states arbitrarily.

The standard defines sufficiency, not truth.

## B. Non-Purpose

This standard does **not**:

- determine truth or falsity;
- detect all synthetic media;
- certify authenticity;
- prove fraud;
- establish guilt;
- accuse people or institutions;
- determine whether an event occurred;
- create an active classifier or tool;
- replace human, legal, forensic, journalistic, or institutional review.

## C. Governing Principle

**The standard defines sufficiency, not truth.**

**A sufficient evidence posture is not a truth verdict. An insufficient evidence posture is not an accusation.**

## D. Scope

### Applies To

- evidence artifacts;
- evidence chains;
- claim records;
- source records;
- provenance signals;
- context signals;
- coherence signals;
- evidence posture outputs later governed by protocol.

### Does Not Apply To

- people;
- institutions;
- brands;
- organizations;
- events as subjects of judgment.

## E. Relationship to Taxonomy

- **The taxonomy** names the states and dimensions (`EVIDENCE_POSTURE_TAXONOMY.md`, `data/evidence-posture-taxonomy.json`).
- **The standard** defines the minimum sufficiency rules for using those states.
- **The protocol** will later define the step-by-step classification process.
- **The engine/tool** will later operationalize the protocol only after output boundaries exist.

No protocol, classifier, or tool is created by this standard.

## F. Standard Dimensions

Each dimension maps to a taxonomy dimension (DIM-0001 through DIM-0009).

### 1. Artifact Identification

| Condition | Criterion |
|-----------|-----------|
| Sufficient | The artifact is clearly identified with bounded scope and examinable boundaries. |
| Limited | The artifact is identifiable but scope, format, or boundaries remain partially unclear. |
| Weak | Identification depends on inference or incomplete metadata. |
| Not assessable | Available information does not permit responsible artifact identification. |
| Prohibited interpretation | Identifying an artifact does not identify, accuse, or judge any connected subject. |

### 2. Provenance Visibility

| Condition | Criterion |
|-----------|-----------|
| Sufficient | Origin, custody, creation context, or publication path is visible within available scope. |
| Limited | Some provenance signals exist but custody, path, or origin remains incomplete. |
| Weak | Provenance signals are sparse, indirect, or heavily dependent on secondary reporting. |
| Not assessable | Provenance cannot be examined from available information. |
| Prohibited interpretation | Limited provenance does not establish manipulation, bad faith, or subject deception. |

### 3. Source Confidence

| Condition | Criterion |
|-----------|-----------|
| Sufficient | Source record is known, bounded, and appropriate to the artifact or claim. |
| Limited | Source is partially known or weakly bounded relative to the artifact. |
| Weak | Source attribution is uncertain, indirect, or inconsistently documented. |
| Not assessable | Source confidence cannot be responsibly assessed from available information. |
| Prohibited interpretation | Low source confidence does not accuse a person or institution of dishonesty or fraud. |

### 4. Contextual Stability

| Condition | Criterion |
|-----------|-----------|
| Sufficient | Surrounding context is stable and sufficiently bounded for examination. |
| Limited | Context is present but incomplete or only partially stable. |
| Weak | Context is disputed, thin, or dependent on missing situational information. |
| Not assessable | Context cannot be responsibly mapped from available information. |
| Prohibited interpretation | Unstable context does not determine whether a depicted or referenced event occurred. |

### 5. Forensic Coherence

| Condition | Criterion |
|-----------|-----------|
| Sufficient | Internal signals appear coherent with no major unresolved inconsistencies. |
| Limited | Minor inconsistencies exist but do not prevent bounded posture language. |
| Weak | Coherence signals are mixed or require further examination. |
| Not assessable | Coherence cannot be responsibly examined from available information. |
| Prohibited interpretation | Questioned coherence does not imply synthetic generation, falsity, or fraud. |

### 6. Evidence Chain Continuity

| Condition | Criterion |
|-----------|-----------|
| Sufficient | Artifact connects to a stable chain of supporting records with examinable linkage. |
| Limited | Chain exists but has gaps, weak custody, or partial linkage. |
| Weak | Chain continuity depends on inference or incomplete records. |
| Not assessable | Chain continuity cannot be responsibly assessed. |
| Prohibited interpretation | Broken continuity does not prove subject involvement or institutional misconduct. |

### 7. Corroboration Posture

| Condition | Criterion |
|-----------|-----------|
| Sufficient | Supporting evidence exists and is consistent within available scope. |
| Limited | Partial corroboration exists with unresolved gaps or mild conflict. |
| Weak | Corroboration is absent, thin, or conflicting. |
| Not assessable | Corroboration posture cannot be responsibly assessed. |
| Prohibited interpretation | Absent corroboration does not issue a verdict on the underlying claim or subject. |

### 8. Subject Boundary Clarity

| Condition | Criterion |
|-----------|-----------|
| Sufficient | Output confines posture to artifact or evidence chain without subject transfer. |
| Limited | Output mostly artifact-focused but requires careful subject-boundary review. |
| Weak | Language risks implying subject judgment without explicit boundary correction. |
| Not assessable | Subject boundary cannot be evaluated because output scope is undefined. |
| Prohibited interpretation | Artifact risk must not be read as subject accusation, guilt, or involvement. |

### 9. Output Boundary

| Condition | Criterion |
|-----------|-----------|
| Sufficient | Statement remains within evidence posture framing with explicit limitations. |
| Limited | Output is mostly bounded but lacks full limitation clarity. |
| Weak | Output risks verdict, score, or accusation language without correction. |
| Not assessable | Output boundary cannot be evaluated from available draft or scope. |
| Prohibited interpretation | Output boundary violation converts posture into verdict or subject judgment. |

## G. Posture Sufficiency Rules

### 1. documented_posture

**Required conditions:**

- artifact is clearly identified;
- source context is visible or bounded;
- provenance is sufficiently visible within the available scope;
- context is stable enough for bounded reliance;
- no major unresolved coherence issue is present;
- output remains within evidence posture.

**Boundary:** Does not mean verified as fact, authentic, complete, legally verified, or final.

### 2. partially_supported_posture

**Required conditions:**

- at least one supporting signal exists;
- at least one major posture dimension remains incomplete, limited, or unresolved;
- output clearly identifies the limitation.

**Boundary:** Does not imply falsity, deception, or unreliability as a whole.

### 3. provenance_limited_posture

**Required conditions:**

- origin, custody, publication path, or source-chain visibility is insufficient;
- the limitation affects reliance on the artifact;
- output names the provenance limitation without inferring manipulation.

**Boundary:** Does not establish manipulation, bad faith, fraud, or deception.

### 4. contextually_unstable_posture

**Required conditions:**

- surrounding context is missing, ambiguous, disputed, unstable, or not sufficiently bounded;
- interpretation would be risky without further context;
- output avoids determining whether the depicted or referenced event occurred.

**Boundary:** Does not determine the occurrence verdict of the event.

### 5. coherence_questioned_posture

**Required conditions:**

- one or more coherence signals require further examination;
- the issue is described as a coherence question, not as proof of synthetic origin;
- output avoids verdict language.

**Boundary:** Does not imply synthetic generation, falsity, or fraud.

### 6. high_risk_evidence_posture

**Required conditions:**

- multiple posture dimensions contain unresolved risk signals;
- reliance on the artifact would be inappropriate without further review;
- output states the risk applies to the artifact or evidence chain only.

**Boundary:** Does not accuse any person, institution, brand, organization, or event. Does not prove deception, guilt, fraud, misconduct, or involvement.

### 7. not_assessable_posture

**Required conditions:**

- available information is insufficient for responsible posture classification;
- missing data prevents a bounded statement;
- output clearly states that no responsible classification can be made.

**Boundary:** Not assessable is not suspicious by itself.

### 8. planned_not_claimed_posture

**Required conditions:**

- a capability, route, protocol, tool, output, report, or system layer is discussed as planned;
- it is not described as currently active;
- public language avoids implying operational availability.

**Boundary:** Planned is not live. Mention is not capability.

## H. Minimum Output Boundary

Every future output using this standard must include:

- artifact focus;
- posture state;
- limitation statement;
- subject-separation boundary;
- no truth verdict;
- no fake/real binary;
- no accusation.

## I. Prohibited Standard Uses

- scoring people;
- scoring institutions;
- declaring truth;
- declaring falsity;
- declaring fake/real;
- certifying authenticity;
- proving fraud;
- implying legal findings;
- using high-risk posture as accusation;
- using not-assessable as suspicion;
- using planned capabilities as existing services.

## J. Standard Maturity

| Field | Value |
|-------|-------|
| Version | v1.0.0 |
| Status | governed_internal_standard |

This standard is not yet a public product, classifier, or service output.

## Machine-Readable Source

Canonical machine-readable standard: `data/evidence-posture-standard.json`

## Related Governance

- DEC-017 — Evidence Posture Taxonomy v1
- DEC-018 — Evidence Posture Standard v1
- DEC-012 — Classify the Artifact, Not the Subject
