---
title: Data Loader
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

# Data Loader

## Purpose

Validate Data Loader / Import Wizard patterns for controlled loads.

## Reasoning Model

1. Confirm insert vs upsert vs update vs delete operations.
2. Validate CSV headers and External ID columns.
3. Review success/error file triage process.
4. Prefer Bulk for LDV; document tool choice rationale.

## Decision Rules

- UI Import Wizard for LDV without rationale → Performance risk.

## Cross-Links (Canonical Depth)

- [Data Loader Encyclopedia](../../knowledge/data/data-loader.md)
- [External IDs](external-ids.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.23.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
