---
title: Salesforce Release Readiness (Framework Compatibility)
version: 0.14.0
tags: [continuous-improvement, sprint-11, salesforce-release]
---

# Salesforce Release Readiness — Framework Compatibility

## Purpose

Repeatable process to assess QE framework compatibility with Salesforce seasonal releases and product changes.

## Validation Objective

Ensure knowledge, scenarios, and advisory guidance stay aligned with Spring / Summer / Winter releases, new clouds, Agentforce, OmniStudio, Data Cloud, and platform deprecations—**without inventing product behaviour**.

## Inputs

- Salesforce Release Notes (edition-confirmed)
- Current `knowledge/clouds/`, Agentforce/OmniStudio/Data Cloud articles
- Validation scorecards

## Expected Outputs

- Compatibility assessment (Impacts / No impact / TBC)
- Update backlog for affected articles
- Temporary “verify in org” flags where behaviour is edition-specific

## Pass Criteria

- Assessment recorded for the release cycle
- Impacted articles listed with owners
- No unverified feature claims added to knowledge

## Fail Criteria

- Framework claims new product features without citation
- Deprecations ignored after two cycles

## Validation Steps (repeatable)

1. **Identify cycle** — Spring / Summer / Winter (year).  
2. **Scan notes** for Agentforce, OmniStudio, Data Cloud, platform deprecations, new clouds.  
3. **Map to framework paths** — clouds/, automation-intelligence/, enterprise-quality/salesforce/, production-support/.  
4. **Classify** — Impact / Watch / N/A.  
5. **Backlog** updates; bump versions on changed articles.  
6. **Regression** — run S4B + S8 + S10 sample cases.  
7. **Record** in session table below.

## Sample Inputs

- “Winter ’XX — Agentforce topic X changed” (cite note URL/title in real assessments)

## Sample Outputs

| Area | Impact | Action |
|------|--------|--------|
| Agentforce knowledge | Watch | Re-verify prompts; mark TBC until org-confirmed |
| Deprecated API used in examples | Impact | Update example; add deprecation note |

## Scoring Rules

Compatibility assessment is Pass if cycle reviewed and backlog filed—not if “100% compatible” is claimed without evidence.

## Common Failures

- Copying marketing claims into knowledge as facts
- Skipping Experience/Industry cloud impacts

## Recommendations

- Schedule assessment each seasonal release
- Prefer “overview / verify in target org” language for new features

## Related Documents

- [README.md](README.md)
- [../../knowledge/clouds/](../../knowledge/clouds/README.md)
- [improvement-backlog.md](improvement-backlog.md)

## Navigation

- **Up:** [README.md](README.md)

## Future Enhancements

- Checklist template per cloud product line
