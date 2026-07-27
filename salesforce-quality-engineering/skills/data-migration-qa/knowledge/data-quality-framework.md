---
title: Data Quality Framework
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

# Data Quality Framework

## Purpose

Evaluate completeness, accuracy, consistency, validity, uniqueness, timeliness.

## Reasoning Model

1. Profile nulls, formats, and duplicates pre-load.
2. Validate cleansing rules with fixtures.
3. Define DQ thresholds and exception owners.
4. Do not invent DQ % without evidence.

## Decision Rules

- No DQ Assessment when cleansing claimed → Incomplete.

## Cross-Links (Canonical Depth)

- [Data Quality Encyclopedia](../../knowledge/data/data-quality.md)
- [Common Migration Pitfalls](common-migration-pitfalls.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.23.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
