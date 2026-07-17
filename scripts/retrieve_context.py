"""Deterministic context retriever for the Salesforce BA skill (Layer 2).

BA-scoped by design. QE requests are detected early and redirected to the
Quality Engineering skill + Enterprise Orchestrator (not expanded as BA tasks).

Given a BA user request, returns the exact file bundle (brain, knowledge,
templates, playbooks, scenarios) the agent must load before producing a
deliverable. Replaces free-form file discovery with the routing rules from
`.cursor/rules/routing.mdc` plus one-hop expansion of the frontmatter
metadata graph (`related_*` fields).

Tier-0 SEACF Framework Core files are always included for BA tasks.

Usage:
  python scripts/retrieve_context.py --query "create user story for banking loan complaints"
  python scripts/retrieve_context.py --query "run fit-gap on these requirements" --json
  python scripts/retrieve_context.py --query "..." --no-expand
  python scripts/retrieve_context.py --list-tasks
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SKILL = "salesforce-business-analyst"
QE_SKILL = "salesforce-quality-engineering"

# SEACF Tier-0 — loaded for every BA task (and echoed on QE redirect).
TIER0_CORE = [
    "framework-core/README.md",
    "framework-core/orchestration/request-router.md",
    "framework-core/orchestration/context-manager.md",
    "framework-core/governance/quality-standards.md",
]

# Files loaded for EVERY BA task (skill entry + identity + validation core).
ALWAYS_LOAD = [
    *TIER0_CORE,
    f"{SKILL}/skill.md",
    f"{SKILL}/brain/identity.md",
    f"{SKILL}/brain/reasoning-framework.md",
    f"{SKILL}/brain/validation-framework.md",
    f"{SKILL}/brain/anti-hallucination.md",
    f"{SKILL}/checklists.md",
    "shared/glossary.md",
    "shared/output-standards.md",
]

# Dominant QE signals — if matched (and not clearly BA-authored), redirect.
QE_REDIRECT_KEYWORDS = [
    r"\bqe\b",
    r"quality engineering",
    r"test strateg",
    r"test design engine",
    r"defect intelligence",
    r"automation intelligence",
    r"automation roi",
    r"playwright.*(strateg|framework|feasib)",
    r"\bsev\s*[1-3]\b",
    r"hypercare",
    r"production support",
    r"incident triage",
    r"enterprise orchestrator",
    r"quality advisory",
    r"certif(y|ication).*(framework|qe|module)",
    r"regression suite.*(sprint|framework)",
    r"coverage matrix",
    r"requirement analysis engine",
]

QE_REDIRECT_BUNDLE = [
    *TIER0_CORE,
    f"{QE_SKILL}/skill.md",
    f"{QE_SKILL}/enterprise-orchestrator/enterprise-orchestrator.md",
    f"{QE_SKILL}/enterprise-orchestrator/capability-routing-table.md",
    f"{QE_SKILL}/brain/README.md",
]

# Task routing rules. Mirrors `.cursor/rules/routing.mdc` keyword triggers.
# Order matters only for reporting; ALL matching tasks contribute seeds.
TASK_RULES: list[dict] = [
    {
        "task": "user-story",
        "label": "User stories / backlog / acceptance criteria",
        "keywords": [
            r"user stor(y|ies)", r"\bstory\b", r"\bstories\b", r"backlog",
            r"acceptance criteria", r"\bsprint\b", r"\bepic\b", r"\binvest\b",
        ],
        "seeds": [
            f"{SKILL}/brain/output-framework.md",
            f"{SKILL}/knowledge/user-stories.md",
            f"{SKILL}/knowledge/acceptance-criteria.md",
            f"{SKILL}/knowledge/epic-design.md",
            f"{SKILL}/templates/user-story-template.md",
            f"{SKILL}/templates/epic-template.md",
            f"{SKILL}/playbooks/story-refinement-playbook.md",
            ".cursor/rules/userstory-generation.mdc",
            "examples/sample-user-story/service-cloud-complaint-story.md",
        ],
    },
    {
        "task": "ado-publish",
        "label": "Azure DevOps work item publishing",
        "keywords": [
            r"\bado\b", r"azure devops", r"work item", r"devops board",
            r"publish.*(story|task|backlog)",
        ],
        "seeds": [
            f"{SKILL}/knowledge/ado-backlog-integration.md",
            f"{SKILL}/knowledge/acceptance-criteria.md",
            ".cursor/rules/userstory-generation.mdc",
        ],
    },
    {
        "task": "brd",
        "label": "Business requirements / BRD",
        "keywords": [
            r"\bbrd\b", r"business requirements", r"as-?is", r"to-?be",
            r"requirements document",
        ],
        "seeds": [
            f"{SKILL}/brain/output-framework.md",
            f"{SKILL}/knowledge/requirement-types.md",
            f"{SKILL}/knowledge/requirements-engineering.md",
            f"{SKILL}/templates/brd-template.md",
        ],
    },
    {
        "task": "frd",
        "label": "Functional requirements / FRD",
        "keywords": [r"\bfrd\b", r"functional requirement", r"system behaviou?r"],
        "seeds": [
            f"{SKILL}/brain/output-framework.md",
            f"{SKILL}/knowledge/requirement-types.md",
            f"{SKILL}/templates/frd-template.md",
        ],
    },
    {
        "task": "fit-gap",
        "label": "Fit-gap / solution recommendation",
        "keywords": [
            r"fit-?gap", r"gap analysis", r"standard vs custom",
            r"build vs buy", r"solution (option|recommendation)",
            r"recommend (an? )?(approach|solution)", r"analyz?e requirement",
        ],
        "seeds": [
            f"{SKILL}/brain/decision-framework.md",
            f"{SKILL}/playbooks/fit-gap-analysis.md",
            f"{SKILL}/playbooks/gap-analysis-playbook.md",
            f"{SKILL}/playbooks/solution-recommendation-playbook.md",
            "shared/salesforce-capability-map.md",
        ],
    },
    {
        "task": "discovery",
        "label": "Discovery / workshops / stakeholder interviews",
        "keywords": [
            r"discovery", r"workshop", r"kick-?off", r"stakeholder (map|interview|analysis)",
            r"elicitation",
        ],
        "seeds": [
            f"{SKILL}/brain/enterprise-behaviors.md",
            f"{SKILL}/playbooks/discovery-playbook.md",
            f"{SKILL}/playbooks/discovery-workshop-playbook.md",
            f"{SKILL}/knowledge/stakeholder-analysis.md",
            f"{SKILL}/templates/workshop-agenda-template.md",
        ],
    },
    {
        "task": "uat",
        "label": "UAT / test scenarios / sign-off",
        "keywords": [r"\buat\b", r"test (case|scenario)", r"sign-?off", r"defect"],
        "seeds": [
            f"{SKILL}/playbooks/uat-playbook.md",
            f"{SKILL}/playbooks/uat-planning-playbook.md",
            f"{SKILL}/templates/traceability-matrix-template.md",
        ],
    },
    {
        "task": "raid",
        "label": "RAID / risks / assumptions / dependencies",
        "keywords": [
            r"\braid\b", r"\brisk", r"assumption", r"\bissue log\b", r"dependenc",
        ],
        "seeds": [
            f"{SKILL}/knowledge/risk-management.md",
            f"{SKILL}/knowledge/assumptions-management.md",
            f"{SKILL}/knowledge/dependency-management.md",
            f"{SKILL}/templates/raid-log-template.md",
        ],
    },
    {
        "task": "traceability",
        "label": "Traceability / RTM",
        "keywords": [r"traceability", r"\brtm\b", r"req(uirement)? to test"],
        "seeds": [
            f"{SKILL}/templates/traceability-matrix-template.md",
            f"{SKILL}/templates/rtm-template.md",
        ],
    },
    {
        "task": "process-mapping",
        "label": "Process mapping / BPMN",
        "keywords": [r"process map", r"\bbpmn\b", r"process flow", r"value stream"],
        "seeds": [
            f"{SKILL}/knowledge/process-mapping.md",
            f"{SKILL}/knowledge/bpmn.md",
            f"{SKILL}/knowledge/current-state-analysis.md",
            f"{SKILL}/templates/process-flow-template.md",
            f"{SKILL}/playbooks/value-stream-mapping-playbook.md",
        ],
    },
    {
        "task": "prioritization",
        "label": "Prioritization (MoSCoW, Kano, WSJF)",
        "keywords": [r"prioriti[sz]", r"moscow", r"\bkano\b", r"\bwsjf\b"],
        "seeds": [
            f"{SKILL}/knowledge/moscow-prioritization.md",
            f"{SKILL}/knowledge/prioritization-techniques.md",
            f"{SKILL}/knowledge/kano-model.md",
        ],
    },
    {
        "task": "integration",
        "label": "Integration / API / middleware",
        "keywords": [r"integrat", r"\bapi\b", r"middleware", r"\bmulesoft\b"],
        "seeds": [
            f"{SKILL}/knowledge/integration-patterns.md",
            f"{SKILL}/templates/api-catalogue-template.md",
        ],
    },
    {
        "task": "data-migration",
        "label": "Data migration / cutover",
        "keywords": [r"data migration", r"cutover", r"\betl\b", r"data load"],
        "seeds": [
            f"{SKILL}/knowledge/data-migration.md",
            f"{SKILL}/templates/migration-plan-template.md",
        ],
    },
    {
        "task": "security",
        "label": "Security / sharing / permissions",
        "keywords": [r"security", r"sharing", r"permission", r"profile", r"\bcrud\b"],
        "seeds": [f"{SKILL}/knowledge/security-model.md"],
    },
    {
        "task": "governance",
        "label": "Governance / release management",
        "keywords": [r"governance", r"release management", r"go-?live", r"production readiness"],
        "seeds": [
            f"{SKILL}/knowledge/governance-framework.md",
            f"{SKILL}/knowledge/release-management.md",
            f"{SKILL}/playbooks/production-readiness-playbook.md",
        ],
    },
    {
        "task": "kpi-baseline",
        "label": "KPI definition / baselines / target outcomes",
        "keywords": [
            r"\bkpi\b", r"baseline metric", r"target outcome", r"success metric",
            r"benefit realiz?ation", r"metric baseline",
        ],
        "seeds": [
            f"{SKILL}/brain/output-framework.md",
            f"{SKILL}/templates/kpi-baseline-template.md",
            f"{SKILL}/templates/business-case-template.md",
            f"{SKILL}/knowledge/future-state-design.md",
        ],
    },
    {
        "task": "change-management",
        "label": "Change management / adoption / upskilling (OCM)",
        "keywords": [
            r"change management", r"\bocm\b", r"resistance", r"upskill",
            r"comms plan", r"communication plan", r"adoption plan",
            r"role transition", r"training plan",
        ],
        "seeds": [
            f"{SKILL}/brain/enterprise-behaviors.md",
            f"{SKILL}/brain/communication-framework.md",
            f"{SKILL}/playbooks/change-management-playbook.md",
            f"{SKILL}/templates/comms-upskilling-plan-template.md",
            f"{SKILL}/knowledge/stakeholder-analysis.md",
        ],
    },
    {
        "task": "digital-transformation",
        "label": "Digital transformation / reinvention strategy",
        "keywords": [
            r"digital transformation", r"digital reinvention", r"digital[- ]first",
            r"reinvention strateg", r"automation strateg",
            r"process standardi[sz]ation", r"standardi[sz]e .*(process|region)",
        ],
        "seeds": [
            f"{SKILL}/brain/decision-framework.md",
            f"{SKILL}/playbooks/digital-transformation-strategy-playbook.md",
            f"{SKILL}/playbooks/change-management-playbook.md",
            f"{SKILL}/templates/kpi-baseline-template.md",
            f"{SKILL}/templates/vision-document-template.md",
            f"{SKILL}/knowledge/future-state-design.md",
            f"{SKILL}/knowledge/capability-models.md",
            "shared/salesforce-capability-map.md",
        ],
    },
    {
        "task": "sprint-planning",
        "label": "Sprint planning / backlog grooming",
        "keywords": [r"sprint plan", r"backlog groom", r"refinement session"],
        "seeds": [
            f"{SKILL}/playbooks/sprint-planning-playbook.md",
            f"{SKILL}/playbooks/backlog-grooming-playbook.md",
        ],
    },
    {
        "task": "interview",
        "label": "Interview prep / hiring / assessment",
        "keywords": [r"interview", r"hiring", r"mock", r"screening", r"capability assessment"],
        "seeds": [
            f"{SKILL}/interview-guide/interview-index.md",
            f"{SKILL}/ba-maturity-model.md",
        ],
    },
    {
        "task": "validation",
        "label": "Validate output / review draft",
        "keywords": [r"validate", r"review draft", r"quality check", r"quality gate"],
        "seeds": [f"{SKILL}/validation/README.md"],
    },
]

# Salesforce cloud knowledge. Loaded when the query names a cloud.
CLOUD_RULES: list[dict] = [
    {
        "cloud": "Service Cloud",
        "keywords": [r"service cloud", r"\bcase(s)?\b", r"complaint", r"omni-?channel", r"entitlement"],
        "seeds": [
            f"{SKILL}/knowledge/salesforce-clouds-overview.md",
            f"{SKILL}/knowledge/service-cloud-patterns.md",
        ],
    },
    {
        "cloud": "Sales / Experience / other clouds",
        "keywords": [r"sales cloud", r"experience cloud", r"marketing cloud", r"cpq", r"field service"],
        "seeds": [
            f"{SKILL}/knowledge/salesforce-clouds-overview.md",
            f"{SKILL}/knowledge/salesforce-platform.md",
        ],
    },
]

# Industry scenario routing. Mirrors routing.mdc industry table.
INDUSTRY_RULES: list[dict] = [
    {
        "industry": "banking",
        "keywords": [r"\bbank", r"\bkyc\b", r"\bloan\b", r"\baml\b", r"credit", r"collections"],
        "seeds": [f"{SKILL}/scenarios/banking"],
    },
    {
        "industry": "insurance",
        "keywords": [r"insurance", r"\bfnol\b", r"underwriting", r"quote.to.bind", r"claims?"],
        "seeds": [f"{SKILL}/scenarios/insurance"],
    },
    {
        "industry": "financial-services",
        "keywords": [r"financial services", r"wealth", r"polic(y|ies)"],
        "seeds": [f"{SKILL}/scenarios/financial-services.md"],
    },
    {
        "industry": "healthcare",
        "keywords": [r"health", r"patient", r"hipaa", r"provider", r"care plan"],
        "seeds": [f"{SKILL}/scenarios/healthcare.md", f"{SKILL}/scenarios/healthcare"],
    },
    {
        "industry": "manufacturing",
        "keywords": [r"manufactur", r"dealer", r"supply chain"],
        "seeds": [f"{SKILL}/scenarios/manufacturing.md"],
    },
    {
        "industry": "utilities",
        "keywords": [r"utilit", r"\bmeter\b", r"outage", r"tariff"],
        "seeds": [f"{SKILL}/scenarios/utilities"],
    },
    {
        "industry": "retail",
        "keywords": [r"retail", r"omnichannel", r"loyalty", r"promotion"],
        "seeds": [f"{SKILL}/scenarios/retail"],
    },
    {
        "industry": "telecom",
        "keywords": [r"telecom", r"provisioning", r"activation"],
        "seeds": [f"{SKILL}/scenarios/telecom"],
    },
    {
        "industry": "public-sector",
        "keywords": [r"public sector", r"government", r"constituent", r"grant", r"\bfoia\b"],
        "seeds": [f"{SKILL}/scenarios/public-sector.md"],
    },
]

# Frontmatter fields followed during graph expansion. Interview topics and
# governance documents are intentionally excluded: they are noise for delivery
# tasks and are seeded directly by the `interview` task rule when relevant.
RELATED_FIELDS = [
    "related_brain_modules",
    "related_knowledge",
    "related_templates",
    "related_playbooks",
    "related_scenarios",
    "related_examples",
]

LAYER_ORDER = [
    ("Rules", ".cursor/rules/"),
    ("Framework Core", "framework-core/"),
    ("Skill core", f"{SKILL}/skill.md"),
    ("Brain", f"{SKILL}/brain/"),
    ("Knowledge", f"{SKILL}/knowledge/"),
    ("Templates", f"{SKILL}/templates/"),
    ("Playbooks", f"{SKILL}/playbooks/"),
    ("Scenarios", f"{SKILL}/scenarios/"),
    ("Interview guide", f"{SKILL}/interview-guide/"),
    ("Validation", f"{SKILL}/validation/"),
    ("QE redirect", f"{QE_SKILL}/"),
    ("Shared", "shared/"),
    ("Examples", "examples/"),
]


def is_qe_redirect(query: str) -> bool:
    """True when the request is clearly QE-dominated (not BA UAT / story work)."""
    lowered = query.lower()
    # BA-owned UAT / story / BRD wording should stay on BA path even if "test" appears.
    ba_anchors = [
        r"\bbrd\b", r"\bfrd\b", r"user stor", r"\binvest\b", r"fit-?gap",
        r"workshop", r"acceptance criteria", r"\buat\b", r"moscow",
    ]
    if any(re.search(k, lowered) for k in ba_anchors):
        return False
    return any(re.search(k, lowered) for k in QE_REDIRECT_KEYWORDS)


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    meta: dict[str, str] = {}
    for line in text[3:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            meta[key.strip()] = value.strip()
    return meta


def parse_list_field(raw: str) -> list[str]:
    raw = raw.strip()
    if raw.startswith("[") and raw.endswith("]"):
        raw = raw[1:-1]
    return [item.strip().strip("'\"") for item in raw.split(",") if item.strip()]


def expand_seed(seed: str) -> list[str]:
    """Resolve a seed path: a directory expands to its markdown files."""
    path = REPO / seed
    if path.is_dir():
        return sorted(
            str(p.relative_to(REPO)).replace("\\", "/")
            for p in path.glob("*.md")
            if p.name != "README.md"
        )
    return [seed]


def related_files(repo_rel: str) -> list[str]:
    """One-hop neighbors from a file's frontmatter metadata graph."""
    path = REPO / repo_rel
    if not path.is_file():
        return []
    meta = parse_frontmatter(path.read_text(encoding="utf-8", errors="replace"))
    neighbors: list[str] = []
    for field in RELATED_FIELDS:
        if field in meta:
            for target in parse_list_field(meta[field]):
                # Skip README hubs: they fan out to everything and bloat the bundle.
                if target.endswith("README.md"):
                    continue
                if (REPO / target).is_file():
                    neighbors.append(target)
    return neighbors


