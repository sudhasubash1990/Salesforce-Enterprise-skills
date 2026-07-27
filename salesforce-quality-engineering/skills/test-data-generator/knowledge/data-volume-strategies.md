---
title: Data Volume Strategies
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

# Data Volume Strategies

## Purpose

Select generation path by volume without inventing capacity numbers.

## Reasoning Model

1. Classify single/bulk/LDV/concurrent.
2. Recommend Loader vs Bulk API vs Apex.
3. State assumptions for row counts.
4. Require cleanup for bulk/LDV.

## Decision Rules

- Do not invent org governor timing SLAs.

## Cross-Links (Canonical Depth)

- [Large Data Volumes](../../knowledge/data/large-data-volumes.md)
- [Performance Knowledge](../../knowledge/performance/README.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.20.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
