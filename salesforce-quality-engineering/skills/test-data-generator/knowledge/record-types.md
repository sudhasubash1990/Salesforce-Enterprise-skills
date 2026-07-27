---
title: Record Types
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

# Record Types

## Purpose

Align payloads to record types and business processes.

## Reasoning Model

1. Map persona journeys to record types.
2. Respect picklist value sets per record type.
3. Include negative: wrong record type.
4. Chain MIA when record type metadata changes.

## Decision Rules

- Wrong record type causing VR failures → document as data defect or config gap.

## Cross-Links (Canonical Depth)

- [Metadata Impact Analyzer](../../metadata-impact-analyzer/SKILL.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.20.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