def match_rules(query: str, rules: list[dict]) -> list[dict]:
    lowered = query.lower()
    return [r for r in rules if any(re.search(k, lowered) for k in r["keywords"])]


def layer_of(repo_rel: str) -> str:
    for label, prefix in LAYER_ORDER:
        if repo_rel.startswith(prefix):
            return label
    return "Other"


def retrieve(query: str, expand: bool = True) -> dict:
    if is_qe_redirect(query):
        ordered = list(dict.fromkeys(QE_REDIRECT_BUNDLE))
        missing = [f for f in ordered if not (REPO / f).is_file()]
        files = [f for f in ordered if (REPO / f).is_file()]
        grouped: dict[str, list[str]] = {}
        for f in files:
            grouped.setdefault(layer_of(f), []).append(f)
        return {
            "query": query,
            "matched_tasks": ["qe-redirect"],
            "matched_clouds": [],
            "matched_industries": [],
            "files": files,
            "grouped": grouped,
            "missing": missing,
            "redirect": "salesforce-quality-engineering",
            "redirect_message": (
                "This request matches Quality Engineering. Load the QE redirect "
                "bundle, then follow salesforce-quality-engineering/skill.md "
                "Pre-Execution Gate and enterprise-orchestrator/. Do not continue "
                "as a BA deliverable path."
            ),
        }

    tasks = match_rules(query, TASK_RULES)
    clouds = match_rules(query, CLOUD_RULES)
    industries = match_rules(query, INDUSTRY_RULES)

    seeds: list[str] = list(ALWAYS_LOAD)
    for rule in tasks + clouds + industries:
        for seed in rule["seeds"]:
            seeds.extend(expand_seed(seed))

    ordered: list[str] = []
    seen: set[str] = set()
    for item in seeds:
        if item not in seen:
            seen.add(item)
            ordered.append(item)

    if expand:
        for item in list(ordered):
            for neighbor in related_files(item):
                if neighbor not in seen:
                    seen.add(neighbor)
                    ordered.append(neighbor)

    missing = [f for f in ordered if not (REPO / f).is_file()]
    files = [f for f in ordered if (REPO / f).is_file()]

    grouped = {}
    for f in files:
        grouped.setdefault(layer_of(f), []).append(f)

    return {
        "query": query,
        "matched_tasks": [t["task"] for t in tasks],
        "matched_clouds": [c["cloud"] for c in clouds],
        "matched_industries": [i["industry"] for i in industries],
        "files": files,
        "grouped": grouped,
        "missing": missing,
        "redirect": None,
    }


