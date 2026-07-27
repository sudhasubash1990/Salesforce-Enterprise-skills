---
title: Session Context
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: Knowledge Article
version: 0.18.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [agentforce-testing, knowledge]
---

# Session Context

## Purpose

Validate session memory and context retention.

## Reasoning Model

1. Confirm fields retained across turns.
2. Test context reset and session timeout.
3. Verify PII not leaked across users/sessions.

## Decision Rules

- Cross-session PII leakage → Critical security.

## Cross-Links (Canonical Depth)

- [Permission Testing Agent](../../permission-testing-agent/SKILL.md)
- [AI Governance](../../enterprise-quality/ai-governance/README.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.18.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
