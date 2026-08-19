---
title: Security Test Assessment Prompt
module: Salesforce Quality Engineering
category: QE Specialized Skill Prompts
document_type: Prompt
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-specialized-testing, security-testing, prompt]
---

# Security Test Assessment Prompt

## Usage

Use when the primary concern is security testing scope for a Salesforce implementation.

## Prompt

```
Assess the security testing scope for the following Salesforce implementation:

**Security context:**
- Objects affected: [list objects]
- Personas: [list personas/profiles]
- Sharing model: [OWD, sharing rules, role hierarchy]
- Experience Cloud: [yes/no — partner/customer/guest]
- API access: [connected apps, Named Credentials]
- Permission changes: [profiles, PSs, PSGs being modified]

**Produce:**
1. Security Assessment with CRUD, FLS, sharing, profile/PS, record visibility, guest user, API security scope
2. Chain recommendation to PTA for detailed test scenarios
3. Risk areas and open questions

Do not produce detailed test cases — chain to PTA. Label all assumptions.
```
