---
title: Salesforce Security Architecture
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

# Salesforce Security Architecture

## Purpose

Map business process to layered security model before test design.

## Reasoning Model

1. Identify personas and channels (UI, API, community).
2. Layer CRUD → FLS → sharing → record access.
3. Note automation running system vs user mode.
4. Cross-link impacted metadata from MIA if present.

## Decision Rules

- Never skip sharing when OWD is Private.
- Community/guest paths are separate validation packs.

## Cross-Links (Canonical Depth)

- [Security Knowledge](../../knowledge/security/README.md)
- [Security Model BA](../../../salesforce-business-analyst/knowledge/security-model.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.17.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
