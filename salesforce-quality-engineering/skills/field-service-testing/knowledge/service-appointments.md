---
title: Service Appointments
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

# Service Appointments

## Purpose

Validate SA scheduling, status, and completion.

## Reasoning Model

1. Test Scheduled → Dispatched → In Progress → Completed.
2. Validate duration, arrival windows, and cannot-complete reasons.
3. Backend SOQL for Assigned Resource.

## Decision Rules

- Completed SA without resource → Fail backend validation.

## Cross-Links (Canonical Depth)

- [SOQL Validation Assistant](../../soql-validation-assistant/SKILL.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.19.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
