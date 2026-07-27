---
title: User Mode vs System Mode
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: Knowledge Article
version: 0.17.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [permission-testing, knowledge]
---

# User Mode vs System Mode

## Purpose

Choose validation channel matching real user experience.

## Reasoning Model

1. UI and user-mode API reflect true access.
2. System mode for admin/investigation only — document separately.
3. Flow/Apex context determines mode.

## Decision Rules

- Never sign off community access using system admin verification only.

## Cross-Links (Canonical Depth)

- [Apex Security](apex-security.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.17.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
