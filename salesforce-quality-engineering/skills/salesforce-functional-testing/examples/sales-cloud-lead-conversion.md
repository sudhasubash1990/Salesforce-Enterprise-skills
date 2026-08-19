---
title: Sales Cloud Lead Conversion — Example
module: Salesforce Quality Engineering
category: QE Specialized Skill Example
document_type: Example
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-functional-testing, sales-cloud-lead-conversion]
---

# Sales Cloud Lead Conversion

## Business Scenario

Sales representatives qualify leads and convert them to Account, Contact, and Opportunity records. Conversion must handle both new record creation and matching to existing Accounts/Contacts. Custom field mappings transfer lead data to the converted records.

## Cloud

Sales Cloud

## Objects

Lead, Account, Contact, Opportunity, CampaignMember

## Test Scenarios

### Positive

| ID | Scenario | Expected Result |
|----|----------|-----------------|
| LC-P01 | Convert qualified lead — no existing Account | New Account, Contact, and Opportunity created |
| LC-P02 | Convert lead matching existing Account by Company name | Lead merged into existing Account, new Contact created |
| LC-P03 | Convert lead with Campaign association | CampaignMember status updated to Converted |
| LC-P04 | Custom field mapping transfers Lead.Industry__c to Account.Industry | Field value matches post-conversion |

### Negative

| ID | Scenario | Expected Result |
|----|----------|-----------------|
| LC-N01 | Attempt conversion without required Opportunity Name | Validation error, conversion blocked |
| LC-N02 | Convert lead with Status = Disqualified | Conversion blocked per validation rule |
| LC-N03 | Non-sales profile attempts lead conversion | Convert button not visible or action blocked |

### Boundary

| ID | Scenario | Expected Result |
|----|----------|-----------------|
| LC-B01 | Convert lead with maximum field lengths populated | All fields transfer without truncation |
| LC-B02 | Bulk convert 200 leads simultaneously | All conversions complete within governor limits |

### Permission

| ID | Scenario | Expected Result |
|----|----------|-----------------|
| LC-PM01 | Marketing user (read-only Lead) attempts conversion | Action blocked |

## Expected Results

Post-conversion records verified for field mapping accuracy, ownership, and record type assignment.

## Chain Skills

- [SOVA](../../soql-validation-assistant/SKILL.md) — verify Account, Contact, Opportunity fields post-conversion
- [TDG](../../test-data-generator/SKILL.md) — create prerequisite Lead and Account records
- [PTA](../../permission-testing-agent/SKILL.md) — conversion permission by profile

## Related Documents

- [Sales Cloud Testing Knowledge](../knowledge/sales-cloud-testing.md)
- [SKILL.md](../SKILL.md)
