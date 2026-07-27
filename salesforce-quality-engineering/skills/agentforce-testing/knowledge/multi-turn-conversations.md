---
title: Multi-turn Conversations
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

# Multi-turn Conversations

## Purpose

Validate multi-step reasoning and context continuity.

## Reasoning Model

1. Design 3–5 turn journeys with changing intent.
2. Verify prior facts retained correctly.
3. Test correction and contradiction handling.

## Decision Rules

- Context drop mid-journey → High regression priority.

## Cross-Links (Canonical Depth)

- [Conversation Design](conversation-design.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.18.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
