---
title: Integration Procedures
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: Knowledge Article
version: 0.22.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [omnistudio-qa, knowledge]
---

# Integration Procedures

## Purpose

Validate IP orchestration: branches, cache, retry, remotes, SF operations.

## Reasoning Model

1. Map step sequence and conditional branches.
2. Validate response mapping into Data JSON / OS.
3. Review cache keys and retry policy (document; do not invent SLAs).
4. Confirm error handling and rollback expectations.

## Decision Rules

- Happy-path-only IP tests → Fail Integration Validation.
- External HTTP without contract stub → Label TBC.

## Cross-Links (Canonical Depth)

- [OmniStudio Cloud Knowledge](../../knowledge/clouds/omnistudio.md)
- [Remote Actions](remote-actions.md)
- [Error Handling](error-handling.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.22.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
