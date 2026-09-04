# TRIOS Experiment Architecture

## 1. Purpose

Experiments are educational/scientific scenarios built on top of stable physical infrastructure.

An experiment answers a question such as:

> What happens when one controlled physical property changes while the rest of the scenario remains fixed?

---

## 2. Experiment Philosophy

TRIOS experiments should generally expose a small number of meaningful choices rather than turning every physical parameter into a free-form editor.

Example:

### Experiment A

Learner may change:

```text
Body A mass
```

Everything else is fixed.

### Experiment B

Learner may change:

```text
Body A position.x
Body A position.y
```

Everything else is fixed.

### Experiment C

Learner may change:

```text
Body A velocity.x
Body A velocity.y
```

Everything else is fixed.

The exact list belongs to each experiment definition.

---

## 3. Separation of Responsibilities

An experiment should not directly manipulate low-level physics internals.

Preferred flow:

```text
Experiment Definition
        |
        v
Allowed Parameter Selection
        |
        v
Physical Configuration
        |
        v
Simulation
        |
        v
Measurements / Result
```

---

## 4. Conceptual Components

The infrastructure is expected to evolve toward concepts such as:

- ExperimentDefinition
- ExperimentEngine
- ExperimentRuntime
- ExperimentResult

The exact class names are not final until the architecture is implemented and reviewed.

---

## 5. Experiment Content vs Infrastructure

These are different things.

### Infrastructure

Reusable machinery for:

- validating selections,
- building physical configurations,
- executing simulations,
- recording results.

### Experiment Content

The scientific/educational definition of a specific activity:

- objective,
- fixed parameters,
- editable parameters,
- learner prompt,
- expected observation,
- measurements,
- interpretation.

A new experiment should preferably plug into the shared infrastructure rather than duplicate the execution machinery.

---

## 6. First Implementation Target

Before building a large experiment catalog, TRIOS should establish one small end-to-end experiment proving the architecture.

That experiment should demonstrate:

1. a defined physical configuration,
2. a limited set of editable parameters,
3. simulation execution,
4. measurement collection,
5. result storage,
6. clear educational feedback.
