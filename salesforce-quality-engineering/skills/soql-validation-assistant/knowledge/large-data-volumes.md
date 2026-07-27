---
title: Large Data Volumes
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: Knowledge Article
version: 0.16.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [soql-validation, knowledge]
---

# Large Data Volumes

## Purpose

Adapt validation queries for LDV contexts.

## Reasoning Model

1. Use narrow filters, LIMIT, and aggregate rollups.
2. Recommend parallel batch validation for full reconciliation.
3. Avoid full-table scans in production.

## Decision Rules

- Production full reconcile → No-Go without batch plan.

## Cross-Links (Canonical Depth)

- [Large Data Volumes](../../knowledge/performance/large-data-volumes.md)
- [LDV Data](../../knowledge/data/large-data-volumes.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.16.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
