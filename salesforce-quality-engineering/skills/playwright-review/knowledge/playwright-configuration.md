---
title: Playwright Configuration
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

# Playwright Configuration

## Purpose

Review playwright.config for env, projects, retries, reporters.

## Reasoning Model

1. Inventory projects (browsers/envs).
2. Check retries, timeout, workers.
3. Flag hardcoded org URLs in config.
4. Ensure reporters/traces on failure.

## Decision Rules

- Hardcoded secrets in config → Critical security.

## Cross-Links (Canonical Depth)

- [CI/CD Integration](../../automation-intelligence/playwright/ci-cd-integration.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.21.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
