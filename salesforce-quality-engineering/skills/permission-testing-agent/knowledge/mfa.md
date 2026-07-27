---
title: MFA
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

# MFA

## Purpose

Validate MFA requirements for privileged personas.

## Reasoning Model

1. Identify MFA-required profiles/perm sets.
2. Document test user bypass only in non-prod.
3. Never disable MFA in prod for testing.

## Decision Rules

- Admin MFA bypass in sandbox — label assumption.

## Cross-Links (Canonical Depth)

- [MFA](../../knowledge/security/mfa.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.17.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
