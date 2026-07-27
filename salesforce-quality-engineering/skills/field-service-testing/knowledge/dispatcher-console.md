---
title: Dispatcher Console
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

# Dispatcher Console

## Purpose

Validate dispatcher UX for assign, drag-drop, Gantt, and alerts.

## Reasoning Model

1. Map dispatcher persona permissions.
2. Test assign/unassign/reschedule paths.
3. Verify console filters by territory and capacity.
4. Capture negative: cannot assign unqualified resource.

## Decision Rules

- Dispatcher without territory visibility → PTA escalation.

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
