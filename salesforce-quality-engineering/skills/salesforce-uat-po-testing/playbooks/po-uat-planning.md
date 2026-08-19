---
title: PO UAT Planning Playbook
module: Salesforce Quality Engineering
category: QE Specialized Skill Playbook
document_type: playbook
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-uat-po-testing, uat-planning]
---

# PO UAT Planning Playbook

## When to Use

At the start of a UAT cycle — typically after SIT completion and before UAT execution begins.

## Inputs

- User stories with acceptance criteria
- Business process documentation (AS-IS / TO-BE)
- Stakeholder list and sign-off authority
- Release scope and timeline
- Environment and data readiness status

## Steps

### Step 1 — Identify Stakeholders and Governance

1. Confirm the business owner with sign-off authority
2. Identify UAT participants by persona / role
3. Establish the UAT communication cadence (daily stand-up, status reports)
4. Define escalation paths for blockers and critical defects

### Step 2 — Define UAT Scope

1. List all user stories / features in the release
2. For each, confirm: is this in UAT scope? (yes / no / partial)
3. Document out-of-scope items with rationale
4. Identify regression areas that need business re-validation

### Step 3 — Apply the 12 PO Questions

For each in-scope feature, work through the 12 PO questions (see SKILL.md). Document answers or flag as "open — needs business input."

### Step 4 — Define Entry and Exit Criteria

Use the UAT Framework (knowledge/uat-framework.md) as a starting point. Tailor entry/exit criteria to the project context.

### Step 5 — Build the UAT Schedule

1. Allocate time per business process area
2. Schedule scenario walkthroughs with business users before execution
3. Build in buffer for defect retesting
4. Set the Go/No-Go meeting date

### Step 6 — Confirm Data and Environment

1. Verify UAT environment mirrors production configuration
2. Confirm test data is loaded and realistic
3. Chain to Test Data Generator (TDG) if data gaps exist

## Outputs

- UAT Strategy document
- UAT Scope matrix
- Entry / Exit Criteria
- UAT Schedule
- Stakeholder RACI for UAT

## Quality Gate

- [ ] All 12 PO questions addressed or flagged
- [ ] Every in-scope feature has at least one business scenario
- [ ] Entry criteria are achievable before planned UAT start
- [ ] Business owner has reviewed and approved the plan
