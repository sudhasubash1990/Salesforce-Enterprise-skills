---
title: Permission Sets
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

# Permission Sets

## Purpose

Validate additive permissions and muting sets.

## Reasoning Model

1. List permission sets and groups per persona.
2. Identify View All/Modify All/Author Apex.
3. Validate assignment scope (user vs group).

## Decision Rules

- Prefer perm set delta over profile rewrite for testing focus.

## Cross-Links (Canonical Depth)

- [Permission Sets](../../knowledge/security/permission-sets.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.17.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
