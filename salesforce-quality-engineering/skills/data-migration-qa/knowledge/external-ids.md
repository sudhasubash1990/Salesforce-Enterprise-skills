---
title: External IDs
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

# External IDs

## Purpose

Validate External ID uniqueness and upsert keys.

## Reasoning Model

1. Inventory External ID fields per object.
2. Test uniqueness and null External ID behavior.
3. Confirm upsert matching rules.
4. Recommend SOVA stubs for duplicate External IDs.

## Decision Rules

- Non-unique External ID → Critical integrity risk.

## Cross-Links (Canonical Depth)

- [Upsert Strategy](upsert-strategy.md)
- [SOQL Validation Assistant](../../soql-validation-assistant/SKILL.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.23.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
