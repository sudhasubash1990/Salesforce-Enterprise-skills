---
title: ADO Test Case Designer — README
module: Salesforce Quality Engineering
category: QE Specialized Skill README
document_type: README
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [ado-test-case-designer, readme]
---

# ADO Test Case Designer (ATCD)

Enterprise test case design skill that generates Azure DevOps-compatible test cases from Salesforce requirements with full traceability.

## Quick Start

1. Load `SKILL.md` — the skill entry point
2. Provide a requirement, user story, or acceptance criteria
3. Receive ADO-formatted test cases with traceability

## Key Principle

**ADO format is the default.** If the user provides a custom template, the custom template overrides ADO format. Never force ADO format when the user explicitly provides another.

## Directory Structure

```
ado-test-case-designer/
├── SKILL.md                  # Skill entry — identity, scope, rules, output schema
├── README.md                 # This file
├── skill-config.yaml         # Registry and routing configuration
├── knowledge/                # Domain knowledge
│   ├── ado-test-case-model.md
│   ├── test-design-techniques.md
│   ├── requirement-to-test-traceability.md
│   └── salesforce-test-design.md
├── playbooks/                # Step-by-step workflows
│   ├── README.md
│   ├── requirement-to-ado-test-case.md
│   ├── acceptance-criteria-to-test-cases.md
│   ├── salesforce-user-story-to-test-cases.md
│   └── bulk-test-case-generation.md
├── templates/                # Output templates
│   ├── README.md
│   ├── ado-test-case-template.md
│   ├── test-case-report.md
│   └── traceability-matrix-template.md
├── prompts/                  # Prompt patterns
│   ├── README.md
│   ├── generate-ado-test-case.md
│   ├── generate-ado-test-suite.md
│   └── convert-to-custom-template.md
├── examples/                 # Worked examples
│   ├── README.md
│   ├── user-story-to-ado-test-case.md
│   ├── bulk-test-case-generation.md
│   └── custom-template-override.md
└── tests/                    # Validation scenarios
    ├── README.md
    ├── scenario-ado-default-format.md
    ├── scenario-custom-template.md
    ├── scenario-quality-gate.md
    └── scenario-traceability.md
```

## Integration Points

| Direction | Skill | Purpose |
|-----------|-------|---------|
| Upstream | SFT, SPUAT, LFUT | Receive test scenarios |
| Downstream | ADO Defect Logger | Log defects from failed test cases |
| Validation | PTA, SOVA, TDG | Permission, query, and data validation |

## Quality Gates

Every test case must pass: requirement understandable, AC available or assumed, assumptions labeled, test data identified, persona identified, expected result measurable, no vague expected results.

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.25.0 | 2026-08-19 | QE Practice Lead | Initial creation |
