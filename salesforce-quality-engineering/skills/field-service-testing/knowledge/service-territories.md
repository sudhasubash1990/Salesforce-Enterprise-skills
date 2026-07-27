---
title: Service Territories
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: Knowledge Article
version: 0.19.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [field-service-testing, knowledge]
---

# Service Territories

## Purpose

Validate territory membership, coverage, and visibility.

## Reasoning Model

1. Map territories and members.
2. Test SA scheduling outside territory.
3. Validate hierarchy if used.
4. Cross-check sharing with PTA.

## Decision Rules

- Resource scheduled outside territory → Fail unless exception rule documented.

## Cross-Links (Canonical Depth)

- [Field Service Cloud Knowledge](../../knowledge/clouds/field-service.md)
- [Permission Testing Agent](../../permission-testing-agent/SKILL.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.19.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
