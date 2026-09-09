"""
Experiment execution adapter.

This module connects experiment definition to simulation construction.
It does not define experiment objectives, predictions, scoring,
rewards, editability rules, or GUI behavior.
"""

from experiment_infrastructure import Experiment
from simulation.physical_configuration_adapter import simulation_from_stage


def simulations_from_experiment(
    experiment,
    time_step=1,
    force_engine=None,
):
    """
    Create one independent SimulationEngine for each experiment stage.

    Stages are processed in their existing order. Each simulation is
    initialized only from that stage's physical configuration.

    This function prepares simulations; it does not run them. The
    number of simulation steps and result semantics are intentionally
    left undefined until the experiment execution contract is defined.
    """

    if not isinstance(experiment, Experiment):
        raise TypeError(
            "simulations_from_experiment expects an Experiment instance, "
            f"got {type(experiment)!r}."
        )

    simulations = []

    for stage in experiment.stages():
        simulations.append(
            simulation_from_stage(
                stage,
                time_step=time_step,
                force_engine=force_engine,
            )
        )

    return simulations
