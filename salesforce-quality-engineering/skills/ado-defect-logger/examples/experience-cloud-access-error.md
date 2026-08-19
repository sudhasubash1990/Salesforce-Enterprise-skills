---
title: "Example: Experience Cloud Access Error Defect"
module: Salesforce Quality Engineering
category: QE Specialized Skill Example
document_type: Example
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [ado-defect-logger, example, experience-cloud]
---

# Example: Experience Cloud Access Error Defect

## Input (Tester Report)

> "Partner users on the Partner Community portal cannot see the 'Submit Order' button on the Order detail page. They get 'Insufficient Privileges' when trying to access the page directly via URL. Internal users can see it fine."

**Environment:** UAT Sandbox (SFUAT-01), Partner Community user with Partner Sales profile

## 1. Intent

Log a defect for an Experience Cloud permission/visibility issue affecting partner users.

## 2. Context

| Dimension | Value |
|-----------|-------|
| Project | Partner Portal Implementation |
| Sprint | Sprint 11 |
| Salesforce Cloud | Experience Cloud |
| Component | Order detail page, Submit Order button |
| Environment | UAT Sandbox SFUAT-01 |
| Reporter | UAT Tester |
| Date reported | 2026-08-19 |

## 3. Defect Analysis

| Dimension | Assessment |
|-----------|------------|
| Is this a defect? | Yes — partner users should see Submit Order per requirement |
| Title | [Experience Cloud] Partner users cannot see Submit Order button — Insufficient Privileges |
| Category | Security / Permission / Experience Cloud |
| Severity | 2-High — Core partner workflow blocked |
| Priority | 1-Critical — Blocks UAT sign-off for Partner Portal |
| Reproducibility | Always (all partner users affected) |
| Business impact | Partners cannot submit orders via portal, revenue impact |
| Technical impact | Permission model gap for Experience Cloud guest/partner profiles |

## 4. ADO Defect

### Title

`[Experience Cloud] Partner users cannot see Submit Order button — Insufficient Privileges`

### Severity: 2-High | Priority: 1

### Repro Steps

1. Log in to Partner Community portal (SFUAT-01) as a Partner Sales profile user
2. Navigate to an existing Order record via the Orders tab
3. Observe the Order detail page — note the "Submit Order" button is not visible
4. Attempt to access the Submit Order action via direct URL: `/lightning/action/Order.Submit_Order`
5. Observe the "Insufficient Privileges" error message

### Expected Result

Partner Sales profile users see the "Submit Order" button on the Order detail page and can execute the action.

### Actual Result

The "Submit Order" button is not visible. Direct URL access returns "Insufficient Privileges." Internal users with the same page layout can see and use the button.

### Evidence

| Type | Reference |
|------|-----------|
| Error message | "Insufficient Privileges" on direct URL access |
| Comparison | Internal Sales Rep profile can see the button on the same Order |
| User profile | Partner Sales (Experience Cloud profile) |

## 5. Root Cause Hypothesis

- **Category:** Permission
- **Hypothesis:** The Partner Sales profile or associated Permission Set is missing object-level (CRUD) or field-level security (FLS) access to the Submit_Order action or the underlying Order fields required by the action. Alternatively, the page layout assigned to the Partner Sales profile does not include the button.
- **Confidence:** High
- **Evidence needed:** Compare Profile/Permission Set for Partner Sales vs internal Sales Rep; check page layout assignment for Order by profile; check Experience Cloud page component visibility rules

## 6. Regression Impact

- **Regression?** Unknown — first UAT cycle for partner portal
- **Release impact:** Blocks UAT sign-off for Partner Portal go-live

## 7. Quality Gates

All gates pass.

## 8. Dependencies

| Type | Description |
|------|-------------|
| Upstream requirement | US-078: Partners can submit orders via portal |
| Blocked by | Permission Set configuration for Partner Sales profile |

## 9. Recommended Next Actions

1. Admin to review Partner Sales profile CRUD on Order and related objects
2. Check page layout assignment for Order by record type and profile
3. Review Experience Cloud page component visibility settings
4. After fix, test with multiple partner user accounts

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.25.0 | 2026-08-19 | QE Practice Lead | Initial creation |
