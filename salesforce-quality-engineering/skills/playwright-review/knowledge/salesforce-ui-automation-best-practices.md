---
title: Salesforce UI Automation Best Practices
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

# Salesforce UI Automation Best Practices

## Purpose

Salesforce-specific UI automation review lens.

## Reasoning Model

1. Centralize Lightning navigation helpers.
2. Handle related lists, console tabs, utility bar.
3. Experience vs LEX differences.
4. Agentforce UI → chain AFT for AI quality beyond clicks.

## Decision Rules

- UI-only Agentforce tests without AFT → Incomplete.

## Cross-Links (Canonical Depth)

- [Salesforce Best Practices](../../automation-intelligence/playwright/salesforce-best-practices.md)
- [Agentforce Testing](../../agentforce-testing/SKILL.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.21.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
