---
title: AI Guardrails
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

# AI Guardrails

## Purpose

Validate safety and policy guardrails.

## Reasoning Model

1. List disallowed topics and data classes.
2. Test jailbreak and policy-bypass attempts.
3. Verify refusal language and escalation.

## Decision Rules

- Guardrail bypass in sandbox → block production enablement.

## Cross-Links (Canonical Depth)

- [AI Governance](../../enterprise-quality/ai-governance/README.md)
- [Permission Testing Agent](../../permission-testing-agent/SKILL.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.18.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
