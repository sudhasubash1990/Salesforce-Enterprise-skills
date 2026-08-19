---
title: Convert to Custom Template Prompt
module: Salesforce Quality Engineering
category: QE Specialized Skill Prompt
document_type: Prompt
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [ado-test-case-designer, prompt, custom-template]
---

# Convert to Custom Template

## Prompt Pattern

```
Generate test cases for the following requirement using my custom template:

**Requirement:** [Requirement text]

**My Template:**
[Paste the custom template structure here]
```

## Behavior

1. The skill detects a user-provided template
2. ADO default format is **NOT** used
3. Test cases are generated matching the user's template structure
4. Any fields in the user template that map to ADO fields are populated
5. Missing critical fields (preconditions, expected result) are added as supplementary sections if not present in the user template

## Example Custom Template

```
Test ID: [ID]
Module: [Module Name]
Scenario: [Description]
Steps:
  1. [Action] → [Result]
  2. [Action] → [Result]
Status: [Not Run]
Linked Requirement: [ID]
```

## Quality Rules Still Apply

Even with a custom template:
- Expected results must be measurable (never vague)
- Traceability must be maintained
- Assumptions must be labeled
