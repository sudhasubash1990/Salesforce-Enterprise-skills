---
title: Human Escalation
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

# Human Escalation

## Purpose

Validate handoff to human agents.

## Reasoning Model

1. Define escalation triggers (confidence, sentiment, policy).
2. Test transfer payload and context.
3. Verify agent stops acting after handoff.

## Decision Rules

- Silent failure without handoff → Fail release readiness.

## Cross-Links (Canonical Depth)

- [Agentforce Cloud Knowledge](../../knowledge/clouds/agentforce.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.18.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
