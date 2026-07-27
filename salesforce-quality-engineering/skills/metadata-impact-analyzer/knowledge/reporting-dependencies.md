---
title: Reporting Dependencies
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

# Reporting Dependencies

## Purpose

Identify reports, dashboards, and analytics dependencies on changed fields and objects.

## Reasoning Model

1. Search report types, fields, filters, and bucket fields referencing changed metadata.
2. Map dashboard components and dynamic dashboards.
3. Check Einstein / CRM Analytics dependencies if in scope.
4. Flag historical trending and snapshot fields.

## Decision Rules

- Field type change → all dependent reports may break (High reporting risk).
- Deleted field → run report inventory before deploy.

## Cross-Links (Canonical Depth)

- [Reporting Knowledge](../../knowledge/reporting/README.md)
- [Metadata Dependencies](../../knowledge/metadata/metadata-dependencies.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)
- [../../knowledge/metadata/README.md](../../knowledge/metadata/README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.15.0 | 2026-07-27 | QE Practice Lead | Initial specialized skill knowledge |
