---
title: Specialized Skills — README
module: Salesforce Quality Engineering
category: Specialized Skills
document_type: Guide
version: 0.24.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-28
review_cycle: quarterly
tags: [specialized-skills, skills]
---

# Specialized Skills

## Purpose

Host enterprise-grade specialized QE skills that extend the parent [`SKILL.md`](../SKILL.md) without duplicating Sprint engines.

## Architecture

```
salesforce-quality-engineering/skills/
├── README.md                          ← This file
└── <skill-name>/
    ├── SKILL.md                       ← Canonical skill entry
    ├── README.md                      ← Usage guide
    ├── skill-config.yaml              ← Routing, output schema, gates
    ├── knowledge/                     ← Skill reasoning (+ standard indexes)
    ├── playbooks/
    ├── templates/
    ├── prompts/
    ├── examples/
    └── tests/
```

Each specialized skill:

1. Loads Tier-0 `framework-core/` and QE brain + Enterprise Orchestrator first.
2. Owns **reasoning models, output schema, playbooks, templates, prompts, examples, tests**.
3. **Cross-links** to existing module `knowledge/` encyclopedia — does not duplicate long-form reference content.

## Available Skills

| Skill | Path | Focus |
|-------|------|-------|
| **Metadata Impact Analyzer** (MIA) | [metadata-impact-analyzer/](metadata-impact-analyzer/SKILL.md) | Pre-deployment metadata dependency and impact analysis |
| **SOQL Validation Assistant** (SOVA) | [soql-validation-assistant/](soql-validation-assistant/SKILL.md) | Validation objective before SOQL; backend/data/integration/release verification |
| **Permission Testing Agent** (PTA) | [permission-testing-agent/](permission-testing-agent/SKILL.md) | Security context before scenarios; CRUD/FLS/sharing/community/API validation |
| **Agentforce Testing** (AFT) | [agentforce-testing/](agentforce-testing/SKILL.md) | AI agent quality—prompt, grounding, tools, guardrails, hallucination |
| **Playwright Review** (PWR) | [playwright-review/](playwright-review/SKILL.md) | Playwright framework/script review—locators, SF sync, flake, CI/CD |
| **OmniStudio QA** (OSQA) | [omnistudio-qa/](omnistudio-qa/SKILL.md) | Industries/OmniStudio journeys—OmniScript, FlexCard, DR, IP, JSON |
| **Data Migration QA** (DMQA) | [data-migration-qa/](data-migration-qa/SKILL.md) | Migration lifecycle—mapping, transform, reconcile, cutover, rollback |
| **Test Data Generator** (TDG) | [test-data-generator/](test-data-generator/SKILL.md) | Enterprise TDM—synthetic, relationship-aware, VR-compliant seed data |
| **Field Service Testing** (FSQA) | [field-service-testing/](field-service-testing/SKILL.md) | FSL scheduling, dispatch, mobile/offline, inventory, security |
| **Production RCA** (PRCA) | [production-rca/](production-rca/SKILL.md) | Production defect/incident root-cause analysis *(scaffold)* |
| **Risk-Based Regression** (RBRR) | [risk-based-regression/](risk-based-regression/SKILL.md) | Risk-prioritized regression scope *(scaffold)* |

## Integration Patterns

| From | To | When |
|------|-----|------|
| Metadata Impact Analyzer | SOQL Validation Assistant | Expand Recommended SOQL Validations |
| Metadata Impact Analyzer | Permission Testing Agent | Profile, perm set, sharing, FLS deploy |
| Metadata Impact Analyzer | Agentforce Testing | Agentforce metadata/action deploy |
| Metadata Impact Analyzer | Field Service Testing | FSL metadata/policy deploy |
| Metadata Impact Analyzer | Test Data Generator | New required fields/VR/record types |
| Metadata Impact Analyzer | Playwright Review | FlexiPage/LWC/UI layout changes |
| Metadata Impact Analyzer | OmniStudio QA | OmniStudio / Industries package deploy |
| Metadata Impact Analyzer | Data Migration QA | New objects/fields for migration waves |
| SOQL Validation Assistant | Metadata Impact Analyzer | Validation depends on undeployed metadata |
| Permission Testing Agent | SOQL Validation Assistant | Security-aware SOQL |
| Data Migration QA | SOQL Validation Assistant | Expand reconciliation query stubs |
| OmniStudio QA | Playwright Review | OmniScript/FlexCard UI automation |

## Routing

Parent [`SKILL.md`](../SKILL.md) and [`enterprise-orchestrator/capability-routing-table.md`](../enterprise-orchestrator/capability-routing-table.md) delegate matching requests to the appropriate skill entry. Registry: [`../skill-config.yaml`](../skill-config.yaml).

## Related Documents

- [../SKILL.md](../SKILL.md)
- [../enterprise-orchestrator/README.md](../enterprise-orchestrator/README.md)
- [../knowledge/README.md](../knowledge/README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.24.0 | 2026-07-28 | QE Practice Lead | Unified skills/ namespace — migrated all capabilities; added PRCA/RBRR scaffolds |
| 0.15.0 | 2026-07-27 | QE Practice Lead | Initial specialized skills architecture + Metadata Impact Analyzer |
