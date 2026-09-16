import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest

from experiment_infrastructure import ExperimentResult
from first_experiment import build_first_experiment, run_first_experiment


def test_first_experiment_definition_has_one_editable_parameter():
    experiment, configuration, rules = build_first_experiment()

    assert experiment.name == "جرم جسم A و حرکت گرانشی"
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
