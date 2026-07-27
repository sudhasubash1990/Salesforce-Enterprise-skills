---
title: FSL Deployment Strategy
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

# FSL Deployment Strategy

## Purpose

Align FSL metadata and config deploys with QA gates.

## Reasoning Model

1. Inventory FSL settings and permission sets.
2. Chain MIA for package.xml FSL components.
3. Require mobile regression after policy/permission change.

## Decision Rules

- Policy deploy without scheduling regression → No-Go.

## Cross-Links (Canonical Depth)

- [Metadata Impact Analyzer](../../metadata-impact-analyzer/SKILL.md)
- [Release Readiness](../../knowledge/release/release-readiness.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.19.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
