---
title: Session Security
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

# Session Security

## Purpose

Validate session policies affecting test execution.

## Reasoning Model

1. Login hours, session timeout, IP restrictions.
2. Test blocked vs allowed sessions.
3. Document MFA interaction.

## Decision Rules

- IP restriction blocks automation user — separate service account.

## Cross-Links (Canonical Depth)

- [Session Policies](../../knowledge/security/session-policies.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.17.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
