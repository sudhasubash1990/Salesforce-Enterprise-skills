#!/usr/bin/env python3
"""Generate salesforce-quality-engineering/validation/ pack."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VAL = ROOT / "salesforce-quality-engineering" / "validation"
INDUSTRIES = ["utilities", "retail", "banking", "healthcare", "insurance", "telecom"]


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")
    print("WRITE", path.relative_to(ROOT))


def domain_doc(
    title: str,
    purpose: str,
    sprint: str,
    engine_path: str,
    checks: list[str],
) -> str:
    checklist = "\n".join(f"- [ ] {c}" for c in checks)
    return f"""---
title: {title}
module: Salesforce Quality Engineering
category: Validation
document_type: Checklist
version: 0.13.0
status: draft
last_updated: 2026-07-18
tags: [validation, qe, {sprint}]
---

# {title}

## Purpose

{purpose}

## Business Context

Use before claiming the QE skill (or a delivery artifact) is ready for the corresponding capability. Complements BA validation; does not replace Legal/Compliance or formal audit certification.

## Scope

**In:** Structural presence, routing, anti-hallucination rules, and sample artifact quality for {sprint}.  
**Out:** Inventing metrics, pass rates, or compliance attestations; executing live org tests.

## Assessment Criteria

| Criterion | Pass |
|-----------|------|
| Engine/entry loadable | Path resolves; README present |
| Hard rules visible | No-invent / no-scripts / Sev1-first as applicable |
| Traceability | Links to prior sprints without duplication |
| Checklist executable | Human or agent can mark items with evidence |

## Inputs

- Target repository checkout
- Optional sample artifact under `outputs/`
- [validation-checklist.md](validation-checklist.md)

## Outputs

- Pass / Fail / Partial with evidence notes
- Open gaps and remediation owners

## Evaluation Method

1. Confirm capability folder and engine entry exist.  
2. Spot-check hard rules in skill.md Pre-Execution Gate.  
3. Run checklist items; attach file paths as evidence.  
4. Record result in [benchmark-scorecard.md](benchmark-scorecard.md).

## Decision Framework

| Result | Action |
|--------|--------|
| Pass | Capability validated for advisory use |
| Partial | Document gaps; do not claim full readiness |
| Fail | Remediate before demos or certification claims |

## Checklist

{checklist}

## Examples

- Validate `{engine_path}` loads after Enterprise Orchestrator routes a matching request.
- Reject any sample that invents SLA, maturity %, or compliance certification.

## Best Practices

- Cite file paths and Rule/Decision IDs in evidence.
- Prefer thin pointers over duplicated knowledge.
- Align with [docs/multi-lens-policy.md](../../docs/multi-lens-policy.md).

## Common Anti-Patterns

- Green-lighting without opening the engine file
- Treating pointer stubs as full knowledge depth
- Skipping anti-hallucination checks on metrics

## Interview Questions

1. Which hard rule applies to this capability?
2. How does the Enterprise Orchestrator route to this sprint?
3. What evidence proves validation passed?

## Related Documents

- [README.md](README.md)
- [repository-validation.md](repository-validation.md)
- [{engine_path}](../{engine_path})
- [validation-checklist.md](validation-checklist.md)

## Navigation

- **Up:** [README.md](README.md)
- **See also:** [end-to-end-scenarios/README.md](end-to-end-scenarios/README.md)

## Future Enhancements

- Machine-readable JSON results for CI
- Optional link to `scripts/validate_repository.py` hooks
"""


def industry_readme(industry: str) -> str:
    return f"""---
title: E2E Validation — {industry.title()}
version: 0.13.0
tags: [validation, e2e, {industry}]
---

# End-to-End Validation — {industry.title()}

## Purpose

Exercise the QE Enterprise Orchestrator and sprint engines against a **synthetic** {industry} journey (no client PII).

## Scope

**In:** Route plan, requirement analysis, test design objectives, defect/automation/ops/advisory touchpoints as triggered.  
**Out:** Live org execution; inventing industry regulations.

## Scenario seed

Reuse BA industry packs where present: `salesforce-business-analyst/scenarios/{industry}/`  
QE industry knowledge: `salesforce-quality-engineering/knowledge/industry/` (if available).

## Validation steps

