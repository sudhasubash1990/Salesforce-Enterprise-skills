---
title: Optimization Rules
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

# Optimization Rules

## Purpose

Validate optimization runs and conflict resolution.

## Reasoning Model

1. Define optimization scope (territory, date range).
2. Compare before/after schedule for conflicts reduced—qualitative.
3. Test timeout and partial optimization behavior.
4. Do not invent numeric optimization scores.

## Decision Rules

- Optimization timeout on LDV → Performance escalation.

## Cross-Links (Canonical Depth)

- [Scheduling Engine](scheduling-engine.md)
- [Performance Knowledge](../../knowledge/performance/README.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.19.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
