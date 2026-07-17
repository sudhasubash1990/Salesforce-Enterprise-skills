#!/usr/bin/env python3
"""Generate framework-core/ — reusable SEACF foundation for all modules."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FC = ROOT / "framework-core"
VER = "0.1.0"

MODULES = [
    ("salesforce-business-analyst", "Business Analyst", "BA"),
    ("salesforce-quality-engineering", "Quality Engineering", "QE"),
    ("salesforce-solution-architect", "Solution Architect", "SA"),  # future
    ("salesforce-developer", "Developer", "DEV"),  # future
    ("salesforce-devops", "DevOps", "DO"),  # future
    ("salesforce-production-support", "Production Support", "PS"),  # future module pack
]


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")
    print("WRITE", path.relative_to(ROOT))


def std_doc(
    title: str,
    purpose: str,
    body: str,
    related: str,
) -> str:
    return f"""---
title: {title}
version: {VER}
tags: [framework-core]
status: draft
last_updated: 2026-07-18
---

# {title}

## Purpose

{purpose}

## Scope

**In:** Cross-module SEACF contracts reusable by BA, QE, SA, Developer, DevOps, and Production Support packs.  
**Out:** Module-specific deep knowledge (lives in each module); inventing client metrics or certifications.

## Business Context

SEACF modules must share one orchestration, governance, and evaluation language so agents and humans do not re-implement routing, standards, or certification differently per skill.

{body}

## Inputs

- User request / module intent
- Module `skill.md` and brain (when loaded)
- Optional evidence pack

## Outputs

- Route / context / workflow decisions
- References into module engines
- Governance-compliant artifacts

## Navigation

- **Up:** [README.md](../README.md) or parent folder README
- **Core root:** [../README.md](../README.md)

## Related Documents

{related}

## Future Enhancements

- Machine-readable route schemas
- Shared CI hooks for all modules
"""


def main() -> None:
    write(
        FC / "README.md",
        f"""---
title: SEACF Framework Core
version: {VER}
tags: [framework-core, seacf]
status: draft
last_updated: 2026-07-18
---

# SEACF Framework Core

## Purpose

Reusable **Framework Core** for the Salesforce Enterprise AI Consulting Framework (SEACF). Every present and future module—Business Analyst, Quality Engineering, Solution Architect, Developer, DevOps, Production Support—loads this core for orchestration, shared knowledge pointers, governance, and evaluation.

## Business Context

Without a core, each module invents its own router, glossary fork, and certification logic. Framework Core is the **single contract** for:

1. How requests are routed and reasoned  
2. Where shared Salesforce / industry / consulting knowledge lives  
3. How documentation and quality are governed  
4. How modules are benchmarked, scored, and certified  

## Scope

| In | Out |
|----|-----|
| Cross-module orchestration contracts | Full BA/QE/SA domain engines |
| Pointers + thin shared indexes | Duplicating `shared/` or module knowledge bodies |
| Governance & evaluation methodology | Awarding certification without evidence |
| Module integration map | Replacing module `skill.md` |

## Architecture

```
User Request
      │
      ▼
framework-core/orchestration  (route · context · workflow · reasoning)
      │
      ▼
Module skill (BA | QE | SA | DEV | DO | PS)
      │
      ├── module brain + engines
      └── framework-core/shared-knowledge (pointers)
      │
      ▼
framework-core/governance  (standards · versioning · contribution)
      │
      ▼
framework-core/evaluation  (benchmark · score · certify · release readiness)
```

## Folder map

| Path | Role |
|------|------|
| [orchestration/](orchestration/README.md) | Request routing, context, workflow, reasoning pipeline |
| [shared-knowledge/](shared-knowledge/README.md) | Cross-module Salesforce, industry, consulting, glossary |
| [governance/](governance/README.md) | Documentation, quality, versioning, contribution |
| [evaluation/](evaluation/README.md) | Benchmark, scoring, certification, release readiness |

