# Hoax.ai Evidence Posture Taxonomy

**Version:** 1.0  
**Status:** Active — internal/governed  
**Decision:** DEC-017

## A. Purpose

This taxonomy defines bounded states and dimensions for describing **evidence posture**: the condition of an evidence artifact or evidence chain.

Evidence posture describes how reliably an artifact or chain can be examined, supported, contextualized, and bounded — not whether it is ultimately correct, deceptive, or attributable to a subject.

The taxonomy provides controlled vocabulary for future standards, protocols, tools, and reference pages. It does not activate any classifier, score, or public route.

## B. Non-Purpose

This taxonomy does **not**:

- determine truth or falsity;
- detect all synthetic media;
- certify authenticity;
- accuse people or institutions;
- establish guilt, fraud, intent, deception, or involvement;
- create an active tool or classifier.

Evidence posture describes the condition of evidence. It does not perform the verdict.

## C. Scope

### Applies To

- evidence artifacts;
- evidence chains;
- source records;
- claim records;
- provenance signals;
- contextual signals;
- coherence signals.

### Does Not Apply To

- people;
- institutions;
- brands;
- organizations;
- events as subjects of judgment.

Artifact–Subject Separation applies: classification remains on artifacts and evidence chains only.

## D. Evidence Posture Dimensions

### 1. Artifact Identification

Whether the item being examined is clearly defined as an artifact.

### 2. Provenance Visibility

Whether origin, custody, creation context, or publication path is visible.

### 3. Source Confidence

Whether the source record is known, bounded, and appropriate to the claim.

### 4. Contextual Stability

Whether surrounding context is stable, missing, disputed, or unclear.

### 5. Forensic Coherence

Whether internal signals appear coherent or contain unresolved inconsistencies.

### 6. Evidence Chain Continuity

Whether the artifact can be connected to a stable chain of supporting records.

### 7. Corroboration Posture

Whether supporting evidence exists, is absent, partial, or conflicting.

### 8. Subject Boundary Clarity

Whether the output avoids transferring artifact risk to connected people or institutions.

### 9. Output Boundary

Whether the resulting statement remains within evidence posture and avoids verdict language.

## E. Evidence Posture States

### 1. documented_posture

**Definition:**  
The artifact or evidence chain has visible support, bounded source context, and no major unresolved posture gaps within the available scope.

**Boundary:**  
Does not mean verified as fact, authentic, complete, or legally verified.

### 2. partially_supported_posture

**Definition:**  
The artifact has some supporting signals, but one or more posture dimensions remain incomplete, weak, or unresolved.

**Boundary:**  
Does not imply falsity or deception.

### 3. provenance_limited_posture

**Definition:**  
The artifact lacks sufficient origin, custody, publication path, or source-chain visibility.

**Boundary:**  
Does not establish manipulation or bad faith.

### 4. contextually_unstable_posture

**Definition:**  
The artifact may be difficult to interpret because surrounding context is missing, ambiguous, disputed, or unstable.

**Boundary:**  
Does not determine whether the depicted or referenced event occurred.

### 5. coherence_questioned_posture

**Definition:**  
The artifact contains internal or relational signals that require further examination before stronger posture language is used.

**Boundary:**  
Does not imply synthetic generation, falsity, or fraud.

### 6. high_risk_evidence_posture

**Definition:**  
Multiple posture dimensions contain unresolved risk signals, making the artifact unsuitable for strong reliance without further review.

**Boundary:**  
Does not accuse any connected subject and does not prove deception, guilt, fraud, or subject involvement.

### 7. not_assessable_posture

**Definition:**  
Available information is insufficient to classify the evidence posture responsibly.

**Boundary:**  
Not assessable is not suspicious by itself.

### 8. planned_not_claimed_posture

**Definition:**  
A capability, output, route, protocol, or tool layer is described as planned but not currently active.

**Boundary:**  
Must never be presented as an existing capability.

## F. Prohibited State Names

The following must never appear as taxonomy state labels or canonical output names:

- fake
- real
- true
- false
- hoax confirmed
- deepfake detected
- authentic certified
- verified truth
- fraud signal
- guilty subject
- deceptive person
- lie score
- truth score

## G. Output Language Rules

### Allowed Examples

- "The artifact has a provenance-limited posture."
- "The evidence chain is partially supported within the available context."
- "This record is not assessable from the available information."
- "The posture applies to the artifact, not the connected subject."

### Prohibited Examples

- "The person is lying."
- "This proves fraud."
- "This is fake."
- "This confirms the event did not happen."
- "The institution is deceptive."
- "The subject is involved."

## Governing Principle

**Evidence posture describes the condition of an evidence artifact or evidence chain. It does not determine truth, falsity, guilt, deception, or subject status.**

## Machine-Readable Source

Canonical machine-readable taxonomy: `data/evidence-posture-taxonomy.json`

## Related Governance

- DEC-001 — Evidence Posture, Not Truth Verdict
- DEC-012 — Classify the Artifact, Not the Subject
- DEC-016 — Category Factory Enforcement Layer
- DEC-017 — Evidence Posture Taxonomy v1
