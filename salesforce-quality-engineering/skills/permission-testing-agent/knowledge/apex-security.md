---
title: Apex Security
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

# Apex Security

## Purpose

Validate Apex sharing mode and elevated access risks.

## Reasoning Model

1. Identify without sharing / inherited sharing classes.
2. Map run-as and elevated DML.
3. Test data created by automation visibility.

## Decision Rules

- without sharing class → explicit sharing validation required.

## Cross-Links (Canonical Depth)

- [Sharing Security Testing](../../knowledge/sharing-security-testing.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.17.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
