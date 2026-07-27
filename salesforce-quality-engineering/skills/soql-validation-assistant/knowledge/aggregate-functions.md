---
title: Aggregate Functions
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

# Aggregate Functions

## Purpose

Use COUNT, SUM, GROUP BY, HAVING for reconciliation and duplicate detection.

## Reasoning Model

1. Define aggregation purpose (reconcile, detect duplicates, smoke metric).
2. Choose GROUP BY keys aligned to business rule.
3. Add HAVING for post-aggregate filters.

## Decision Rules

- COUNT() vs COUNT(Id) — document null handling.
- GROUP BY picklist — watch record-type specific values.

## Cross-Links (Canonical Depth)

- [Data Reconciliation](../../knowledge/data/data-reconciliation.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.16.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
