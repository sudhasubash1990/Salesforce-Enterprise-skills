---
title: Fixtures
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

# Fixtures

## Purpose

Review fixture design for personas, auth, and isolation.

## Reasoning Model

1. Typed fixtures preferred.
2. Worker isolation; no shared mutable page.
3. Persona fixtures map to PTA themes.
4. Setup via API where possible.

## Decision Rules

- Shared mutable fixture state → Flake risk.

## Cross-Links (Canonical Depth)

- [Fixtures](../../automation-intelligence/playwright/fixtures.md)
- [Test Data Generator](../../test-data-generator/SKILL.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.21.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
