---
title: Assertions
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: Knowledge Article
version: 0.21.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [playwright-review, knowledge]
---

# Assertions

## Purpose

Review assertion clarity and failure diagnostics.

## Reasoning Model

1. Assert business outcomes, not only element presence.
2. Use web-first assertions with auto-wait.
3. Avoid soft-assert spam that hides defects.
4. Pair UI assert with SOVA when data state matters.

## Decision Rules

- Presence-only asserts for critical CRM writes → Weak.

## Cross-Links (Canonical Depth)

- [SOQL Validation Assistant](../../soql-validation-assistant/SKILL.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.21.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
