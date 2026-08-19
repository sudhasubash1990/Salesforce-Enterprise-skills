---
title: Salesforce Quality Engineering — README
module: Salesforce Quality Engineering
category: Root
document_type: Guide
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-17
last_updated: 2026-08-19
tags: [README, sprint-11]
---

# Salesforce Quality Engineering Skill

Enterprise Quality Engineering for Salesforce—from requirement testability through production operations into **Enterprise Quality Advisory**, coordinated by the **Enterprise Orchestrator**, and **validated/certified** under Sprint 11.

**Purpose:** Landing page and navigation hub for SEACF Module 2.

**Owner:** QE Practice Lead

**Version:** 0.25.0

**Status:** Draft (Unified Skills Architecture)

---

## Sprint 11 Overview

Sprint **11** delivers the **Enterprise Validation & Certification Engine**—proving Sprints 1–10 are complete, accurate, consistent, reusable, scalable, maintainable, enterprise-ready, AI-ready, and consulting-ready.

| Area | Path | Status |
|------|------|--------|
| Enterprise Validation Engine | [validation/](validation/README.md) | **Complete** |
| Certification (Bronze→Enterprise Certified) | [certification/](validation/certification/README.md) | **Complete** |
| Benchmark Suite (10 industries) | [benchmarking/](validation/benchmarking/README.md) | **Complete** |
| Regression Suite (S1–S10) | [regression-suite/](validation/regression-suite/README.md) | **Complete** |
| Quality Scorecards | [quality-scorecards/](validation/quality-scorecards/README.md) | **Complete** |
| Golden Datasets | [golden-datasets/](validation/golden-datasets/README.md) | **Complete** |
| Continuous Improvement + SF Release Readiness | [continuous-improvement/](validation/continuous-improvement/README.md) | **Complete** |

## Validation Framework

Structural and behavioural suites for repository, knowledge, and every sprint capability — [enterprise-validation-engine.md](validation/enterprise-validation-engine.md).

## Certification Process

Scored session → weighted scorecards → [levels.md](validation/certification/levels.md) → [certification-report-template.md](validation/certification/certification-report-template.md).  
**Never** claim a level without evidence.

## Benchmark Suite

Utilities · Retail · Banking · Insurance · Healthcare · Manufacturing · Telecommunications · Public Sector · Energy · Consumer Goods — [benchmarking/](validation/benchmarking/README.md).

## Regression Suite

Per-sprint cases so new knowledge does not break prior capabilities — [regression-suite/](validation/regression-suite/README.md).

## Quality Scorecards

Weighted Pass/Partial/Fail with improvement actions — [quality-scorecards/](validation/quality-scorecards/README.md).

## Continuous Improvement

Gaps, duplicates, knowledge lifecycle, improvement backlog, Salesforce seasonal release compatibility — [continuous-improvement/](validation/continuous-improvement/README.md).

## Framework Governance

QE Practice Lead ownership · CHANGELOG versioning · multi-lens policy · Orchestrator routing · certification gate before “enterprise ready” claims.

## Enterprise Orchestrator

```
User Request → Enterprise Orchestrator
  → Sprint 2 | 3 | 5 | 6 | 7 | 8 | 9
  → Sprint 10 Advisory Engine
  → Executive Recommendations
  → (framework meta) Sprint 11 Validation / Certification
```

Entry: [enterprise-orchestrator/README.md](enterprise-orchestrator/README.md)

## Sprint 10 Overview (Advisory Platform)

[enterprise-quality/](enterprise-quality/README.md) — project/portfolio health, maturity, architecture, AI/compliance, audits, dashboards, decisions, roadmaps.

## Prior sprints (summary)

| Sprint | Capability |
|--------|------------|
| 1–9 | Brain → Production Support |
| **10** | Enterprise Quality Advisory |
| **11** | **Validation, Certification & Continuous Improvement** |

## Repository Structure

