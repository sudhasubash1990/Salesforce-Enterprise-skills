---
title: Reconciliation Techniques
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

# Reconciliation Techniques

## Purpose

Design count, aggregate, financial, and sample-journey reconciliation.

## Reasoning Model

1. Define tolerances and exception criteria.
2. Produce SOQL stubs for SOVA expansion.
3. Cover delta/incremental reconcile.
4. Include business journey smoke after counts.

## Decision Rules

- Counts-only with no field sample → Weak Reconciliation Strategy.

## Cross-Links (Canonical Depth)

- [Data Reconciliation Encyclopedia](../../knowledge/data/data-reconciliation.md)
- [SOQL Validation Assistant](../../soql-validation-assistant/SKILL.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.23.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
