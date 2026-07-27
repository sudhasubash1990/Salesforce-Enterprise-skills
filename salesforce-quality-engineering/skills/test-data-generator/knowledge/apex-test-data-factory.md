---
title: Apex Test Data Factory
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

# Apex Test Data Factory

## Purpose

Design Apex @TestSetup / factory method stubs for unit/integration tests.

## Reasoning Model

1. Isolate factories from production data.
2. SeeAllData=false by default.
3. Cover required relationships.
4. Document limitations vs env seed packs.

## Decision Rules

- SeeAllData=true without justification → anti-pattern.

## Cross-Links (Canonical Depth)

- [Data Factories](data-factories.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.20.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
