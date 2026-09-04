# TRIOS Copilot Instructions

You are contributing to the TRIOS repository.

Before making changes, understand these project documents:

- `docs/TRIOS_OVERVIEW.md`
- `docs/ARCHITECTURE.md`
- `docs/PHYSICS.md`
- `docs/EXPERIMENTS.md`
- `docs/AGENT_WORKFLOW.md`

## Mandatory Rules

1. Do not silently redesign TRIOS architecture.
2. Do not change the physics model without scientific justification.
3. Do not change existing import conventions as unrelated cleanup.
4. Do not delete or weaken tests to make a task pass.
5. Preserve existing behavior unless the task explicitly requires a behavior change.
6. Keep physics concepts separate from experiment/UI concepts.
7. `editable`, learner controls, GUI state, and educational rules do not belong in the low-level physics core.
8. Prefer small, reviewable changes over broad rewrites.
9. Run relevant tests after modifications.
10. Report important assumptions and architectural consequences.
11. Do not modify local user data under `data/` unless the task explicitly requires it.
12. Never commit credentials, passwords, session files, or other local runtime secrets.

## Repository-Specific Import Policy

The current project intentionally uses direct imports such as:

```python
from vector import Vector2
from body import Body
```

Do not convert these to package imports unless an explicit architecture task authorizes that migration.

## Physics Caution

A passing test is not by itself proof of physical correctness.

When changing numerical or physical code, compare against existing validation baselines and report numerical effects.

Do not claim that sensitivity to initial conditions alone proves chaos.

## Change Protocol

For non-trivial work:

1. Inspect existing code.
2. Read the relevant documentation.
3. Explain the intended change.
4. Implement it.
5. Add or update tests.
6. Run the relevant test suite.
7. Summarize what changed and any remaining uncertainty.

When architecture is unclear, do not guess silently. State the ambiguity and choose the smallest change consistent with the documented design.
