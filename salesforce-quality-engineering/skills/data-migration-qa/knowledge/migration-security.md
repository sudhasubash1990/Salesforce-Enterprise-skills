---
title: Migration Security
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

# Migration Security

## Purpose

Assess CRUD/FLS, PII, masking, and audit field handling.

## Reasoning Model

1. Classify PII fields; prefer masked dry-run (TDG).
2. Validate CRUD/FLS for post-migrate personas (PTA).
3. Review encryption/audit field expectations.
4. Never claim GDPR certification — escalate Legal/Compliance.

## Decision Rules

- Production PII in dry-run artifacts → Critical escalate Security.

## Cross-Links (Canonical Depth)

- [PII Considerations](../../knowledge/data/pii-considerations.md)
- [GDPR Awareness](../../knowledge/data/gdpr-awareness.md)
- [Data Masking](../../knowledge/data/data-masking.md)
- [Permission Testing Agent](../../permission-testing-agent/SKILL.md)
- [Test Data Generator](../../test-data-generator/SKILL.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.23.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
