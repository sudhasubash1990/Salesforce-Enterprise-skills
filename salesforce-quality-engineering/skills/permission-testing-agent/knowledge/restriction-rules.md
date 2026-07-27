---
title: Restriction Rules
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: Knowledge Article
version: 0.17.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [permission-testing, knowledge]
---

# Restriction Rules

## Purpose

Validate record filtering for visibility reduction.

## Reasoning Model

1. Document criteria excluding records from view.
2. Test records that should disappear vs remain.
3. Combine with sharing rules in test plan.

## Decision Rules

- Restriction rule deploy without comms → false defect reports.

## Cross-Links (Canonical Depth)

- [Restriction Rules](../../knowledge/security/restriction-rules.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.17.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
