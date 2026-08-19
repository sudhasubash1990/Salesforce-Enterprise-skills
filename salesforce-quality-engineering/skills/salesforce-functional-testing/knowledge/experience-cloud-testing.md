---
title: Experience Cloud Functional Testing
module: Salesforce Quality Engineering
category: QE Specialized Skill Guide
document_type: Guide
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-functional-testing, experience-cloud-testing]
---

# Experience Cloud Functional Testing

## Purpose

Provide testing guidance for Experience Cloud portals — login, registration, guest access, case creation, Knowledge access, file upload, search, navigation, LWC exposure, persona access, CRUD/FLS, record visibility, and negative authorization.

## Business Context

Experience Cloud exposes Salesforce data to external users — customers, partners, and guests. Functional defects in access control, self-service flows, or data visibility create security and usability risks. Testing must validate both functional correctness and access boundaries.

## Assessment Criteria

- Authentication flows verified for login, registration, SSO, and password reset
- Guest user access restricted to intended objects and fields only
- Self-service flows (case creation, Knowledge search) functional across personas
- CRUD/FLS enforced per external user profile and sharing set

## Key Areas

- **Authentication:** Login, registration, SSO, MFA, password reset, session management
- **Guest User:** Public access limits, guest profile restrictions, unauthenticated paths
- **Self-Service Case Creation:** Form fields, file attachment, confirmation, case visibility
- **Knowledge Access:** Article visibility by channel, search results, article feedback
- **File Upload:** Size limits, file type restrictions, virus scan, storage location
- **Search:** Global search, filtered search, search scope per persona
- **Navigation:** Menu structure, page access, redirect rules, 404 handling
- **LWC Exposure:** Component rendering, data binding, error states, responsive behavior
- **Record Visibility:** Sharing sets, sharing rules, org-wide defaults, owner-based visibility
- **Negative Authorization:** Attempting access to restricted records, objects, fields, pages

## Decision Framework

| Scenario | Testing Focus |
|----------|---------------|
| Customer portal launch | Login + self-service + case creation + Knowledge |
| Partner portal | Authentication + record sharing + collaboration |
| Public-facing site | Guest user restrictions + SEO + performance |
| Community migration | Feature parity + data visibility + URL redirects |

## Best Practices

- Test guest user access with both authenticated and unauthenticated sessions
- Verify CRUD/FLS per external user profile — chain [PTA](../../permission-testing-agent/SKILL.md)
- Test self-service case creation with file attachments at size boundary
- Validate Knowledge article visibility respects channel assignment
- Test navigation with expired session to verify redirect behavior

## Anti-Patterns

- Testing only authenticated paths — missing guest user attack surface
- Assuming internal CRUD/FLS applies to external users
- Skipping negative authorization scenarios (accessing other users' cases)

## Related Documents

- [Experience Cloud Knowledge](../../../knowledge/clouds/experience-cloud.md)
- [SKILL.md](../SKILL.md)
- [Permission Testing Agent](../../permission-testing-agent/SKILL.md)
