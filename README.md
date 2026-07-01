---
title: Readme
module: Salesforce Business Analyst
category: Root
document_type: Guide
version: 1.3.0
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

## Getting Started

### For Human Practitioners

1. Read [docs/vision.md](docs/vision.md) for strategic intent.
2. Review [salesforce-business-analyst/skill-guide.md](salesforce-business-analyst/skill-guide.md) for the full implementation guide.
3. Open [salesforce-business-analyst/skill.md](salesforce-business-analyst/skill.md) for the core BA workflow.
4. Use templates in `salesforce-business-analyst/templates/` for deliverables.

### For AI Agents (Cursor)

1. Load `.cursor/instructions.md` and `.cursor/routing.md`.
2. When the user asks for BA work (requirements, BRD, user stories, discovery, fit-gap, UAT), route to `salesforce-business-analyst/skill.md`.
3. Follow [shared/output-standards.md](shared/output-standards.md) for all generated artifacts.

## Current Skills

| Skill | Status | Description |
|-------|--------|-------------|
| Salesforce Business Analyst | Active (v1.3.0) | Brain, knowledge, templates, playbooks, scenarios, interview guide, validation, learning paths |

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

- **Previous:** [Readme](README.md)
- **Next:** [Readme](README.md)
- **See Also:** [cross-linking-framework](docs/cross-linking-framework.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.3.0 | 2026-07-02 | BA Practice Lead | Sprints 8–9 validation and continuous knowledge management |
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
