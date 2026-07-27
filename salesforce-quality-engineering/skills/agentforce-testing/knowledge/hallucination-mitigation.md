---
title: Hallucination Mitigation
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

# Hallucination Mitigation

## Purpose

Detect and reduce ungrounded agent claims.

## Reasoning Model

1. Compare response claims to grounding sources.
2. Design trap questions with no source.
3. Require refuse/escalate when ungrounded.

## Decision Rules

- Hallucinated financial/legal/medical claim → Critical.

## Cross-Links (Canonical Depth)

- [Knowledge Grounding](knowledge-grounding.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.18.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
