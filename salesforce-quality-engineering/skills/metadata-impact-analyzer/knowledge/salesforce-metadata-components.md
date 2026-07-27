---
title: Salesforce Metadata Components
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

# Salesforce Metadata Components

## Purpose

Map changed metadata types to dependency surfaces and impact categories for QE analysis.

## Reasoning Model

1. Identify metadata type from change manifest (package.xml, change set, or diff).
2. Classify as data model, UI, automation, security, integration, or analytics.
3. Load type-specific dependency rules from cross-linked Sprint 4A articles.
4. Enumerate upstream producers and downstream consumers before impact statements.

## Decision Rules

- Never skip type classification — unknown type → mark Partial and request manifest detail.
- Treat packaged metadata separately from unpackaged (managed package constraints).
- Custom Metadata Types affect runtime config — trace Apex/LWC/Flow readers.

## Cross-Links (Canonical Depth)

- [Metadata Types](../../knowledge/metadata/metadata-types.md)
- [Metadata Overview](../../knowledge/metadata/metadata-overview.md)
- [Metadata Dependencies](../../knowledge/metadata/metadata-dependencies.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)
- [../../knowledge/metadata/README.md](../../knowledge/metadata/README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.15.0 | 2026-07-27 | QE Practice Lead | Initial specialized skill knowledge |
