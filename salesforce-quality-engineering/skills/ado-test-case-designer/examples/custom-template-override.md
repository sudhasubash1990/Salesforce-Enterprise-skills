---
title: "Example: Custom Template Override"
module: Salesforce Quality Engineering
category: QE Specialized Skill Example
document_type: Example
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [ado-test-case-designer, example, custom-template]
---

# Example: Custom Template Override

## Scenario

The user provides their own test case template. The skill uses the user's template instead of ADO default format.

## Input

**User request:**
> Generate test cases for Case creation in Service Cloud. Use my template:
>
> ```
> Test ID: [ID]
> Module: [Module]
> Scenario: [Scenario Description]
> Pre-Requisites: [Setup needed]
> Steps:
>   1. [Action] → [Expected Outcome]
>   2. [Action] → [Expected Outcome]
> Linked Req: [Requirement ID]
> Priority: [P1/P2/P3]
> Tester: [Role]
> ```

**Requirement:** FR-020 — Service Agents can create Cases with Subject, Description, Priority, and Account lookup. Cases default to Status = "New" and are auto-assigned via assignment rules.

## Output — Using User's Custom Template

### Test Case 1

```
Test ID: TC-FR020-001
Module: Service Cloud — Case Management
Scenario: Create Case with all required fields — happy path
Pre-Requisites: Logged in as Service Agent; Account "Acme Corp" exists
Steps:
  1. Navigate to Cases tab and click "New" → New Case form opens with required fields marked (*)
  2. Enter Subject: "Billing Inquiry", Description: "Customer asks about invoice #1234", Priority: "Medium", Account: "Acme Corp" → Fields accept input without validation errors
  3. Click "Save" → Case is created with Case Number auto-generated, Status = "New", Owner assigned via assignment rule, Created Date = today
Linked Req: FR-020
Priority: P1
Tester: Service Agent
```

### Test Case 2

```
Test ID: TC-FR020-002
Module: Service Cloud — Case Management
Scenario: Create Case with missing Subject — validation error
Pre-Requisites: Logged in as Service Agent
Steps:
  1. Navigate to Cases tab and click "New" → New Case form opens
  2. Leave Subject blank, fill other required fields, click "Save" → Validation error displayed: "Subject is required". Case is not saved
Linked Req: FR-020
Priority: P1
Tester: Service Agent
```

### Test Case 3

```
Test ID: TC-FR020-003
Module: Service Cloud — Case Management
Scenario: Create Case — assignment rule assigns to correct queue
Pre-Requisites: Logged in as Service Agent; Assignment rule configured: Priority = "High" → "Tier 2 Support" queue
Steps:
  1. Create a new Case with Priority = "High" and save → Case Owner = "Tier 2 Support" queue (not the creating agent)
  2. Verify Case detail page shows Owner = "Tier 2 Support" → Owner field displays "Tier 2 Support" queue name
Linked Req: FR-020
Priority: P2
Tester: Service Agent
```

## Key Points Demonstrated

1. **ADO format was NOT used** — the user's custom template was applied
2. **Expected outcomes are still measurable** — no vague results
3. **Traceability is maintained** — Linked Req field populated
4. **Quality gates still enforced** — all expected results are specific and observable

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.25.0 | 2026-08-19 | QE Practice Lead | Initial creation |
