# TRIOS Physics Rules

## 1. Purpose

This document defines the principles that AI agents must preserve when modifying the physics side of TRIOS.

TRIOS is a numerical simulation project. Code quality alone does not establish scientific validity.

---

## 2. Physical State

The fundamental state of a body currently includes:

- name
- mass
- position
- velocity
- force accumulator

At the physical-configuration level, the initial-state parameters of interest are:

```text
mass
position.x
position.y
velocity.x
velocity.y
```

---

## 3. Force Calculation

The physics architecture supports a collection of bodies and pairwise force processing.

For gravitational interaction, each interaction must preserve Newton's third-law structure:

```text
F(A <- B) = -F(B <- A)
```

unless a future force model explicitly defines a different physical interaction.

---

## 4. Numerical Evolution

The simulation updates physical state using forces and the selected time step.

An agent must not change the numerical method merely for code style.

A numerical-method change is a scientific change and requires:

- justification,
- validation,
- comparison against the previous implementation,
- relevant regression tests.

---

## 5. Scientific Validation

The following measurements are important to TRIOS:

- total energy
- total momentum
- angular momentum
- center of mass
- sensitivity to time step
- sensitivity to initial conditions

Validation results must retain numerical values, not only pass/fail labels.

---

## 6. Important Scientific Caveat

A change in trajectory caused by a small perturbation is evidence of sensitivity, but it is not by itself sufficient to establish chaos.

Agents must not use stronger scientific claims than the measurements support.

Prefer:

```text
"The simulation shows sensitivity to the tested perturbation."
```

over an unsupported conclusion such as:

```text
"The system is proven chaotic."
```

---

## 7. Existing Numerical Baseline

The project has previously established successful validation behavior including:

- very small long-duration momentum error,
- very small angular-momentum error,
- very small center-of-mass deviation,
- measurable but controlled energy drift,
- time-step refinement reducing numerical drift.

These baselines are regression targets.

An agent that changes the numerical engine must compare new results against the existing baseline.

---

## 8. Physical Accuracy vs Software Tests

A passing test suite does not automatically prove physical correctness.

The project should maintain both:

```text
Software tests
+
Scientific validation
```

A feature is not scientifically accepted merely because its unit tests pass.