1. Prompt: industry-flavored incomplete story → confirm Sprint 2 analysis (not jump to cases).  
2. Prompt: generate scenarios → confirm Sprint 3 design engine before cases.  
3. Prompt: production incident → confirm Sprint 9 first.  
4. Prompt: portfolio/exec health → confirm Sprint 10 advisory sink.  
5. Record Route lines and gaps in parent [benchmark-scorecard.md](../benchmark-scorecard.md).

## Pass criteria

- [ ] Orchestrator route stated
- [ ] Upstream gates respected
- [ ] No invented KPIs/SLA/maturity
- [ ] Cross-links to BA scenario without duplicating BA authorship

## Related

- [../README.md](../README.md)
- [../../scenarios/README.md](../../scenarios/README.md)
- [../../../salesforce-business-analyst/scenarios/](../../../salesforce-business-analyst/scenarios/)
"""


def main() -> None:
    write(
        VAL / "README.md",
        """---
title: QE Validation Hub
module: Salesforce Quality Engineering
category: Validation
document_type: Framework
version: 0.13.0
status: draft
last_updated: 2026-07-18
tags: [validation, qe, certification]
---

# Salesforce Quality Engineering — Validation

## Purpose

Validate that SEACF Module 2 (Salesforce Quality Engineering) is structurally complete, correctly routed, and safe to use as an Enterprise Quality Advisory Platform—from requirement analysis through production and Sprint 10 advisory.

## Business Context

After Sprints 1–10 and the Enterprise Orchestrator, the module needs a **certification-style** validation layer (parallel to BA `salesforce-business-analyst/validation/`) so teams can prove readiness without inventing scores.

## Scope

| In | Out |
|----|-----|
| Repo/structure checks for QE module | Live Salesforce org testing |
| Capability checklists per sprint engine | Formal external ISO/SOC certification |
| Industry E2E tabletop scenarios | Client PII or real meter/account data |
| Benchmark scorecard + regression suite for the *skill* | Invented maturity or KPI targets |

## Folder map

| Path | Focus |
|------|-------|
| [validation-checklist.md](validation-checklist.md) | Master checklist |
| [repository-validation.md](repository-validation.md) | Structure, links, README hygiene |
| [knowledge-validation.md](knowledge-validation.md) | 4A/4B + engines knowledge |
| [requirement-validation.md](requirement-validation.md) | Sprint 2 |
| [test-design-validation.md](test-design-validation.md) | Sprint 3 |
| [documentation-validation.md](documentation-validation.md) | Sprint 5 |
| [ado-validation.md](ado-validation.md) | Sprint 6 |
| [defect-validation.md](defect-validation.md) | Sprint 7 |
| [automation-validation.md](automation-validation.md) | Sprint 8 |
| [production-validation.md](production-validation.md) | Sprint 9 |
| [advisory-validation.md](advisory-validation.md) | Sprint 10 + Orchestrator |
| [end-to-end-scenarios/](end-to-end-scenarios/README.md) | Industry tabletops |
| [benchmark-scorecard.md](benchmark-scorecard.md) | Score recording (evidence-based) |
| [regression-suite.md](regression-suite.md) | Repeatable skill regression prompts |

## How to run

1. Start with [repository-validation.md](repository-validation.md).  
2. Walk sprint validations 2→10 (or risk-based subset).  
3. Run one industry pack under [end-to-end-scenarios/](end-to-end-scenarios/README.md).  
4. Fill [benchmark-scorecard.md](benchmark-scorecard.md).  
5. Optionally re-run [regression-suite.md](regression-suite.md) after major module changes.

```powershell
# Repo-wide helpers (shared with BA)
python scripts/validate_metadata.py
python scripts/validate_repository.py
```

## Inputs / Outputs

- **Inputs:** This checkout; optional `outputs/` samples  
- **Outputs:** Completed scorecard; gap list; Pass/Partial/Fail per capability

## Navigation

- **Up:** [../README.md](../README.md) · [../skill.md](../skill.md)
- **Orchestrator:** [../enterprise-orchestrator/README.md](../enterprise-orchestrator/README.md)
- **BA validation (sibling):** [../../salesforce-business-analyst/validation/README.md](../../salesforce-business-analyst/validation/README.md)

## Related Documents

- [docs/multi-lens-policy.md](../../docs/multi-lens-policy.md)
- [docs/quality-framework.md](../../docs/quality-framework.md) (if present)
- [../enterprise-quality/README.md](../enterprise-quality/README.md)

## Future Enhancements

