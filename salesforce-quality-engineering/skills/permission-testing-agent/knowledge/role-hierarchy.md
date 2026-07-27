---
title: Role Hierarchy
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

# Role Hierarchy

## Purpose

Validate role-based record access inheritance.

## Reasoning Model

1. Map role tree and record ownership.
2. Test manager visibility to subordinate records.
3. Note role + sharing rule interaction.

## Decision Rules

- Role change deploy → regression on ownership-based reports.

## Cross-Links (Canonical Depth)

- [Role Hierarchy](../../knowledge/security/role-hierarchy.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.17.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
