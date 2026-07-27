---
title: Permission Model
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

# Permission Model

## Purpose

Evaluate CRUD, FLS, and permission set assignments affected by metadata changes.

## Reasoning Model

1. Map changed objects/fields/tabs/apps to permission requirements.
2. Identify persona-specific access deltas.
3. Check permission set group assignments and muting permission sets.
4. Validate Experience Cloud and guest user profiles separately.

## Decision Rules

- FLS change → mandatory negative test per affected persona.
- Profile change in production → treat as High security risk.

## Cross-Links (Canonical Depth)

- [Security Knowledge](../../knowledge/security/README.md)
- [Permission Set Testing](../../knowledge/permission-set-testing.md)
- [Sharing Security Testing](../../knowledge/sharing-security-testing.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)
- [../../knowledge/metadata/README.md](../../knowledge/metadata/README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.15.0 | 2026-07-27 | QE Practice Lead | Initial specialized skill knowledge |
