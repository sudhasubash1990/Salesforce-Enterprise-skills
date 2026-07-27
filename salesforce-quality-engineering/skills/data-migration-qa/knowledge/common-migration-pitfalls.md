---
title: Common Migration Pitfalls
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

# Common Migration Pitfalls

## Purpose

Catalog frequent migration defects and preventive checks.

## Reasoning Model

1. Duplicates, orphans, wrong owners, picklist mismatches.
2. Silent upsert collisions and partial batch failures.
3. Attachment/File gaps and ContentDocumentLink misses.
4. Count match with wrong field values.

## Decision Rules

- Every DMQA report should address applicable pitfalls explicitly.

## Cross-Links (Canonical Depth)

- [Data Quality Framework](data-quality-framework.md)
- [Relationship Migration](relationship-migration.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.23.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
