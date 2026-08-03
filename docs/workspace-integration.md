---
title: Workspace Integration
module: Salesforce Business Analyst
category: Governance
document_type: Guide
version: 1.0.0
review_status: Approved
owner: BA Practice Lead
created_date: 2026-08-04
last_updated: 2026-08-04
review_cycle: quarterly
related_documents: [docs/metadata-schema.md, docs/cross-linking-framework.md]
keywords: [workspace integration, cursor rules, routing, multi-root, bridge rule, skills discovery]
tags: [workspace-integration, governance, routing]
---

# Making the Enterprise Skills Active from Any Workspace Root

How to activate SEACF skill routing (`.cursor/rules/`, the BA retriever, and the QE
Enterprise Orchestrator) when this repository is **not** the workspace root — for
example when it is cloned as a subfolder inside a larger project workspace.

## Why This Matters

Cursor auto-loads `alwaysApply` rules only from the **workspace root's**
`.cursor/rules/` directory. When `Salesforce-Enterprise-Skills` sits nested inside
another folder, its routing rules (`instructions.mdc`, `routing.mdc`,
`userstory-generation.mdc`, `output-generation.mdc`, `ai-productivity-ADO.mdc`)
are dormant: the agent will not run the context retriever, enforce the
pre-execution gates, or apply the output engine automatically.

The Python tooling itself is nesting-safe — `scripts/retrieve_context.py` and the
validators resolve paths from their own file location, not the current working
directory — so only **rule discovery** needs bridging.

## Integration Options

Choose one of four options, ordered by fidelity.

### Option A — Open the repository as its own workspace (full fidelity)

Open the `Salesforce-Enterprise-Skills` folder directly (*File → Open Folder*).
The repo root becomes the workspace root, all rules auto-load, and everything
works exactly as designed. Best for dedicated BA/QE working sessions.

### Option B — Multi-root workspace (recommended for daily use)

Keep your project workspace and add this repository as a second root:

1. *File → Add Folder to Workspace* → select the `Salesforce-Enterprise-Skills` clone.
2. *File → Save Workspace As…* → save the `.code-workspace` file.

Cursor loads `.cursor/rules` from **each** workspace root, so your project rules
and the enterprise routing rules are active at the same time. This is the
cleanest answer when your code lives elsewhere but you want the skill pack active.

### Option C — Bridge rule in the actual workspace root (permanently nested clone)

If the repository must stay nested, add one always-apply rule to the **parent**
workspace's `.cursor/rules/` folder that delegates to this repository. Copy the
template below to `<workspace-root>/.cursor/rules/enterprise-skills-router.mdc`
and adjust the relative path:

```markdown
---
description: Route Salesforce BA/QE tasks to the Salesforce-Enterprise-Skills framework
alwaysApply: true
---

# Salesforce Enterprise Skills Router (bridge)

The SEACF enterprise skill pack lives at `<relative-path-to>/Salesforce-Enterprise-Skills/`
(adjust the path to where the repo is cloned in this workspace).

For ANY Salesforce Business Analyst or Quality Engineering task:

1. Read `Salesforce-Enterprise-Skills/.cursor/rules/instructions.mdc` and
   `Salesforce-Enterprise-Skills/.cursor/rules/routing.mdc` FIRST and follow them
   as if they were always-applied rules of this workspace.
2. For BA tasks, run the deterministic retriever from the skill repo root:
   `python Salesforce-Enterprise-Skills/scripts/retrieve_context.py --query "<request>"`
   and load exactly the bundle it returns (paths are relative to the skill repo).
3. If it reports qe-redirect, switch to
   `Salesforce-Enterprise-Skills/salesforce-quality-engineering/skill.md`
   and the Enterprise Orchestrator.
4. Save deliverables under `Salesforce-Enterprise-Skills/outputs/<project>/` and run
   the output engine per `output-generation.mdc`.
```

### Option D — Personal skills for cross-workspace discovery

Copy the two discovery stubs from
[.cursor/skills/salesforce-business-analyst/SKILL.md](../.cursor/skills/salesforce-business-analyst/SKILL.md)
and
[.cursor/skills/salesforce-quality-engineering/SKILL.md](../.cursor/skills/salesforce-quality-engineering/SKILL.md)
into your user-level skills folder (`~/.cursor/skills/`), editing the stub paths
to point at the clone's absolute location. Any workspace then discovers the
skills. Note: skills cover discovery only — the always-applied gates (output
engine, user-story format, ADO productivity fields) still need Option B or C to
be enforced.

## Option Comparison

| Option | Rules auto-load | Setup effort | Best for |
|--------|-----------------|--------------|----------|
| A — Own workspace | Yes (native) | None | Dedicated BA/QE sessions |
| B — Multi-root workspace | Yes (per root) | One-time, 1 minute | Daily use beside project code |
| C — Bridge rule | Via delegation | One file in parent root | Permanently nested clones |
| D — Personal skills | Discovery only | Copy 2 stubs | Cross-workspace skill discovery |

## Verification Checklist

After setup, verify routing is active:

1. Ask the agent a BA question (e.g. "draft a user story for billing adjustment")
   and confirm it runs `scripts/retrieve_context.py` and loads the returned bundle.
2. Ask a QE question (e.g. "test strategy and regression scope") and confirm the
   retriever reports a `qe-redirect` to
   [salesforce-quality-engineering/skill.md](../salesforce-quality-engineering/skill.md).
3. Generate a deliverable and confirm it is saved under `outputs/<project>/` with
   an office-format conversion beside the Markdown source.

## Related Brain Modules

N/A — governance guide; no direct brain module relationships.

## Related Knowledge

- [Knowledge Index](../salesforce-business-analyst/knowledge/README.md)

## Related Templates

N/A — no template relationships for this guide.

## Related Playbooks

N/A — no playbook relationships for this guide.

## Related Industry Scenarios

N/A — not industry-specific.

## Related Interview Topics

N/A — not an interview topic.

## Related Examples

N/A — no example relationships for this guide.

## Related Documents

- [Metadata Schema](metadata-schema.md)
- [Cross Linking Framework](cross-linking-framework.md)
- [Framework Core](../framework-core/README.md)
- [BA Skill Entry](../salesforce-business-analyst/skill.md)
- [QE Skill Entry](../salesforce-quality-engineering/skill.md)

## Traceability

**Upstream:** `.cursor/rules/instructions.mdc`, `.cursor/rules/routing.mdc` |
**Downstream:** Any workspace consuming this repository | **Validation:** validate_metadata.py

## Navigation

- **Up:** [docs/README.md](README.md)
- **See Also:** [cross-linking-framework](cross-linking-framework.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-08-04 | BA Practice Lead | Initial workspace integration guide (assessment feedback follow-up) |
