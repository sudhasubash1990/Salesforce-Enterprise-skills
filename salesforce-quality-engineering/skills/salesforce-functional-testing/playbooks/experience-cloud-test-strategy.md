---
title: Experience Cloud Test Strategy
module: Salesforce Quality Engineering
category: QE Specialized Skill Playbook
document_type: Playbook
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-functional-testing, experience-cloud-test-strategy]
---

# Experience Cloud Test Strategy

## Objective

Plan and execute functional testing for Experience Cloud portals covering authentication, self-service, Knowledge access, persona-based CRUD/FLS, and guest user restrictions.

## Inputs

- Portal requirements (customer portal, partner portal, public site)
- Experience Cloud configuration (pages, navigation, sharing sets)
- External user persona list with profiles, permission sets, and licenses
- Guest user profile configuration
- Integration points with Service Cloud / Sales Cloud

## Validation Workflow

1. Confirm authentication flows (login, registration, SSO, MFA, password reset)
2. Map self-service scenarios per persona (case creation, Knowledge search)
3. Design guest user restriction tests (what is and is not accessible)
4. Validate CRUD/FLS per external user profile and sharing set
5. Test navigation, search, and LWC component rendering
6. Verify file upload with size and type boundaries
7. Chain [PTA](../../permission-testing-agent/SKILL.md) for CRUD/FLS matrix per external persona
8. Chain [PWR](../../playwright-review/SKILL.md) for UI automation of portal flows

## Decision Points

| Decision | Criteria |
|----------|----------|
| Include guest user testing | Public site or unauthenticated pages exist |
| Include SSO testing | SSO configured for external users |
| Include negative authorization | Multiple personas with different access levels |
| Chain PWR for UI automation | Portal flows require browser-level validation |

## Expected Results

- Authentication flows complete successfully for all configured methods
- Guest users can access only designated public content
- External users see only their own records (or shared records per sharing set)
- Self-service case creation persists correctly with proper ownership
- Knowledge articles respect channel visibility settings

## Anti-Patterns

- Testing portal only with internal admin user
- Skipping guest user / unauthenticated access validation
- Assuming internal sharing rules apply to external users

## Related Documents

- [Experience Cloud Testing Knowledge](../knowledge/experience-cloud-testing.md)
- [SKILL.md](../SKILL.md)
