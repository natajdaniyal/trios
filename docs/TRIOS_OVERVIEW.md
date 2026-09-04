# TRIOS Overview

## 1. What is TRIOS?

TRIOS is a software project for simulating and studying the gravitational three-body problem.

The project has two complementary goals:

1. **Scientific / research goal**
   - Provide a reliable numerical physics engine.
   - Study numerical stability and conservation laws.
   - Investigate sensitivity to initial conditions.
   - Provide infrastructure for reproducible experiments and measurements.

2. **Educational / interactive goal**
   - Turn the three-body problem into an interactive learning environment.
   - Let the experiment designer define what physical information the learner may change.
   - Let the learner make predictions, run experiments, observe results, and understand the physical consequences.

TRIOS is therefore more than a physics engine and more than a GUI. It is a layered scientific-educational system built around a physics simulation core.

---

## 2. Current Project Status

The following parts already exist and are considered established unless a documented architecture decision changes them:

- Physics engine: operational
- Project organization: established
- Validation utilities: established
- Profile / session infrastructure: operational
- Test system: operational
- GitHub repository and branch/PR workflow: established

The existing physics engine is not a disposable prototype. New work must preserve its validated behavior unless a deliberate scientific or architectural change is approved.

---

## 3. Core Design Philosophy

### 3.1 Separate physics from education

The physics core represents physical reality:

- bodies
- mass
- position
- velocity
- forces
- integration
- simulation state

The physics core must not contain concepts such as:

- editable
- learner
- game
- experiment objective
- UI control
- educational difficulty

Those concepts belong above the physics layer.

### 3.2 Separate physical values from parameter rules

A physical value is not inherently editable or fixed.

Example:

- `Body A mass = 10`

is a physical value.

Whether the learner can change that mass is an experiment rule.

Therefore:

```text
Physical value
    !=
Selection / control rule
```

This separation is fundamental to TRIOS.

### 3.3 Documentation is part of the architecture

Architecture decisions must be documented before they become implementation conventions.

Agents must not silently redefine the architecture through code.

---

## 4. High-Level System Model

```text
                    TRIOS
                      |
        +-------------+-------------+
        |             |             |
        v             v             v
   Physics Core   Experiments      GUI
        |             |             |
        +-------------+-------------+
                      |
                 Validation
                      |
                  Results
```

A more detailed model:

```text
GUI / User Interaction
          |
          v
Experiment Layer
          |
          v
Parameter / Selection Rules
          |
          v
Physical Configuration
          |
          v
Simulation
          |
          v
Physics Core
          |
          v
Forces / Numerical Integration
          |
          v
Measurements / Results
          |
          v
Validation
```

---

## 5. Development Principle

TRIOS should be developed in layers.

Preferred order:

1. Establish architecture and contracts.
2. Build stable physical configuration infrastructure.
3. Build experiment infrastructure.
4. Strengthen scientific validation.
5. Define educational experiments.
6. Build the GUI on stable interfaces.
7. Integrate and perform full-system validation.

Do not reverse this order merely for convenience.

---

## 6. Agent Collaboration Principle

AI agents are development tools, not architectural authorities.

Every agent must:

- understand the documented architecture,
- stay within its assigned responsibility,
- avoid unrelated changes,
- preserve existing tests,
- explain important architectural changes,
- produce reviewable commits/PRs.

Final architectural and scientific decisions belong to the project owners and maintainers.

---

## 7. Source of Truth

For architecture:

```text
docs/ARCHITECTURE.md
```

For physical-engine rules:

```text
docs/PHYSICS.md
```

For experiment design:

```text
docs/EXPERIMENTS.md
```

For agent behavior:

```text
docs/AGENT_WORKFLOW.md
.github/copilot-instructions.md
```

If code conflicts with documentation, the conflict must be identified and resolved deliberately. An agent must not silently choose one side.
