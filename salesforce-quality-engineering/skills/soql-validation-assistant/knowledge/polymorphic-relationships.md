---
title: Polymorphic Relationships
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: Knowledge Article
version: 0.16.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [soql-validation, knowledge]
---

# Polymorphic Relationships

## Purpose

Handle WhoId, WhatId, and polymorphic lookups in validation SOQL.

## Reasoning Model

1. Use TYPEOF when multiple object types in one field.
2. Split queries per object type when simpler.
3. Document which types are in scope.

## Decision Rules

- Task.WhoId / WhatId — specify Person Account vs Contact scenarios.

## Cross-Links (Canonical Depth)

- [Platform Knowledge](../../knowledge/platform/README.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.16.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
