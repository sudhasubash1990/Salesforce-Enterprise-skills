---
title: ETL Fundamentals
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

# ETL Fundamentals

## Purpose

Validate extract/transform/load contracts and error handling.

## Reasoning Model

1. Inventory extract filters and source of truth.
2. Validate transform rules against fixtures.
3. Confirm reject/quarantine and retry paths.
4. Label middleware tool names TBC when unknown.

## Decision Rules

- Happy-path-only ETL → Fail Negative Test Scenarios.

## Cross-Links (Canonical Depth)

- [Data Mapping Best Practices](data-mapping-best-practices.md)
- [Error Handling via pitfalls](common-migration-pitfalls.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.23.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
