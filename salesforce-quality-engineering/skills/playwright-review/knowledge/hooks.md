---
title: Hooks
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

# Hooks

## Purpose

Assess before/after hooks for cleanup and side effects.

## Reasoning Model

1. Prefer fixtures over global hooks where possible.
2. Ensure cleanup does not hide failures.
3. Avoid heavy UI login in every beforeEach when storageState exists.

## Decision Rules

- Login UI in every test without storageState → Performance smell.

## Cross-Links (Canonical Depth)

- [Fixtures](fixtures.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.21.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
