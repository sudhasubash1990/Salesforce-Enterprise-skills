---
title: Salesforce Security Testing
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: Knowledge Article
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-specialized-testing, security-testing]
---

# Salesforce Security Testing

## Purpose

Reference for assessing Salesforce security testing scope within SST. For detailed security test scenario generation, chain to [PTA](../../permission-testing-agent/SKILL.md).

## Security Testing Layers

| Layer | What to Assess | Key Artifacts |
|-------|---------------|---------------|
| **CRUD** | Object-level Create, Read, Update, Delete per profile/PS | Profile metadata, PS assignments |
| **FLS** | Field-level read/edit per profile/PS | Field permissions, sensitive fields |
| **Sharing** | OWD, role hierarchy, sharing rules, restriction/scoping rules | Sharing settings, role tree |
| **Profiles** | Standard vs custom, login restrictions, IP ranges | Profile XML, session settings |
| **Permission Sets / PSGs** | Grants beyond profile, PSG composition | PS metadata, PSG membership |
| **Record Visibility** | Ownership, manual shares, territory, queues | Sharing records, territory model |
| **Guest User** | Experience Cloud unauthenticated access, guest profile | Guest user profile, sharing sets |
| **API Security** | Connected apps, OAuth scopes, Named Credentials | Connected app settings, OAuth config |

## Common Risk Areas

- Overly permissive OWD (Public Read/Write on sensitive objects)
- Guest user with excessive object access
- Permission sets granting "Modify All" without justification
- API-only users with broader access than integration requires
- Missing restriction rules on Experience Cloud objects

## Chain Rule

SST identifies security testing as a required dimension → PTA produces the detailed test scenarios with negative paths, regression scope, and SOQL validation.

## Related

- [../../../knowledge/security/](../../../knowledge/security/) — Security encyclopedia
- [PTA SKILL.md](../../permission-testing-agent/SKILL.md)
- [Specialized Testing Model](specialized-testing-model.md)
