---
title: Sharing Keywords
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

# Sharing Keywords

## Purpose

Interpret with sharing, without sharing, inherited sharing for test scope.

## Reasoning Model

1. Map keyword to class/trigger visibility behavior.
2. Design tests for records created by each keyword path.
3. Identify false positives in automation tests.

## Decision Rules

- inherited sharing — default for most triggers; still validate owner.

## Cross-Links (Canonical Depth)

- [Apex Security](apex-security.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.17.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
