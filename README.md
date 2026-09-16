# 🌌 TRIOS

**TRIOS** is a Python project for simulating and studying the **gravitational three-body problem** — with a focus on physics correctness, numerical stability, reproducible experiments, and clean architecture.

> 🧪 TRIOS is being built in layers: **Physics → Simulation → Physical Configuration → Experiment Infrastructure → Validation/Education → GUI/Game**.

## 🚀 Current Status

The project currently has a working foundation for building reliable physics experiments:

- ✅ Physics Core: bodies, vectors, forces, force engine, physics engine
- ✅ Gravitational force model
- ✅ Two-body and three-body simulation support
- ✅ Physical Configuration layer
- ✅ Physical Configuration → Simulation adapter
- ✅ Experiment / Stage infrastructure
- ✅ Experiment Definition and selection/parameter rules
- ✅ Experiment execution pipeline
- ✅ Scientific validation utilities
- ✅ Center-of-mass calculation
- ✅ Automated test suite: **160 tests passing**
- ✅ Test suite currently runs with **0 warnings**

### 🧭 What is *not* being built yet

TRIOS is **not** currently creating a catalog of real educational experiments.

For now, the goal is to finish and stabilize the architecture and general infrastructure first. Real experiments, learner flows, scoring/reward systems, and GUI/Game features will come later.

## 🏗️ Architecture

The core architectural idea is a strict separation of responsibilities:

```text
Experiment
   ↓
Stage
   ↓
Physical Configuration
   ↓
Simulation
   ↓
Physics Core
```

The Physics Core stays independent from learner logic, GUI behavior, prediction, rewards, scores, or experiment-specific rules.

## 📁 Project Structure

```text
TRIOS/
├── core/                         # Physics core
│   ├── body.py
│   ├── vector.py
│   ├── force.py
│   ├── force_engine.py
│   ├── physics_engine.py
│   ├── state.py
│   └── forces/                   # Gravitational / magnetic forces
│
├── simulation/                  # Simulation layer
│   ├── simulation_engine.py
│   ├── three_body_simulation.py
│   ├── two_body_simulation.py
│   └── physical_configuration_adapter.py
│
├── validation/                  # Scientific validation utilities
│   ├── energy.py
│   ├── momentum.py
│   ├── angular_momentum.py
│   └── center_of_mass.py
│
├── tests/                       # Automated tests
│   └── validation/              # Validation-specific tests
│
├── physical_configuration.py   # Physical configuration layer
├── parameter_rules.py            # Parameter / selection rules
├── selection_configuration.py    # Selection → configuration bridge
├── experiment_infrastructure.py  # Experiment / stage / result infrastructure
├── experiment_definition.py      # Experiment definition layer
├── experiment_execution.py       # Experiment execution pipeline
├── experiment.py                 # Existing compatibility entry point
├── main.py                       # Main entry point
├── docs/                         # Architecture and project documentation
├── tools/                        # Development utilities
├── legacy/                       # Preserved older implementations
├── README.md
├── pyproject.toml
└── uv.lock
```

## ▶️ Running TRIOS

### Run the main program

```powershell
uv run python main.py
```

### Run the full test suite

```powershell
uv run pytest
```

Current baseline:

```text
160 passed
0 warnings
```

## 🔬 Scientific Focus

TRIOS is being developed around questions such as:

- How reliably can a three-body system be simulated?
- How stable are the numerical results?
- How well are energy, momentum, and angular momentum conserved?
- How sensitive is the system to initial conditions?
- How can experiments be defined and reproduced cleanly?

## 🧠 Development Principles

- **Physics stays independent.**
- **Simulation stays separate from configuration.**
- **Experiment infrastructure does not control the Physics Core.**
- **Existing functionality is preserved whenever possible.**
- **Changes are made incrementally and tested continuously.**
- **No unnecessary rewrites.**

TRIOS is a work in progress — the foundation comes first, and the more interactive/educational layers will be built on top of it step by step. 🌌🚀
