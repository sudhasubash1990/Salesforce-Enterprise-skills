---
title: WITH SECURITY_ENFORCED
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

# WITH SECURITY_ENFORCED

## Purpose

Advise SOQL/Apex user-mode enforcement for validation.

## Reasoning Model

1. Recommend WITH SECURITY_ENFORCED in validation SOQL where applicable.
2. Contrast system mode query results vs user mode.
3. Delegate query text to SOVA.

## Decision Rules

- System mode SOQL in validation must be labeled — not default for business proof.

## Cross-Links (Canonical Depth)

- [SOQL Validation Assistant](../../soql-validation-assistant/SKILL.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.17.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
