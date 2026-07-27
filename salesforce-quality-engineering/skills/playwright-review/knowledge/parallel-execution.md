---
title: Parallel Execution
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

# Parallel Execution

## Purpose

Evaluate fullyParallel, workers, and data isolation.

## Reasoning Model

1. Confirm isolated test data per worker.
2. Flag shared Pricebook/Account collisions.
3. Recommend External ID prefixes (TDG).
4. Measure only with evidence — no invented speedups.

## Decision Rules

- Parallel without data isolation → Flake Critical.

## Cross-Links (Canonical Depth)

- [Parallel Execution](../../automation-intelligence/playwright/parallel-execution.md)
- [Test Data Generator](../../test-data-generator/SKILL.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.21.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
