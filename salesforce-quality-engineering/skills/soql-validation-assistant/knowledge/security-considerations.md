---
title: Security Considerations
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: Knowledge Article
version: 0.16.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [soql-validation, knowledge]
---

# Security Considerations

## Purpose

Warn when query results may mislead due to security.

## Reasoning Model

1. State run-as user/profile/permission set.
2. Note CRUD, FLS, sharing, and sharing-only records.
3. Zero rows may mean hidden data — not always clean validation.

## Decision Rules

- Always include Security Considerations section.

## Cross-Links (Canonical Depth)

- [Security Knowledge](../../knowledge/security/README.md)
- [Sharing Security Testing](../../knowledge/sharing-security-testing.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.16.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
