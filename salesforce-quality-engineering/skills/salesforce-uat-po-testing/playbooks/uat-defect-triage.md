---
title: UAT Defect Triage Playbook
module: Salesforce Quality Engineering
category: QE Specialized Skill Playbook
document_type: playbook
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-uat-po-testing, defect-triage]
---

# UAT Defect Triage Playbook

## When to Use

During UAT execution when defects are found and need classification, prioritization, and resolution tracking from a business-impact perspective.

## Business-Impact Defect Classification

| Severity | Business Impact | Example | UAT Action |
|----------|----------------|---------|------------|
| **Sev-1 Critical** | Business process completely blocked; no workaround | Customer cannot submit an order | Stop affected scenarios; escalate immediately |
| **Sev-2 High** | Major business impact; workaround exists but is painful | Approval emails delayed by 4 hours | Continue with workaround; escalate for fix |
| **Sev-3 Medium** | Minor business inconvenience; easy workaround | Report column header shows internal name | Log; fix before go-live if possible |
| **Sev-4 Low** | Cosmetic; no business process impact | Button alignment slightly off | Log; fix post-go-live |

## Triage Steps

### Step 1 — Understand the Business Impact

Ask the UAT tester:
- "What were you trying to do when this happened?"
- "Can you complete the business process another way?"
- "How many users would be affected by this?"
- "Is this blocking other scenarios?"

### Step 2 — Classify Severity

Use the business-impact table above. Do not classify based on technical root cause — classify based on business effect.

### Step 3 — Decide Action

| Decision | When |
|----------|------|
| **Fix now** | Sev-1 or Sev-2 blocking critical scenarios |
| **Fix before go-live** | Sev-2 with workaround, Sev-3 affecting user experience |
| **Fix post-go-live** | Sev-4, Sev-3 with minimal impact |
| **Defer to next release** | Enhancement requests discovered during UAT |
| **Not a defect** | Working as designed; update documentation or training |

### Step 4 — Log in ADO

Chain to ADO Defect Logger (ADL) with:
- Business-language title (not technical)
- Business impact description
- Affected business process and persona
- Steps to reproduce in business terms
- Expected vs. actual business outcome
- Evidence (screenshots, data)

### Step 5 — Track and Re-test

- Track defect resolution status daily
- Re-test fixed defects against the original business scenario
- Update AC traceability matrix with re-test results

## Outputs

- Defect triage log with business-impact classification
- Daily defect summary for UAT status report
- Defect resolution tracking for Go/No-Go assessment
