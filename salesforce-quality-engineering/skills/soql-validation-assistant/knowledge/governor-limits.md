---
title: Governor Limits
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

# Governor Limits

## Purpose

Evaluate query impact on SOQL rows and limits.

## Reasoning Model

1. Estimate row volume; apply LIMIT for exploratory queries.
2. Flag queries in loops (Apex/integration context).
3. Recommend batch for large reconciliations.

## Decision Rules

- More than 50k rows scanned → High performance risk.

## Cross-Links (Canonical Depth)

- [Governor Limits](../../knowledge/performance/governor-limits.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.16.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
