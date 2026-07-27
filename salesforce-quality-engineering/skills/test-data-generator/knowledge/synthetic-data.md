---
title: Synthetic Data
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

# Synthetic Data

## Purpose

Generate realistic but non-identifying values by default.

## Reasoning Model

1. Use realistic formats (email, phone, address) that are clearly synthetic.
2. Avoid names/emails of real customers.
3. Document synthetic markers (e.g. @example.test).
4. Industry flavor without inventing regulatory claims.

## Decision Rules

- Default = synthetic. Production copy only via approved masking program.

## Cross-Links (Canonical Depth)

- [PII Considerations](../../knowledge/data/pii-considerations.md)
- [GDPR Awareness](../../knowledge/data/gdpr-awareness.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.20.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