- CI job publishing validation JSON
- Auto-assert Orchestrator route plans in tests
""",
    )

    write(
        VAL / "validation-checklist.md",
        """---
title: QE Master Validation Checklist
version: 0.13.0
tags: [validation, checklist]
---

# QE Master Validation Checklist

## Purpose

Single checklist spanning repository, knowledge, sprint engines, orchestrator, advisory, and industry E2E.

## Checklist

### Repository & governance

- [ ] `salesforce-quality-engineering/skill.md` loads; version current
- [ ] `enterprise-orchestrator/` present and wired in Pre-Execution Gate
- [ ] Major L1 folders have README.md
- [ ] Multi-lens pointers resolve to canonical knowledge
- [ ] No invented metrics in sample outputs under review

### Sprint capabilities

- [ ] Sprint 2 Requirement Analysis — [requirement-validation.md](requirement-validation.md)
- [ ] Sprint 3 Test Design — [test-design-validation.md](test-design-validation.md)
- [ ] Sprint 4A/4B Knowledge — [knowledge-validation.md](knowledge-validation.md)
- [ ] Sprint 5 Documentation — [documentation-validation.md](documentation-validation.md)
- [ ] Sprint 6 ADO — [ado-validation.md](ado-validation.md)
- [ ] Sprint 7 Defect Intelligence — [defect-validation.md](defect-validation.md)
- [ ] Sprint 8 Automation Intelligence — [automation-validation.md](automation-validation.md)
- [ ] Sprint 9 Production Support — [production-validation.md](production-validation.md)
- [ ] Sprint 10 Advisory + Orchestrator — [advisory-validation.md](advisory-validation.md)

### End-to-end

- [ ] At least one industry scenario executed — [end-to-end-scenarios/](end-to-end-scenarios/README.md)
- [ ] Benchmark scorecard updated — [benchmark-scorecard.md](benchmark-scorecard.md)
- [ ] Skill regression suite sampled — [regression-suite.md](regression-suite.md)

## Scoring note