## Module integration

| Module | Status | Skill entry | Uses core |
|--------|--------|-------------|-----------|
| Business Analyst | Active | `salesforce-business-analyst/skill.md` | Load governance + shared-knowledge; BA router remains in `.cursor/rules` |
| Quality Engineering | Active | `salesforce-quality-engineering/skill.md` | Orchestrator aligns to core; validation aligns to evaluation/ |
| Solution Architect | Planned | — | Same contracts |
| Developer | Planned | — | Same contracts |
| DevOps | Planned | — | Same contracts |
| Production Support (standalone pack) | Planned | — | QE Sprint 9 remains until pack extracts |

**Rule:** Module engines own depth. Framework Core owns **contracts and shared indexes**. Prefer link over copy ([docs/multi-lens-policy.md](../docs/multi-lens-policy.md) themes apply cross-module).

## Relationship to existing repo roots

| Existing | Relationship |
|----------|----------------|
| [`shared/`](../shared/README.md) | Canonical enterprise files; `shared-knowledge/` indexes and extends |
| [`docs/`](../docs/README.md) | Repo governance; `governance/` summarizes + points here |
| QE `enterprise-orchestrator/` | Module-specific router; implements core orchestration contracts |
| QE `validation/` (Sprint 11) | Module evaluation pack; implements core evaluation contracts |
| BA `validation/` | BA certification; maps to core evaluation |

## Inputs / Outputs

- **Inputs:** Any SEACF user request  
- **Outputs:** Route plan, loaded module bundle, governed deliverable, optional evaluation

## Navigation

- **Repo root:** [../README.md](../README.md)
- **Roadmap:** [../ROADMAP.md](../ROADMAP.md)

## Related Documents

- [orchestration/request-router.md](orchestration/request-router.md)
- [governance/documentation-standards.md](governance/documentation-standards.md)
- [evaluation/certification-engine.md](evaluation/certification-engine.md)

## Future Enhancements

- `scripts/retrieve_context.py` routes that include framework-core by default
- SA/DEV/DO/PS module scaffolds that import this core on day one
""",
    )

    # --- Orchestration ---
    write(
        FC / "orchestration" / "README.md",
        f"""---
title: Orchestration
version: {VER}
tags: [framework-core, orchestration]
---

# Orchestration

## Purpose

Cross-module request routing, context assembly, workflow execution, and reasoning pipeline contracts.

## Scope

Contracts only. Module routers (e.g. QE `enterprise-orchestrator/`, BA `.cursor/rules/routing.mdc`) **implement** these contracts.

## Documents

| Document | Focus |
|----------|-------|
| [request-router.md](request-router.md) | Intent → module → capability |
| [context-manager.md](context-manager.md) | What to load; progressive disclosure |
| [workflow-engine.md](workflow-engine.md) | Multi-step composition patterns |
| [reasoning-pipeline.md](reasoning-pipeline.md) | Shared think → decide → deliver flow |

## Navigation

- **Up:** [../README.md](../README.md)
""",
    )

    write(
        FC / "orchestration" / "request-router.md",
        std_doc(
            "Request Router",
            "Classify intent and route to the correct SEACF module and capability engine.",
            """
## Evaluation Method

1. Detect **discipline** (BA / QE / SA / DEV / DO / PS).  
2. Detect **capability** within module (e.g. BRD vs user story; requirement analysis vs advisory).  
3. Emit Route line: `Module · Primary capability · Support · Advisory/Validation`.  
4. Hand off to module skill Pre-Execution Gate.

## Decision Framework

| Signal | Module |
|--------|--------|
| BRD, FRD, user story, fit-gap, workshop, KPI, OCM | Business Analyst |
| Test strategy, defects, automation, UAT quality, prod incident QE lens, project health | Quality Engineering |
| Target architecture, integration design, Well-Architected | Solution Architect (when pack exists) |
| Apex/LWC implementation, package, metadata deploy code | Developer (when pack exists) |
| Pipeline, CI/CD, environments, DevOps Center | DevOps (when pack exists) |
| Incident/problem/change ops (standalone pack) | Production Support pack — until then QE Sprint 9 |

