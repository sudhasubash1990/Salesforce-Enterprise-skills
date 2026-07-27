---
title: Topics
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

# Topics

## Purpose

Validate topic classification and routing to correct agent behavior.

## Reasoning Model

1. List topics and classification criteria.
2. Design utterances for in-topic and out-of-topic.
3. Verify handoff when topic confidence is low.

## Decision Rules

- Ambiguous utterance → expect clarification or escalation, not silent wrong topic.

## Cross-Links (Canonical Depth)

- [Agentforce Cloud Knowledge](../../knowledge/clouds/agentforce.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.18.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
