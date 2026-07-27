---
title: Metadata API
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

# Metadata API

## Purpose

Use Metadata API concepts to evidence dependency and deployment impact (QE lens — no live calls required).

## Reasoning Model

1. Interpret package.xml members and destructive changes.
2. Understand deploy/test/validate-only modes for readiness gates.
3. Map component types to regression surfaces.

## Decision Rules

- DestructiveChanges.xml present → mandatory rollback and data backup review.

## Cross-Links (Canonical Depth)

- [Metadata Overview](../../knowledge/metadata/metadata-overview.md)
- [Deployment Considerations](../../knowledge/metadata/deployment-considerations.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)
- [../../knowledge/metadata/README.md](../../knowledge/metadata/README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.15.0 | 2026-07-27 | QE Practice Lead | Initial specialized skill knowledge |
