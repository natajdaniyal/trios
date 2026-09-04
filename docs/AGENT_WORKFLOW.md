# TRIOS Agent Workflow

## 1. Principle

AI agents are specialized contributors.

They do not own TRIOS architecture.

They must follow repository documentation and produce reviewable changes.

---

## 2. Recommended Agent Roles

### Core Agent

Primary responsibility:

- physics core,
- low-level infrastructure,
- safe refactoring,
- core tests.

Default owner: GitHub Copilot.

---

### Science / Experiment Agent

Primary responsibility:

- experiment infrastructure,
- experiment definitions,
- educational/scientific workflow.

Potential tools: Claude, Codex, or another specialized coding agent.

---

### GUI Agent

Primary responsibility:

- user interface,
- interaction design,
- visualization,
- presentation.

Potential owner: Replit Agent or another UI-focused agent.

---

### Validation Agent

Primary responsibility:

- software regression checks,
- numerical validation,
- scientific consistency checks,
- review of agent-generated changes.

---

## 3. Branch Policy

No agent should work directly on `master`.

Preferred workflow:

```text
Issue
  |
  v
Agent
  |
  v
Feature Branch
  |
  v
Implementation
  |
  v
Tests / Validation
  |
  v
Pull Request
  |
  v
Human Review
  |
  v
Merge to master
```

---

## 4. Scope Discipline

An agent should modify only the files necessary for its assigned task.

Do not:

- perform unrelated refactors,
- rename unrelated files,
- rewrite imports without approval,
- delete tests because they are inconvenient,
- modify data files,
- change architectural boundaries silently.

---

## 5. Before Coding

Every agent should:

1. inspect the relevant repository structure,
2. read the applicable documentation,
3. identify existing implementations,
4. identify relevant tests,
5. state its plan,
6. implement the smallest coherent change.

---

## 6. During Coding

The agent should:

- preserve existing behavior unless the task requires change,
- write focused changes,
- add/update tests,
- avoid speculative abstractions,
- keep scientific logic explicit.

---

## 7. Before Opening a PR

The agent should report:

- files changed,
- tests executed,
- validation performed,
- known limitations,
- architectural decisions introduced.

---

## 8. Merge Gate

A change should not be merged when:

- relevant tests fail,
- scientific regressions are unexplained,
- architecture is ambiguous,
- the agent changed unrelated subsystems,
- the implementation contradicts the documented architecture without an approved decision.

---

## 9. Human Authority

Agents assist with implementation and analysis.

The final authority for:

- scientific interpretation,
- architecture,
- scope,
- release readiness

remains with the project maintainers.
