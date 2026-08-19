---
title: Analyze Defect Prompt
module: Salesforce Quality Engineering
category: QE Specialized Skill Prompt
document_type: Prompt
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [ado-defect-logger, analyze-defect]
---

# Analyze Defect

## Prompt

```
Analyze the following reported issue and determine:

1. Is this a valid defect? (Yes / No / Needs clarification / Enhancement request)
2. If vague, list the specific clarifying questions needed before proceeding
3. If valid, provide the full defect analysis:
   - Title (concise, component-prefixed)
   - Category (Functional, UI, Integration, Data, Security, etc.)
   - Severity (1-4) with justification
   - Priority (1-4) with justification
   - Reproducibility (Always / Intermittent / Once / Unknown)
   - Business impact
   - Technical impact
   - Root cause hypothesis (category, hypothesis, confidence)
   - Evidence available vs evidence needed

Reported issue:
<paste issue details here>

Environment:
<paste environment details here>

Related requirement/test case (if any):
<paste reference here>
```

## Expected Output

Full 9-section defect analysis report per the output schema.
