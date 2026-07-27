---
title: Query Selectivity
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: Knowledge Article
version: 0.16.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [soql-validation, knowledge]
---

# Query Selectivity

## Purpose

Ensure filters use selective predicates.

## Reasoning Model

1. Prefer Id, Name (if indexed), foreign keys, standard indexed fields.
2. Avoid leading-wildcard LIKE on large objects.
3. Document when filter may be non-selective.

## Decision Rules

- Custom field without index + high cardinality → warn and suggest alternative.

## Cross-Links (Canonical Depth)

- [Query Selectivity](../../knowledge/performance/query-selectivity.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.16.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
