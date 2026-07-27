---
title: Sharing Model
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

# Sharing Model

## Purpose

Analyze sharing rules, OWD, role hierarchy, and manual sharing impacts.

## Reasoning Model

1. Identify OWD and sharing rule changes on affected objects.
2. Map role hierarchy and public group membership dependencies.
3. Check Apex sharing (with sharing / without sharing) on changed classes.
4. Validate report and dashboard visibility for restricted records.

## Decision Rules

- OWD tightening → validate integration service account access.
- New sharing rule → regression on record visibility per persona.

## Cross-Links (Canonical Depth)

- [Sharing Security Testing](../../knowledge/sharing-security-testing.md)
- [Security Knowledge](../../knowledge/security/README.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)
- [../../knowledge/metadata/README.md](../../knowledge/metadata/README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.15.0 | 2026-07-27 | QE Practice Lead | Initial specialized skill knowledge |
