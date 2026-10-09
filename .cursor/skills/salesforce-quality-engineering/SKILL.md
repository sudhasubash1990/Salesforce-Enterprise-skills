---
name: salesforce-quality-engineering
description: >-
  Salesforce Quality Engineering through Sprint 11 Validation & Certification:
  Enterprise Orchestrator routes to requirement analysis, test design, SF
  knowledge, documentation, ADO, defect intelligence, automation intelligence,
  production support, Sprint 10 CQO advisory, Sprint 11 framework
  validation/certification, and specialized skills under skills/ (MIA, SOVA,
  PTA, AFT, FSQA, TDG, PWR, OSQA, DMQA, PRCA, RBRR). Load Tier-0 framework-core
  first. Never invent metrics, maturity scores, SLA, compliance certifications,
  or certification levels without evidence.
version: 0.24.0
---

# Salesforce Quality Engineering (Cursor Discovery Stub)

## Canonical location

**[`salesforce-quality-engineering/`](../../../salesforce-quality-engineering/README.md)**

| Priority | Path |
|----------|------|
| **Tier-0 Framework Core** | [`framework-core/`](../../../framework-core/README.md) |
| Skill entry | [`skill.md`](../../../salesforce-quality-engineering/skill.md) (alias `SKILL.md` on case-insensitive FS) |
| Skill contract (thin) | [`skill-contract.yaml`](../../../salesforce-quality-engineering/skill-contract.yaml) |
| **Module skill registry** | [`skill-config.yaml`](../../../salesforce-quality-engineering/skill-config.yaml)
| **Enterprise Orchestrator** | [`enterprise-orchestrator/`](../../../salesforce-quality-engineering/enterprise-orchestrator/README.md) |
| Brain | [`brain/`](../../../salesforce-quality-engineering/brain/README.md) |
| Engines (1–4) | [`knowledge/`](../../../salesforce-quality-engineering/knowledge/README.md) |
| Documentation | [`templates/`](../../../salesforce-quality-engineering/templates/README.md) |
| ADO | [`ado/`](../../../salesforce-quality-engineering/ado/README.md) |
| Defect Intelligence | [`quality-intelligence/`](../../../salesforce-quality-engineering/quality-intelligence/README.md) |
| Automation Intelligence | [`automation-intelligence/`](../../../salesforce-quality-engineering/automation-intelligence/README.md) |
| Production Support (QE Sprint 9) | [`production-support/`](../../../salesforce-quality-engineering/production-support/README.md) |
| **Enterprise Quality Advisory** | [`enterprise-quality/`](../../../salesforce-quality-engineering/enterprise-quality/README.md) |
| **Validation & Certification (Sprint 11)** | [`validation/`](../../../salesforce-quality-engineering/validation/README.md) |
| **Specialized Skills** | [`skills/`](../../../salesforce-quality-engineering/skills/README.md) · [MIA](../../../salesforce-quality-engineering/skills/metadata-impact-analyzer/SKILL.md) · [SOVA](../../../salesforce-quality-engineering/skills/soql-validation-assistant/SKILL.md) · [PTA](../../../salesforce-quality-engineering/skills/permission-testing-agent/SKILL.md) · [AFT](../../../salesforce-quality-engineering/skills/agentforce-testing/SKILL.md) · [FSQA](../../../salesforce-quality-engineering/skills/field-service-testing/SKILL.md) · [TDG](../../../salesforce-quality-engineering/skills/test-data-generator/SKILL.md) · [PWR](../../../salesforce-quality-engineering/skills/playwright-review/SKILL.md) · [OSQA](../../../salesforce-quality-engineering/skills/omnistudio-qa/SKILL.md) · [DMQA](../../../salesforce-quality-engineering/skills/data-migration-qa/SKILL.md) · [PRCA](../../../salesforce-quality-engineering/skills/production-rca/SKILL.md) · [RBRR](../../../salesforce-quality-engineering/skills/risk-based-regression/SKILL.md) |
| Prompts | [`prompts.md`](../../../salesforce-quality-engineering/prompts.md) · [`prompts/`](../../../salesforce-quality-engineering/prompts/README.md) |
| Examples | [`examples/`](../../../salesforce-quality-engineering/examples/README.md) |

## Hard rules

1. Load Tier-0 `framework-core/` then route via Enterprise Orchestrator before deep work.
2. Sprint 11: Pass/Partial/Fail with evidence; no invented certification levels.
3. Never invent maturity/SLA/compliance scores.
4. No full automation scripts unless explicitly requested.
5. BA story authorship stays in `salesforce-business-analyst/` — do not duplicate.
6. Specialized skills live under `skills/` only (capabilities/ namespace retired in v0.24.0).
