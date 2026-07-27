---
title: Test Data Management Reasoning
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

# Test Data Management Reasoning

## Purpose

Apply TDM discipline: synthetic vs masked, personas, refresh, ownership.

## Reasoning Model

1. Classify environment purpose (SIT/UAT/regression/perf).
2. Choose synthetic vs masked with justification.
3. Define persona packs and ownership model.
4. Plan refresh and cleanup cadence.

## Decision Rules

- Real PII → refuse; redirect to synthetic/masking.
- Prefer TDG over encyclopedia when generation intent is clear.

## Cross-Links (Canonical Depth)

- [Test Data Management](../../knowledge/data/test-data-management.md)
- [Sprint 5 Test Data Strategy](../../templates/test-data-strategy.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.20.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
