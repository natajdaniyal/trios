"""
Adapters between experiment configuration and simulation objects.
"""

from body import Body
from vector import Vector2
from force_engine import ForceEngine
from forces.gravitational_force import GravitationalForce
from physical_configuration import StagePhysicalConfiguration
from experiment_infrastructure import ExperimentStage
from simulation_engine import SimulationEngine


def bodies_from_configuration(configuration):
    if not isinstance(configuration, StagePhysicalConfiguration):
        raise TypeError(
            "bodies_from_configuration expects a StagePhysicalConfiguration instance, "
            f"got {type(configuration)!r}."
        )

    return [
        Body(
            body_configuration.name,
            body_configuration.mass,
            Vector2(body_configuration.position_x, body_configuration.position_y),
            Vector2(body_configuration.velocity_x, body_configuration.velocity_y),
        )
        for body_configuration in configuration.bodies()
    ]


def simulation_from_configuration(configuration, time_step=1, force_engine=None):
    if not isinstance(configuration, StagePhysicalConfiguration):
        raise TypeError(
            "simulation_from_configuration expects a StagePhysicalConfiguration instance, "
            f"got {type(configuration)!r}."
        )

    if force_engine is None:
        force_engine = ForceEngine()
        force_engine.add_force(GravitationalForce())

    return SimulationEngine(
        bodies=bodies_from_configuration(configuration),
        time_step=time_step,
        force_engine=force_engine,
    )


def simulation_from_stage(stage, time_step=1, force_engine=None):
    if not isinstance(stage, ExperimentStage):
        raise TypeError(
            "simulation_from_stage expects an ExperimentStage instance, "
            f"got {type(stage)!r}."
        )

    return simulation_from_configuration(
        stage.physical_configuration,
        time_step=time_step,
        force_engine=force_engine,
    )
