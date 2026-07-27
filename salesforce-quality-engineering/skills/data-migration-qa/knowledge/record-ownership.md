---
title: Record Ownership
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: Knowledge Article
version: 0.23.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [data-migration-qa, knowledge]
---

# Record Ownership

## Purpose

Validate OwnerId mapping, queues, and post-migrate sharing impact.

## Reasoning Model

1. Map legacy owners to Salesforce users/queues.
2. Validate inactive user / default owner rules.
3. Assess OWD/sharing after ownership change.
4. Chain PTA for persona visibility.

## Decision Rules

- All records owned by admin → Security/visibility defect.

## Cross-Links (Canonical Depth)

- [Permission Testing Agent](../../permission-testing-agent/SKILL.md)
- [Migration Security](migration-security.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.23.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
