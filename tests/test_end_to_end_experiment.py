import pytest

from experiment_execution import run_experiment
from experiment_infrastructure import Experiment, ExperimentStage, ExperimentResult
from physical_configuration import BodyPhysicalConfiguration, StagePhysicalConfiguration


def make_experiment():
    configuration = StagePhysicalConfiguration(stage_name="e2e-stage")
    configuration.add_body(
        BodyPhysicalConfiguration(
            name="A",
            mass=1.0,
            position_x=0.0,
            position_y=0.0,
            velocity_x=0.0,
            velocity_y=0.0,
        )
    )
    configuration.add_body(
        BodyPhysicalConfiguration(
            name="B",
            mass=1.0,
            position_x=1.0,
            position_y=0.0,
            velocity_x=0.0,
            velocity_y=0.0,
        )
    )

    experiment = Experiment("end-to-end-gravity")
    experiment.add_stage(ExperimentStage("e2e-stage", configuration))
    return experiment


def test_end_to_end_experiment_reaches_physics_and_result():
    experiment = make_experiment()

    result = run_experiment(
        experiment,
        steps_per_stage=1,
        time_step=0.1,
    )

    assert isinstance(result, ExperimentResult)
    assert result.data["experiment_name"] == "end-to-end-gravity"

    stage_result = result.data["stages"][0]
    assert stage_result["stage_name"] == "e2e-stage"
    assert stage_result["time"] == pytest.approx(0.1)

    bodies = stage_result["bodies"]
    assert [body["name"] for body in bodies] == ["A", "B"]

    # The default adapter path must activate gravity and reach the
    # PhysicsEngine, so the initially resting bodies must acquire
    # equal-and-opposite x velocities.
    assert bodies[0]["velocity_x"] > 0
    assert bodies[1]["velocity_x"] < 0
    assert bodies[0]["velocity_y"] == pytest.approx(0.0)
    assert bodies[1]["velocity_y"] == pytest.approx(0.0)
