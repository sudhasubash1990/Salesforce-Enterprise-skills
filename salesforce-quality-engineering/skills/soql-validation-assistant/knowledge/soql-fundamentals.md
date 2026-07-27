---
title: SOQL Fundamentals
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

# SOQL Fundamentals

## Purpose

Establish validation intent and query type before writing SOQL.

## Reasoning Model

1. Clarify business question the query must answer.
2. Choose query type: list, relationship, aggregate, count.
3. Identify object, fields, filters, and run-as persona.
4. Only then draft SOQL.

## Decision Rules

- Never output SOQL without Validation Objective.
- Prefer selective filters on indexed fields.

## Cross-Links (Canonical Depth)

- [Data Validation](../../knowledge/data/data-validation.md)
- [Data Model](../../knowledge/data/data-model.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.16.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
