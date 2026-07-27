---
title: Agentforce Architecture
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

# Agentforce Architecture

## Purpose

Map agent, topics, actions, and grounding layers before designing AI QA.

## Reasoning Model

1. Identify agent type and channel (employee, customer, service).
2. Inventory topics, instructions, actions, knowledge sources.
3. Separate configuration review from conversation scripts.
4. Flag licensed features—do not invent Agentforce capabilities.

## Decision Rules

- Confirm edition/license before asserting features.
- UI automation alone is insufficient for Agentforce QA.

## Cross-Links (Canonical Depth)

- [Agentforce Cloud Knowledge](../../knowledge/clouds/agentforce.md)
- [AI Governance](../../enterprise-quality/ai-governance/README.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.18.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
