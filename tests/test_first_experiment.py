import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest

from experiment_execution import run_experiment
from experiment_infrastructure import Experiment, ExperimentResult, ExperimentStage
from parameter_rules import ParameterRule, SelectionRules
from physical_configuration import (
    BodyPhysicalConfiguration,
    StagePhysicalConfiguration,
)
from selection_configuration import configuration_from_selection


def build_first_experiment():
    configuration = StagePhysicalConfiguration(stage_name="stage-1")
    configuration.add_body(
        BodyPhysicalConfiguration(
            name="A", mass=10.0, position_x=0.0, position_y=0.0,
            velocity_x=0.0, velocity_y=0.0,
        )
    )
    configuration.add_body(
        BodyPhysicalConfiguration(
            name="B", mass=10.0, position_x=1.0, position_y=0.0,
            velocity_x=0.0, velocity_y=0.0,
        )
    )

    rules = SelectionRules()
    rules.add_rule(
        ParameterRule(
            "A.mass", editable=True, default=10.0,
            minimum=5.0, maximum=20.0, step=5.0,
        )
    )
    return configuration, rules


def run_first_experiment(selected_mass):
    configuration, rules = build_first_experiment()
    selected_configuration = configuration_from_selection(
        configuration, rules, {"A.mass": selected_mass}
    )
    experiment = Experiment("جرم جسم A و حرکت گرانشی")
    experiment.add_stage(ExperimentStage("stage-1", selected_configuration))
    return run_experiment(experiment, steps_per_stage=1, time_step=0.01)


def test_first_experiment_definition_has_one_editable_parameter():
    configuration, rules = build_first_experiment()
    assert configuration.get_body("A").mass == 10.0
    assert configuration.get_body("B").mass == 10.0
    assert rules.has_rule("A.mass")
    assert rules.get_rule("A.mass").is_editable()


def test_first_experiment_runs_end_to_end():
    result = run_first_experiment(15.0)
    assert isinstance(result, ExperimentResult)
    stage = result.data["stages"][0]
    bodies = {body["name"]: body for body in stage["bodies"]}
    assert stage["stage_name"] == "stage-1"
    assert stage["time"] == pytest.approx(0.01)
    assert bodies["A"]["mass"] == 15.0
    assert bodies["B"]["mass"] == 10.0
    assert bodies["A"]["velocity_x"] > 0
    assert bodies["B"]["velocity_x"] < 0


def test_first_experiment_rejects_invalid_selection():
    with pytest.raises(ValueError):
        run_first_experiment(12.0)
