---
title: Locator Strategies
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

# Locator Strategies

## Purpose

Score locator robustness for Lightning and Experience UI.

## Reasoning Model

1. Prefer getByRole / label / test-id.
2. Flag absolute XPath and brittle CSS.
3. Centralize SF-specific locators.
4. Chain MIA when FlexiPage/LWC changes.

## Decision Rules

- XPath soup for Lightning → Fail Locator Review.

## Cross-Links (Canonical Depth)

- [Locators](../../automation-intelligence/playwright/locators.md)
- [Locator Robustness](../../automation-intelligence/review-engine/locator-robustness.md)
- [Metadata Impact Analyzer](../../metadata-impact-analyzer/SKILL.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.21.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
