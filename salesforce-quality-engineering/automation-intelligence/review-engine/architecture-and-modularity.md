---
title: Architecture and Modularity Review
version: 0.10.1
tags: [automation-intelligence, sprint-8, review-engine]
---

# Architecture and Modularity Review

## Purpose

Evaluate whether the framework uses clear layers and modular boundaries suitable for enterprise scale.

## Business Context

Monolithic test classes and mixed concerns drive change cost on Salesforce releases.

## Architecture

Expect: tests → page/component/screenplay → clients/utilities → config/CI. API and UI layers separated. Shared fixtures without global mutable state.

## Decision Criteria (score cues)

| Score | Signals |
|-------|---------|
| 5 | Clear layers; reusable modules; no circular deps; scalable packages |
| 3 | Partial layering; some God-classes; inconsistent structure |
| 1 | Tests embed drivers, data, and assertions with no reuse |

## Advantages / Limitations

Structured architecture lowers onboarding cost; over-abstraction without ownership slows delivery.

## Best Practices

- One responsibility per module; shared waits/utils centralized.  
- Align folder structure with [framework-design/folder guidance](../framework-design/README.md).  

## Salesforce Considerations

- Separate persona/auth helpers; isolate org-specific config.  

## Automation Considerations

- Pyramid: flag inverted UI-only estates as architecture risk.  

## Common Pitfalls

- Copy-paste suites per cloud with no shared core.  

## Examples

`tests/`, `pages/`, `api/`, `fixtures/`, `config/` present → score 4–5 if dependencies clean.

## Interview Questions

- What layers do you expect in an enterprise automation repo?  

## Related Documents

- [../framework-design/layered-architecture.md](../framework-design/layered-architecture.md)
- [POM / Screenplay Quality](pom-screenplay-quality.md)

## Navigation

- **Previous:** [review-scoring-model.md](review-scoring-model.md)
- **Next:** [pom-screenplay-quality.md](pom-screenplay-quality.md)

## Future Enhancements

- Dependency smell catalog  
