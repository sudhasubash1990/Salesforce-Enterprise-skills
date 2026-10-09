---
title: SEACF AI Hardening Program
version: 0.3.0
tags: [framework-core, governance, hardening]
status: draft
last_updated: 2026-10-09
---

# SEACF AI Hardening Program

Program controls for P0/P1 AI hardening: repository change plan, definition of done, Cursor implementation checklist, final report format, and repository-specific notes.

## Repository change plan

| Phase | Action | Expected result | Status |
|-------|--------|-----------------|--------|
| 1 | Add instruction precedence, grounding, security and Responsible AI contracts | Tier-0 behavior becomes explicit | **Done (P0)** |
| 2 | Wire contracts into Framework Core routing and BA/QE skill entry points | Existing skills inherit controls | **Done (P0)** |
| 3 | Add tool governance and agent state model | Actions become permissioned and auditable | **Done (P0 tools + P1 state)** |
| 4 | Extend validation schemas and tests | New policies become regression-testable | **Done (P0+P1 contract tests)** |
| 5 | Update prompt catalogs to reference grounding/assumption/validation rules | Prompt behavior becomes consistent | **In progress** — [prompt-contract.md](prompt-contract.md) + catalog pointers |
| 6 | Update README, module integration, docs indexes and CHANGELOG | Repository stays navigable and versioned | **Done / ongoing** |
| 7 | Run existing + new benchmark/regression suites | Confirm no unacceptable regression | **Done (deterministic)** — LLM red-team deferred |

Canonical packs: [../README.md](../README.md) · reports: [../../docs/implementation-reports/](../../docs/implementation-reports/).

## Definition of Done

- [x] Every active skill has a clear route to Tier-0 security, Responsible AI, grounding and instruction-precedence contracts (`tier-0-manifest.yaml` + skill Pre-Execution Gates).
- [x] Retrieved content cannot override governing instructions ([instruction-precedence.md](instruction-precedence.md); ADV injection suite).
- [x] Material claims support evidence classification and assumptions are explicit ([grounding-policy.md](../grounding/grounding-policy.md), [claim-validation.md](../grounding/claim-validation.md)).
- [x] Tools/actions are assigned a risk tier and approval policy ([tool-governance.md](../tools/tool-governance.md), T0–T4).
- [x] Context classes have lifecycle and isolation rules ([context-policy.md](../orchestration/context-policy.md) A–H).
- [x] Agent workflows have safe execution states and failure paths ([execution-state-model.md](../orchestration/execution-state-model.md)).
- [x] AI-specific adversarial tests exist and run with regression suites ([red-team-suite.md](../evaluation/red-team-suite.md); ADV fixtures; pytest).
- [x] New documents are indexed and linked; CHANGELOG/version metadata is updated.
- [x] Existing BA/QE golden flows remain functional or intentional breaking changes are documented (retriever tests pass; no intentional breaks).
- [x] Standard skill + prompt contracts published; BA/QE thin skill-contract YAML aligned without breaking discovery.

## Cursor implementation checklist

- [x] Inventory existing files before creating new ones; map overlaps.
- [x] Implement P0 policies first.
- [x] Update Framework Core README/navigation.
- [x] Wire BA `skill.md` to new Tier-0 contracts.
- [x] Wire QE `skill.md`/orchestrator to new Tier-0 contracts.
- [x] Extend context retriever/router only where needed; avoid duplicated retrieval logic (manifest-driven `always_load` only).
- [x] Add validation schemas/lint checks for MUST/MUST NOT rules where automatable (`framework_core_contract_registry.yaml`, claim checker).
- [x] Add adversarial/golden scenarios (ADV + AI reliability fixtures).
- [x] Run repository validators and relevant tests (contracts PASS; full metadata FAIL pre-existing).
- [x] Update root README / ROADMAP only if scope/status changes, and CHANGELOG.
- [x] Produce implementation report with changed files and validation evidence.
- [x] Publish skill-contract + prompt-contract; align BA/QE thin contracts.

## Suggested final report format

Use this structure for consolidated hardening reports (see [../../docs/implementation-reports/seacf-ai-hardening-implementation-report.md](../../docs/implementation-reports/seacf-ai-hardening-implementation-report.md)):

```markdown
# SEACF AI Hardening Implementation Report
## Summary
## Files Created
## Files Modified
## Contracts Added
## Routing/Loading Changes
## Validation Tests Added
## Existing Tests Run
## Results
## Backward-Compatibility Notes
## Deferred Items / Risks
## Recommended Next Iteration
```

## Repository-specific notes

The repository exposes Framework Core (orchestration, shared knowledge, governance, evaluation), BA and QE modules, a root prompt library, context retrieval/routing utilities, governance/quality standards, and BA pre-response validation/anti-hallucination modules.

Hardening **extends** those structures rather than replacing them:

| Concern | Canonical | Specialization |
|---------|-----------|----------------|
| Routing | `framework-core/orchestration/` | BA `.cursor/rules/routing.mdc` + `retrieve_context.py`; QE Enterprise Orchestrator |
| Grounding | `framework-core/grounding/` | BA `anti-hallucination.md` / `validation-framework.md` |
| RAI | `framework-core/responsible-ai/` | QE `enterprise-quality/ai-governance/responsible-ai.md` |
| Prompts | [prompt-contract.md](prompt-contract.md) | `prompts/`, module `prompts.md` |
| Skills | [skill-contract.md](skill-contract.md) | `skill.md` + Cursor stubs + thin `skill-contract.yaml` |

**Source posture:** Architecture recommendation reconciled against this workspace (2026-10-09). Proposed paths are created only after inventory to prevent duplication ([docs/multi-lens-policy.md](../../docs/multi-lens-policy.md)).

## Related Documents

- [skill-contract.md](skill-contract.md)
- [prompt-contract.md](prompt-contract.md)
- [../tier-0-manifest.yaml](../tier-0-manifest.yaml)