Do **not** invent percentage scores. Use Pass / Partial / Fail per row with evidence paths.
""",
    )

    specs = [
        (
            "repository-validation.md",
            "Repository Validation",
            "Validate QE module structure, READMEs, link hygiene, and orchestrator wiring.",
            "repository",
            "README.md",
            [
                "skill.md, README.md, prompts.md, CHANGELOG.md, ROADMAP.md exist",
                "enterprise-orchestrator/, brain/, knowledge/, templates/, ado/, quality-intelligence/, automation-intelligence/, production-support/, enterprise-quality/, validation/ exist",
                "Pre-Execution Gate mentions Enterprise Orchestrator",
                "Legacy automation/ is pointer-only",
                "docs/multi-lens-policy.md exists and is referenced",
                "Broken critical nav links = Fail (run link scan or validate_repository.py)",
            ],
        ),
        (
            "knowledge-validation.md",
            "Knowledge Validation",
            "Validate Sprint 4A/4B and core knowledge engines are present and multi-lens safe.",
            "sprint-4",
            "knowledge/README.md",
            [
                "knowledge/requirement-analysis.md and test-design-engine.md exist",
                "knowledge/platform/, metadata/, security/, data/, clouds/, integration/ present",
                "Canonical platform-events is knowledge/integration/platform-events.md",
                "Root smoke/sanity/regression are pointers to knowledge/release/",
                "Cloud canonicals under knowledge/clouds/ for multi-lens topics",
            ],
        ),
        (
            "requirement-validation.md",
            "Requirement Validation",
            "Validate Sprint 2 Requirement Analysis Engine behaviour and gates.",
            "sprint-2",
            "knowledge/requirement-analysis.md",
            [
                "Incomplete story yields gaps/questions—not detailed test cases",
                "Salesforce component scan section present in engine",
                "skill.md marks Requirement Analysis mandatory before strategy/cases",
                "Cross-link to BA skill without BA story authorship duplication",
            ],
        ),
        (
            "test-design-validation.md",
            "Test Design Validation",
            "Validate Sprint 3 Test Design Engine produces scenarios/coverage before cases.",
            "sprint-3",
            "knowledge/test-design-engine.md",
            [
                "Engine forbids jumping straight to detailed cases",
                "Coverage matrix / regression scope / automation readiness concepts present",
                "Techniques articles link from design engine",
                "Orchestrator routes scenario asks to Sprint 3 after Sprint 2 when needed",
            ],
        ),
        (
            "documentation-validation.md",
            "Documentation Validation",
            "Validate Sprint 5 templates, guidelines, and document-generation pack.",
            "sprint-5",
            "templates/README.md",
            [
                "templates/, guidelines/, document-generation/, playbooks/ exist",
                "deliverable-selection.md and document-generation-rules.md exist",
                "Test Strategy template exists",
                "Generated outputs under outputs/ follow metadata + conversion practice when published",
            ],
        ),
        (
            "ado-validation.md",
            "ADO Validation",
            "Validate Sprint 6 Azure DevOps Delivery Intelligence pack.",
            "sprint-6",
            "ado/README.md",
            [
                "ado/ work-item folders and relationship-model present",
                "Hard rule: no invented API publish unless explicitly requested",
                "BA ado-backlog-integration cross-link present (sibling)",
                "ado/README Related links resolve inside module (../brain etc.)",
            ],
        ),
        (
            "defect-validation.md",
            "Defect Validation",
            "Validate Sprint 7 Defect Intelligence and Rules Engine.",
            "sprint-7",
            "quality-intelligence/defect-intelligence-engine.md",
            [
                "quality-intelligence/ and rules/ present",
                "Hard rule: no invented leakage % / metrics without data",
                "Rules cite Rule IDs pattern documented",
                "RCA reuses Sprint 5 templates by reference",
            ],
        ),
        (
            "automation-validation.md",
            "Automation Validation",
            "Validate Sprint 8 Automation Intelligence and Review Engine.",
            "sprint-8",
            "automation-intelligence/automation-intelligence-engine.md",
            [
                "automation-intelligence/ engines and review-engine/ present",
                "Hard rule: no full automation script generation by default",
                "Playwright-first but framework-agnostic stated",
                "Legacy automation/ points to automation-intelligence/",
            ],
        ),
        (
            "production-validation.md",
            "Production Validation",
            "Validate Sprint 9 Production Support and Operations Intelligence.",
            "sprint-9",
            "production-support/production-support-engine.md",
            [
                "production-support/ and operations-intelligence/ present",
                "Sev1 restore-first rule documented",
                "Hard rule: no invented SLA/MTTR/KPI",
                "Orchestrator prioritizes Sprint 9 on production-down signals",
            ],
        ),
        (
            "advisory-validation.md",
            "Advisory Validation",
            "Validate Sprint 10 Enterprise Quality Advisory and Enterprise Orchestrator.",
            "sprint-10",
            "enterprise-quality/enterprise-quality-advisory-engine.md",
            [
                "enterprise-quality/ advisory engine and decision/recommendation engines present",
                "enterprise-orchestrator/ routes to Sprint 10 for exec/portfolio/health",
                "Hard rule: no invented maturity/compliance scores",
                "Project health assessment states confidence and RAG without fake %",
                "Prompts include Orchestrate QE Request and Sprint 10 advisory prompts",
            ],
        ),
    ]

    for filename, title, purpose, sprint, engine, checks in specs:
        write(VAL / filename, domain_doc(title, purpose, sprint, engine, checks))

    write(
        VAL / "end-to-end-scenarios" / "README.md",
        """---
title: E2E Validation Scenarios
version: 0.13.0
tags: [validation, e2e]
---

# End-to-End Validation Scenarios

## Purpose

Tabletop industry journeys that exercise Orchestrator → sprint engines → advisory sink.

## Industries

| Industry | Path |
|----------|------|
| Utilities | [utilities/](utilities/README.md) |
| Retail | [retail/](retail/README.md) |
| Banking | [banking/](banking/README.md) |
| Healthcare | [healthcare/](healthcare/README.md) |
| Insurance | [insurance/](insurance/README.md) |
| Telecom | [telecom/](telecom/README.md) |

## Method

Run as **desktop exercises** with the QE skill loaded. Record Route lines and Pass/Partial/Fail on the [benchmark-scorecard.md](../benchmark-scorecard.md).

## Related

- [../README.md](../README.md)
- [../../scenarios/README.md](../../scenarios/README.md)
""",
    )

    for ind in INDUSTRIES:
        write(VAL / "end-to-end-scenarios" / ind / "README.md", industry_readme(ind))
        # one seed scenario file per industry
        write(
            VAL / "end-to-end-scenarios" / ind / "scenario-validation.md",
            f"""---
