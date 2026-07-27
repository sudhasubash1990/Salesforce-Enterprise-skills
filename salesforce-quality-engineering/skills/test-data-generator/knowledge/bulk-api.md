---
title: Bulk API
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

# Bulk API

## Purpose

Advise Bulk API–compatible structures for high-volume seed.

## Reasoning Model

1. Prefer Bulk for large inserts/updates.
2. Batch sizing guidance as qualitative.
3. Error file / retry strategy.
4. SOQL validation after load.

## Decision Rules

- Bulk without External ID strategy → High risk.

## Cross-Links (Canonical Depth)

- [Data Loader](../../knowledge/data/data-loader.md)
- [Data Volume Strategies](data-volume-strategies.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.20.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
