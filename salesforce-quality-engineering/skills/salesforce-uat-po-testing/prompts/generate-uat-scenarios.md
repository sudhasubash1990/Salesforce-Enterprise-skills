---
title: Generate UAT Scenarios Prompt
module: Salesforce Quality Engineering
category: QE Specialized Skill Prompt
document_type: prompt
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-uat-po-testing, generate-scenarios]
---

# Generate UAT Scenarios

## Prompt

```
You are a Salesforce UAT Lead using the PO/UAT Testing skill (SPUAT).

Given the following user stories and acceptance criteria:

[Paste user stories with AC here]

Generate UAT business scenarios using the PO-friendly format:

For each scenario, provide:
1. Business Scenario — plain-language description
2. Business Objective — why this matters
3. Preconditions — what must be true before starting
4. Business Steps — in the user's language, not click-by-click
5. Expected Business Outcome — concrete, observable result
6. Acceptance Criteria — AC ID(s) validated
7. Business Risk — what goes wrong if this fails
8. Evidence Required — proof needed for sign-off
9. Business Owner — who validates
10. UAT Status — default to "Not Started"

Rules:
- Use BUSINESS language only — no Apex, API names, or developer jargon
- Include happy-path, exception, and negative scenarios
- Prioritize by business risk (Critical / High / Medium / Low)
- Ensure every AC maps to at least one scenario
- Do NOT invent acceptance rates or pass percentages
```

## Expected Output

A set of prioritized business scenarios in the PO-friendly format, with AC traceability and persona coverage noted.
