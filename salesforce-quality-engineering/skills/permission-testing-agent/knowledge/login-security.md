---
title: Login Security
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

# Login Security

## Purpose

Validate login policies and lockout behavior.

## Reasoning Model

1. Login IP ranges, trusted IPs, password policies.
2. Negative: blocked login paths.
3. Integration OAuth separate from user login.

## Decision Rules

- Lockout during UAT — coordinate test data users.

## Cross-Links (Canonical Depth)

- [Login Policies](../../knowledge/security/login-policies.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.17.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
