---
title: Query Optimization
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

# Query Optimization

## Purpose

Recommend improvements to proposed SOQL.

## Reasoning Model

1. Reduce selected fields to validation minimum.
2. Replace non-selective filters where possible.
3. Suggest alternative queries in section 13.

## Decision Rules

- Optimize only after validation objective is clear.

## Cross-Links (Canonical Depth)

- [SOQL Performance](../../knowledge/performance/soql-performance.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.16.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
