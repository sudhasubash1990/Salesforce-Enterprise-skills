---
title: Connected Apps
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

# Connected Apps

## Purpose

Validate OAuth connected app scope and user access.

## Reasoning Model

1. Map profiles/perm sets authorized for app.
2. Validate scope vs least privilege.
3. Test token and refresh flows at QA design level.

## Decision Rules

- Connected app scope expansion → API Security regression In.

## Cross-Links (Canonical Depth)

- [Integration Knowledge](../../knowledge/integration/README.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.17.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
