import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest

from parameter_rules import ParameterRule, SelectionRules
from physical_configuration import BodyPhysicalConfiguration, StagePhysicalConfiguration
from selection_configuration import configuration_from_selection


def _configuration():
    configuration = StagePhysicalConfiguration(stage_name="stage-1")
    configuration.add_body(
        BodyPhysicalConfiguration(
            "A", 10, position_x=1, position_y=2, velocity_x=3, velocity_y=4
        )
    )
    return configuration


def _rules():
    rules = SelectionRules()
    rules.add_rule(ParameterRule("A.mass", True, 10, minimum=5, maximum=20, step=5))
    rules.add_rule(ParameterRule("A.position_x", False, 1))
    return rules


def test_applies_valid_selection_without_mutating_original():
    original = _configuration()
    result = configuration_from_selection(original, _rules(), {"A.mass": 15})

    assert result is not original
    assert result.get_body("A").mass == 15
    assert result.get_body("A").position_x == 1
    assert original.get_body("A").mass == 10


def test_rejects_invalid_selection():
    with pytest.raises(ValueError):
        configuration_from_selection(_configuration(), _rules(), {"A.mass": 12})


def test_rejects_selection_without_rule():
    with pytest.raises(ValueError):
        configuration_from_selection(
            _configuration(), _rules(), {"A.velocity_x": 8}
        )


def test_rejects_unknown_selection_name():
    with pytest.raises(ValueError):
        configuration_from_selection(_configuration(), _rules(), {"B.mass": 15})
