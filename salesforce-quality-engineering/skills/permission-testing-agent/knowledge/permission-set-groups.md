---
title: Permission Set Groups
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

# Permission Set Groups

## Purpose

Validate PSG composition and muting.

## Reasoning Model

1. Map PSG → constituent perm sets.
2. Apply muting permission set rules.
3. Verify effective permissions after group assignment.

## Decision Rules

- PSG change affects all members — high blast radius.

## Cross-Links (Canonical Depth)

- [Permission Set Groups](../../knowledge/security/permission-set-groups.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.17.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
