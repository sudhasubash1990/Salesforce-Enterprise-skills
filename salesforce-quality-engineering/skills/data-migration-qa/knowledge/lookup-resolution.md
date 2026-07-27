---
title: Lookup Resolution
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

# Lookup Resolution

## Purpose

Validate how lookups are resolved via External ID, staging keys, or post-update.

## Reasoning Model

1. Classify resolve-at-load vs two-pass update.
2. Test missing-parent and multi-match cases.
3. Document default/null lookup policy.
4. Recommend exception reports for unresolved keys.

## Decision Rules

- Silent null on required lookup → Critical.

## Cross-Links (Canonical Depth)

- [Relationship Migration](relationship-migration.md)
- [SOQL Validation Assistant](../../soql-validation-assistant/SKILL.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.23.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
