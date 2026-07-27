---
title: Azure DevOps Pipeline Review
module: Salesforce Quality Engineering
category: QE Specialized Skill Example
document_type: Example
version: 0.21.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [playwright-review, example]
---

# Azure DevOps Pipeline Review

## Original Implementation

ADO pipeline runs Playwright but no artifacts; PAT in YAML.

## Identified Issues

- Secrets in source
- No HTML report publish
- No smoke vs full split

## Recommended Improvements

- Variable group secrets
- PublishPipelineArtifact for playwright-report
- Smoke stage gate

## Refactored Example

```yaml
- task: PublishPipelineArtifact@1
  inputs:
    targetPath: playwright-report
    artifact: playwright-report
```

## Best Practices

Never commit PAT.

## QA Recommendations

CI/CD Readiness Critical until secrets fixed.
