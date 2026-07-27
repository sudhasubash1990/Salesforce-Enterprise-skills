---
title: API Testing
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

# API Testing

## Purpose

Assess Playwright request context for setup and API coverage.

## Reasoning Model

1. Use request fixture for seed/cleanup.
2. Keep API tests independent of UI flakes.
3. Recommend SOVA for post-condition queries.
4. Auth for API must not leak secrets.

## Decision Rules

- UI-only setup for bulk data → recommend TDG/API.

## Cross-Links (Canonical Depth)

- [API Testing](../../automation-intelligence/playwright/api-testing.md)
- [SOQL Validation Assistant](../../soql-validation-assistant/SKILL.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.21.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
