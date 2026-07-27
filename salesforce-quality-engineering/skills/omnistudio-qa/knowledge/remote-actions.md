---
title: Remote Actions
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: Knowledge Article
version: 0.22.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [omnistudio-qa, knowledge]
---

# Remote Actions

## Purpose

Validate Remote/HTTP/Apex remotes and Salesforce Object actions.

## Reasoning Model

1. Classify action type and auth/contract expectations.
2. Stub request/response samples (sanitized).
3. Validate error mapping back to OS messaging.
4. Chain SOVA when SF object writes occur.

## Decision Rules

- Live credentials in artifacts → Critical Security escalate.
- No error-path remote tests → Incomplete Integration.

## Cross-Links (Canonical Depth)

- [Integration Procedures](integration-procedures.md)
- [SOQL Validation Assistant](../../soql-validation-assistant/SKILL.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.22.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
