import os
import sys

sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

import pytest

from physical_configuration import (
    BodyPhysicalConfiguration,
    StagePhysicalConfiguration,
)

from experiment_infrastructure import (
    Experiment,
    ExperimentStage,
    ExperimentResult,
)

from measurement import MeasurementSet


def make_body(name="A", mass=10):
    return BodyPhysicalConfiguration(
        name=name,
        mass=mass,
        position_x=1.0,
        position_y=2.0,
        velocity_x=0.5,
        velocity_y=-0.5,
    )


def make_stage_config(*body_names):
    config = StagePhysicalConfiguration()
    for name in body_names:
        config.add_body(make_body(name))
    return config


# --------------------------------------------------------------
# Experiment
# --------------------------------------------------------------

def test_experiment_creation():
    experiment = Experiment(name="Test Experiment")

    assert experiment.name == "Test Experiment"


def test_experiment_starts_with_no_stages():
    experiment = Experiment(name="Test Experiment")

    assert len(experiment) == 0
    assert experiment.stages() == []


def test_experiment_add_stage():
    experiment = Experiment(name="Test Experiment")
    stage = ExperimentStage("Stage 1", make_stage_config("A"))

    experiment.add_stage(stage)

    assert len(experiment) == 1
    assert experiment.stages() == [stage]


def test_experiment_get_stage():
    experiment = Experiment(name="Test Experiment")
    stage = ExperimentStage("Stage 1", make_stage_config("A"))

    experiment.add_stage(stage)

    assert experiment.get_stage(0) is stage


def test_experiment_multiple_stages():
    experiment = Experiment(name="Test Experiment")

    stage_1 = ExperimentStage("Stage 1", make_stage_config("A"))
    stage_2 = ExperimentStage("Stage 2", make_stage_config("A"))

    experiment.add_stage(stage_1)
    experiment.add_stage(stage_2)

    assert experiment.stages() == [stage_1, stage_2]


def test_experiment_stage_count():
    experiment = Experiment(name="Test Experiment")

    experiment.add_stage(ExperimentStage("Stage 1", make_stage_config("A")))
    experiment.add_stage(ExperimentStage("Stage 2", make_stage_config("A")))
    experiment.add_stage(ExperimentStage("Stage 3", make_stage_config("A")))

    assert len(experiment) == 3


def test_experiment_add_stage_rejects_invalid_type():
    experiment = Experiment(name="Test Experiment")

    with pytest.raises(TypeError):
        experiment.add_stage("not a stage")


# --------------------------------------------------------------
# ExperimentStage
# --------------------------------------------------------------

def test_experiment_stage_creation():
    config = make_stage_config("A")
    stage = ExperimentStage("Stage 1", config)

    assert stage.name == "Stage 1"


def test_experiment_stage_holds_physical_configuration():
    config = make_stage_config("A")
    stage = ExperimentStage("Stage 1", config)

    assert stage.physical_configuration is config


def test_experiment_stage_rejects_invalid_physical_configuration_type():
    with pytest.raises(TypeError):
        ExperimentStage("Stage 1", "not a physical configuration")


# --------------------------------------------------------------
# ExperimentResult
# --------------------------------------------------------------

def test_experiment_result_creation():
    result = ExperimentResult()

    assert result.data is None
    assert isinstance(result.measurements, MeasurementSet)
    assert len(result.measurements) == 0


def test_experiment_result_holds_data():
    result = ExperimentResult(data={"anything": "goes"})

    assert result.data == {"anything": "goes"}


def test_experiment_result_adds_and_reads_measurement():
    result = ExperimentResult()

    result.add_measurement("energy", 12.5)

    assert result.has_measurement("energy")
    assert result.get_measurement("energy") == 12.5


# --------------------------------------------------------------
# Stage independence (through Experiment Infrastructure)
# --------------------------------------------------------------

def test_stages_are_independent_through_experiment():
    experiment = Experiment(name="Independence Test")

    config_1 = StagePhysicalConfiguration()
    config_1.add_body(make_body("A", mass=10))

    config_2 = StagePhysicalConfiguration()
    config_2.add_body(make_body("A", mass=999))

    stage_1 = ExperimentStage("Stage 1", config_1)
    stage_2 = ExperimentStage("Stage 2", config_2)

    experiment.add_stage(stage_1)
    experiment.add_stage(stage_2)

    assert stage_1.physical_configuration.get_body("A").mass == 10
    assert stage_2.physical_configuration.get_body("A").mass == 999

    # Mutating stage 2's configuration must not affect stage 1
    stage_2.physical_configuration.get_body("A").mass = 12345

    assert stage_1.physical_configuration.get_body("A").mass == 10
