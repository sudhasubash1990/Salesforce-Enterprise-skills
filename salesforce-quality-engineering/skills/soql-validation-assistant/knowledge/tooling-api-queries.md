---
title: Tooling API Queries
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

# Tooling API Queries

## Purpose

Advise Tooling API SOQL for metadata dependency evidence.

## Reasoning Model

1. Use for Flow, Apex, ValidationRule dependency discovery.
2. Not for business data validation — separate from data SOQL.
3. Human/tool executes in org; skill recommends query text.

## Decision Rules

- Label Tooling vs data SOQL explicitly.

## Cross-Links (Canonical Depth)

- [MIA Tooling API](../../metadata-impact-analyzer/knowledge/tooling-api.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.16.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
