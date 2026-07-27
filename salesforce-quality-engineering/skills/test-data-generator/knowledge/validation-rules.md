---
title: Validation Rules
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

# Validation Rules

## Purpose

Respect VRs for positive data; intentionally violate only for negative packs.

## Reasoning Model

1. List known VRs in scope or mark TBC.
2. Design compliant happy-path rows.
3. Design explicit negative rows with expected error.
4. Chain MIA when VR deploy changes payloads.

## Decision Rules

- Positive pack that fails known VR → Fail.

## Cross-Links (Canonical Depth)

- [Data Validation](../../knowledge/data/data-validation.md)
- [Metadata Impact Analyzer](../../metadata-impact-analyzer/SKILL.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.20.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
