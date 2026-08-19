---
title: Experience Cloud Case Creation — Example
module: Salesforce Quality Engineering
category: QE Specialized Skill Example
document_type: Example
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-functional-testing, experience-cloud-case-creation]
---

# Experience Cloud Portal Case Creation

## Business Scenario

Customers log into a self-service portal built on Experience Cloud to create support cases, attach files, and track case status. Guest users can view Knowledge articles but cannot create cases. Authenticated users see only their own cases.

## Cloud

Experience Cloud (with Service Cloud backend)

## Objects

Case, CaseComment, ContentVersion (file), Knowledge__kav, User (external)

## Test Scenarios

### Positive

| ID | Scenario | Expected Result |
|----|----------|-----------------|
| EC-P01 | Authenticated customer creates case via portal form | Case created, Status = New, ContactId = logged-in user's Contact |
| EC-P02 | Customer attaches file to case | ContentVersion linked to case, file accessible |
| EC-P03 | Customer views own case list | Only cases owned by or related to the customer displayed |
| EC-P04 | Customer searches Knowledge articles | Articles with portal channel visibility returned |

### Negative

| ID | Scenario | Expected Result |
|----|----------|-----------------|
| EC-N01 | Guest user attempts to create case | Case creation form not accessible, redirect to login |
| EC-N02 | Customer attempts to view another customer's case by URL manipulation | Access denied or record not found |
| EC-N03 | Customer submits case without required fields | Validation error displayed on portal form |

### Boundary

| ID | Scenario | Expected Result |
|----|----------|-----------------|
| EC-B01 | File upload at maximum allowed size (e.g., 10 MB) | File uploaded successfully |
| EC-B02 | File upload exceeding maximum size | Error message displayed, file not uploaded |
| EC-B03 | Session timeout during case creation | Redirect to login, unsaved data lost (expected behavior) |

### Permission

| ID | Scenario | Expected Result |
|----|----------|-----------------|
| EC-PM01 | Guest user navigates to restricted page | Access denied or redirect to login |
| EC-PM02 | Customer attempts to delete own case | Delete action not available per profile |

Chain [PTA](../../permission-testing-agent/SKILL.md) for full external user CRUD/FLS matrix.

## Expected Results

Portal functionality verified for authenticated, guest, and negative-authorization paths.

## Chain Skills

- [PTA](../../permission-testing-agent/SKILL.md) — external user CRUD/FLS and sharing set validation
- [PWR](../../playwright-review/SKILL.md) — browser-level portal UI automation
- [TDG](../../test-data-generator/SKILL.md) — create prerequisite external user, Account, Contact

## Related Documents

- [Experience Cloud Testing Knowledge](../knowledge/experience-cloud-testing.md)
- [SKILL.md](../SKILL.md)
