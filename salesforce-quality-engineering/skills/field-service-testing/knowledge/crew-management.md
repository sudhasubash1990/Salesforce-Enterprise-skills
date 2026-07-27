---
title: Crew Management
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

# Crew Management

## Purpose

Validate crews, members, and multi-resource appointments.

## Reasoning Model

1. Map Service Crew and members.
2. Test crew assignment vs individual.
3. Validate capacity when member absent.

## Decision Rules

- Crew scheduled with unavailable member → Fail unless rule allows.

## Cross-Links (Canonical Depth)

- [Service Appointments](service-appointments.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.19.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
