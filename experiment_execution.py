"""
Experiment execution adapter.

Connects experiment definitions to simulation construction, execution,
measurements, and optional scientific validation.
"""

from bot_runtime import BotRuntime
from experiment_infrastructure import Experiment, ExperimentResult
from simulation.physical_configuration_adapter import simulation_from_stage
from validation.system_validation import PhysicalStateSnapshot


def simulations_from_experiment(experiment, time_step=1, force_engine=None):
    """Create one independent SimulationEngine for each experiment stage."""
    if not isinstance(experiment, Experiment):
        raise TypeError(
            "simulations_from_experiment expects an Experiment instance, "
            f"got {type(experiment)!r}."
        )

    return [
        simulation_from_stage(
            stage,
            time_step=time_step,
            force_engine=force_engine,
        )
        for stage in experiment.stages()
    ]


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


def _callable_list(values, name):
    if values is None:
        return None
    if isinstance(values, (str, bytes)):
        raise TypeError(f"{name} must be an iterable of callables.")
    try:
        values = list(values)
    except TypeError as exc:
        raise TypeError(f"{name} must be an iterable of callables.") from exc
    if not all(callable(value) for value in values):
        raise TypeError(f"{name} must contain only callables.")
    return values


def run_experiment(
    experiment,
    steps_per_stage=1,
    time_step=1,
    force_engine=None,
    measurements=None,
    validators=None,
    bot_answer=None,
    bot_language=None,
):
    """Execute stages and optionally collect measurements and validations.

    A validator receives ``(initial_snapshot, final_snapshot)`` and must
    return ``(name, value)``. This keeps scientific interpretation outside
    the execution engine while giving results a stable validation container.
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

    measurements = _callable_list(measurements, "measurements")
    validators = _callable_list(validators, "validators")

    if (bot_answer is None) != (bot_language is None):
        raise ValueError("bot_answer and bot_language must be provided together.")

    if experiment.bot_configuration is not None and bot_answer is None:
        raise ValueError(
            "This experiment has a TRIOS Bot configuration and requires "
            "bot_answer and bot_language."
        )

    bot_evaluation = None
    if experiment.bot_configuration is not None:
        bot_evaluation = BotRuntime(experiment.bot_configuration).evaluate(
            bot_answer,
            bot_language,
        )

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
    if bot_evaluation is not None:
        result.set_bot_evaluation(bot_evaluation)

    for stage, simulation in zip(experiment.stages(), simulations):
        initial_snapshot = (
            PhysicalStateSnapshot.capture(simulation.bodies)
            if validators
            else None
        )

        simulation.run(steps_per_stage)
        result.data["stages"].append(_stage_result(stage, simulation))

        for measurement in measurements or []:
            name, value = measurement(simulation)
            result.add_measurement(name, value)

        if validators:
            final_snapshot = PhysicalStateSnapshot.capture(simulation.bodies)
            for validator in validators:
                name, value = validator(initial_snapshot, final_snapshot)
                result.add_validation(name, value)

    return result
