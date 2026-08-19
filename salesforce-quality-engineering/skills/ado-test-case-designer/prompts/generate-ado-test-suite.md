---
title: Generate ADO Test Suite Prompt
module: Salesforce Quality Engineering
category: QE Specialized Skill Prompt
document_type: Prompt
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [ado-test-case-designer, prompt, test-suite]
---

# Generate ADO Test Suite

## Prompt Pattern

```
Generate a complete ADO test suite for:

**Epic / Feature:** [Title]
**Requirements:**
1. [BR-001]: [Description]
2. [BR-002]: [Description]
3. [US-001]: [User story]

**Salesforce Cloud:** [Sales Cloud / Service Cloud / etc.]
**Objects:** [Account, Case, Opportunity, etc.]
**Personas:** [Sales Rep, Service Agent, Admin]
**Sprint:** [Sprint N]
```

## Expected Output

1. Test suite structure (hierarchy)
2. Test cases per requirement in ADO format
3. Shared steps identified across test cases
4. Consolidated traceability matrix
5. Summary statistics (total TCs, by type, coverage)

## Tips

- For large epics, the skill organizes test cases into sub-suites by feature
- Shared preconditions are extracted as ADO Shared Steps
- Cross-requirement E2E scenarios are identified and grouped separately
