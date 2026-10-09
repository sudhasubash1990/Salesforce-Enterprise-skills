---
title: Evaluation
version: 0.3.0
tags: [framework-core, evaluation]
---

# Evaluation

## Purpose

Cross-module benchmarking, scoring, certification, and release-readiness contracts — plus AI reliability / red-team suites.

## Documents

| Document | Focus |
|----------|-------|
| [benchmark-engine.md](benchmark-engine.md) | Industry/capability benchmarks |
| [scoring-model.md](scoring-model.md) | Weighted Pass/Partial/Fail |
| [certification-engine.md](certification-engine.md) | Bronze→Enterprise Certified methodology |
| [release-readiness.md](release-readiness.md) | Framework + Salesforce seasonal readiness |
| [red-team-suite.md](red-team-suite.md) | AI reliability suites and pass criteria |
| [ai-reliability-scenarios.yaml](ai-reliability-scenarios.yaml) | Scenario catalog (GRD/CTX/HALL/… + ADV reuse) |

## AI safety / adversarial

- Injection contract fixtures: [../security/adversarial-scenarios.yaml](../security/adversarial-scenarios.yaml)
- P1 reliability suite: [red-team-suite.md](red-team-suite.md) + `fixtures/`
- Deterministic pytest via `scripts/test_framework_core_contracts.py` and `scripts/test_retrieve_context.py`
- **Deferred:** live LLM-executed red-team runner (manual use of fixtures until then)

## Module implementations

- QE: [validation/](../../salesforce-quality-engineering/validation/README.md) (Sprint 11)  
- BA: [validation/](../../salesforce-business-analyst/validation/README.md)  

## Navigation

- **Up:** [../README.md](../README.md)
