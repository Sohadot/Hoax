# Hoax.ai Automation Governance

**Version:** v1.0.0  
**Status:** governed_internal_automation_quality_gate  
**Maturity:** validation_only_no_deployment  
**Decision:** DEC-030

## A. Purpose

This document governs automated validation, CI behavior, agent execution, and repository workflow boundaries for Hoax.ai.

## B. Non-Purpose

Automation governance does **not**:

- create public pages;
- create routes;
- create sitemap expansion;
- create SEO expansion;
- create public deployment readiness;
- enable GitHub Pages;
- create DNS or Cloudflare work;
- create public classifier functionality;
- create a public tool;
- create upload functionality;
- create forms;
- create analytics;
- create APIs;
- create monetization;
- collect data;
- use secrets.

## C. Governing Principle

**Rules that are not automated become optional under pressure.**

**Automation may validate governance; it must not deploy, publish, collect data, or mutate external infrastructure.**

## D. Approved Automation

Approved current automation:

- run Python validators;
- run `validators/validate_all.py`;
- validate registry integrity;
- validate public file integrity;
- validate route/link integrity;
- validate claim/source traceability;
- validate technical quality;
- validate reference blueprint gates;
- validate automation governance;
- generate `BUILD_MANIFEST.json` locally or inside CI for validation context;
- report PASS/FAIL.

## E. Prohibited Automation

- deployment jobs;
- GitHub Pages deployment;
- Cloudflare API calls;
- DNS updates;
- external publishing;
- artifact upload to external services;
- secrets usage;
- write permissions;
- workflow token write scope;
- `pull_request_target` workflows;
- curl/wget external calls unless explicitly approved later;
- npm/pip package installation unless explicitly approved later;
- third-party deployment actions;
- analytics insertion;
- form/upload generation;
- route generation without registry approval;
- sitemap expansion.

## F. CI Permission Rule

Require:

- `permissions: contents: read`
- no write permissions;
- no `id-token` permission;
- no `pages` permission;
- no `deployments` permission;
- no secrets.

## G. Workflow Trigger Rule

**Allowed:**

- push to `main`
- pull_request to `main`
- `workflow_dispatch` for validation only

**Prohibited:**

- `pull_request_target`
- schedule unless explicitly approved later
- deployment-triggering workflows

## H. Agent Rule

Any AI or human agent must:

- read `ROADMAP.md`;
- read `MASTER_EXECUTION_PLAN.md`;
- respect Sprint 1C blocked status;
- respect DEPLOY gates not passed;
- run `validators/validate_all.py` before closure;
- not introduce public routes without gate approval;
- not introduce deployment/DNS/Cloudflare work;
- not create public classifier/tool/upload/scoring/forms/analytics;
- document any new governance decision in `DECISION_LOG.md`;
- update source registry when adding governance files;
- update evidence ledger and claim-source map when adding governance claims.

## I. Branch/PR Rule

Direct-to-main work may continue only if the user explicitly chooses it.

For future stricter operation, recommend branch protection:

- require quality-gate workflow pass;
- require linear history if desired;
- disallow force pushes;
- require PR review if collaborators are added;
- do not enable automated deployment.

## J. Maturity

| Field | Value |
|-------|-------|
| Version | v1.0.0 |
| Status | governed_internal_automation_quality_gate |
| Maturity | validation_only_no_deployment |

## Machine-Readable Sources

- Policy: `data/automation-governance-policy.json`
- CI policy: `data/ci-quality-gate-policy.json`
- Agent rules: `AGENT_EXECUTION_RULES.md`
- Workflow: `.github/workflows/quality-gate.yml`
- Validator: `validators/validate_automation_governance.py`