## Ambiguity

If discipline unclear → ask **one** clarifying question. Prefer BA for requirements authorship; QE for testability/quality; SA for architecture decisions.

## Module implementations

- QE: [salesforce-quality-engineering/enterprise-orchestrator/](../../salesforce-quality-engineering/enterprise-orchestrator/README.md)
- BA: [.cursor/rules/routing.mdc](../../.cursor/rules/routing.mdc) + `scripts/retrieve_context.py`
""",
            "- [context-manager.md](context-manager.md)\n- [workflow-engine.md](workflow-engine.md)\n- [../README.md](../README.md)",
        ),
    )

    write(
        FC / "orchestration" / "context-manager.md",
        std_doc(
            "Context Manager",
            "Define progressive disclosure: load the minimum file bundle for a request.",
            """
## Loading tiers

| Tier | Load | When |
|------|------|------|
| 0 | `framework-core/` contracts (this pack) | Any SEACF task |
| 1 | Module `skill.md` + identity/brain entry | Any module task |
| 2 | Task engines (analysis, design, templates) | Per intent |
| 3 | Deep knowledge articles | Only when component/cloud implicated |
| 4 | Evaluation / certification | When validating the framework or module |

## Rules

1. **Do not** preload all modules.  
2. Prefer README → engine → article.  
3. Shared knowledge via [../shared-knowledge/](../shared-knowledge/README.md) before copying into a module.  
4. Mark assumptions when context is missing.
""",
            "- [request-router.md](request-router.md)\n- [../../shared/README.md](../../shared/README.md)",
        ),
    )

    write(
        FC / "orchestration" / "workflow-engine.md",
        std_doc(
            "Workflow Engine",
            "Compose multi-step consulting workflows across and within modules.",
            """
## Standard composition patterns

| Pattern | Order |
|---------|-------|
| Requirements → Stories | BA analysis → BA stories → (optional) QE testability review |
| Story → Test design | QE Sprint 2 → Sprint 3 → Sprint 5 docs |
| Defect → Prevention | QE Sprint 7 → 8/9 as needed → 10 if exec |
| Incident → Restore | PS/QE Sprint 9 first → RCA → advisory |
| Architecture decision | SA (or open question) → BA/QE impact |
| Framework certify | evaluation/ + module validation packs |

## Handoff contract

Every hop passes: IDs, assumptions, open questions, evidence refs, residual risk.
""",
            "- [reasoning-pipeline.md](reasoning-pipeline.md)\n- QE [composition-patterns.md](../../salesforce-quality-engineering/enterprise-orchestrator/composition-patterns.md)",
        ),
    )

    write(
        FC / "orchestration" / "reasoning-pipeline.md",
        std_doc(
            "Reasoning Pipeline",
            "Shared think → decide → deliver pipeline for all SEACF agents.",
            """
## Pipeline

```
Receive request
    → Route (request-router)
    → Assemble context (context-manager)
    → Module Pre-Execution Gate
    → Reason (facts vs assumptions; risks; options)
    → Decide (proceed / clarify / escalate)
    → Deliver (template-aligned artifact)
    → Self-check (anti-hallucination; traceability)
```

## Hard rules (all modules)

1. Never invent regulatory requirements, SLA/KPI %, or certification levels without evidence.  
2. Separate **Facts** vs **Assumptions**.  
3. Prefer platform-native Salesforce solutions before custom.  
4. Do not bypass security/sharing controls in recommendations.  
5. Pause on multi-cloud scope, undefined compliance, or material buy/build decisions.
""",
            "- [../governance/quality-standards.md](../governance/quality-standards.md)\n- BA brain / QE brain module files",
        ),
    )

    # --- Shared knowledge ---
    write(
        FC / "shared-knowledge" / "README.md",
        f"""---
