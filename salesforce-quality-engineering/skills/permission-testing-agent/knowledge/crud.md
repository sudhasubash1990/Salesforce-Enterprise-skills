---
title: CRUD
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

# CRUD

## Purpose

Validate object-level Create/Read/Update/Delete per persona.

## Reasoning Model

1. Build CRUD matrix: persona × object × action.
2. Test UI and API channels separately if both in scope.
3. Note tab visibility vs object CRUD distinction.

## Decision Rules

- Missing Create but tab visible → document UX vs security gap.
- Integration user CRUD ≠ business user CRUD.

## Cross-Links (Canonical Depth)

- [Object Level Security](../../knowledge/security/object-level-security.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.17.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
