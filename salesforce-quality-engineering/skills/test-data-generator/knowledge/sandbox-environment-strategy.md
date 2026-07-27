---
title: Sandbox and Environment Strategy
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

# Sandbox and Environment Strategy

## Purpose

Align seed packs to sandbox type, refresh, and environment purpose.

## Reasoning Model

1. Map SIT/UAT/Dev purposes.
2. Plan post-refresh reseed.
3. Synthetic vs masked decision per env.
4. Ownership of seed packs.

## Decision Rules

- Full copy with unmasked PII → escalate Security.

## Cross-Links (Canonical Depth)

- [Test Data Management](../../knowledge/data/test-data-management.md)
- [Release Knowledge](../../knowledge/release/README.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.20.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