title: Shared Knowledge
version: {VER}
tags: [framework-core, shared-knowledge]
---

# Shared Knowledge

## Purpose

Cross-module indexes into Salesforce platform, industries, consulting patterns, and glossary—**without duplicating** canonical files under [`shared/`](../../shared/README.md) or module knowledge trees.

## Scope

Thin indexes + ownership map. Deep articles remain in modules or `shared/`.

## Folders

| Folder | Role |
|--------|------|
| [salesforce-platform/](salesforce-platform/README.md) | Platform capability index |
| [industries/](industries/README.md) | Industry scenario index |
| [consulting-patterns/](consulting-patterns/README.md) | Cross-discipline consulting patterns |
| [enterprise-glossary/](enterprise-glossary/README.md) | Glossary entry points |

## Navigation

- **Up:** [../README.md](../README.md)
- **Canonical shared:** [../../shared/README.md](../../shared/README.md)
""",
    )

    write(
        FC / "shared-knowledge" / "salesforce-platform" / "README.md",
        f"""---
title: Shared Knowledge — Salesforce Platform
version: {VER}
---

# Salesforce Platform (Shared Index)

## Purpose

Point all modules to a common Salesforce capability map and module deep-dives.

## Canonical sources

| Asset | Path |
|-------|------|
| Capability map | [../../../shared/salesforce-capability-map.md](../../../shared/salesforce-capability-map.md) |
| QE platform foundation | [../../../salesforce-quality-engineering/knowledge/platform/](../../../salesforce-quality-engineering/knowledge/platform/README.md) |
| QE clouds | [../../../salesforce-quality-engineering/knowledge/clouds/](../../../salesforce-quality-engineering/knowledge/clouds/README.md) |
| BA clouds overview | [../../../salesforce-business-analyst/knowledge/salesforce-clouds-overview.md](../../../salesforce-business-analyst/knowledge/salesforce-clouds-overview.md) |

## Rule

Modules may add **lens** articles (BA process / QE test / SA architecture). Do not fork a second capability map—extend `shared/salesforce-capability-map.md` or add module lens files.

## Navigation

- **Up:** [../README.md](../README.md)
""",
    )

    write(
        FC / "shared-knowledge" / "industries" / "README.md",
        f"""---
title: Shared Knowledge — Industries
version: {VER}
---

# Industries (Shared Index)

## Purpose

Single industry navigation for all modules.

## Canonical sources

| Industry packs | Path |
|----------------|------|
| BA scenarios | [../../../salesforce-business-analyst/scenarios/](../../../salesforce-business-analyst/scenarios/README.md) |
| QE industry knowledge | [../../../salesforce-quality-engineering/knowledge/industry/](../../../salesforce-quality-engineering/knowledge/industry/README.md) |
| QE benchmarks | [../../../salesforce-quality-engineering/validation/benchmarking/](../../../salesforce-quality-engineering/validation/benchmarking/README.md) |

## Industries (common set)

Utilities · Retail · Banking · Insurance · Healthcare · Manufacturing · Telecom · Public Sector · Energy · Consumer Goods

## Rule

BA owns business scenario narrative; QE owns quality overlay; future SA owns architecture overlay. Link, do not copy full scenarios.

## Navigation

- **Up:** [../README.md](../README.md)
""",
    )

    write(
        FC / "shared-knowledge" / "consulting-patterns" / "README.md",
        f"""---
title: Shared Knowledge — Consulting Patterns
version: {VER}
---

# Consulting Patterns (Shared Index)

## Purpose

Enterprise consulting behaviours shared across disciplines.

## Canonical sources

