import pytest

from experiment_execution import simulations_from_experiment, run_experiment
from experiment_infrastructure import Experiment, ExperimentStage
from physical_configuration import BodyPhysicalConfiguration, StagePhysicalConfiguration
from simulation_engine import SimulationEngine


def make_stage(name, mass):
    configuration = StagePhysicalConfiguration()
    configuration.add_body(BodyPhysicalConfiguration("A", mass, 1.0, 2.0, 0.5, -0.5))
    return ExperimentStage(name, configuration)


def test_empty_experiment_creates_no_simulations():
    assert simulations_from_experiment(Experiment("Empty")) == []


def test_creates_one_simulation_per_stage_in_order():
    experiment = Experiment("Test")
    experiment.add_stage(make_stage("Stage 1", 10))
    experiment.add_stage(make_stage("Stage 2", 20))
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


def test_end_to_end_experiment_reaches_gravity_and_final_state():
    experiment = Experiment("gravity-integration")
    configuration = StagePhysicalConfiguration(stage_name="gravity-stage")
    configuration.add_body(BodyPhysicalConfiguration("A", 1.0, 0.0, 0.0, 0.0, 0.0))
    configuration.add_body(BodyPhysicalConfiguration("B", 1.0, 1.0, 0.0, 0.0, 0.0))
    experiment.add_stage(ExperimentStage("gravity-stage", configuration))
    result = run_experiment(experiment, steps_per_stage=1, time_step=0.01)
    stage = result.data["stages"][0]
    assert stage["time"] == pytest.approx(0.01)
    assert stage["bodies"][0]["velocity_x"] > 0
    assert stage["bodies"][1]["velocity_x"] < 0
    assert stage["bodies"][0]["position_x"] > 0
    assert stage["bodies"][1]["position_x"] < 1.0
