---
title: Defect Logging Playbook
module: Salesforce Quality Engineering
category: QE Specialized Skill Playbook
document_type: Playbook
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [ado-defect-logger, defect-logging]
---

# Defect Logging Playbook

End-to-end process for logging a Salesforce defect into Azure DevOps.

## Pre-Conditions

- Defect input received (error, screenshot, test failure, user complaint)
- Environment details available
- Related requirement or test case identified (if applicable)

## Steps

### Step 1 — Validate the Defect

1. Confirm this is a defect (not an enhancement, question, or known limitation)
2. Check for vague descriptions — reject and ask for evidence if insufficient
3. Confirm the issue is reproducible or gather reproduction details

### Step 2 — Analyze the Defect

1. Identify the affected Salesforce component (Object, Flow, LWC, Apex, Integration)
2. Determine the Salesforce Cloud context
3. Assess severity using [severity-priority-model](../knowledge/severity-priority-model.md)
4. Assess priority based on business urgency
5. Formulate root cause hypothesis using [root-cause-analysis](../knowledge/root-cause-analysis.md)

### Step 3 — Structure the ADO Defect

1. Write a concise, searchable title: `[Component] Short summary`
2. Write numbered repro steps — each step a single atomic action
3. State expected result (from requirement/design)
4. State actual result (with evidence)
5. Document environment details
6. Attach evidence (screenshots, logs, SOQL results)
7. Populate all ADO fields per [ado-defect-template](../templates/ado-defect-template.md)

### Step 4 — Quality Gate Check

Verify against quality gates:
- [ ] Repro steps numbered and reproducible
- [ ] Expected vs actual clear
- [ ] Severity and priority justified
- [ ] No vague descriptions remain
- [ ] Evidence attached or referenced
- [ ] Root cause hypothesis provided

### Step 5 — Create in ADO (When Requested)

1. Confirm user has explicitly requested ADO creation
2. Verify ADO MCP/API is available and authenticated
3. Map all fields to ADO Bug schema
4. Create Bug work item
5. Return real work item ID and URL
6. If API unavailable: generate template and state clearly that creation was not performed

### Step 6 — Post-Creation

1. Link Bug to related User Story / Requirement
2. Link Bug to Test Case (if applicable)
3. Notify suggested assignee
4. Document in defect log

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.25.0 | 2026-08-19 | QE Practice Lead | Initial creation |