| Pattern | Path |
|---------|------|
| Consulting principles | [../../../shared/consulting-principles.md](../../../shared/consulting-principles.md) |
| Enterprise standards | [../../../shared/enterprise-standards.md](../../../shared/enterprise-standards.md) |
| Traceability model | [../../../shared/traceability-model.md](../../../shared/traceability-model.md) |
| Output standards | [../../../shared/output-standards.md](../../../shared/output-standards.md) |
| BA brain delta | [../../../salesforce-business-analyst/brain/consulting-principles.md](../../../salesforce-business-analyst/brain/consulting-principles.md) |
| QE brain delta | [../../../salesforce-quality-engineering/brain/consulting-principles.md](../../../salesforce-quality-engineering/brain/consulting-principles.md) |

## Common patterns

- Outcomes over features  
- Options with trade-offs  
- Platform-native first  
- Facts vs assumptions  
- Evidence for go/no-go  

## Navigation

- **Up:** [../README.md](../README.md)
""",
    )

    write(
        FC / "shared-knowledge" / "enterprise-glossary" / "README.md",
        f"""---
title: Shared Knowledge — Enterprise Glossary
version: {VER}
---

# Enterprise Glossary (Shared Index)

## Purpose

One glossary for all modules.

## Canonical source

**[shared/glossary.md](../../../shared/glossary.md)**

Supporting taxonomy: [shared/taxonomy.md](../../../shared/taxonomy.md) · [shared/document-types.md](../../../shared/document-types.md)

## Rule

Add new cross-module terms to `shared/glossary.md`. Module-specific terms may live in module glossaries only if truly local—and must link here.

## Navigation

- **Up:** [../README.md](../README.md)
""",
    )

    # --- Governance ---
    write(
        FC / "governance" / "README.md",
        f"""---
title: Governance
version: {VER}
tags: [framework-core, governance]
---

# Governance

## Purpose

Cross-module documentation, quality, versioning, and contribution contracts.

## Documents

| Document | Focus |
|----------|-------|
| [documentation-standards.md](documentation-standards.md) | Doc structure & cross-linking |
| [quality-standards.md](quality-standards.md) | Quality / anti-hallucination |
| [versioning.md](versioning.md) | Version & CHANGELOG practice |
| [contribution-guide.md](contribution-guide.md) | How modules contribute to core |

## Navigation

- **Up:** [../README.md](../README.md)
- **Repo docs:** [../../docs/README.md](../../docs/README.md)
""",
    )

    write(
        FC / "governance" / "documentation-standards.md",
        std_doc(
            "Documentation Standards",
            "Unify documentation expectations across SEACF modules.",
            """
## Required sections (module articles)

Purpose · Scope · Inputs · Outputs · Navigation · Related Documents  

Deliverables additionally follow [shared/output-standards.md](../../shared/output-standards.md) and module templates.

## Canonical repo standards

| Topic | Path |
|-------|------|
| Markdown | [docs/markdown-standards.md](../../docs/markdown-standards.md) |
| Naming | [docs/naming-conventions.md](../../docs/naming-conventions.md) |
| Metadata | [docs/metadata-schema.md](../../docs/metadata-schema.md) |
| Cross-linking | [docs/cross-linking-framework.md](../../docs/cross-linking-framework.md) |
| Multi-lens | [docs/multi-lens-policy.md](../../docs/multi-lens-policy.md) |
| Output engine | [output-engine/README.md](../../output-engine/README.md) |

## Rule

Framework Core does not replace `docs/`—it **binds modules** to those standards.
""",
            "- [quality-standards.md](quality-standards.md)\n- [../../docs/README.md](../../docs/README.md)",
        ),
    )

    write(
        FC / "governance" / "quality-standards.md",
        std_doc(
            "Quality Standards",
            "Cross-module quality and anti-hallucination bar.",
            """
## Alignment

ISTQB / TMMi themes (QE) · Agile/SAFe quality · ITIL (ops) · TOGAF governance themes (SA) · Salesforce Well-Architected · Responsible AI · [docs/quality-framework.md](../../docs/quality-framework.md)

## Non-negotiables

