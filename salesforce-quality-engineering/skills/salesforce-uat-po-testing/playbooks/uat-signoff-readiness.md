---
title: UAT Sign-off Readiness Playbook
module: Salesforce Quality Engineering
category: QE Specialized Skill Playbook
document_type: playbook
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-uat-po-testing, signoff-readiness]
---

# UAT Sign-off Readiness Playbook

## When to Use

When UAT execution is nearing completion and you need to assess readiness for business sign-off and produce a Go/No-Go recommendation.

## Steps

### Step 1 — Compile Execution Summary

1. Total scenarios: executed vs. planned
2. Results: Passed / Failed / Blocked / Not Executed
3. Persona coverage: which roles were tested
4. Business process coverage: which journeys were validated

### Step 2 — Review Exit Criteria

For each exit criterion defined in the UAT plan:
- Is it met? (Yes / No / Partial)
- If not met, what is the gap and business impact?

### Step 3 — Assess Open Defects

1. List all open defects by severity
2. For each Sev-1 / Sev-2: is there a fix timeline or accepted workaround?
3. Determine: do open defects block Go?

### Step 4 — Validate AC Traceability

1. Review the AC-to-scenario-to-evidence matrix
2. Identify any AC without traced evidence
3. Flag gaps to the business owner

### Step 5 — Document Residual Risks

For items not fully resolved:
- Business impact if deployed as-is
- Mitigation or workaround plan
- Post-go-live fix timeline
- Risk acceptance required from business owner

### Step 6 — Produce Recommendation

Based on evidence, recommend one of:

| Recommendation | Criteria |
|----------------|----------|
| **Go** | All exit criteria met; no open Sev-1/2; AC fully traced |
| **Conditional Go** | Minor gaps with accepted risk; workarounds in place |
| **No-Go** | Critical gaps, open Sev-1 defects, or insufficient coverage |

### Step 7 — Present to Business Owner

1. Walk through the sign-off document
2. Highlight residual risks requiring acceptance
3. Obtain formal sign-off (or document No-Go decision)

## Outputs

- UAT sign-off document (use templates/uat-signoff-template.md)
- Go/No-Go recommendation with evidence
- Residual risk register
- Post-go-live validation plan (if Conditional Go)
