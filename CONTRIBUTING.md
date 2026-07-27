---
title: Contributing
module: Salesforce Enterprise Skills
category: Root
document_type: Guide
version: 1.2.0
review_status: Approved
owner: SEACF Practice Lead
created_date: 2026-07-02
last_updated: 2026-07-28
review_cycle: quarterly
related_brain_modules:
  - salesforce-business-analyst/brain/README.md
  - salesforce-quality-engineering/brain/README.md
related_knowledge:
  - salesforce-business-analyst/knowledge/README.md
  - salesforce-quality-engineering/knowledge/README.md
related_templates:
  - salesforce-business-analyst/templates/README.md
  - salesforce-quality-engineering/templates/README.md
related_playbooks:
  - salesforce-business-analyst/playbooks/README.md
  - salesforce-quality-engineering/playbooks/README.md
related_scenarios:
  - salesforce-business-analyst/scenarios/README.md
  - salesforce-quality-engineering/scenarios/README.md
related_interview_topics:
  - salesforce-business-analyst/interview-guide/interview-index.md
related_examples: [examples/sample-project/README.md]
related_documents:
  - docs/cross-linking-framework.md
  - ROADMAP.md
  - framework-core/governance/contribution-guide.md
  - salesforce-quality-engineering/skills/README.md
keywords: [CONTRIBUTING]
tags: [CONTRIBUTING, SEACF]
---

# Contributing

Thank you for contributing to **Salesforce Enterprise Skills (SEACF)**. This repository encodes practitioner expertise for humans and AI agents—quality and consistency matter.

## How to Contribute

1. **Fork** the repository and create a feature branch from `main`.
2. **Read** [docs/repository-guidelines.md](docs/repository-guidelines.md) and [docs/markdown-standards.md](docs/markdown-standards.md).
3. **Load Tier-0** contracts in [framework-core/](framework-core/README.md) when adding cross-module behaviour.
4. **Make changes** following [docs/naming-conventions.md](docs/naming-conventions.md).
5. **Self-review** using [docs/quality-framework.md](docs/quality-framework.md).
6. **Submit** a pull request with a clear description and test plan.

## Branch Naming

```
feature/<short-description>
fix/<short-description>
docs/<short-description>
skill/<skill-name>/<short-description>
```

## Commit Messages

Use conventional commits:

```
feat(ba): add healthcare prior authorization scenario
feat(qe): add OmniStudio QA specialized skill pack
docs: update metadata schema for skill frontmatter
fix(templates): correct acceptance criteria format in user story template
```

### BA skill version bump

After **BA skill pack** changes (`salesforce-business-analyst/` or `.cursor/rules/userstory-generation.mdc`), run:

```powershell
python scripts/update_skill_version.py --message "<your commit subject line>"
```

This bumps semver from the commit type and updates BA `README.md` version history. Use `--sync-only --force` to align README to `skill.md` without bumping.

### QE specialized skills

New or updated packs live under [`salesforce-quality-engineering/skills/<skill-name>/`](salesforce-quality-engineering/skills/README.md):

| Required | Notes |
|----------|--------|
| `SKILL.md` | Agent entry (hard rules + loading order) |
| `skill-config.yaml` | `name`, `short_id`, `version`, `entry: SKILL.md`, routing keywords |
| `knowledge/` | Reasoning articles + standard indexes (`concepts.md`, `best-practices.md`, `salesforce-reference.md`, `glossary.md`) as pointers—**do not duplicate** Sprint 4A/4B encyclopedia |
| `playbooks/` · `templates/` · `prompts/` · `examples/` · `tests/` | Skill-owned deliverables |

Also update:

1. [`salesforce-quality-engineering/skill-config.yaml`](salesforce-quality-engineering/skill-config.yaml) registry  
2. [`enterprise-orchestrator/capability-routing-table.md`](salesforce-quality-engineering/enterprise-orchestrator/capability-routing-table.md)  
3. Parent [`skill.md`](salesforce-quality-engineering/skill.md) Specialized Skills table  
4. Module [`CHANGELOG.md`](salesforce-quality-engineering/CHANGELOG.md) and root [`CHANGELOG.md`](CHANGELOG.md) when the change is repo-visible  

Register new **modules** (SA/DEV/DO/PS) via [framework-core/governance/contribution-guide.md](framework-core/governance/contribution-guide.md).

## Pull Request Checklist

- [ ] Follows markdown and naming standards
- [ ] No client-specific or confidential content
- [ ] Links are relative and valid (especially sibling links under `skills/*/knowledge/`)
- [ ] Skill descriptions include WHAT and WHEN (third person)
- [ ] Examples are realistic but anonymized
- [ ] No secrets (`.env`, PAT, credentials) — see `.gitignore`
- [ ] `CHANGELOG.md` updated under `[Unreleased]` or a dated release section
- [ ] QE changes: orchestrator routing + `skill-config.yaml` updated when adding a skill
- [ ] Repository validation: `python scripts/validate_repository.py` (when applicable)

## Content Guidelines

### Do

- Write from practitioner experience with actionable guidance
- Use Salesforce-standard terminology (see [shared/glossary.md](shared/glossary.md))
- Include decision criteria, not just lists of activities
- Provide templates with filled examples
- Cross-link Sprint encyclopedias instead of copying long-form reference content into skill packs

### Do Not

- Include proprietary client artifacts or PII
- Duplicate Salesforce Help documentation verbatim
- Add time-sensitive release notes without an archive section
- Create skills without a clear trigger description and routing keywords
- Commit generated `outputs/`, conversion logs, or OneDrive/Office lock files

## Review Process

See [docs/review-process.md](docs/review-process.md).

- BA skill changes: at least one senior BA practitioner  
- QE skill / orchestrator changes: at least one senior QE practitioner  
- Framework Core contracts: SEACF maintainer review  

## Questions

Open a discussion issue or contact the maintainers listed in the root README.

## Related Documents

- [Framework Core contribution guide](framework-core/governance/contribution-guide.md)
- [QE Specialized Skills](salesforce-quality-engineering/skills/README.md)
- [Roadmap](ROADMAP.md)
- [Changelog](CHANGELOG.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.2.0 | 2026-07-28 | SEACF Practice Lead | Multi-module SEACF: QE skills/ packs, registry, routing checklist |
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking baseline |
