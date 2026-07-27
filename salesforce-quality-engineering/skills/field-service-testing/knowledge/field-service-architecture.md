---
title: Salesforce Field Service Architecture
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

# Salesforce Field Service Architecture

## Purpose

Map WO → SA → Resource → Territory → Policy layers before test design.

## Reasoning Model

1. Inventory core objects and personas (dispatcher, technician, crew).
2. Separate scheduling, mobile, inventory surfaces.
3. Confirm FSL license/features—do not invent capabilities.
4. Identify integrations (ERP inventory, GIS, Agentforce booking).

## Decision Rules

- UI-only WO tests are insufficient for FSL QA.
- Confirm edition before asserting optimization features.

## Cross-Links (Canonical Depth)

- [Field Service Cloud Knowledge](../../knowledge/clouds/field-service.md)
- [Enterprise Field Service](../../enterprise-quality/salesforce/field-service.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.19.0 | 2026-07-27 | QE Practice Lead | Initial capability knowledge |
