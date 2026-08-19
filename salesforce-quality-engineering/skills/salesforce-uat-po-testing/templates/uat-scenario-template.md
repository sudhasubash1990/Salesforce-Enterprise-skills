---
title: UAT Scenario Template
module: Salesforce Quality Engineering
category: QE Specialized Skill Template
document_type: template
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-uat-po-testing, uat-scenario]
---

# UAT Scenario Template — PO-Friendly Format

> Copy this template for each UAT scenario. Use business language throughout.

---

## Scenario [S-XXX]: [Business Scenario Name]

| Field | Value |
|-------|-------|
| **Business Scenario** | [Plain-language description of what the business user is doing — e.g., "Sales manager approves a discount request above 15% for a strategic account."] |
| **Business Objective** | [Why this matters to the business — e.g., "Ensures discount governance is enforced while enabling competitive pricing for key accounts."] |
| **Preconditions** | [What must be true before this scenario starts — e.g., "Opportunity exists with a line item requesting 18% discount. Sales manager is assigned as the opportunity owner's manager."] |
| **Business Steps** | *(See numbered steps below)* |
| **Expected Business Outcome** | [What the business user expects to see when the scenario completes successfully — e.g., "Discount is approved, opportunity stage advances, and the sales rep receives an approval notification."] |
| **Acceptance Criteria** | [AC ID(s) this scenario validates — e.g., "AC-003, AC-004"] |
| **Business Risk** | [What goes wrong for the business if this fails — e.g., "Unapproved discounts could erode margin; sales reps may be blocked from closing deals."] |
| **Evidence Required** | [What proof is needed — e.g., "Screenshot of approval notification, opportunity stage change, discount field value."] |
| **Business Owner** | [Name and role of the person who validates this scenario] |
| **UAT Status** | Not Started / In Progress / Passed / Failed / Blocked |

### Business Steps

1. [Step 1 in the user's language — e.g., "Sales rep submits the opportunity for discount approval"]
2. [Step 2 — e.g., "Sales manager receives an approval request notification"]
3. [Step 3 — e.g., "Sales manager reviews the discount details and approves"]
4. [Step 4 — e.g., "Sales rep sees the opportunity updated with approved discount"]

### Negative / Exception Path

| Exception | Expected Behaviour |
|-----------|-------------------|
| [What if the discount exceeds 25%?] | [Requires VP approval instead of manager] |
| [What if the manager rejects?] | [Sales rep is notified with rejection reason; opportunity stays in current stage] |

### Notes

- [Any additional context, assumptions, or open questions for this scenario]
