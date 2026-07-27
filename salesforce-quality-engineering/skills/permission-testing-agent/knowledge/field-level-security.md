---
title: Field Level Security
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: Knowledge Article
version: 0.17.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [permission-testing, knowledge]
---

# Field Level Security

## Purpose

Validate readable/editable/hidden fields per persona.

## Reasoning Model

1. Map sensitive fields explicitly.
2. Test read-only vs hidden vs editable.
3. Validate related list field exposure.

## Decision Rules

- Hidden field must not appear in UI or API response for persona.
- Formula roll-up read-only exceptions documented.

## Cross-Links (Canonical Depth)

- [FLS Knowledge](../../knowledge/security/field-level-security.md)
- [Permission Set Testing](../../knowledge/permission-set-testing.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.17.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
