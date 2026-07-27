---
title: Inventory Management
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: Knowledge Article
version: 0.19.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [field-service-testing, knowledge]
---

# Inventory Management

## Purpose

Validate van stock, product requests, consumption, transfers.

## Reasoning Model

1. Map Products Consumed on WOLI.
2. Test Product Request and Transfer paths.
3. Reconcile inventory with SOVA queries.
4. Validate returns and shortages.

## Decision Rules

- Negative stock without override → Fail.

## Cross-Links (Canonical Depth)

- [SOQL Validation Assistant](../../soql-validation-assistant/SKILL.md)
- [Data Validation](../../knowledge/data/data-validation.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.19.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
