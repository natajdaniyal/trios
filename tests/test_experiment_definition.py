import pytest

from experiment_definition import ExperimentDefinition
from parameter_rules import SelectionRules
from physical_configuration import StagePhysicalConfiguration


def make_configuration():
    configuration = StagePhysicalConfiguration("stage-1")
    return configuration


def test_experiment_definition_stores_core_definition():
    configuration = make_configuration()
    rules = SelectionRules()
    definition = ExperimentDefinition("mass experiment", configuration, rules)

    assert definition.name == "mass experiment"
    assert definition.physical_configuration is configuration
    assert definition.selection_rules is rules


def test_experiment_definition_creates_empty_rules_when_omitted():
    definition = ExperimentDefinition("test", make_configuration())

    assert isinstance(definition.selection_rules, SelectionRules)
    assert len(definition.selection_rules) == 0


def test_experiment_definition_builds_stage():
    configuration = make_configuration()
    definition = ExperimentDefinition("test", configuration)

    stage = definition.stage()

    assert stage.name == "test"
    assert stage.physical_configuration is configuration


def test_experiment_definition_validates_inputs():
    with pytest.raises(ValueError):
        ExperimentDefinition("", make_configuration())

    with pytest.raises(TypeError):
        ExperimentDefinition("test", object())

    with pytest.raises(TypeError):
        ExperimentDefinition("test", make_configuration(), object())
