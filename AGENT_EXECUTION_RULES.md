# Hoax.ai Agent Execution Rules

**Version:** v1.0.0  
**Status:** Active  
**Decision:** DEC-030

## Mission Boundary

The agent may build governance and validation infrastructure, but it may not create public exposure before the approved gates pass.

Hoax.ai is a governed Category Intelligence Factory — not a detector, truth machine, upload tool, or SEO site.

## Required Reading Before Work

Before modifying the repository, read:

- `ROADMAP.md`
- `MASTER_EXECUTION_PLAN.md`
- `DECISION_LOG.md` (recent decisions)
- Relevant sprint audit for the current phase

Confirm Sprint 1C is **BLOCKED** and DEPLOY-G1 through DEPLOY-G3 are **not passed**.

## Absolute Prohibitions

The agent must not:

- configure DNS;
- configure Cloudflare;
- enable GitHub Pages;
- deploy to any external host;
- create a public classifier;
- create a public tool;
- create upload functionality;
- create scoring;
- create forms;
- create analytics;
- create cookies or tracking;
- create APIs;
- add a new public route without registry and gate approval;
- expand sitemap.xml without approval;
- perform SEO expansion;
- introduce external factual claims without source governance.

## Required Validation Before Closure

Before closing any sprint or governance task:

```bash
python validators/validate_all.py
```

Required result: **PASS**.

`validators/validate_all.py` is the canonical local validation command.

## File Update Obligations

When adding governance artifacts:

- update `data/source-registry.json`;
- regenerate `BUILD_MANIFEST.json` through `validate_all.py`;
- add sprint audit file when closing a sprint;
- update `ROADMAP.md` and `MASTER_EXECUTION_PLAN.md` when gates change.

## Decision Log Obligations

New governance decisions require an entry in `DECISION_LOG.md` with decision ID, rationale, and implications.

## Source Registry Obligations

Every new governance file, validator, registry, or workflow policy must be registered in `data/source-registry.json`.

## Evidence Ledger Obligations

Repository-supported governance adoption claims require:

- entry in `data/evidence-ledger.json`;
- mapping in `data/claim-source-map.json`;
- support location pointing to doctrine file and decision log entry.

No external factual claims without registered source support.

## Deployment Block

External deployment remains deferred. Sprint 1C is blocked. DEPLOY gates are not passed. No CI workflow may deploy, publish Pages, or mutate DNS/Cloudflare.

## Public Tool Block

No public classifier, upload workflow, scoring, forms, or analytics may be created unless explicitly approved through future gates.

## Reference Expansion Block

No reference pages, routes, or sitemap entries without:

- reference page blueprint compliance;
- expansion gate approval;
- claim and source traceability;
- technical quality validation.

Candidate registry must be used before page creation.

## Communication Rule

Do not describe future capabilities as existing. Do not imply deployment completion, live tools, or external domain readiness.
