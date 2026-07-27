---
title: Scheduling Engine
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

# Scheduling Engine

## Purpose

Validate candidate selection, travel, availability, and conflicts.

## Reasoning Model

1. Identify scheduling policy and work rules in scope.
2. Design tests for availability, skills, territory, travel.
3. Verify double-booking prevention and emergency insert.
4. Document expected candidate set qualitatively—no invented scores.

## Decision Rules

- Double booking → Fail scheduling assessment.
- Do not invent optimization scores.

## Cross-Links (Canonical Depth)

- [Field Service Cloud Knowledge](../../knowledge/clouds/field-service.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.19.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
