---
title: Defect Triage Prompt
module: Salesforce Quality Engineering
category: QE Specialized Skill Prompt
document_type: Prompt
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [ado-defect-logger, defect-triage]
---

# Defect Triage

## Prompt

```
Triage the following defects for sprint planning:

For each defect:
1. Validate severity and priority — are they correctly classified?
2. Check for duplicates or related defects in the list
3. Recommend disposition: Fix this sprint / Fix next sprint / Backlog / Reject / Defer
4. Flag any escalation triggers (Sev1, security, data corruption)
5. Suggest assignment based on component and root cause

Defects:
<paste list of defects with IDs, titles, severity, priority>

Sprint context:
<sprint goal, capacity, release date>
```

## Expected Output

Prioritized triage table with disposition, assignment, and escalation flags.
