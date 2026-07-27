---
title: CI/CD Integration
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

# CI/CD Integration

## Purpose

Generic CI readiness for Playwright Salesforce suites.

## Reasoning Model

1. Sharding, browsers, artifacts, secrets injection.
2. Smoke vs full suite gates.
3. Fail-fast vs complete report tradeoffs.
4. Cross-link ADO/GH specifics.

## Decision Rules

- Secrets in pipeline logs → Critical.

## Cross-Links (Canonical Depth)

- [CI/CD Integration](../../automation-intelligence/playwright/ci-cd-integration.md)
- [CI/CD Readiness](../../automation-intelligence/review-engine/cicd-readiness-review.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.21.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
