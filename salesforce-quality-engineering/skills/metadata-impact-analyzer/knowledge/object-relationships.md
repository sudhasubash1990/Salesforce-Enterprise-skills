---
title: Object Relationships
module: Salesforce Quality Engineering
category: Specialized Skill Knowledge
document_type: Knowledge Article
version: 0.15.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [metadata-impact-analyzer, knowledge]
---

# Object Relationships

## Purpose

Trace lookup, master-detail, junction, and polymorphic relationships affected by object/field changes.

## Reasoning Model

1. List parent and child objects for each changed field or object.
2. Identify roll-up summary fields, required lookups, and delete constraints.
3. Check sharing inheritance on master-detail relationships.
4. Map related list and report dependencies on relationship fields.

## Decision Rules

- Master-detail change → mandatory sharing and roll-up impact review.
- New required lookup → validate existing records and integration payloads.

## Cross-Links (Canonical Depth)

- [Metadata Relationships](../../knowledge/metadata/metadata-relationships.md)
- [Platform Knowledge](../../knowledge/platform/README.md)
- [Record Types](../../knowledge/platform/record-types.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)
- [../../knowledge/metadata/README.md](../../knowledge/metadata/README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.15.0 | 2026-07-27 | QE Practice Lead | Initial specialized skill knowledge |
