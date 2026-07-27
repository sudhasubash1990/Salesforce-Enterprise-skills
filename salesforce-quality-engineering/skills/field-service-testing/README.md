---
title: Field Service Testing — README
module: Salesforce Quality Engineering
category: QE Specialized Skill
document_type: Guide
version: 0.19.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [field-service-testing]
---

# Field Service (FSL) QA

## Purpose

Enterprise **Field Service Quality Engineering** capability for Salesforce FSL. Validates scheduling, dispatch, mobile/offline, inventory, security, and performance — not Work Order CRUD alone.

Canonical product overview remains in [`../../knowledge/clouds/field-service.md`](../../knowledge/clouds/field-service.md). This pack holds **FSL QA reasoning models**.

## Capabilities

- Work Order and Service Appointment lifecycle testing  
- Scheduling policy, skills, territory, and optimization validation  
- Dispatcher Console assignment and conflict handling  
- Mobile online/offline sync and conflict scenarios  
- Inventory (van stock, requests, consumption, transfers)  
- Crew management and multi-day projects  
- Security (dispatcher/technician) and performance risk assessment  
- Regression and release readiness  

## Supported FSL Components

Work Order · WOLI · Service Appointment · Service Resource · Service Territory · Operating Hours · Work Type · Skills · Scheduling Policy · Optimization · Dispatcher Console · Maintenance Plan · Service Report · Crew · Product Request/Transfer · Products Consumed · Field Service Mobile · Offline · Appointment Booking (via AFT)

## Folder Structure

```
skills/field-service-testing/
├── SKILL.md
├── README.md
├── skill-config.yaml
├── knowledge/       ← 17 reasoning articles
├── playbooks/       ← 9 playbooks
├── templates/       ← 9 templates
├── prompts/         ← 10 prompts
├── examples/        ← 10 examples
└── tests/           ← 12 scenarios
```

## Inputs

| Input | Required |
|-------|----------|
| Business scenario / personas | Yes |
| FSL component inventory (WO/SA/resources/territory/policy) | Yes |
| Scheduling policy / work rules | When scheduling in scope |
| Mobile/offline scope | When mobile in scope |
| Inventory model | When parts in scope |
| MIA impact report | When FSL metadata changes |

## Outputs

18-section FSL QA report — see [SKILL.md](SKILL.md). Primary template: [templates/work-order-test-report.md](templates/work-order-test-report.md).

## Sample Prompts

```
Load skills/field-service-testing/SKILL.md.
Business Scenario: Emergency utility outage insert ahead of planned work.
Components: WO, SA, Emergency Work Type, Territory X, Scheduling Policy Y.
Produce all 18 sections including Scheduling, Offline (N/A if not in scope), Inventory, and Recommended SOQL.
```

See [prompts/README.md](prompts/README.md).

## Examples

See [examples/README.md](examples/README.md) — Utilities, Telecom, HVAC, Healthcare, Public Sector, Manufacturing.

## Best Practices

- Business scenario + component inventory **before** detailed cases  
- Always include negative scheduling (double-book / unqualified resource) when scheduling in scope  
- Offline conflict path when mobile offline in scope  
- Chain SOVA for WO/SA/inventory proofs; PTA for access; MIA for metadata; AFT for agent booking  
- Label assumptions; never invent optimization scores or SLA %  

## Common Anti-Patterns

- WO CRUD-only packs  
- Invented optimization/travel-time metrics  
- Full mobile automation scripts instead of design advisory  
- Duplicating cloud Field Service encyclopedia  

## Limitations

- No live org or device execution  
- Mobile automation is design-only (Sprint 8)  
- Planned sibling capabilities (OmniStudio QA, Production RCA) not built — cross-link existing packs; seed data via [Test Data Generator](../test-data-generator/SKILL.md)  

## Future Enhancements

- Deeper OmniStudio / Guided Action QA when that capability exists  
- FSL LDV seed packs via [Test Data Generator](../test-data-generator/SKILL.md)  
- Production RCA themes for FSL incidents  

## Related Documents

- [SKILL.md](SKILL.md)  
- [skill-config.yaml](skill-config.yaml)  
- [Parent skill.md](../../skill.md)  
- [Field Service Cloud Knowledge](../../knowledge/clouds/field-service.md)  

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.19.0 | 2026-07-27 | QE Practice Lead | Initial Field Service FSL QA capability |
