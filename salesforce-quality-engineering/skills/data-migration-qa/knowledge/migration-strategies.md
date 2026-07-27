---
title: Migration Strategies
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: Knowledge Article
version: 0.23.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [data-migration-qa, knowledge]
---

# Migration Strategies

## Purpose

Select and validate big-bang vs phased vs parallel-run strategies.

## Reasoning Model

1. Classify full refresh vs incremental/delta.
2. Assess business freeze and coexistence needs.
3. Define success criteria per wave.
4. Document residual risk for deferred history.

## Decision Rules

- Phased without delta rules → Incomplete Reconciliation Strategy.

## Cross-Links (Canonical Depth)

- [Data Migration Validation](../../knowledge/data/data-migration-validation.md)
- [Cutover Planning](cutover-planning.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.23.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
