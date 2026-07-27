---
title: Salesforce Synchronization Techniques
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

# Salesforce Synchronization Techniques

## Purpose

Sync patterns for Lightning rendering and async saves.

## Reasoning Model

1. Prefer auto-wait + network idle sparingly.
2. Ready helpers for spinner/toast.
3. Avoid fixed sleeps.
4. Validate save via UI toast + optional SOVA.

## Decision Rules

- Sleep-only sync → Fail Synchronization Review.

## Cross-Links (Canonical Depth)

- [Common Failures](../../automation-intelligence/playwright/common-failures.md)
- [SOQL Validation Assistant](../../soql-validation-assistant/SKILL.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.21.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
