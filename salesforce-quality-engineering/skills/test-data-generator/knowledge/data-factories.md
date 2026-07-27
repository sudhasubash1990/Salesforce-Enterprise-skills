---
title: Data Factories
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

# Data Factories

## Purpose

Design reusable factories (Apex/CLI/Loader) for deterministic seed packs.

## Reasoning Model

1. Choose factory approach by volume and reuse need.
2. Parameterize personas and record types.
3. Keep factories deterministic and cleanup-aware.
4. Prefer Apex factories for unit tests; Loader/CLI for env seed.

## Decision Rules

- Factories must not hardcode production IDs.

## Cross-Links (Canonical Depth)

- [Apex Test Data Factory](apex-test-data-factory.md)
- [Automation Test Data](../../automation-intelligence/test-data/README.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.20.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
