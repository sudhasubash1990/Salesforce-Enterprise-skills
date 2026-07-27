---
title: Tooling API
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

# Tooling API

## Purpose

Use Tooling API concepts for dependency discovery evidence (QE advisory — no credentials in skill).

## Reasoning Model

1. Reference Dependency API / MetadataComponentDependency patterns for impact evidence.
2. Identify Flow, Apex, and ValidationRule dependency queries for SOQL validation section.
3. Document when human architect must run live queries in org.

## Decision Rules

- If dependency graph not supplied → state assumption and recommend Tooling query pack.

## Cross-Links (Canonical Depth)

- [Metadata Dependencies](../../knowledge/metadata/metadata-dependencies.md)
- [Platform Knowledge](../../knowledge/platform/README.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)
- [../../knowledge/metadata/README.md](../../knowledge/metadata/README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.15.0 | 2026-07-27 | QE Practice Lead | Initial specialized skill knowledge |
