---
title: Upsert Strategy
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

# Upsert Strategy

## Purpose

Validate upsert vs insert/update decisioning for re-runs and deltas.

## Reasoning Model

1. Define idempotent re-run rules.
2. Cover insert-only vs upsert collision paths.
3. Document merge/delete policies separately.
4. Align with incremental/delta strategy.

## Decision Rules

- Re-run without upsert plan → Cutover No-Go risk.

## Cross-Links (Canonical Depth)

- [External IDs](external-ids.md)
- [Migration Strategies](migration-strategies.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.23.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
