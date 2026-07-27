---
title: Apex Dependencies
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

# Apex Dependencies

## Purpose

Trace Apex class and trigger dependencies across automation, integrations, and tests.

## Reasoning Model

1. List SOQL/DML targets and shared service classes.
2. Identify trigger handler frameworks and recursion guards.
3. Map @AuraEnabled, @InvocableMethod, REST, and Batch entry points.
4. Check test class coverage dependencies (advisory — not coverage % invention).

## Decision Rules

- Trigger logic change → regression on all bulk and single-record paths.
- Shared utility class change → enumerate all callers before scoping regression.

## Cross-Links (Canonical Depth)

- [Platform Apex](../../knowledge/platform/apex.md)
- [Automation Knowledge](../../knowledge/automation/README.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)
- [../../knowledge/metadata/README.md](../../knowledge/metadata/README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.15.0 | 2026-07-27 | QE Practice Lead | Initial specialized skill knowledge |
