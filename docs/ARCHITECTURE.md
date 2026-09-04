# TRIOS Architecture

## 1. Architectural Goal

TRIOS is designed as a layered system where each layer has a narrow responsibility.

The primary architectural rule is:

> Lower layers must not depend on higher-level educational or UI concepts.

---

## 2. Layers

### Layer 1 — Physics Core

Responsible for physical state and physical evolution.

Examples:

- Body
- Vector
- Force
- ForceEngine
- PhysicsEngine
- State

The physics core should know nothing about:

- experiments,
- learners,
- UI widgets,
- editable controls,
- game rules.

---

### Layer 2 — Simulation

Responsible for assembling physical systems and running simulations.

Examples of the current direction:

- two-body simulation/model
- three-body simulation/model
- simulation engine

Simulation code may build physical scenarios, but it should not become the owner of educational rules.

---

### Layer 3 — Physical Configuration

Purpose: represent a complete physical initial condition independently of UI or experiment logic.

Initial target parameters include:

- mass
- position.x
- position.y
- velocity.x
- velocity.y

Conceptual model:

```text
PhysicalConfiguration
    |
    +-- BodyConfiguration A
    |      +-- mass
    |      +-- position
    |      +-- velocity
    |
    +-- BodyConfiguration B
    |
    +-- BodyConfiguration C
```

This layer should make it possible to describe arbitrary initial physical states without forcing every scenario through a fixed preset model.

---

### Layer 4 — Parameter / Selection Rules

Purpose: describe what an experiment allows the learner to change.

Example:

```text
Body A
    mass       -> editable
    position.x -> fixed
    position.y -> fixed
    velocity.x -> fixed
    velocity.y -> fixed
```

This layer owns concepts such as:

- editable / fixed
- minimum
- maximum
- step
- default value
- selection metadata
- validation of allowed learner input

These are experiment-side rules, not physics properties.

---

### Layer 5 — Experiment Infrastructure

Purpose: define and run experiments.

Conceptual responsibilities:

```text
Experiment Definition
        |
        v
Selection Rules
        |
        v
Physical Configuration
        |
        v
Simulation
        |
        v
Measurements
        |
        v
Experiment Result
```

The infrastructure should eventually support many experiments without hard-coding every experiment directly into the engine.

---

### Layer 6 — Validation / Scientific Analysis

Responsible for checking numerical and scientific behavior.

Examples:

- energy conservation / drift
- momentum
- angular momentum
- center of mass
- time-step sensitivity
- initial-condition sensitivity
- regression testing

Software tests and scientific validation are related but not identical.

```text
Software correctness
        !=
Physical correctness
        !=
Scientific interpretation
```

---

### Layer 7 — GUI / UX

Responsible for presenting experiments and results to users.

The GUI must consume stable experiment/simulation interfaces.

The GUI must not implement its own physics engine.

The GUI must not secretly bypass experiment selection rules.

---

## 3. Dependency Direction

Preferred dependency direction:

```text
GUI
 |
 v
Experiment
 |
 v
Parameter Rules
 |
 v
Physical Configuration
 |
 v
Simulation
 |
 v
Physics Core
```

Validation may consume results from the simulation/experiment layers.

Lower layers must not depend upward on GUI or educational rules.

---

## 4. Existing Import Policy

The current project intentionally uses direct module imports such as:

```python
from vector import Vector2
from body import Body
```

Do not change this import strategy as part of unrelated refactoring.

Any future package/import redesign requires an explicit architecture decision.

---

## 5. Existing Infrastructure Must Be Preserved

The physics engine already supports independent physical bodies at the core level.

The existing standard two-body / three-body models are scenario generators, not the universal definition of physical state.

A new physical-configuration layer should therefore build on the existing core rather than replacing it without need.

---

## 6. Architectural Change Policy

An agent proposing an architectural change must provide:

1. Problem being solved.
2. Existing behavior that would be affected.
3. Proposed design.
4. Alternatives considered.
5. Test impact.
6. Migration impact.

No silent architectural rewrite is allowed.
