---
title: Formula Fields
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

# Formula Fields

## Purpose

Validate via SOQL limitations on formula and roll-up fields.

## Reasoning Model

1. Formula fields queryable but not filterable in all cases — check filter rules.
2. Roll-up summary only on master-detail parent.
3. Cross-object formulas — document limitations.

## Decision Rules

- Cannot filter on some formula types — use alternative query path.

## Cross-Links (Canonical Depth)

- [Platform Knowledge](../../knowledge/platform/README.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.16.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
