---
title: Experience Cloud Security
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

# Experience Cloud Security

## Purpose

Validate partner/customer/guest community access separately.

## Reasoning Model

1. Separate profiles/perm sets for external users.
2. Guest user — minimal CRUD, high risk.
3. Test sharing sets and super user access if used.

## Decision Rules

- Guest profile change → Critical deployment risk.

## Cross-Links (Canonical Depth)

- [Sharing Security Testing](../../knowledge/sharing-security-testing.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.17.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
