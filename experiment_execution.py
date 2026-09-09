"""
Experiment execution adapter.

This module connects experiment definition to simulation construction
and execution. It does not define experiment objectives, predictions,
scoring, rewards, editability rules, or GUI behavior.
"""

from experiment_infrastructure import Experiment, ExperimentResult
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


def run_experiment(
    experiment,
    steps_per_stage=1,
    time_step=1,
    force_engine=None,
):
    """
    Execute each experiment stage independently for a fixed number of steps.

    The returned ExperimentResult contains one record per stage. Each
    record stores the stage name, final simulation time, and the final
    physical state of each body.

    This function does not evaluate predictions, calculate scores or
    rewards, apply educational rules, or persist experiment data.
    """

    if not isinstance(experiment, Experiment):
        raise TypeError(
            "run_experiment expects an Experiment instance, "
            f"got {type(experiment)!r}."
        )

    if not isinstance(steps_per_stage, int) or isinstance(steps_per_stage, bool):
        raise TypeError("steps_per_stage must be an integer.")

    if steps_per_stage < 0:
        raise ValueError("steps_per_stage must be >= 0.")

    simulations = simulations_from_experiment(
        experiment,
        time_step=time_step,
        force_engine=force_engine,
    )

    stage_results = []

    for stage, simulation in zip(experiment.stages(), simulations):
        simulation.run(steps_per_stage)

        stage_results.append(
            {
                "stage_name": stage.name,
                "time": simulation.time,
                "bodies": [
                    {
                        "name": body.name,
                        "mass": body.mass,
                        "position_x": body.position.x,
                        "position_y": body.position.y,
                        "velocity_x": body.velocity.x,
                        "velocity_y": body.velocity.y,
                    }
                    for body in simulation.bodies
                ],
            }
        )

    return ExperimentResult(
        data={
            "experiment_name": experiment.name,
            "stages": stage_results,
        }
    )
