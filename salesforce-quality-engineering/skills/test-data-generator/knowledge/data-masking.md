---
title: Data Masking
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

# Data Masking

## Purpose

Guide masking when partial sandbox clones are unavoidable.

## Reasoning Model

1. Identify PII/sensitive fields.
2. Recommend masking vs regenerate synthetic.
3. Preserve referential integrity after mask.
4. Document residual risk.

## Decision Rules

- Masking without integrity plan → Fail.

## Cross-Links (Canonical Depth)

- [Data Masking](../../knowledge/data/data-masking.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.20.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