1. Facts vs assumptions separated  
2. No invented regulatory, SLA, KPI %, maturity, or certification claims  
3. Traceable IDs where requirements/stories/defects exist  
4. Security/sharing respected  
5. Progressive disclosure — link deep packs  

## Module checklists

- BA: `salesforce-business-analyst/checklists.md` + brain validation  
- QE: `salesforce-quality-engineering/validation/` + skill Pre-Execution Gate  
""",
            "- [documentation-standards.md](documentation-standards.md)\n- [../evaluation/scoring-model.md](../evaluation/scoring-model.md)",
        ),
    )

    write(
        FC / "governance" / "versioning.md",
        std_doc(
            "Versioning",
            "Version discipline for framework-core and consuming modules.",
            """
## Canonical

[docs/versioning.md](../../docs/versioning.md) · [docs/release-process.md](../../docs/release-process.md)

## Framework Core

- Semver for `framework-core` (`version` in frontmatter / README)  
- Breaking contract changes → major; new contracts → minor; typos → patch  

## Modules

- Each module keeps its own CHANGELOG / skill version  
- When adopting a new core contract, note core version in module CHANGELOG  

## Rule

Do not case-collide filenames on Windows (`CHANGELOG.md` vs `changelog.md`).
""",
            "- [contribution-guide.md](contribution-guide.md)\n- [../../docs/versioning.md](../../docs/versioning.md)",
        ),
    )

    write(
        FC / "governance" / "contribution-guide.md",
        std_doc(
            "Contribution Guide (Framework Core)",
            "How to extend Framework Core and register new modules.",
            """
## Adding a new module

1. Create `salesforce-<discipline>/` with `skill.md`, `README.md`, `brain/`.  
2. Implement module router that **conforms** to [../orchestration/request-router.md](../orchestration/request-router.md).  
3. Link shared knowledge via [../shared-knowledge/](../shared-knowledge/README.md)—do not fork glossary.  
4. Add module validation under module `validation/` implementing [../evaluation/](../evaluation/README.md).  
5. Register in Framework Core README module table + root [ROADMAP.md](../../ROADMAP.md).  
6. Add Cursor discovery stub under `.cursor/skills/`.  

## Changing a core contract

1. Update the core markdown.  
2. Bump framework-core version.  
3. Note migration in module CHANGELOGs.  
4. Prefer additive changes.

## Also see

[CONTRIBUTING.md](../../CONTRIBUTING.md) · [docs/repository-guidelines.md](../../docs/repository-guidelines.md)
""",
            "- [versioning.md](versioning.md)\n- [../../CONTRIBUTING.md](../../CONTRIBUTING.md)",
        ),
    )

    # --- Evaluation ---
    write(
        FC / "evaluation" / "README.md",
        f"""---
title: Evaluation
version: {VER}
tags: [framework-core, evaluation]
---

# Evaluation

## Purpose

Cross-module benchmarking, scoring, certification, and release-readiness contracts.

## Documents

| Document | Focus |
|----------|-------|
| [benchmark-engine.md](benchmark-engine.md) | Industry/capability benchmarks |
| [scoring-model.md](scoring-model.md) | Weighted Pass/Partial/Fail |
| [certification-engine.md](certification-engine.md) | Bronze→Enterprise Certified methodology |
| [release-readiness.md](release-readiness.md) | Framework + Salesforce seasonal readiness |

## Module implementations

- QE: [validation/](../../salesforce-quality-engineering/validation/README.md) (Sprint 11)  
- BA: [validation/](../../salesforce-business-analyst/validation/README.md)  

## Navigation

- **Up:** [../README.md](../README.md)
""",
    )

    write(
        FC / "evaluation" / "benchmark-engine.md",
        std_doc(
            "Benchmark Engine",
            "Define how modules run industry and capability benchmarks.",
            """
## Contract

Every benchmark includes: Business Context · Requirements seed · Expected Analysis · Expected Risks · Expected Documents · Expected Recommendations · Expected Deliverables · Evaluation Criteria.

## Implementations

