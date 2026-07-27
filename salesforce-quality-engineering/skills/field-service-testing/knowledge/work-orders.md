---
title: Work Orders
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

# Work Orders

## Purpose

Validate Work Order and WOLI lifecycle.

## Reasoning Model

1. Trace create → schedule → execute → close.
2. Validate required fields and status transitions.
3. Link child SA and inventory consumption.
4. Chain MIA when WO automation/metadata changes.

## Decision Rules

- Status skip without business rule → Fail.

## Cross-Links (Canonical Depth)

- [Field Service Cloud Knowledge](../../knowledge/clouds/field-service.md)
- [Metadata Impact Analyzer](../../metadata-impact-analyzer/SKILL.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.19.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