title: {ind.title()} Scenario Validation Script
version: 0.13.0
tags: [validation, e2e, {ind}]
---

# {ind.title()} — Scenario Validation Script

## Purpose

Executable prompt sequence for {ind} tabletop validation.

## Prompts (run in order)

1. **Incomplete story** — e.g. "User needs to complete a critical {ind} transaction in Salesforce."  
   Expect: Sprint 2 analysis, gaps, no detailed cases.

2. **Test strategy ask** — after assumptions stated.  
   Expect: Sprint 5 strategy with assumptions; entry blocked without AC if gates enforced.

3. **Production symptom** — e.g. "Production users cannot complete the {ind} transaction."  
   Expect: Sprint 9 triage first; no invented SLA.

4. **Exec health** — paste synthetic RAG signals.  
   Expect: Sprint 10 project health; Hold/Escalate style decision; no fake maturity %.

## Evidence log

| Step | Route observed | Result (Pass/Partial/Fail) | Notes |
|------|----------------|----------------------------|-------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |

## Related

- [README.md](README.md)
- [../../benchmark-scorecard.md](../../benchmark-scorecard.md)
""",
        )

    write(
        VAL / "benchmark-scorecard.md",
        """---
title: QE Benchmark Scorecard
version: 0.13.0
tags: [validation, benchmark]
---

# QE Benchmark Scorecard

## Purpose

Record evidence-based Pass / Partial / Fail results for QE module validation. **Do not invent numeric maturity or percentage scores.**

## Assessment session

| Field | Value |
|-------|--------|
| Date | |
| Assessor | |
| Repo commit / version | |
| QE module version (skill.md) | |
| Overall result | Pass / Partial / Fail |

## Capability results

| Area | Result | Evidence (paths) | Gaps |
|------|--------|------------------|------|
| Repository | | | |
| Knowledge 4A/4B | | | |
| Requirement (S2) | | | |
| Test Design (S3) | | | |
| Documentation (S5) | | | |
| ADO (S6) | | | |
| Defect (S7) | | | |
| Automation (S8) | | | |
| Production (S9) | | | |
| Advisory + Orchestrator (S10) | | | |
| E2E industry (name) | | | |
| Regression suite sample | | | |

## Decision

| Recommendation | Rationale |
|----------------|-----------|
| Ready for advisory demos | |
| Ready with caveats | |
| Not ready | |

## Sign-off

| Role | Name | Date |
|------|------|------|
| QE Practice Lead | | |
| Assessor | | |
""",
    )

    write(
        VAL / "regression-suite.md",
        """---
title: QE Skill Regression Suite
version: 0.13.0
tags: [validation, regression]
---

# QE Skill Regression Suite

## Purpose

Repeatable prompt pack to detect **skill regressions** after module changes (Orchestrator, engines, pointers, gates).

## Scope

**In:** Behavioural checks (routing, gates, anti-hallucination).  
**Out:** Full industry UAT; live org automation.

## Suite (minimum)

| ID | Prompt intent | Expect |
|----|---------------|--------|
| REG-01 | Incomplete story | Sprint 2 analysis only |
| REG-02 | "Generate test cases now" without analysis | Gate: analysis/design first or explicit waiver |
| REG-03 | "Write Playwright script for login" | Sprint 8 design/review; no full script dump |
| REG-04 | "Sev1 production down" | Sprint 9 first |
| REG-05 | "Assess project health" + thin metrics | Sprint 10; RAG + no invented maturity % |
| REG-06 | "Orchestrate this request" multi-hop | Route line + COMP pattern |
| REG-07 | Record Types / Platform Events explain | Canonical knowledge path; multi-lens OK |
| REG-08 | Pointer file (e.g. smoke-testing.md) | Resolves to release/ canonical |

## Execution log

| ID | Build/version | Result | Notes |
|----|---------------|--------|-------|
| REG-01 | | | |
| REG-02 | | | |
| REG-03 | | | |
| REG-04 | | | |
| REG-05 | | | |
| REG-06 | | | |
| REG-07 | | | |
| REG-08 | | | |

## Cadence

Run after each sprint pack change, Orchestrator change, or multi-lens bulk edit.

## Related

- [README.md](README.md)
- [benchmark-scorecard.md](benchmark-scorecard.md)
- [../enterprise-orchestrator/README.md](../enterprise-orchestrator/README.md)
""",
    )

    print("DONE", VAL)


if __name__ == "__main__":
    main()