`
salesforce-quality-engineering/
├── skill.md / SKILL.md · skill-config.yaml · README.md · prompts.md · CHANGELOG.md · ROADMAP.md
├── prompts/ · examples/     ← Indexes to module catalog + skills/*/
├── enterprise-orchestrator/
├── validation/              ← Sprint 11 ✓
├── brain/ knowledge/ templates/ guidelines/ document-generation/ playbooks/
├── ado/ · quality-intelligence/ · automation-intelligence/
├── production-support/      ← Sprint 9 ✓
├── enterprise-quality/      ← Sprint 10 ✓
└── skills/                  ← All specialized skills (MIA, SOVA, PTA, AFT, SFT, LFUT, SPUAT, ATCD, ADL, SST, …)
`
salesforce-quality-engineering/
├── skill.md · README.md · prompts.md · CHANGELOG.md · ROADMAP.md
├── enterprise-orchestrator/
├── validation/              ← Sprint 11 ✓
├── brain/ knowledge/ templates/ guidelines/ document-generation/ playbooks/
├── ado/ · quality-intelligence/ · automation-intelligence/
├── production-support/      ← Sprint 9 ✓
└── enterprise-quality/      ← Sprint 10 ✓
```

## Specialized Skills

| Skill | Path |
|-------|------|
| Metadata Impact Analyzer (MIA) | [skills/metadata-impact-analyzer/SKILL.md](skills/metadata-impact-analyzer/SKILL.md) |
| SOQL Validation Assistant (SOVA) | [skills/soql-validation-assistant/SKILL.md](skills/soql-validation-assistant/SKILL.md) |
| Permission Testing Agent (PTA) | [skills/permission-testing-agent/SKILL.md](skills/permission-testing-agent/SKILL.md) |
| Agentforce Testing (AFT) | [skills/agentforce-testing/SKILL.md](skills/agentforce-testing/SKILL.md) |
| Field Service Testing (FSQA) | [skills/field-service-testing/SKILL.md](skills/field-service-testing/SKILL.md) |
| Test Data Generator (TDG) | [skills/test-data-generator/SKILL.md](skills/test-data-generator/SKILL.md) |
| Playwright Review (PWR) | [skills/playwright-review/SKILL.md](skills/playwright-review/SKILL.md) |
| OmniStudio QA (OSQA) | [skills/omnistudio-qa/SKILL.md](skills/omnistudio-qa/SKILL.md) |
| Data Migration QA (DMQA) | [skills/data-migration-qa/SKILL.md](skills/data-migration-qa/SKILL.md) |
| Production RCA (PRCA) | [skills/production-rca/SKILL.md](skills/production-rca/SKILL.md) *(scaffold)* |
| Risk-Based Regression (RBRR) | [skills/risk-based-regression/SKILL.md](skills/risk-based-regression/SKILL.md) *(scaffold)* |
| Salesforce Functional Testing (SFT) | [skills/salesforce-functional-testing/SKILL.md](skills/salesforce-functional-testing/SKILL.md) |
| LWC & Flow UI Testing (LFUT) | [skills/lwc-flow-ui-testing/SKILL.md](skills/lwc-flow-ui-testing/SKILL.md) |
| Salesforce PO/UAT Testing (SPUAT) | [skills/salesforce-uat-po-testing/SKILL.md](skills/salesforce-uat-po-testing/SKILL.md) |
| ADO Test Case Designer (ATCD) | [skills/ado-test-case-designer/SKILL.md](skills/ado-test-case-designer/SKILL.md) |
| ADO Defect Logger (ADL) | [skills/ado-defect-logger/SKILL.md](skills/ado-defect-logger/SKILL.md) |
| Salesforce Specialized Testing (SST) | [skills/salesforce-specialized-testing/SKILL.md](skills/salesforce-specialized-testing/SKILL.md) |

Index: [skills/README.md](skills/README.md) · Registry: [skill-config.yaml](skill-config.yaml)

## Sprint Map

| Sprint | Theme | Status |
|--------|-------|--------|
| 0–10 | Brain → Enterprise Advisory | Complete |
| **11** | **Validation & Certification** | **Complete** |
| Optional | Continuous evolution / Regression Intelligence deep-pack | Planned |

## Quick Start

1. [skill.md](skill.md)  
2. [enterprise-orchestrator/](enterprise-orchestrator/README.md)  
3. Delivery engines → Sprint 10 advisory when needed  
4. [validation/](validation/README.md) to certify / regress / improve the framework  

## Related Documents

| Document | Path |
|----------|------|
| Skill | [skill.md](skill.md) |
| Validation Engine | [validation/enterprise-validation-engine.md](validation/enterprise-validation-engine.md) |
| Roadmap | [ROADMAP.md](ROADMAP.md) |
| Changelog | [CHANGELOG.md](CHANGELOG.md) |

## Navigation

- **Next:** [skill.md](skill.md)
- **See Also:** [validation/README.md](validation/README.md)
