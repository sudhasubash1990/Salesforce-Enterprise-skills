---
title: Knowledge Grounding
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

# Knowledge Grounding

## Purpose

Assess whether responses are grounded in approved knowledge/data.

## Reasoning Model

1. Identify grounding sources (Knowledge, Data Cloud, CRM records).
2. Design retrieval-hit and retrieval-miss tests.
3. Require citation/source behavior when configured.

## Decision Rules

- Missed retrieval → refuse or escalate; never invent policy.

## Cross-Links (Canonical Depth)

- [Agentforce Cloud Knowledge](../../knowledge/clouds/agentforce.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.18.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
