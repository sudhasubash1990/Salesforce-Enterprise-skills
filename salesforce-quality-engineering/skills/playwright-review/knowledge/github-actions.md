---
title: GitHub Actions
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: Knowledge Article
version: 0.21.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [playwright-review, knowledge]
---

# GitHub Actions

## Purpose

Review GH Actions workflows for Playwright.

## Reasoning Model

1. actions/setup-node, cache, matrix browsers.
2. Artifacts upload on failure.
3. OIDC/secrets — never echo.
4. PR vs main branch gates.

## Decision Rules

- Unpinned actions at latest without rationale → Governance note.

## Cross-Links (Canonical Depth)

- [CI/CD Integration](cicd-integration.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.21.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
