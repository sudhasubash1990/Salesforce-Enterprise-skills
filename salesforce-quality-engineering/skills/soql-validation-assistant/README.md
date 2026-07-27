---
title: SOQL Validation Assistant — README
module: Salesforce Quality Engineering
category: QE Specialized Skill
document_type: Guide
version: 0.16.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [soql-validation]
---

# SOQL Validation Assistant

## Purpose

Enterprise **QA reasoning engine** for Salesforce backend validation through SOQL. Determines **why** a query is needed before generating it — not a syntax generator.

## Capabilities

- Validation objective and business context analysis
- Purpose-built SOQL with explanation and expected results
- Security analysis (CRUD, FLS, sharing, run-as)
- Performance analysis (selectivity, governors, LDV)
- Negative validation, edge cases, alternative queries
- Integration with [Metadata Impact Analyzer](../metadata-impact-analyzer/SKILL.md)

## Supported Query Types

| Type | Examples |
|------|----------|
| List | `SELECT Id, Name FROM Account WHERE ...` |
| Relationship | Subqueries, parent.field notation |
| Aggregate | COUNT, GROUP BY, HAVING |
| Date | LAST_N_DAYS, THIS_MONTH, date functions |
| Polymorphic | TYPEOF patterns (advisory) |
| Tooling/Metadata | Dependency evidence (advisory) |

## Folder Structure

```
skills/soql-validation-assistant/
├── SKILL.md           ← Agent entry
├── README.md               ← This file
├── skill-config.yaml
├── knowledge/              ← 15 reasoning articles
├── playbooks/              ← 6 playbooks
├── templates/              ← 6 templates
├── prompts/                ← 10 prompts
├── examples/               ← 13 examples
└── tests/                  ← 9 scenarios
```

## Inputs

| Input | Required |
|-------|----------|
| Validation question / AC / business rule | Yes |
| Object(s) and field(s) | Yes |
| Run-as persona | Recommended |
| Environment | Recommended |
| MIA impact report | When chained from metadata analysis |

## Outputs

14-section validation pack (see [SKILL.md](SKILL.md)). Primary template: [templates/soql-validation-report.md](templates/soql-validation-report.md).

## Usage

1. Load Tier-0 `framework-core/` and QE `skill.md`
2. Load [SKILL.md](SKILL.md)
3. Run [prompts/generate-validation-soql.md](prompts/generate-validation-soql.md) with business context
4. Save to `outputs/<project>/` and run output-engine conversion

## Sample Prompt

```
Load skills/soql-validation-assistant/SKILL.md.
Validation Objective: Confirm no closed Cases missing Resolution Code after VR deploy.
Business Context: Service Cloud, Agent persona, UAT sandbox.
Produce all 14 sections.
```

## Example Scenarios

[examples/README.md](examples/README.md) — Account, Opportunity, Case, migration, integration, utilities, Service/Sales Cloud, etc.

## Best Practices

- Objective before SOQL — always
- State run-as user; warn on zero-row false positives
- Use aggregates for reconciliation; LIMIT for LDV samples
- Chain from MIA for deploy-related validation packs

## Limitations

- No live org query execution
- Index availability assumed — confirm with architect when critical
- CPQ/OmniStudio object models vary by org — mark Partial when unknown

## Future Enhancements

- Permission Testing Agent integration
- Automated query review in CI (lint/selectivity rules)
- ADO test case linkage for SOQL validation steps

## Related Documents

- [SKILL.md](SKILL.md)
- [../README.md](../README.md)
- [../../knowledge/performance/soql-performance.md](../../knowledge/performance/soql-performance.md)
- [../metadata-impact-analyzer/SKILL.md](../metadata-impact-analyzer/SKILL.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.16.0 | 2026-07-27 | QE Practice Lead | Initial release |
