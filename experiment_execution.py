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
    """Create one independent SimulationEngine for each experiment stage."""
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


def _stage_result(stage, simulation):
    return {
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


def run_experiment(
    experiment,
    steps_per_stage=1,
    time_step=1,
    force_engine=None,
    measurements=None,
):
    """Execute experiment stages and optionally collect measured values.

    ``measurements`` is an optional iterable of callables. Each callable
    receives the completed stage simulation and must return ``(name, value)``.
    Measurement storage remains generic; this function does not define
    scientific metrics itself.
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
    if measurements is not None:
        if isinstance(measurements, (str, bytes)):
            raise TypeError("measurements must be an iterable of callables.")
        try:
            measurements = list(measurements)
        except TypeError as exc:
            raise TypeError("measurements must be an iterable of callables.") from exc
        if not all(callable(measurement) for measurement in measurements):
            raise TypeError("measurements must contain only callables.")

    simulations = simulations_from_experiment(
        experiment,
        time_step=time_step,
        force_engine=force_engine,
    )

    result = ExperimentResult(
        data={
            "experiment_name": experiment.name,
            "stages": [],
        }
    )

    for stage, simulation in zip(experiment.stages(), simulations):
        simulation.run(steps_per_stage)
        result.data["stages"].append(_stage_result(stage, simulation))

        for measurement in measurements or []:
            name, value = measurement(simulation)
            result.add_measurement(name, value)

    return result
