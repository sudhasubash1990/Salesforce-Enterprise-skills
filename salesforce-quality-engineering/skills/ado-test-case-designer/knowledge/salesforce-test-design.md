---
title: Salesforce Test Design Considerations
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: Knowledge
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [ado-test-case-designer, salesforce-test-design]
---

# Salesforce Test Design Considerations

Platform-specific test design guidance for generating Salesforce-aware ADO test cases.

## Objects & Fields

| Consideration | Test Cases To Generate |
|---------------|----------------------|
| Standard vs. custom objects | Verify CRUD on both; custom object API names in test data |
| Required fields | Positive: all required filled; Negative: each required field blank |
| Field types (text, number, date, picklist, lookup, formula) | Type-specific boundary and validation tests |
| Field dependencies | Controlling → dependent picklist combinations |
| Field history tracking | Verify history records for tracked fields after update |
| Encrypted fields | Verify masking in UI, unmasked for authorized profiles |

## Record Types

| Consideration | Test Cases To Generate |
|---------------|----------------------|
| Page layout per record type | Verify correct layout renders per RT |
| Picklist values per RT | Only valid picklist values appear for each RT |
| Business process per RT | Correct stages/statuses available per RT |
| RT assignment on create | Default RT based on profile; RT selection if multiple available |
| RT change | Verify allowed RT changes and field re-validation |

## Profiles, Permission Sets & PSGs

| Consideration | Test Cases To Generate |
|---------------|----------------------|
| Object CRUD per profile | Create/Read/Update/Delete per object per profile |
| Field-level security | Visible/read-only/hidden per field per profile |
| Tab visibility | Verify tab access per profile |
| Permission set stacking | Aggregate permissions from multiple PS |
| PSG with muting | Verify muting PS removes specific permissions |
| Login IP/hour restrictions | Access denied outside allowed range |

## Sharing Model

| Consideration | Test Cases To Generate |
|---------------|----------------------|
| OWD settings | Private: owner-only access; Public Read/Write: all access |
| Role hierarchy | Manager sees subordinate records |
| Sharing rules (criteria/owner-based) | Records shared when criteria met |
| Manual sharing | Ad hoc sharing grants/revokes |
| Apex managed sharing | Programmatic sharing record creation |
| Teams (Account/Opportunity) | Team member access levels |

## Validation Rules

| Consideration | Test Cases To Generate |
|---------------|----------------------|
| Rule fires on create | Submit invalid data → verify error message |
| Rule fires on update | Modify to invalid state → verify block |
| Rule bypass scenarios | System admin, integration user bypass |
| Cross-object validation | Related record state affects validation |
| Error message accuracy | Exact error text matches specification |

## Flows

| Flow Type | Test Cases To Generate |
|-----------|----------------------|
| Screen Flow | Input screens, navigation, fault paths, conditional visibility |
| Record-Triggered (before) | Field defaults, validation, cross-object updates |
| Record-Triggered (after) | Child record creation, callouts, platform events |
| Scheduled Flow | Batch processing, criteria matching, time-based actions |
| Autolaunched | Invoked from other flows/Apex, input/output variables |
| Fault paths | Error handling, retry logic, admin notification |

## Apex Triggers & Classes

| Consideration | Test Cases To Generate |
|---------------|----------------------|
| Before triggers | Field modification, validation, default values |
| After triggers | Related record updates, callouts, events |
| Bulk patterns | Insert/update 200+ records — verify no governor limit breach |
| Governor limits | SOQL 101, DML 150, CPU timeout, heap size |
| Mixed DML | Setup + non-setup object in same transaction |
| Exception handling | Try/catch behavior, error message propagation |

## LWC Components

| Consideration | Test Cases To Generate |
|---------------|----------------------|
| Component rendering | Correct display based on record data |
| Wire adapter | Data loading, error handling, refresh |
| Imperative calls | Apex method invocation, loading states, error states |
| User interaction | Button clicks, form input, navigation |
| Responsive design | Mobile vs. desktop rendering |
| Error states | Network failure, permission denied, no data |

## Integrations

| Consideration | Test Cases To Generate |
|---------------|----------------------|
| REST/SOAP callouts | Success response, error codes (400, 401, 404, 500), timeout |
| Platform events | Publish, subscribe, replay, high-volume |
| Change Data Capture | Event delivery for tracked objects |
| Outbound messages | Delivery, retry, failure notification |
| Named credentials | Authentication flow, token refresh |
| Middleware (MuleSoft, etc.) | Transformation, routing, error handling |

## Experience Cloud

| Consideration | Test Cases To Generate |
|---------------|----------------------|
| Guest user | Limited access, registration flow |
| Authenticated user | Portal-specific permissions, sharing sets |
| Sharing sets | Record access based on user-account relationship |
| Audience targeting | Component visibility per audience |
| SEO and caching | Public page rendering |

## Service Cloud Specifics

| Area | Test Cases To Generate |
|------|----------------------|
| Case lifecycle | Create → assign → escalate → resolve → close |
| Entitlements & milestones | SLA tracking, milestone violations |
| Knowledge articles | Publish, attach to case, feedback |
| Omni-Channel | Routing, capacity, presence, skill-based |
| Email-to-Case | Email parsing, threading, auto-response |

## Data Migration

| Consideration | Test Cases To Generate |
|---------------|----------------------|
| Record mapping | Source-to-target field mapping verification |
| Data transformation | Format conversion, default values, lookups |
| Validation post-load | Record counts, relationship integrity, field values |
| Duplicate handling | Duplicate rules, matching rules behavior |
| Rollback | Ability to reverse migration batch |

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.25.0 | 2026-08-19 | QE Practice Lead | Initial creation |
