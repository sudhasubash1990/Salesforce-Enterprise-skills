---
title: Salesforce CLI Data Operations
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

# Salesforce CLI Data Operations

## Purpose

Advise `sf data` / tree import patterns as templates only.

## Reasoning Model

1. Prefer tree import for small related graphs.
2. Document file layout for CLI.
3. No live execution claims.
4. Cleanup via delete queries labeled for SOVA.

## Decision Rules

- CLI templates are advisory — do not claim org success without run evidence.

## Cross-Links (Canonical Depth)

- [Data Import](../../knowledge/data/data-import.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.20.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
