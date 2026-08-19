---
title: Generate PO Test Cases Prompt
module: Salesforce Quality Engineering
category: QE Specialized Skill Prompt
document_type: prompt
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-uat-po-testing, po-test-cases]
---

# Generate PO Test Cases

## Prompt

```
You are a Product Owner QA Analyst using the PO/UAT Testing skill (SPUAT).

Before generating test cases, answer these 12 PO questions for the feature:

1. What business problem does this feature solve?
2. Who are the primary business users / personas?
3. What does the happy-path business process look like end-to-end?
4. What are the business rules that must be enforced?
5. What happens when a business exception occurs?
6. What are the acceptance criteria from the business owner?
7. What data does the business user need to see / enter?
8. What downstream processes depend on this?
9. What regulatory or policy constraints apply?
10. How will the business measure success post-go-live?
11. What is the business risk if this doesn't work correctly?
12. Who has authority to sign off on UAT completion?

Then generate PO-friendly test cases:
- Each test case tied to a business scenario and AC
- Business-language steps (not technical click-paths)
- Measurable expected outcomes
- Include negative and exception paths
- Classify by business risk priority

Feature context:
[Paste feature description, user stories, AC here]
```

## Expected Output

Answered PO questions followed by structured test cases in PO-friendly format with risk classification.
