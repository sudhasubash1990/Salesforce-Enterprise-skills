---
title: Service Cloud Case Creation — Example
module: Salesforce Quality Engineering
category: QE Specialized Skill Example
document_type: Example
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-functional-testing, service-cloud-case-creation]
---

# Service Cloud Case Creation

## Business Scenario

A customer service organization uses Service Cloud for case management. Cases are created via manual entry, Email-to-Case, and Web-to-Case. Assignment rules route cases to queues based on case origin and priority. Agents work cases in the Service Console.

## Cloud

Service Cloud

## Objects

Case, Account, Contact, Queue, EmailMessage, CaseComment

## Test Scenarios

### Positive

| ID | Scenario | Expected Result |
|----|----------|-----------------|
| SC-P01 | Create case manually with all required fields | Case saved with Status = New, assigned to correct queue |
| SC-P02 | Create case via Email-to-Case | Case created, EmailMessage attached, Contact matched |
| SC-P03 | Create case via Web-to-Case form | Case created with field mapping from web form |
| SC-P04 | Assignment rule routes High priority case to Tier 2 queue | Case Owner = Tier 2 Queue |

### Negative

| ID | Scenario | Expected Result |
|----|----------|-----------------|
| SC-N01 | Submit case without required Subject field | Validation error displayed, case not saved |
| SC-N02 | Email-to-Case with unrecognized sender | Case created with no Contact association |
| SC-N03 | Web-to-Case with HTML injection in description | Input sanitized, case created without script execution |

### Boundary

| ID | Scenario | Expected Result |
|----|----------|-----------------|
| SC-B01 | Case description at 32,000 character limit | Case saved successfully |
| SC-B02 | Email-to-Case with 25 MB attachment | Attachment rejected per org file size limit |

### Permission

| ID | Scenario | Expected Result |
|----|----------|-----------------|
| SC-PM01 | Read-only user attempts to create case | Create button not visible or action blocked |

Chain [PTA](../../permission-testing-agent/SKILL.md) for full CRUD/FLS matrix.

## Expected Results

All scenarios produce measurable, verifiable outcomes as listed above.

## Chain Skills

- [PTA](../../permission-testing-agent/SKILL.md) — permission matrix for case access
- [SOVA](../../soql-validation-assistant/SKILL.md) — verify Case record fields via SOQL
- [TDG](../../test-data-generator/SKILL.md) — create prerequisite Account and Contact records

## Related Documents

- [Service Cloud Testing Knowledge](../knowledge/service-cloud-testing.md)
- [SKILL.md](../SKILL.md)
