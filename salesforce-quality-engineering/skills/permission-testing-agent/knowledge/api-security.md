---
title: API Security
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

# API Security

## Purpose

Validate REST/Bulk API access per integration persona.

## Reasoning Model

1. CRUD/FLS enforced for API user.
2. Compare API vs UI visibility.
3. Named credential identity separate matrix.

## Decision Rules

- API user with Modify All — flag excessive privilege.

## Cross-Links (Canonical Depth)

- [API Security](../../knowledge/integration/README.md)
- [SOQL Validation](../../soql-validation-assistant/SKILL.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.17.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
