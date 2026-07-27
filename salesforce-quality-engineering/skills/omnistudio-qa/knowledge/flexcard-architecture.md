---
title: FlexCard Architecture
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

# FlexCard Architecture

## Purpose

Assess FlexCard rendering, actions, binding, and child-card patterns.

## Reasoning Model

1. Verify data source and refresh strategy.
2. Validate action targets (OS, IP, navigation).
3. Check conditional visibility and pagination.
4. Flag heavy nested cards for performance risk (label assumptions).

## Decision Rules

- Action opens wrong OS version → Critical functional defect.
- PII on card without FLS check → Chain PTA.

## Cross-Links (Canonical Depth)

- [OmniStudio Cloud Knowledge](../../knowledge/clouds/omnistudio.md)
- [Performance Best Practices](performance-best-practices.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.22.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
