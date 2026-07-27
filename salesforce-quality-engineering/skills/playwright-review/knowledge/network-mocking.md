---
title: Network Mocking
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

# Network Mocking

## Purpose

Review route mocking vs real Salesforce API usage.

## Reasoning Model

1. Prefer real SF API for setup/teardown when validating CRM.
2. Mock only unstable third parties with justification.
3. Document mock contracts.
4. Avoid masking SF defects with over-mocking.

## Decision Rules

- Mocking core CRM write path for UI 'pass' → High risk.

## Cross-Links (Canonical Depth)

- [Mocking](../../automation-intelligence/playwright/mocking.md)
- [Network Interception](../../automation-intelligence/playwright/network-interception.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.21.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
