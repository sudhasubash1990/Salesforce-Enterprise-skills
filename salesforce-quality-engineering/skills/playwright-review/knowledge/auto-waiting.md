---
title: Auto Waiting
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

# Auto Waiting

## Purpose

Prefer Playwright auto-wait over hard sleeps for Salesforce UI.

## Reasoning Model

1. Identify sleep()/waitForTimeout abuse.
2. Use expect(...).toBeVisible and locator actions.
3. Document intentional network waits.
4. SF Lightning may need targeted ready helpers — not blanket sleeps.

## Decision Rules

- Hard sleep as primary sync → Fail Synchronization Review.

## Cross-Links (Canonical Depth)

- [Common Failures](../../automation-intelligence/playwright/common-failures.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.21.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
