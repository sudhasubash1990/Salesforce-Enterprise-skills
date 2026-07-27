---
title: Relationship Migration
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

# Relationship Migration

## Purpose

Validate parent-child load order and relationship integrity.

## Reasoning Model

1. Document dependency graph (Account→Contact→Opportunity…).
2. Validate lookup vs master-detail behaviors.
3. Detect orphans and broken references.
4. Include ContentDocumentLink / attachment parents.

## Decision Rules

- Child before parent without External ID resolve → Fail Relationship Validation.

## Cross-Links (Canonical Depth)

- [Lookup Resolution](lookup-resolution.md)
- [Referential Integrity](../../knowledge/data/referential-integrity.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.23.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
