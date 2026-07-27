---
title: Salesforce Data Model for Test Data
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: Knowledge Article
version: 0.20.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [test-data-generator, knowledge]
---

# Salesforce Data Model for Test Data

## Purpose

Frame objects/fields as a generation surface before inventing rows.

## Reasoning Model

1. Inventory standard vs custom objects in scope.
2. Map required vs optional fields and record types.
3. Identify formula/rollup fields that must not be written.
4. Cross-link Sprint 4A data-model encyclopedia — do not duplicate.

## Decision Rules

- Never invent undocumented custom objects as fact.
- Confirm edition/licenses before asserting objects exist.

## Cross-Links (Canonical Depth)

- [Data Model](../../knowledge/data/data-model.md)
- [Data Knowledge Index](../../knowledge/data/README.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.20.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
