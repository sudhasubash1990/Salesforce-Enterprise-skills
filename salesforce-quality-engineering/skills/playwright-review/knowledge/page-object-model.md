---
title: Page Object Model
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

# Page Object Model

## Purpose

Evaluate POM/Screenplay abstractions for Salesforce flows.

## Reasoning Model

1. Pages own locators/actions; tests own assertions/flow.
2. Avoid dumping business logic only in tests.
3. Score against Sprint 8 POM lens.
4. Prefer small cohesive pages over god objects.

## Decision Rules

- God page objects → Fail maintainability gate.

## Cross-Links (Canonical Depth)

- [Page Objects](../../automation-intelligence/playwright/page-objects.md)
- [POM / Screenplay Quality](../../automation-intelligence/review-engine/pom-screenplay-quality.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.21.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
