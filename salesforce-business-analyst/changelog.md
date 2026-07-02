---
title: Changelog
module: Salesforce Business Analyst
category: Root
document_type: Guide
version: 1.1.0
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
keywords: [changelog]
tags: [changelog]
---

# Salesforce Business Analyst — Changelog

Skill-specific version history.

## [Unreleased]
## [1.6.0] - 2026-07-02

### Changed

- Layer 2 deterministic context retriever with routing rules and metadata-graph expansion

## [1.5.0] - 2026-07-02

### Changed

- Sprint 10 pre-execution gate, Service Cloud patterns, validator exclusions, cross-link and playbook dedupe fixes


## [1.3.0] - 2026-07-02

### Added

- Sprint 9 continuous knowledge management: skill guide, maturity model, learning paths, implementation hub
- Competency assessment template and KM governance doc

### Changed

- Skill orchestrator v1.3.0

## [1.2.0] - 2026-07-02

### Added

- Sprint 8 Enterprise Validation hub (`validation/`)
- Repository validation automation via `scripts/validate_repository.py`

### Changed

- Skill orchestrator v1.2.0

## [1.1.0] - 2026-07-02

### Added

- Sprint 7 cross-linking governance docs and validation automation
- Repo-wide metadata enrichment on all Markdown files

### Changed

- Skill orchestrator v1.1.0
- Mandatory Related sections, traceability, navigation on all documents

## [1.0.0] - 2026-07-02

### Added

- Sprint 6 Interview Intelligence Framework (`interview-guide/`) — 670 Q&A items
- Topic files: core BA (7), Salesforce (6), delivery (6), advanced (5)
- Per-question structure: intent, strong/weak answers, follow-ups, tips, cross-links

### Changed

- Skill orchestrator v1.0.0 integrates interview guide index
- `interview-guide.md` redirect stub preserves inbound links

## [0.6.0] - 2026-07-02

### Added

- Sprint 3 template library (31 templates including upgrades)
- Sprint 4 playbook library (15 methodologies)
- Sprint 5 industry scenarios (28 domain scenarios in 6 industries)

### Changed

- Skill orchestrator integrates templates, playbooks, scenarios indexes
- Version alignment: Sprint 3=v0.4, Sprint 4=v0.5, Sprint 5=v0.6 skill release

## [0.3.0] - 2026-07-02

### Added

- Sprint 2 Enterprise Knowledge Base — 27 articles covering BA fundamentals through AI in BA
- [knowledge/README.md](knowledge/README.md) index
- Standard metadata and document structure per Sprint 2 specification

### Changed

- `skill.md` v0.3.0 — knowledge base integration
- Legacy knowledge files updated as cross-link hubs

## [0.2.0] - 2026-07-02

### Added

- **BA Brain** (`brain/`) — Sprint 1 modular reasoning engine:
  - `identity.md`, `consulting-principles.md`, `reasoning-framework.md`
  - `communication-framework.md`, `enterprise-behaviors.md`
  - `anti-hallucination.md`, `validation-framework.md`
  - `output-framework.md`, `decision-framework.md`
- Templates: FRD, RAID log, traceability matrix
- `skill.md` orchestrator with brain loading order and module index

### Changed

- Agent routing and indexing wired to brain modules
- Skill description expanded for FRD, RAID, RTM triggers

## [0.1.0] - 2026-07-01

### Added

- Initial `skill.md` with end-to-end BA workflow
- Knowledge base: requirements engineering, platform, domains, industry patterns
- Playbooks: discovery, elicitation, fit-gap, UAT
- Templates: BRD, user story, workshop agenda, process map
- Industry scenarios: financial services, healthcare, manufacturing, public sector
- Interview guide, checklists, prompts, references
- Worked examples in skill `examples/` folder

### Notes

- Aligned with repository v0.1.0 bootstrap
- Skill description follows Cursor skill metadata conventions

