---
title: Indexing
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

# Indexing

## Purpose

Relate filter fields to index availability for QE advice.

## Reasoning Model

1. Ask whether custom fields are indexed when filtering LDV.
2. Note standard indexed fields (Id, Name, OwnerId, foreign keys).
3. Recommend SA confirmation for custom index needs.

## Decision Rules

- Do not assume custom field is indexed.

## Cross-Links (Canonical Depth)

- [Indexing Concepts](../../knowledge/performance/indexing-concepts.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.16.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
