---
title: Readme
module: Salesforce Business Analyst
category: Root
document_type: Guide
version: 1.5.0
review_status: Approved
owner: BA Practice Lead
created_date: 2026-07-02
last_updated: 2026-07-02
review_cycle: quarterly
related_brain_modules: [salesforce-business-analyst/brain/README.md]
related_knowledge: [salesforce-business-analyst/knowledge/README.md]
related_templates: [salesforce-business-analyst/templates/README.md]
related_playbooks: [salesforce-business-analyst/playbooks/README.md]
related_scenarios: [salesforce-business-analyst/scenarios/README.md]
related_interview_topics: [salesforce-business-analyst/interview-guide/interview-index.md]
related_examples: [examples/sample-project/README.md]
related_documents: [docs/cross-linking-framework.md, ROADMAP.md]
keywords: [README]
tags: [README]
---

# Salesforce Enterprise Skills

A curated, enterprise-grade knowledge repository for Salesforce consulting disciplines—designed for **Cursor**, **Claude**, and human practitioners. Packages delivery experience into reusable skills, playbooks, templates, and governance artifacts for requirements documentation, process mapping, gap analysis, and stakeholder analysis.

## Purpose

Salesforce programs fail more often from unclear requirements, weak traceability, and misaligned solution design than from technical implementation gaps. This repository addresses that gap by encoding **how experienced practitioners think, document, and decide**—starting with the Salesforce Business Analyst discipline.

## Repository Structure

| Path | Purpose |
|------|---------|
| `.cursor/` | Agent routing, indexing, and instruction rules for Cursor |
| `docs/` | Repository governance, architecture, and quality standards |
| `shared/` | Cross-discipline glossary, taxonomy, and enterprise standards |
| `examples/` | Reference artifacts (BRDs, user stories, workshops, projects) |
| `salesforce-business-analyst/` | Primary BA skill, playbooks, templates, and scenarios |
| `scripts/` | Metadata enrichment and repository validation |

## Installation (Cursor)

The repository is designed to be opened directly as a Cursor workspace — the agent rules auto-load and route any BA request to the skill.

### 1. Download the repository

Using git:

```bash
git clone https://github.com/sudhasubash1990/Salesforce-Enterprise-skills.git
```

Or without git: on the GitHub page, click **Code → Download ZIP** and extract it.

### 2. Open the folder in Cursor

**File → Open Folder** → select the `Salesforce-Enterprise-skills` folder. Cursor automatically picks up the agent rules in `.cursor/rules/` (routing, instructions, user-story generation, output generation) and indexes the skill content.

### 3. Start asking

No further setup is required. Ask for any BA deliverable, for example:

- *"Create a BRD for a Service Cloud complaint management process"*
- *"Generate user stories for customer onboarding"*
- *"Run a fit-gap analysis for these requirements"*

The routing rules load the right brain modules, knowledge articles, playbooks, and templates automatically.

### 4. Optional — Azure DevOps publishing

To let the agent create User Stories and Tasks directly in Azure DevOps, copy `.cursor/mcp.json.example` to `.cursor/mcp.json` and fill in your ADO organization, project, and Personal Access Token. Never commit `.cursor/mcp.json` — it is git-ignored by design.

### 5. Optional — Office file conversion

To generate `.docx` / `.xlsx` / `.pptx` / `.pdf` files beside the Markdown deliverables, install [Pandoc](https://pandoc.org/installing.html) and run:

```bash
pip install -r output-engine/requirements.txt
```

If you skip this, everything still works — deliverables are produced as Markdown only.

## Getting Started

### For Human Practitioners

1. Read [docs/vision.md](docs/vision.md) for strategic intent.
2. Review [salesforce-business-analyst/skill-guide.md](salesforce-business-analyst/skill-guide.md) for the full implementation guide.
3. Open [salesforce-business-analyst/skill.md](salesforce-business-analyst/skill.md) for the core BA workflow.
4. Use templates in `salesforce-business-analyst/templates/` for deliverables.

### For AI Agents (Cursor)

1. Load `.cursor/rules/instructions.mdc` and `.cursor/rules/routing.mdc`.
2. When the user asks for BA work (requirements, BRD, user stories, discovery, fit-gap, UAT), route to `salesforce-business-analyst/skill.md`.
3. Follow [shared/output-standards.md](shared/output-standards.md) for all generated artifacts.

## Current Skills

| Skill | Status | Description |
|-------|--------|-------------|
| Salesforce Business Analyst | Active (v1.5.0) | Brain, knowledge, templates, playbooks, scenarios, interview guide, validation, learning paths |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). All contributions must follow [docs/markdown-standards.md](docs/markdown-standards.md) and pass `python scripts/validate_repository.py`.

## License

MIT — see [LICENSE](LICENSE).

## Related Brain Modules

- [Readme](salesforce-business-analyst/brain/README.md)

## Related Knowledge

- [Readme](salesforce-business-analyst/knowledge/README.md)

## Related Templates

- [Readme](salesforce-business-analyst/templates/README.md)

## Related Playbooks

- [Readme](salesforce-business-analyst/playbooks/README.md)

## Related Industry Scenarios

- [Readme](salesforce-business-analyst/scenarios/README.md)

## Related Interview Topics

- [Interview Index](salesforce-business-analyst/interview-guide/interview-index.md)

## Related Examples

- [Readme](examples/sample-project/README.md)

## Related Documents

- [Cross Linking Framework](docs/cross-linking-framework.md)
- [Roadmap](ROADMAP.md)

## Traceability

**Upstream:** — | **Downstream:** All skills | **Validation:** ROADMAP alignment

## Navigation

- **Previous:** —
- **Next:** [Salesforce Business Analyst Readme](salesforce-business-analyst/README.md)
- **See Also:** [cross-linking-framework](docs/cross-linking-framework.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.5.0 | 2026-07-02 | BA Practice Lead | Sprint 10 pre-execution gate, Service Cloud patterns, validator exclusions, cross-link and playbook dedupe fixes |
| 1.4.0 | 2026-07-02 | BA Practice Lead | ADO backlog integration, estimation discipline, deliverable ownership, nested AC format |
| 1.3.0 | 2026-07-02 | BA Practice Lead | Sprints 8–9 validation and continuous knowledge management |
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
