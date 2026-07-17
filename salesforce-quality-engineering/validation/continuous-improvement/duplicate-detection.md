---
title: Detect Duplicate Content
version: 0.14.0
tags: [continuous-improvement, sprint-11]
---

# Detect Duplicate Content

## Purpose

Enforce multi-lens pointers vs full copies.

## Validation Objective

Ensure the framework improves continuously without silent drift.

## Inputs

- Validation/scorecard results · link scans · Salesforce release notes (org-confirmed)

## Expected Outputs

- Backlog items with priority and owner
- Restructure / docs / deprecation recommendations

## Pass Criteria

- Gaps logged with evidence
- No silent duplicate proliferation
- Version history updated on material change

## Fail Criteria

- Known gaps ignored across two validation cycles
- Full-content duplicates reintroduced against multi-lens policy

## Validation Steps

1. Review latest scorecards and link scan.  
2. List gaps/duplicates/outdated candidates.  
3. File backlog items.  
4. Track to closure in CHANGELOG.

## Sample Inputs / Outputs

- Input: “97 duplicate basenames” audit → Output: pointer migration backlog  
- Input: Winter release note on Agentforce → Output: release readiness assessment entry

## Scoring Rules

Track backlog burn-down qualitatively; do not invent velocity metrics.

## Common Failures

- Editing knowledge without version bump
- Archiving without pointer for old links

## Recommendations

- Run CI after each sprint pack change
- Tie SF seasonal reviews to [salesforce-release-readiness.md](salesforce-release-readiness.md)

## Related Documents

- [README.md](README.md)
- [../../CHANGELOG.md](../../CHANGELOG.md)

## Navigation

- **Up:** [README.md](README.md)

## Future Enhancements

- Automated stale-file detector by `last_updated`
