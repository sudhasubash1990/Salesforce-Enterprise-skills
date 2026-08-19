---
title: Salesforce PO / UAT Testing — README
module: Salesforce Quality Engineering
category: QE Specialized Skill README
document_type: README
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-uat-po-testing, readme]
---

# Salesforce PO / UAT Testing

Business-perspective validation skill for Salesforce solutions. Ensures Product Owners, business users, and UAT leads can validate that delivered features meet real-world business needs — not just technical specifications.

## Purpose

- Plan and scope UAT from a business perspective
- Generate business-language test scenarios (not technical QA jargon)
- Validate acceptance criteria against business requirements
- Assess production readiness and provide Go/No-Go recommendations
- Support business sign-off with traced evidence

## When to Use

| Trigger | Example |
|---------|---------|
| UAT planning | "Plan UAT for the new opportunity approval process" |
| PO validation | "What should the Product Owner test for case management?" |
| Business sign-off | "Generate a Go/No-Go assessment for the portal release" |
| Scenario generation | "Create UAT scenarios for the customer onboarding journey" |
| AC validation | "Map acceptance criteria to UAT test evidence" |

## Folder Structure

```
salesforce-uat-po-testing/
├── SKILL.md                  # Skill definition and reasoning model
├── README.md                 # This file
├── skill-config.yaml         # Routing, schema, quality gates
├── knowledge/                # Domain knowledge
│   ├── uat-framework.md
│   ├── po-testing-model.md
│   ├── business-acceptance.md
│   └── uat-signoff.md
├── playbooks/                # Step-by-step execution guides
│   ├── README.md
│   ├── po-uat-planning.md
│   ├── business-scenario-workshop.md
│   ├── uat-defect-triage.md
│   └── uat-signoff-readiness.md
├── templates/                # Output templates
│   ├── README.md
│   ├── uat-test-report.md
│   ├── uat-scenario-template.md
│   └── uat-signoff-template.md
├── prompts/                  # Reusable prompts
│   ├── README.md
│   ├── generate-uat-scenarios.md
│   ├── generate-po-test-cases.md
│   └── uat-readiness-assessment.md
├── examples/                 # Worked examples
│   ├── README.md
│   ├── opportunity-approval-uat.md
│   ├── case-management-uat.md
│   └── experience-cloud-uat.md
└── tests/                    # Validation scenarios
    ├── README.md
    ├── scenario-uat-routing.md
    ├── scenario-po-perspective.md
    ├── scenario-business-language.md
    └── scenario-signoff-readiness.md
```

## Integration with Other Skills

| Skill | Relationship |
|-------|-------------|
| Salesforce Functional Testing (SFT) | Chain for technical scenarios derived from UAT |
| ADO Test Case Designer (ATCD) | Publish UAT test cases to Azure DevOps |
| ADO Defect Logger (ADL) | Log UAT defects with business-impact classification |
| Permission Testing Agent (PTA) | Persona permission validation during UAT |
| Test Data Generator (TDG) | Generate realistic UAT test data |

## Key Principles

1. **Business language only** — no Apex, API names, or developer jargon in UAT outputs
2. **PO questions first** — 12 mandatory questions before generating scenarios
3. **Evidence-based** — no invented acceptance rates or pass percentages
4. **Persona coverage** — every impacted role must have representative scenarios
5. **Traceable sign-off** — every Go/No-Go links to test evidence

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.25.0 | 2026-08-19 | QE Practice Lead | Initial creation |
