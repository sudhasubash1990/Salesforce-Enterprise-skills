---
title: Actions
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: Knowledge Article
version: 0.18.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [agentforce-testing, knowledge]
---

# Actions

## Purpose

Validate agent-invoked actions and side effects.

## Reasoning Model

1. Inventory actions (Flow, Apex, API).
2. Map inputs/outputs and failure modes.
3. If action mutates records → chain Metadata Impact Analyzer.

## Decision Rules

- Write actions require backend SOQL and permission validation.

## Cross-Links (Canonical Depth)

- [Agentforce Cloud Knowledge](../../knowledge/clouds/agentforce.md)
- [Metadata Impact Analyzer](../../metadata-impact-analyzer/SKILL.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.18.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
