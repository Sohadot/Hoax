# Branch Protection Recommendation

**Status:** Recommendation only — does not change GitHub repository settings  
**Decision:** DEC-030

## Purpose

This document recommends future GitHub branch protection settings for Hoax.ai. It is governance guidance only. Applying these settings requires manual action by the repository owner.

## Recommended Settings for `main`

When collaborators are added or stricter operation is desired:

1. **Require status check:** `Hoax.ai Quality Gate` (`.github/workflows/quality-gate.yml`) must pass before merge.
2. **Protect branch:** disallow direct pushes if team workflow requires PRs.
3. **Disallow force pushes** to `main`.
4. **Require pull request reviews** when collaborators are added.
5. **Do not enable automated deployment workflows.**
6. **Do not enable GitHub Pages** until DEPLOY-G1 passes through explicit governance.
7. **Keep DNS and Cloudflare** as later DEPLOY gates (DEPLOY-G2, DEPLOY-G3).

## What This Does Not Do

- Does not modify GitHub repository settings.
- Does not enable Pages, DNS, or Cloudflare.
- Does not create deployment workflows.
- Does not require secrets or write permissions.

## Current Posture

Direct-to-main work may continue if the repository owner explicitly chooses it. Automation governance validates on push and pull_request regardless.
