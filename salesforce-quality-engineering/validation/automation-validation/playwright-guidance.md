---
title: Playwright Guidance
version: 0.14.0
tags: [validation, sprint-11, automation-validation]
---

# Playwright Guidance

## Purpose

Validate **playwright guidance** within the Salesforce Quality Engineering framework.

## Validation Objective

Playwright-first

## Inputs

- Relevant module paths under `salesforce-quality-engineering/`
- Optional golden dataset from [../golden-datasets/](../golden-datasets/README.md)
- Prior sprint engine outputs when validating behaviour

## Expected Outputs

- Checklist results (Pass / Partial / Fail)
- Evidence paths (files, Route lines, sample artifacts)
- Gaps and remediation recommendations

## Pass Criteria

- Required files/engines exist and are loadable
- Hard rules visible (no invented metrics/SLA/scripts/maturity as applicable)
- Cross-links to prior sprints without duplicating full knowledge
- Sample exercise (if run) follows Orchestrator gates

## Fail Criteria

- Missing engine/README for the capability
- Agent jumps gates (e.g., cases before analysis) in sample run
- Invented KPI/SLA/maturity/compliance attestation in sample output
- Broken canonical links or orphaned duplicates violating multi-lens policy

## Validation Steps

1. Confirm folder/engine entry exists.  
2. Spot-check hard rules in `skill.md` / engine file.  
3. Run sample input from golden datasets or industry benchmark (optional).  
4. Compare to expected outcomes below.  
5. Record score on the matching quality scorecard.

## Sample Inputs

- See [../golden-datasets/](../golden-datasets/README.md) and [../benchmarking/](../benchmarking/README.md).

## Sample Outputs

- Route line: `Primary: Sprint N · Support: … · Advisory: Yes/No`
- Analysis/design/advisory sections with **Assumptions** labeled
- No fabricated percentages

## Scoring Rules

| Result | Meaning |
|--------|---------|
| Pass | All pass criteria met with evidence |
| Partial | Core present; gaps documented |
| Fail | Missing capability or hard-rule breach |

Do **not** invent a numeric certification score here—roll up via [../quality-scorecards/](../quality-scorecards/README.md) using declared weights.

## Common Failures

- Treating pointer files as full content depth
- Skipping Enterprise Orchestrator on multi-intent asks
- Using 40% automation / defect counts without denominators as “green”

## Recommendations

- Remediate gaps before claiming Enterprise Certified
- Add golden dataset coverage for recurring failures
- Log improvement items in [../continuous-improvement/](../continuous-improvement/README.md)

## Related Documents

- [README.md](README.md)
- [../enterprise-validation-engine.md](../enterprise-validation-engine.md)
- Sprint engines via [../../skill.md](../../skill.md)

## Navigation

- **Up:** [README.md](README.md)
- **See also:** [../regression-suite/](../regression-suite/README.md)

## Future Enhancements

- Automate structural checks in CI
- Machine-readable JSON validation reports
