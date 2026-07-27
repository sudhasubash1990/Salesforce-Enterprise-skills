---
title: Object Relationships
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

# Object Relationships

## Purpose

Generate relationship-aware hierarchies with referential integrity.

## Reasoning Model

1. Classify lookup vs master-detail vs junction.
2. Order inserts correctly.
3. Handle many-to-many via junction rows.
4. Draw logical relationship diagram before payloads.

## Decision Rules

- Orphan children → Fail integrity gate.

## Cross-Links (Canonical Depth)

- [Referential Integrity](../../knowledge/data/referential-integrity.md)
- [Data Integrity](../../knowledge/data/data-integrity.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.20.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
