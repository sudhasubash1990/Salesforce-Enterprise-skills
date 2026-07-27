---
title: Authentication
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: Knowledge Article
version: 0.21.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [playwright-review, knowledge]
---

# Authentication

## Purpose

Review Salesforce login, MFA-aware patterns, and storageState.

## Reasoning Model

1. storageState per persona.
2. Never commit session cookies.
3. MFA: document program approach (TOTP vault, sandbox waiver) — do not invent.
4. Chain PTA for persona coverage.

## Decision Rules

- storageState in git → Critical escalate Security.

## Cross-Links (Canonical Depth)

- [Authentication](../../automation-intelligence/playwright/authentication.md)
- [Storage State](../../automation-intelligence/playwright/storage-state.md)
- [Permission Testing Agent](../../permission-testing-agent/SKILL.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.21.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
