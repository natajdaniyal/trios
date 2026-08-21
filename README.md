
# TRIOS

TRIOS is an interactive physics project for simulating and exploring multi-body systems.

## Current Status

* Physics Engine: Complete ✅
* Two-Body Simulation: Supported ✅
* Three-Body Simulation: Supported ✅
* Physics Calculations: Supported ✅
* Validation: Implemented ✅
* Interactive System: Working ✅
* Project Organization: Completed ✅

## Structure

```text
TRIOS/
├── core/          # Physics engine and core components
│   └── forces/    # Gravitational and magnetic forces
├── simulation/    # Two-body and three-body simulations
├── validation/    # Energy, momentum, angular momentum
├── tools/         # Profile, reports, events and utilities
├── tests/         # Automated tests
├── legacy/        # Preserved older implementations
├── assets/
├── data/
├── experiment.py  # Interactive experiment system
├── main.py        # Main entry point
├── README.md
├── pyproject.toml
└── uv.lock
```

## Running

Run TRIOS:

```text
uv run python main.py
```

Run tests:

```text
uv run pytest
```

## Development

The physics engine is currently the main completed foundation of TRIOS. Existing systems and legacy implementations are preserved. Further development of the experiment system is currently deferred.

## Principles

TRIOS is developed incrementally with emphasis on physics correctness, validation, stability, organization, and preservation of previous work.
