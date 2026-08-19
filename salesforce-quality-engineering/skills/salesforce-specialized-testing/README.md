---
title: Salesforce Specialized Testing — README
module: Salesforce Quality Engineering
category: QE Specialized Skill README
document_type: README
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-specialized-testing, readme]
---

# Salesforce Specialized Testing (SST)

> Orchestration layer that determines which specialized testing dimensions are required for a Salesforce implementation and routes to downstream QE skills.

## Quick Start

1. Load [SKILL.md](SKILL.md) and [skill-config.yaml](skill-config.yaml)
2. Provide implementation context (clouds, features, integrations, changes)
3. SST produces a **Testing Dimension Assessment** identifying required dimensions
4. For each required dimension, SST chains to the appropriate downstream skill

## Architecture

SST is an **orchestrator** — it does not duplicate downstream skills:

| Dimension | Chain Skill | Short ID |
|-----------|-------------|----------|
| Security | [Permission Testing Agent](../permission-testing-agent/SKILL.md) | PTA |
| Data | [Data Migration QA](../data-migration-qa/SKILL.md) / [Test Data Generator](../test-data-generator/SKILL.md) | DMQA / TDG |
| Release/Deployment | [Metadata Impact Analyzer](../metadata-impact-analyzer/SKILL.md) | MIA |
| Regression | [Risk-Based Regression](../risk-based-regression/SKILL.md) | RBRR |
| UI Automation | [Playwright Review](../playwright-review/SKILL.md) | PWR |
| Functional | [Salesforce Functional Testing](../salesforce-functional-testing/SKILL.md) | SFT |
| LWC/Flow UI | [LWC Flow UI Testing](../lwc-flow-ui-testing/SKILL.md) | LFUT |

## Directory Structure

```
salesforce-specialized-testing/
├── SKILL.md                  # Skill entry — orchestration logic
├── README.md                 # This file
├── skill-config.yaml         # Routing, output schema, quality gates
├── knowledge/                # Testing dimension knowledge articles
├── playbooks/                # Assessment playbooks per dimension
├── templates/                # Report and matrix templates
├── prompts/                  # Assessment prompts
├── examples/                 # Sample assessment outputs
└── tests/                    # Scenario-based validation tests
```

## Key Rules

1. **Assess dimensions before detail** — always produce the dimension matrix first
2. **Chain, never duplicate** — if a downstream skill exists, route to it
3. **Never invent performance metrics** — state "Performance evidence not provided"
4. **Never fabricate coverage percentages** — omit or flag as "to be measured"
5. **Label all assumptions** — A1, A2, A3…

## Testing Dimensions Covered

1. Security Testing
2. Integration Testing
3. Data Testing
4. API Testing
5. Performance Testing (advisory only)
6. Accessibility Testing
7. Mobile Testing
8. Compatibility Testing
9. Regression Testing
10. Release/Deployment Testing

## Output

SST produces an 18-section **Specialized Testing Report** — see [templates/specialized-testing-report.md](templates/specialized-testing-report.md).

## Related

- [Enterprise Orchestrator](../../enterprise-orchestrator/enterprise-orchestrator.md)
- [Capability Routing Table](../../enterprise-orchestrator/capability-routing-table.md)
- [QE Skill](../../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.25.0 | 2026-08-19 | QE Practice Lead | Initial creation |
