---
title: Date Literals
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

# Date Literals

## Purpose

Apply date literals and functions for time-bound validation.

## Reasoning Model

1. Confirm timezone and business date boundaries.
2. Use LAST_N_DAYS, THIS_MONTH, etc. with explicit business meaning.
3. Compare CreatedDate vs custom date fields per requirement.

## Decision Rules

- Date-only vs datetime — document truncation risk.

## Cross-Links (Canonical Depth)

- [Release Validation](../../knowledge/release/post-deployment-validation.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.16.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
