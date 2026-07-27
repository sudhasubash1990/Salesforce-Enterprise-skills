---
title: Offline Synchronization
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: Knowledge Article
version: 0.19.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [field-service-testing, knowledge]
---

# Offline Synchronization

## Purpose

Validate offline cache, sync, and conflict handling.

## Reasoning Model

1. Design go-offline → mutate → reconnect scenarios.
2. Test conflict when desktop and mobile both change SA.
3. Verify no silent data loss.
4. Security: offline cache must not expose other territories.

## Decision Rules

- Data loss on sync → Critical escalation.

## Cross-Links (Canonical Depth)

- [Mobile Architecture](mobile-architecture.md)
- [Permission Testing Agent](../../permission-testing-agent/SKILL.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.19.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
