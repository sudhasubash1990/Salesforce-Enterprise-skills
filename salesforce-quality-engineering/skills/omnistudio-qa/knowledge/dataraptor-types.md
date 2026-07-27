---
title: DataRaptor Types
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: Knowledge Article
version: 0.22.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [omnistudio-qa, knowledge]
---

# DataRaptor Types

## Purpose

Validate Extract, Load, Transform, and Turbo Extract mapping accuracy.

## Reasoning Model

1. Classify DR type and input/output contracts.
2. Trace field mappings, formulas, and null handling.
3. Pair Load paths with SOVA stubs for CRM proof.
4. Note bulk/Turbo constraints and error paths.

## Decision Rules

- Load without SOQL proof for critical CRM writes → Incomplete Data Validation.
- Silent null overwrite → High data risk.

## Cross-Links (Canonical Depth)

- [OmniStudio Cloud Knowledge](../../knowledge/clouds/omnistudio.md)
- [SOQL Validation Assistant](../../soql-validation-assistant/SKILL.md)
- [Test Data Generator](../../test-data-generator/SKILL.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.22.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
