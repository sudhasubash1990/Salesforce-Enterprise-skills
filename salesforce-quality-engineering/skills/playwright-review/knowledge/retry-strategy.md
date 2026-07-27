---
title: Retry Strategy
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

# Retry Strategy

## Purpose

Review retries as resilience vs masking defects.

## Reasoning Model

1. Config retries for infra flake only.
2. Investigate root cause before raising retries.
3. Trace on first retry preferred.
4. Do not use retries to hide bad locators.

## Decision Rules

- High retries without flake analysis → Fail Flaky Analysis.

## Cross-Links (Canonical Depth)

- [Retry Strategy](../../automation-intelligence/playwright/retry-strategy.md)
- [Flaky and Stability](../../automation-intelligence/review-engine/flaky-and-stability-review.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.21.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
