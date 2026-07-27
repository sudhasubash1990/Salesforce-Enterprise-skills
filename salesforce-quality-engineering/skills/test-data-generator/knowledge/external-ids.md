---
title: External IDs
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: Knowledge Article
version: 0.20.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [test-data-generator, knowledge]
---

# External IDs

## Purpose

Use External IDs for upsert, migration rehearsal, and stable seed keys.

## Reasoning Model

1. Select External ID fields per object.
2. Design upsert order parents → children.
3. Document collision rules.
4. Recommend SOQL to verify upsert results.

## Decision Rules

- Missing External ID on bulk upsert → High risk.

## Cross-Links (Canonical Depth)

- [Data Import](../../knowledge/data/data-import.md)
- [SOQL Validation Assistant](../../soql-validation-assistant/SKILL.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.20.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
