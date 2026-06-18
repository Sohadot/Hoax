# Hoax.ai Claim and Source Traceability Policy

**Version:** v1.0.0  
**Status:** governed_internal_claim_source_traceability_policy  
**Maturity:** pre_reference_expansion_hardening  
**Decision:** DEC-026

## A. Purpose

This policy governs the relationship between claims, source records, support locations, and public-facing statements.

## B. Non-Purpose

This policy does **not**:

- create new public routes;
- create public reference pages;
- create SEO expansion;
- create external factual claims;
- create a classifier;
- create a public tool;
- create upload functionality;
- create monetization;
- create deployment readiness;
- certify truth;
- certify external factual accuracy.

## C. Governing Principle

**No claim without traceability. No source without support scope.**

**A reference asset must make its claims inspectable before it asks to be trusted.**

## D. Claim Categories

### conceptual_thesis

May be supported by thesis/governance documents. Must not pretend to be external fact. Must be clearly framed as conceptual language.

### operational_claim

Must point to repository evidence showing the operation exists (validator, registry, policy, audit).

### governance_claim

Must point to decision log, governance file, policy, standard, audit, or registry.

### repository_supported_claim

Must point to an existing repository file or data record. Must not claim external-world facts.

### external_factual_claim

Must point to registered external source records. Must not be introduced without source support.

### future_capability_claim

Must be marked `planned_not_claimed`. Must not imply existing public service or active tool.

## E. Source Support Scope

- Each source must declare what it supports.
- Internal governance sources may support governance and operational claims only.
- Internal registry sources must not support broad external factual claims.
- External sources must be registered before supporting external factual claims.
- Source scope must be narrow enough to avoid overclaiming.

## F. Public Claim Mapping

- Public-facing claim-bearing statements should be mapped to evidence ledger IDs.
- The current homepage has a small controlled public claim map.
- Future public pages must not launch without public claim mapping.
- Public mapped claims must not imply active tool availability, external deployment completion, public classifier, upload, scoring, or unsupported superiority.

## G. Support Location Rules

- `support_location` must exist.
- May be a repository file path, data file path, or registered source ID.
- Repository file paths must resolve.
- Source IDs must exist in `data/source-registry.json`.
- Claims with multiple supports must list all relevant supports.
- Missing support must fail validation.

## H. Prohibited Claim Patterns

- unsupported "first in the world" claims;
- "impossible to copy" as factual claim;
- "guaranteed authority";
- "detects all synthetic media";
- "certifies truth";
- "proves fraud";
- "public classifier is live" unless future deployment permits it;
- future capability described as active;
- artifact risk converted into subject accusation.

## I. Traceability Maturity

| Field | Value |
|-------|-------|
| Version | v1.0.0 |
| Status | governed_internal_claim_source_traceability_policy |
| Maturity | pre_reference_expansion_hardening |

## Machine-Readable Sources

- Policy: `data/claim-source-traceability-policy.json`
- Claim-source map: `data/claim-source-map.json`
- Public claim map: `data/public-claim-map.json`
- Validator: `validators/validate_claim_source_traceability.py`

## Related Governance

- DEC-026
- `data/evidence-ledger.json`
- `data/source-registry.json`
