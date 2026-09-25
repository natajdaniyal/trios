"""Physical scenario builders for TRIOS Experiment 1.

These builders connect educational scenario IDs to concrete magnetic
simulation setups. They contain no UI or learner logic.
"""

from force_engine import ForceEngine
from forces.magnetic_force import MagneticForce
from magnet import Magnet
from simulation_engine import SimulationEngine


MAGNETIC_STRENGTH = 1.0
MAGNETIC_FORCE_STRENGTH = 1.0
DEFAULT_TIME_STEP = 0.01


def _resolve_positions(default_positions, positions):
    source = default_positions if positions is None else positions
    if not isinstance(source, dict):
        raise TypeError("positions must be a dictionary.")
    if set(source) != set(default_positions):
        raise ValueError("positions must contain exactly the expected magnet names.")

    resolved = {}
    for name, value in source.items():
        if isinstance(value, bool):
            raise TypeError(f"Position for magnet {name!r} must be a number or x/y mapping.")

        if isinstance(value, (int, float)):
            resolved[name] = {"x": float(value), "y": 0.0}
            continue

        if isinstance(value, dict):
            x = value.get("x")
            y = value.get("y", 0.0)
            if (
                isinstance(x, (int, float)) and not isinstance(x, bool)
                and isinstance(y, (int, float)) and not isinstance(y, bool)
            ):
                resolved[name] = {"x": float(x), "y": float(y)}
                continue

        raise TypeError(
            f"Position for magnet {name!r} must be a number or {{'x', 'y'}} mapping."
        )
    return resolved


def _simulation(magnets, time_step=DEFAULT_TIME_STEP):
    force_engine = ForceEngine()
    force_engine.add_force(MagneticForce(MAGNETIC_FORCE_STRENGTH))
    return SimulationEngine(
        bodies=magnets,
        time_step=time_step,
        force_engine=force_engine,
    )


def build_opposite_poles_scenario(time_step=DEFAULT_TIME_STEP, positions=None):
    """Two magnets with opposite poles: attraction."""
    positions = _resolve_positions({"A": -1.0, "B": 1.0}, positions)
    return _simulation(
        [
            Magnet("A", 1.0, positions["A"]["x"], positions["A"]["y"], MAGNETIC_STRENGTH, "N"),
            Magnet("B", 1.0, positions["B"]["x"], positions["B"]["y"], MAGNETIC_STRENGTH, "S"),
        ],
        time_step=time_step,
    )


def build_same_poles_scenario(time_step=DEFAULT_TIME_STEP, positions=None):
    """Two magnets with like poles: repulsion."""
    positions = _resolve_positions({"A": -1.0, "B": 1.0}, positions)
    return _simulation(
        [
            Magnet("A", 1.0, positions["A"]["x"], positions["A"]["y"], MAGNETIC_STRENGTH, "N"),
            Magnet("B", 1.0, positions["B"]["x"], positions["B"]["y"], MAGNETIC_STRENGTH, "N"),
        ],
        time_step=time_step,
    )


def build_three_magnets_scenario(time_step=DEFAULT_TIME_STEP, positions=None):
    """Three interacting magnets: N-S-N."""
    positions = _resolve_positions(
        {
            "A": {"x": -2.2, "y": -1.0},
            "B": {"x": 0.0, "y": 1.0},
            "C": {"x": 2.2, "y": -1.0},
        },
        positions,
    )
    return _simulation(
        [
            Magnet("A", 1.0, positions["A"]["x"], positions["A"]["y"], MAGNETIC_STRENGTH, "N"),
            Magnet("B", 1.0, positions["B"]["x"], positions["B"]["y"], MAGNETIC_STRENGTH, "S"),
            Magnet("C", 1.0, positions["C"]["x"], positions["C"]["y"], MAGNETIC_STRENGTH, "N"),
        ],
        time_step=time_step,
    )


SCENARIO_BUILDERS = {
    "opposite-poles": build_opposite_poles_scenario,
    "same-poles": build_same_poles_scenario,
    "three-magnets": build_three_magnets_scenario,
}


def build_experiment_one_scenario(scenario_id, time_step=DEFAULT_TIME_STEP, positions=None):
    """Build the concrete simulation for an Experiment 1 scenario."""
    try:
        builder = SCENARIO_BUILDERS[scenario_id]
    except KeyError as exc:
        raise ValueError(f"Unknown Experiment 1 scenario: {scenario_id!r}.") from exc

    return builder(time_step=time_step, positions=positions)
