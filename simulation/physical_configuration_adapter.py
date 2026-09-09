"""
Adapters between experiment configuration and simulation objects.

This module converts physical configuration data into concrete objects
expected by the simulation layer. It does not define physics rules and
does not create or evaluate experiments.
"""

from body import Body
from vector import Vector2
from physical_configuration import StagePhysicalConfiguration
from experiment_infrastructure import ExperimentStage
from simulation_engine import SimulationEngine


def bodies_from_configuration(configuration):
    """
    Create fresh Body objects from a StagePhysicalConfiguration.

    The conversion copies only the physical initial-condition values:

        name, mass, position.x, position.y, velocity.x, velocity.y

    The returned Body objects are independent from the configuration's
    BodyPhysicalConfiguration objects.
    """

    if not isinstance(configuration, StagePhysicalConfiguration):
        raise TypeError(
            "bodies_from_configuration expects a "
            "StagePhysicalConfiguration instance, got "
            f"{type(configuration)!r}."
        )

    bodies = []

    for body_configuration in configuration.bodies():
        bodies.append(
            Body(
                body_configuration.name,
                body_configuration.mass,
                Vector2(
                    body_configuration.position_x,
                    body_configuration.position_y,
                ),
                Vector2(
                    body_configuration.velocity_x,
                    body_configuration.velocity_y,
                ),
            )
        )

    return bodies


def simulation_from_configuration(
    configuration,
    time_step=1,
    force_engine=None,
):
    """
    Create a SimulationEngine initialized from a physical configuration.

    The configuration supplies only the initial physical state. The
    simulation engine remains responsible for execution. No experiment
    semantics are introduced here.
    """

    if not isinstance(configuration, StagePhysicalConfiguration):
        raise TypeError(
            "simulation_from_configuration expects a "
            "StagePhysicalConfiguration instance, got "
            f"{type(configuration)!r}."
        )

    return SimulationEngine(
        bodies=bodies_from_configuration(configuration),
        time_step=time_step,
        force_engine=force_engine,
    )


def simulation_from_stage(
    stage,
    time_step=1,
    force_engine=None,
):
    """
    Create a SimulationEngine from an ExperimentStage.

    The stage remains a definition object. This adapter simply reads its
    physical configuration and delegates the conversion to
    simulation_from_configuration().
    """

    if not isinstance(stage, ExperimentStage):
        raise TypeError(
            "simulation_from_stage expects an ExperimentStage instance, got "
            f"{type(stage)!r}."
        )

    return simulation_from_configuration(
        stage.physical_configuration,
        time_step=time_step,
        force_engine=force_engine,
    )
