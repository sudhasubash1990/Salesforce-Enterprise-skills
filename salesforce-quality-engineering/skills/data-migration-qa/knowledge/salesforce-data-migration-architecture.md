---
title: Salesforce Data Migration Architecture
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

# Salesforce Data Migration Architecture

## Purpose

Assess end-to-end migration architecture before detailed validation cases.

## Reasoning Model

1. Define waves, objects, volumes, and freeze windows.
2. Map staging → transform → load → reconcile layers.
3. Identify External ID strategy and load order.
4. Cross-link Sprint 4A data encyclopedia — do not duplicate.

## Decision Rules

- No Migration Scope → incomplete report.
- Missing load order → High relationship risk.

## Cross-Links (Canonical Depth)

- [Data Migration Validation](../../knowledge/data/data-migration-validation.md)
- [Large Data Volumes](../../knowledge/data/large-data-volumes.md)
- [Metadata Impact Analyzer](../../metadata-impact-analyzer/SKILL.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.23.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
