---
title: Salesforce Functional Testing — README
module: Salesforce Quality Engineering
category: QE Specialized Skill Guide
document_type: Guide
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-functional-testing]
---

# Salesforce Functional Testing

## Purpose

Enterprise **Functional Quality Engineering** capability for Salesforce. Validates cloud-specific business processes across Service Cloud, Sales Cloud, and Experience Cloud — covering case lifecycle, lead conversion, opportunity management, portal self-service, persona-based testing, and cross-cloud E2E journeys.

## Capabilities

- Service Cloud functional testing (Cases, Omni-Channel, Knowledge, Entitlements, escalation)
- Sales Cloud functional testing (Leads, conversion, Opportunities, stages, Campaigns, forecasts)
- Experience Cloud functional testing (portal access, guest user, self-service, CRUD/FLS)
- Cross-cloud E2E journey validation
- Persona-based and role-based testing
- Business rule, validation rule, and approval process testing
- Regression, smoke, and sanity test planning

## Supported Clouds

Service Cloud · Sales Cloud · Experience Cloud (cross-cloud E2E journeys span all three)

## Folder Structure

```
skills/salesforce-functional-testing/
├── SKILL.md
├── README.md
├── skill-config.yaml
├── knowledge/       ← 6 reasoning articles
├── playbooks/       ← 5 playbooks
├── templates/       ← 4 templates
├── prompts/         ← 4 prompts
├── examples/        ← 5 examples
└── tests/           ← 6 scenarios
```

## Inputs

| Input | Required |
|-------|----------|
| Business scenario / process description | Yes |
| Target Salesforce cloud(s) | Yes |
| Personas / roles involved | Yes |
| Org-specific configuration (record types, page layouts) | Recommended |
| MIA impact report | When metadata changes affect functional tests |

## Outputs

15-section functional test report — see [SKILL.md](SKILL.md). Primary template: [templates/functional-test-report.md](templates/functional-test-report.md).

## Sample Prompt

```
Load skills/salesforce-functional-testing/SKILL.md.
Business Scenario: Customer service agents create and manage cases via Service Console.
Cloud: Service Cloud.
Personas: Service Agent, Service Manager, Customer (portal).
Produce all 15 sections including positive/negative/boundary/permission scenarios.
```

## Example Scenarios

See [examples/README.md](examples/README.md) — Service Cloud case creation, case escalation, Sales Cloud lead conversion, opportunity approval, Experience Cloud portal case creation.

## Best Practices

- Confirm cloud scope and personas before generating scenarios
- Cover positive, negative, boundary, and permission paths for every functional flow
- Chain PTA for permission matrices — do not duplicate
- Chain SOVA for backend record verification
- Chain TDG for test data prerequisites
- All expected results must be measurable and observable
- Never invent coverage percentages

## Known Limitations

- No live Salesforce org execution
- Org-specific configuration must be confirmed with project team
- Governor limit context requires data volume estimates
- Experience Cloud license model varies by org

## Future Enhancements

- Additional cloud support (Marketing Cloud, Commerce Cloud)
- Automated regression scope calculation from MIA output
- Integration with CI/CD pipeline test orchestration

## Related Documents

- [Service Cloud Knowledge](../../knowledge/clouds/service-cloud.md)
- [Sales Cloud Knowledge](../../knowledge/clouds/sales-cloud.md)
- [Experience Cloud Knowledge](../../knowledge/clouds/experience-cloud.md)
- [Permission Testing Agent](../permission-testing-agent/SKILL.md)
- [SOQL Validation Assistant](../soql-validation-assistant/SKILL.md)
- [Test Data Generator](../test-data-generator/SKILL.md)
- [Playwright Review](../playwright-review/SKILL.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.25.0 | 2026-08-19 | QE Practice Lead | Initial capability release |
