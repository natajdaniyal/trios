import os
import sys

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

import pytest

from parameter_rules import ParameterRule, SelectionRules


def test_parameter_rule_stores_definition():
    rule = ParameterRule(
        name="mass",
        editable=True,
        default=1.0,
        minimum=1.0,
        maximum=5.0,
        step=0.5,
    )

    assert rule.name == "mass"
    assert rule.is_editable() is True
    assert rule.default == 1.0
    assert rule.minimum == 1.0
    assert rule.maximum == 5.0
    assert rule.step == 0.5


def test_fixed_parameter_only_accepts_default():
    rule = ParameterRule("mass", editable=False, default=2.0)

    assert rule.validate(2.0) is True

    with pytest.raises(ValueError):
        rule.validate(3.0)


def test_editable_parameter_validates_range_and_step():
    rule = ParameterRule(
        "mass",
        editable=True,
        default=1.0,
        minimum=1.0,
        maximum=3.0,
        step=0.5,
    )

    assert rule.validate(1.0) is True
    assert rule.validate(2.5) is True

    with pytest.raises(ValueError):
        rule.validate(0.5)

    with pytest.raises(ValueError):
        rule.validate(3.5)

    with pytest.raises(ValueError):
        rule.validate(2.25)


def test_parameter_rule_rejects_invalid_definition():
    with pytest.raises(ValueError):
        ParameterRule("mass", True, 0.0, minimum=1.0)

    with pytest.raises(ValueError):
        ParameterRule("mass", True, 2.0, minimum=3.0, maximum=1.0)

    with pytest.raises(ValueError):
        ParameterRule("mass", True, 1.0, step=0)


def test_selection_rules_add_get_and_check():
    rules = SelectionRules()
    rule = ParameterRule("mass", True, 1.0)

    rules.add_rule(rule)

    assert len(rules) == 1
    assert rules.get_rule("mass") is rule
    assert rules.has_rule("mass")
    assert "mass" in rules
    assert rules.rules() == [rule]


def test_selection_rules_reject_duplicate_and_invalid_rules():
    rules = SelectionRules()
    rules.add_rule(ParameterRule("mass", True, 1.0))

    with pytest.raises(ValueError):
        rules.add_rule(ParameterRule("mass", True, 2.0))

    with pytest.raises(TypeError):
        rules.add_rule("not a rule")
