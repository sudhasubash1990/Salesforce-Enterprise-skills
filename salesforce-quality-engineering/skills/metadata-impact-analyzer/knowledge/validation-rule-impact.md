---
title: Validation Rule Impact
module: Salesforce Quality Engineering
category: Specialized Skill Knowledge
document_type: Knowledge Article
version: 0.15.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [metadata-impact-analyzer, knowledge]
---

# Validation Rule Impact

## Purpose

Assess validation rule changes on save paths, API integrations, and bulk operations.

## Reasoning Model

1. Capture formula fields and error conditions referenced by the rule.
2. Identify UI-only vs API save paths affected.
3. Check bypass patterns (custom settings, hierarchy custom settings) if documented.
4. Map integrations that create/update records subject to the rule.

## Decision Rules

- New blocking rule on integrated object → High integration risk until backfill validated.
- Rule formula referencing undeployed field → deployment ordering risk.

## Cross-Links (Canonical Depth)

- [Validation Rule Testing](../../knowledge/validation-rule-testing.md)
- [Metadata Impact Analysis](../../knowledge/metadata/metadata-impact-analysis.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)
- [../../knowledge/metadata/README.md](../../knowledge/metadata/README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.15.0 | 2026-07-27 | QE Practice Lead | Initial specialized skill knowledge |