- QE industries: `salesforce-quality-engineering/validation/benchmarking/`  
- BA: `salesforce-business-analyst/validation/benchmark-scenarios.md`  

## Rule

Synthetic data only; no client PII; no invented regulations.
""",
            "- [scoring-model.md](scoring-model.md)\n- [certification-engine.md](certification-engine.md)",
        ),
    )

    write(
        FC / "evaluation" / "scoring-model.md",
        std_doc(
            "Scoring Model",
            "Shared Pass / Partial / Fail model with optional weights.",
            """
## Scale

| Result | Value | Meaning |
|--------|-------|---------|
| Pass | 2 | Criteria met with evidence |
| Partial | 1 | Core present; gaps logged |
| Fail | 0 | Missing capability or hard-rule breach |

## Rules

1. **No invented percentages** without completing dimension rows.  
2. Hard-rule Fail (hallucinated SLA/cert/regulation) fails the area regardless of average.  
3. Modules declare weights in their scorecards (QE example: `validation/quality-scorecards/`).
""",
            "- [certification-engine.md](certification-engine.md)\n- [../governance/quality-standards.md](../governance/quality-standards.md)",
        ),
    )

    write(
        FC / "evaluation" / "certification-engine.md",
        std_doc(
            "Certification Engine",
            "Cross-module certification level methodology.",
            """
## Levels (methodology)

| Level | Intent |
|-------|--------|
| Bronze | Core structure + primary engines |
| Silver | Delivery artifacts / integration with backlog tools |
| Gold | Intelligence / analytics layer |
| Platinum | Ops + advisory / architecture governance |
| Enterprise Certified | Platinum + multi-industry benchmarks + regression sample + improvement process |

## Rule

Levels are **not** awarded without a scored session and signed report. Framework Core defines the ladder; modules supply evidence packs.

## Implementations

- QE: `validation/certification/`  
- BA: `validation/certification-report-template.md`  
""",
            "- [scoring-model.md](scoring-model.md)\n- [release-readiness.md](release-readiness.md)",
        ),
    )

    write(
        FC / "evaluation" / "release-readiness.md",
        std_doc(
            "Release Readiness (Framework)",
            "Assess readiness to release framework or module versions, and Salesforce seasonal compatibility.",
            """
## Framework release checklist

- [ ] Core version bumped; CHANGELOG/ROADMAP noted  
- [ ] Module consumers noted migrations  
- [ ] Link scan / validate_repository.py clean for touched paths  
- [ ] No secrets in examples  

## Salesforce seasonal compatibility

Reuse QE process: [salesforce-release-readiness.md](../../salesforce-quality-engineering/validation/continuous-improvement/salesforce-release-readiness.md)  
Apply across modules that claim product behaviour—cite release notes; mark TBC when org-specific.
""",
            "- [benchmark-engine.md](benchmark-engine.md)\n- [../../docs/release-process.md](../../docs/release-process.md)",
        ),
    )

    # MODULES.md quick reference
    write(
        FC / "MODULE-INTEGRATION.md",
        f"""---
title: Module Integration Map
version: {VER}
---

# Module Integration Map

| Folder | Discipline | Core load order |
|--------|------------|-----------------|
| salesforce-business-analyst | BA | framework-core → skill.md → brain → knowledge/templates |
| salesforce-quality-engineering | QE | framework-core → skill.md → enterprise-orchestrator → engines |
| salesforce-solution-architect | SA (planned) | framework-core → skill.md → architecture brain |
| salesforce-developer | DEV (planned) | framework-core → skill.md → build standards |
| salesforce-devops | DO (planned) | framework-core → skill.md → pipeline intelligence |
| salesforce-production-support | PS (planned) | framework-core → skill.md → ITIL/ops engines |

See [governance/contribution-guide.md](governance/contribution-guide.md) to register a new module.
""",
    )

    print("DONE framework-core", VER)


if __name__ == "__main__":
    main()
