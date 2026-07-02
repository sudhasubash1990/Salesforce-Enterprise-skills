---
title: Contributing
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
keywords: [CONTRIBUTING]
tags: [CONTRIBUTING]
---

# Contributing

Thank you for contributing to Salesforce Enterprise Skills. This repository encodes practitioner expertise for both humans and AI agents—quality and consistency matter.

## How to Contribute

1. **Fork** the repository and create a feature branch from `main`.
2. **Read** [docs/repository-guidelines.md](docs/repository-guidelines.md) and [docs/markdown-standards.md](docs/markdown-standards.md).
3. **Make changes** following [docs/naming-conventions.md](docs/naming-conventions.md).
4. **Self-review** using [docs/quality-framework.md](docs/quality-framework.md).
5. **Submit** a pull request with a clear description and test plan.

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
docs: update metadata schema for skill frontmatter
fix(templates): correct acceptance criteria format in user story template
```

After **skill pack** changes (`salesforce-business-analyst/` or `.cursor/rules/userstory-generation.mdc`), run:

```powershell
python scripts/update_skill_version.py --message "<your commit subject line>"
```

This bumps semver from the commit type and updates `README.md` version history using the commit summary. Use `--sync-only --force` to align README to `skill.md` without bumping.

## Pull Request Checklist

- [ ] Follows markdown and naming standards
- [ ] No client-specific or confidential content
- [ ] Links are relative and valid
- [ ] Skill descriptions include WHAT and WHEN (third person)
- [ ] Examples are realistic but anonymized
- [ ] CHANGELOG.md updated under `[Unreleased]` (or run `python scripts/update_skill_version.py` for skill changes)

## Content Guidelines

### Do

- Write from practitioner experience with actionable guidance
- Use Salesforce-standard terminology (see [shared/glossary.md](shared/glossary.md))
- Include decision criteria, not just lists of activities
- Provide templates with filled examples

### Do Not

- Include proprietary client artifacts or PII
- Duplicate Salesforce Help documentation verbatim
- Add time-sensitive release notes without an archive section
- Create skills without a clear trigger description

## Review Process

See [docs/review-process.md](docs/review-process.md). BA skill changes require review from at least one senior BA practitioner.

## Questions

Open a discussion issue or contact the maintainers listed in the root README.

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

- **Previous:** [Changelog](CHANGELOG.md)
- **Next:** [Roadmap](ROADMAP.md)
- **See Also:** [cross-linking-framework](docs/cross-linking-framework.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
