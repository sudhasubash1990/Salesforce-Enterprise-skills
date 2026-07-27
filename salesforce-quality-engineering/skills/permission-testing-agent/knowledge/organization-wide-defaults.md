---
title: Organization Wide Defaults
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

# Organization Wide Defaults

## Purpose

Validate OWD impact on baseline access.

## Reasoning Model

1. Document OWD per object (Private, Public Read Only, etc.).
2. Predict sharing rule necessity from OWD.
3. Test default vs shared access.

## Decision Rules

- OWD tightening → integration service account review required.

## Cross-Links (Canonical Depth)

- [OWD](../../knowledge/security/organization-wide-defaults.md)
- [Sharing Security Testing](../../knowledge/sharing-security-testing.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.17.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
