---
title: Persona and Role-Based Testing
module: Salesforce Quality Engineering
category: QE Specialized Skill Guide
document_type: Guide
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-functional-testing, persona-based-testing]
---

# Persona and Role-Based Testing

## Purpose

Define the persona-based and role-based testing model for Salesforce functional testing — how to test per profile, permission set, role hierarchy, and sharing model.

## Business Context

Salesforce security is multi-layered: profiles control object/field access, permission sets grant incremental access, role hierarchy controls record visibility, and sharing rules extend access. Functional tests must verify that each persona can perform exactly their permitted actions — no more, no less.

## Assessment Criteria

- Persona matrix defined with profile, permission sets, role, and expected access
- Positive scenarios confirm permitted actions succeed
- Negative scenarios confirm restricted actions are blocked
- Cross-persona scenarios verify record visibility boundaries

## Key Areas

### Persona Matrix Structure

| Persona | Profile | Permission Sets | Role | Key Permissions |
|---------|---------|-----------------|------|-----------------|
| Service Agent | Service Cloud User | Case Management | Service Rep | Case CRUD, Knowledge Read |
| Service Manager | Service Cloud User | Case Management, Reports | Service Manager | Case CRUD + Delete, Reports |
| Sales Rep | Sales Cloud User | Opportunity Management | Sales Rep | Lead/Opp CRUD, Forecast |
| Portal Customer | Customer Community User | Community Base | — | Own Cases, Knowledge Read |
| Guest User | Guest Profile | — | — | Knowledge Read only |

### Testing Dimensions

- **Positive persona:** Verify permitted CRUD operations succeed
- **Negative persona:** Verify restricted operations show appropriate error / no access
- **Cross-persona:** Verify record created by Persona A has expected visibility to Persona B
- **Escalation persona:** Verify manager override / escalation access works correctly

## Decision Framework

| Signal | Decision |
|--------|----------|
| Single persona, single object | Basic positive + negative CRUD |
| Multiple personas, shared records | Add cross-persona visibility scenarios |
| External users involved | Mandatory negative authorization + guest user scenarios |
| Role hierarchy in scope | Test record visibility at each hierarchy level |

## Best Practices

- Build persona matrix before writing scenarios — chain [PTA](../../permission-testing-agent/SKILL.md) for CRUD/FLS detail
- Test with actual profile/permission set combinations — not System Administrator
- Include "persona cannot" scenarios for every "persona can" scenario
- Verify sharing rule behavior with org-wide default set to Private

## Anti-Patterns

- Testing only with System Administrator profile
- Assuming role hierarchy grants field-level access (it does not)
- Skipping guest user / unauthenticated persona testing
- Conflating profile-level and permission-set-level access in test results

## Related Documents

- [SKILL.md](../SKILL.md)
- [Permission Testing Agent](../../permission-testing-agent/SKILL.md)
- [Experience Cloud Testing](experience-cloud-testing.md)
