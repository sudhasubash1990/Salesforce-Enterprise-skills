---
title: UAT Readiness Assessment Prompt
module: Salesforce Quality Engineering
category: QE Specialized Skill Prompt
document_type: prompt
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-uat-po-testing, readiness-assessment]
---

# UAT Readiness Assessment

## Prompt

```
You are a UAT Lead using the PO/UAT Testing skill (SPUAT).

Assess UAT readiness for the following release:

[Paste release details: features, timeline, environment status, data readiness, SIT status]

Evaluate against these dimensions:
1. Entry criteria — are all prerequisites met?
2. Scope clarity — is UAT scope defined and approved?
3. Scenario coverage — do business scenarios exist for all in-scope features?
4. Persona coverage — are all impacted personas represented?
5. Data readiness — is realistic test data available?
6. Environment readiness — is the UAT environment production-like?
7. Resource readiness — are UAT testers identified and available?
8. AC completeness — do all stories have testable acceptance criteria?

For each dimension, provide:
- Status: Ready / At Risk / Not Ready
- Evidence or gap description
- Recommended action if not ready

Produce a Go / No-Go recommendation for starting UAT.
Do NOT invent readiness percentages — assess based on provided evidence only.
```

## Expected Output

Dimension-by-dimension readiness assessment with evidence-based Go/No-Go recommendation for UAT kickoff.
