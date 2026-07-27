---
title: Data Mapping Best Practices
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

# Data Mapping Best Practices

## Purpose

Assess field-level mapping completeness and business correctness.

## Reasoning Model

1. Trace source→target for every in-scope field.
2. Flag unmapped mandatory and unused targets.
3. Validate picklist/record type maps.
4. Chain MIA when new fields required for migration.

## Decision Rules

- Mapping gaps on required fields → Block Cutover Readiness.

## Cross-Links (Canonical Depth)

- [Data Migration Validation](../../knowledge/data/data-migration-validation.md)
- [Metadata Impact Analyzer](../../metadata-impact-analyzer/SKILL.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.23.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