def print_report(result: dict) -> None:
    print(f"Query: {result['query']}")
    if result.get("redirect"):
        print(f"REDIRECT → {result['redirect']}")
        print(result.get("redirect_message", ""))
    print(f"Matched tasks: {', '.join(result['matched_tasks']) or '(none — fallback bundle)'}")
    if result["matched_clouds"]:
        print(f"Matched clouds: {', '.join(result['matched_clouds'])}")
    if result["matched_industries"]:
        print(f"Matched industries: {', '.join(result['matched_industries'])}")
    print(f"\nContext bundle ({len(result['files'])} files) — load these before producing the deliverable:\n")
    for label, _ in LAYER_ORDER:
        if label in result["grouped"]:
            print(f"  [{label}]")
            for f in result["grouped"][label]:
                print(f"    - {f}")
    if "Other" in result["grouped"]:
        print("  [Other]")
        for f in result["grouped"]["Other"]:
            print(f"    - {f}")
    if result["missing"]:
        print("\nWARNING — rule references missing files:")
        for f in result["missing"]:
            print(f"    ! {f}")
    if not result["matched_tasks"]:
        print(
            "\nNo task rule matched. Loaded the Tier-0 + BA core bundle only; "
            "read salesforce-business-analyst/skill.md and ask the user to "
            "clarify deliverable type and industry context."
        )


def main() -> int:
    parser = argparse.ArgumentParser(description="Retrieve the exact skill file bundle for a BA request")
    parser.add_argument("--query", "-q", help="The user's request, verbatim or paraphrased")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    parser.add_argument("--no-expand", action="store_true", help="Skip metadata-graph expansion")
    parser.add_argument("--list-tasks", action="store_true", help="List supported task routes")
    args = parser.parse_args()

    if args.list_tasks:
        print(f"{'qe-redirect':<18} Quality Engineering redirect (not a BA task)")
        for rule in TASK_RULES:
            print(f"{rule['task']:<18} {rule['label']}")
        return 0

    if not args.query:
        parser.error("--query is required (or use --list-tasks)")

    result = retrieve(args.query, expand=not args.no_expand)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print_report(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
