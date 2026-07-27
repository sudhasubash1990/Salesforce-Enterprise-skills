---
title: OmniStudio QA — README
module: Salesforce Quality Engineering
category: QE Specialized Skill
document_type: Guide
version: 0.22.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [omnistudio-qa]
---

# OmniStudio QA (OSQA)

## Purpose

Enterprise **Salesforce Industries / OmniStudio Quality Engineering** capability. Validates OmniScripts, FlexCards, DataRaptors, Integration Procedures, and decision/calculation components end-to-end — not isolated component CRUD.

Canonical product overview remains in [`../../knowledge/clouds/omnistudio.md`](../../knowledge/clouds/omnistudio.md). This pack holds **OmniStudio QA reasoning models**.

## Capabilities

- OmniScript journey and Data JSON validation  
- FlexCard render/action/binding review  
- DataRaptor mapping and accuracy  
- Integration Procedure flow, cache, retry, remotes  
- Decision/calculation/expression logic  
- Security (CRUD/FLS/Experience) and performance risk assessment  
- Regression and release readiness  

## Supported OmniStudio Components

OmniScript · FlexCard · DataRaptor (Extract/Load/Transform/Turbo) · Integration Procedure · Decision Matrix/Table · Calculation Procedure/Matrix · Expression Set · Remote/HTTP/Apex/SF Object/Response Actions · Reusable/Embedded OmniScripts · Data JSON · Context Variables

## Folder Structure

```
skills/omnistudio-qa/
├── SKILL.md
├── README.md
├── skill-config.yaml
├── knowledge/       ← 16 reasoning articles
├── playbooks/       ← 8 playbooks
├── templates/       ← 8 templates
├── prompts/         ← 10 prompts
├── examples/        ← 10 examples
└── tests/           ← 11 scenarios
```

## Inputs

| Input | Required |
|-------|----------|
| Business scenario / industry journey | Yes |
| OmniStudio component inventory | Yes |
| Data JSON / mapping samples (sanitized) | Recommended |
| IP/DR names and contracts | Recommended |
| Personas / Experience access | When security in scope |
| MIA impact report | When Omni metadata changed |

## Outputs

17-section OmniStudio QA report — see [SKILL.md](SKILL.md). Primary template: [templates/omniscript-test-report.md](templates/omniscript-test-report.md).

## Sample Prompt

```
Load skills/omnistudio-qa/SKILL.md.
Business Scenario: Utility Move In guided journey.
Components: OmniScript MoveIn, DR Extract Account, IP CreateServicePoint, FlexCard Status.
Produce all 17 sections including JSON, Integration, Security, and Deployment Readiness.
Label assumptions; do not invent latency %.
```

See [prompts/README.md](prompts/README.md).

## Examples

See [examples/README.md](examples/README.md) — Onboarding, Utilities, CPQ/Quote, Service, Insurance, Healthcare.

## Best Practices

- Business scenario + component inventory **before** detailed cases  
- Always validate Data JSON and submit path for OmniScripts  
- Pair DR Load/IP Salesforce ops with SOVA stubs  
- Chain PTA for Experience/FLS; PWR for UI automation; TDG for seed JSON  
- Label assumptions; never invent performance SLAs  

## Common Anti-Patterns

- Step-navigation-only packs without DR/IP  
- Invented API timing metrics  
- Duplicating Sprint 4B OmniStudio encyclopedia  
- Skipping error/branch paths in Integration Procedures  

## Limitations

- No live Designer/runtime execution  
- Org-specific DR/IP names must be confirmed or labeled TBC  
- Planned siblings (Risk-Based Regression, Production RCA) — cross-link only  

## Future Enhancements

- Deeper EPC/CPQ Industries packs  
- Risk-based regression registry for Omni journeys  
- Production RCA themes for OmniStudio incidents  

## Related Documents

- [SKILL.md](SKILL.md)  
- [skill-config.yaml](skill-config.yaml)  
- [Parent skill.md](../../skill.md)  
- [OmniStudio Cloud Knowledge](../../knowledge/clouds/omnistudio.md)  

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.22.0 | 2026-07-27 | QE Practice Lead | Initial OmniStudio QA capability |
