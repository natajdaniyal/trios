import pytest

from experiment_execution import simulations_from_experiment
from experiment_infrastructure import Experiment, ExperimentStage
from physical_configuration import (
    BodyPhysicalConfiguration,
    StagePhysicalConfiguration,
)
from simulation_engine import SimulationEngine


def make_stage(name, mass):
    configuration = StagePhysicalConfiguration()
    configuration.add_body(
        BodyPhysicalConfiguration(
            name="A",
            mass=mass,
            position_x=1.0,
            position_y=2.0,
            velocity_x=0.5,
            velocity_y=-0.5,
        )
    )
    return ExperimentStage(name, configuration)


def test_empty_experiment_creates_no_simulations():
    experiment = Experiment("Empty")

    simulations = simulations_from_experiment(experiment)

    assert simulations == []


def test_creates_one_simulation_per_stage_in_order():
    experiment = Experiment("Test")
    stage_1 = make_stage("Stage 1", 10)
    stage_2 = make_stage("Stage 2", 20)

    experiment.add_stage(stage_1)
    experiment.add_stage(stage_2)

    simulations = simulations_from_experiment(experiment)

    assert len(simulations) == 2
    assert all(isinstance(simulation, SimulationEngine) for simulation in simulations)
    assert [simulation.bodies[0].mass for simulation in simulations] == [10, 20]


def test_simulations_are_independent():
    experiment = Experiment("Independence")
    experiment.add_stage(make_stage("Stage 1", 10))
    experiment.add_stage(make_stage("Stage 2", 20))

    simulations = simulations_from_experiment(experiment)

    assert simulations[0] is not simulations[1]
    assert simulations[0].bodies[0] is not simulations[1].bodies[0]


def test_time_step_is_forwarded_to_each_simulation():
    experiment = Experiment("Time Step")
    experiment.add_stage(make_stage("Stage 1", 10))
    experiment.add_stage(make_stage("Stage 2", 20))

    simulations = simulations_from_experiment(experiment, time_step=0.25)

    assert [simulation.physics_engine.time_step for simulation in simulations] == [0.25, 0.25]


def test_rejects_invalid_experiment_type():
    with pytest.raises(TypeError):
        simulations_from_experiment("not an experiment")


def make_gravity_experiment():
    configuration = StagePhysicalConfiguration(stage_name="gravity-stage")
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

    experiment = Experiment("gravity-integration")
    experiment.add_stage(ExperimentStage("gravity-stage", configuration))
    return experiment


def test_end_to_end_experiment_reaches_gravity_and_final_state():
    experiment = make_gravity_experiment()

    result = __import__("experiment_execution").run_experiment(
        experiment,
        steps_per_stage=1,
        time_step=0.01,
    )

    assert result.data["experiment_name"] == "gravity-integration"
    assert len(result.data["stages"]) == 1

    stage = result.data["stages"][0]
    assert stage["stage_name"] == "gravity-stage"
    assert stage["time"] == pytest.approx(0.01)

    body_a = stage["bodies"][0]
    body_b = stage["bodies"][1]

    assert body_a["velocity_x"] > 0
    assert body_b["velocity_x"] < 0
    assert body_a["position_x"] > 0
    assert body_b["position_x"] < 1.0


def test_experiment_execution_script_uses_the_same_path(monkeypatch):
    from experiment import _build_demo_experiment, run_test

    class FakeProfile:
        def __init__(self):
            self.saved = None

        def add_experiment(self, name, prediction, result, correct):
            self.saved = {
                "name": name,
                "prediction": prediction,
                "result": result,
                "correct": correct,
            }

    profile = FakeProfile()
    monkeypatch.setattr("builtins.input", lambda prompt: "gravity prediction")

    experiment = _build_demo_experiment()
    assert isinstance(experiment, Experiment)
    assert len(experiment) == 1

    run_test(profile)

    assert profile.saved is not None
    assert profile.saved["name"] == "آزمایش آزمایشی نیرو"
    assert profile.saved["correct"] is True
    assert "گرانشی" in profile.saved["result"]


if __name__ == "__main__":
    print("🌌 TRIOS EXPERIMENT EXECUTION TEST")
    print("=" * 55)
    test_empty_experiment_creates_no_simulations()
    test_creates_one_simulation_per_stage_in_order()
    test_simulations_are_independent()
    test_time_step_is_forwarded_to_each_simulation()
    test_rejects_invalid_experiment_type()
    test_end_to_end_experiment_reaches_gravity_and_final_state()
    print("✅ Experiment → Stage → Configuration → Simulation → Gravity → Result")
    print("🟢 EXPERIMENT EXECUTION CHAIN HEALTHY")
