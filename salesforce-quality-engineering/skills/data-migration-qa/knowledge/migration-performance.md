---
title: Migration Performance
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

# Migration Performance

## Purpose

Assess batch size, parallelism, API limits without inventing SLAs.

## Reasoning Model

1. Identify LDV and chatty transform risks.
2. Document batch/parallel assumptions.
3. Recommend measurement plan.
4. Label any duration claims as assumptions or evidence.

## Decision Rules

- Invented throughput % → Anti-pattern.

## Cross-Links (Canonical Depth)

- [Large Data Volumes](../../knowledge/data/large-data-volumes.md)
- [Bulk API](bulk-api.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.23.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
