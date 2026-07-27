---
title: Bulk API
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

# Bulk API

## Purpose

Assess Bulk API usage for migration loads without inventing timings.

## Reasoning Model

1. Confirm Bulk API 1.0/2.0 intent and job design.
2. Review batch sizing and parallelism assumptions.
3. Flag API limit and governor risks.
4. Require measured evidence for duration claims.

## Decision Rules

- Invented job duration % → Anti-pattern.

## Cross-Links (Canonical Depth)

- [Data Loader](data-loader.md)
- [Migration Performance](migration-performance.md)
- [Large Data Volumes](../../knowledge/data/large-data-volumes.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.23.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
