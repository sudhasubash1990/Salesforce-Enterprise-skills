---
title: Flow Actions
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

# Flow Actions

## Purpose

Validate Flow-backed agent actions.

## Reasoning Model

1. Confirm Flow version and entry criteria.
2. Test success, fault, and partial paths.
3. Verify agent messaging on Flow faults.

## Decision Rules

- Inactive Flow version → Fail deployment readiness.

## Cross-Links (Canonical Depth)

- [Automation Knowledge](../../knowledge/automation/README.md)
- [Metadata Impact Analyzer](../../metadata-impact-analyzer/SKILL.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.18.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
