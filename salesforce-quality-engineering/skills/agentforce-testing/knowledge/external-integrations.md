---
title: External Integrations
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

# External Integrations

## Purpose

Validate external API actions from agents.

## Reasoning Model

1. Map Named Credential / Connected App.
2. Test timeout, 4xx/5xx, and empty payload handling.
3. Verify agent does not invent API data on failure.

## Decision Rules

- API failure must not produce hallucinated business facts.

## Cross-Links (Canonical Depth)

- [Integration Knowledge](../../knowledge/integration/README.md)
- [SOQL Validation](../../soql-validation-assistant/SKILL.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.18.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
