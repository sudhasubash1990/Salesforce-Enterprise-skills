---
title: Flow Dependencies
module: Salesforce Quality Engineering
category: Specialized Skill Knowledge
document_type: Knowledge Article
version: 0.15.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [metadata-impact-analyzer, knowledge]
---

# Flow Dependencies

## Purpose

Analyze Record-Triggered, Scheduled, Screen, and Autolaunched Flow impacts and execution order.

## Reasoning Model

1. Identify changed Flow elements: entry criteria, decisions, DML, subflows, Apex actions.
2. Map referenced objects, fields, formulas, and invocable Apex.
3. Check active vs inactive versions and deployment activation plan.
4. Compare order of execution with triggers and validation rules on same object.

## Decision Rules

- Record-triggered Flow on same object as trigger → flag order-of-execution risk.
- Subflow or invocable Apex change → trace all parent Flows.

## Cross-Links (Canonical Depth)

- [Automation Knowledge](../../knowledge/automation/README.md)
- [Metadata Dependencies](../../knowledge/metadata/metadata-dependencies.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)
- [../../knowledge/metadata/README.md](../../knowledge/metadata/README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.15.0 | 2026-07-27 | QE Practice Lead | Initial specialized skill knowledge |
