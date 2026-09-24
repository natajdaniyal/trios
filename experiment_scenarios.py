"""Physical scenario builders for TRIOS Experiment 1.

These builders connect educational scenario IDs to concrete magnetic
simulation setups. They contain no UI or learner logic.
"""

from force_engine import ForceEngine
from forces.magnetic_force import MagneticForce
from magnet import Magnet
from simulation_engine import SimulationEngine


MAGNETIC_STRENGTH = 5.0
MAGNETIC_FORCE_STRENGTH = 10.0
DEFAULT_TIME_STEP = 0.01


def _simulation(magnets, time_step=DEFAULT_TIME_STEP):
    force_engine = ForceEngine()
    force_engine.add_force(MagneticForce(MAGNETIC_FORCE_STRENGTH))
    return SimulationEngine(
        bodies=magnets,
        time_step=time_step,
        force_engine=force_engine,
    )


def build_opposite_poles_scenario(time_step=DEFAULT_TIME_STEP):
    """Two magnets with opposite poles: attraction."""
    return _simulation(
        [
            Magnet("A", 1.0, -1.0, 0.0, MAGNETIC_STRENGTH, "N"),
            Magnet("B", 1.0, 1.0, 0.0, MAGNETIC_STRENGTH, "S"),
        ],
        time_step=time_step,
    )


def build_same_poles_scenario(time_step=DEFAULT_TIME_STEP):
    """Two magnets with like poles: repulsion."""
    return _simulation(
        [
            Magnet("A", 1.0, -1.0, 0.0, MAGNETIC_STRENGTH, "N"),
            Magnet("B", 1.0, 1.0, 0.0, MAGNETIC_STRENGTH, "N"),
        ],
        time_step=time_step,
    )


def build_three_magnets_scenario(time_step=DEFAULT_TIME_STEP):
    """Three interacting magnets: N-S-N."""
    return _simulation(
        [
            Magnet("A", 1.0, -2.0, 0.0, MAGNETIC_STRENGTH, "N"),
            Magnet("B", 1.0, 0.0, 0.0, MAGNETIC_STRENGTH, "S"),
            Magnet("C", 1.0, 2.0, 0.0, MAGNETIC_STRENGTH, "N"),
        ],
        time_step=time_step,
    )


SCENARIO_BUILDERS = {
    "opposite-poles": build_opposite_poles_scenario,
    "same-poles": build_same_poles_scenario,
    "three-magnets": build_three_magnets_scenario,
}


def build_experiment_one_scenario(scenario_id, time_step=DEFAULT_TIME_STEP):
    """Build the concrete simulation for an Experiment 1 scenario."""
    try:
        builder = SCENARIO_BUILDERS[scenario_id]
    except KeyError as exc:
        raise ValueError(f"Unknown Experiment 1 scenario: {scenario_id!r}.") from exc

    return builder(time_step=time_step)
