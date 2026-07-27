---
title: Relationship Queries
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

# Relationship Queries

## Purpose

Reason about parent-child and child-parent SOQL for backend validation.

## Reasoning Model

1. Map relationship name and cardinality.
2. Choose parent-to-child (subquery) vs child-to-parent (dot notation).
3. Limit relationship depth; flag performance on deep trees.

## Decision Rules

- Master-detail subqueries respect sharing — note persona.
- Polymorphic lookups need TYPEOF or separate queries.

## Cross-Links (Canonical Depth)

- [Referential Integrity](../../knowledge/data/referential-integrity.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.16.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
