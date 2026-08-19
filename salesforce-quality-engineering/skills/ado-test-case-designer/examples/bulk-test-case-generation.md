---
title: "Example: Bulk Test Case Generation"
module: Salesforce Quality Engineering
category: QE Specialized Skill Example
document_type: Example
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [ado-test-case-designer, example, bulk]
---

# Example: Bulk Test Case Generation

## Input — Epic with Multiple User Stories

**Epic:** E-010 — Customer Onboarding Automation

| Story ID | Title | Priority |
|----------|-------|----------|
| US-050 | Create Account with duplicate check | P1 |
| US-051 | Create Contact linked to Account | P1 |
| US-052 | Auto-assign Account to Territory | P2 |
| US-053 | Send Welcome Email on Account creation | P2 |

## Output — Test Suite Structure

```
Test Plan: Customer Onboarding Automation (E-010)
 ├── Suite: Account Creation (US-050)
 │    ├── TC-001: Create Account — happy path (all required fields)
 │    ├── TC-002: Create Account — duplicate detected (matching Name + BillingCity)
 │    ├── TC-003: Create Account — missing required field (Account Name blank)
 │    ├── TC-004: Create Account — boundary (Account Name 255 chars)
 │    └── TC-005: Create Account — permission (Read-Only profile)
 ├── Suite: Contact Creation (US-051)
 │    ├── TC-006: Create Contact linked to Account — happy path
 │    ├── TC-007: Create Contact — no Account selected (validation)
 │    ├── TC-008: Create Contact — duplicate Contact on same Account
 │    └── TC-009: Create Contact — permission (Marketing User profile)
 ├── Suite: Territory Assignment (US-052)
 │    ├── TC-010: Auto-assign Territory — criteria match (BillingState = "CA")
 │    ├── TC-011: Auto-assign Territory — no criteria match (fallback)
 │    └── TC-012: Auto-assign Territory — reassignment on Address change
 ├── Suite: Welcome Email (US-053)
 │    ├── TC-013: Welcome Email sent on Account creation — happy path
 │    ├── TC-014: Welcome Email — Contact has no email address
 │    └── TC-015: Welcome Email — email template merge fields populated
 └── Suite: E2E — Cross-Story
      ├── TC-016: Full onboarding flow (Account → Contact → Territory → Email)
      └── TC-017: Onboarding with duplicate Account (flow interruption)
```

## Summary Statistics

| Metric | Count |
|--------|-------|
| User stories in scope | 4 |
| Test cases generated | 17 |
| Positive scenarios | 6 |
| Negative scenarios | 6 |
| Boundary scenarios | 1 |
| Permission scenarios | 2 |
| E2E scenarios | 2 |
| Coverage gaps | 0 |

## Consolidated Traceability Matrix

| Story | Test Cases | Coverage |
|-------|-----------|----------|
| US-050 | TC-001 – TC-005 | Full |
| US-051 | TC-006 – TC-009 | Full |
| US-052 | TC-010 – TC-012 | Full |
| US-053 | TC-013 – TC-015 | Full |
| E2E | TC-016 – TC-017 | Full |

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.25.0 | 2026-08-19 | QE Practice Lead | Initial creation |
