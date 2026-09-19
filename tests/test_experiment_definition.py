import pytest

from bot_configuration import BotConfiguration
from experiment_definition import ExperimentDefinition
from experiment_infrastructure import Experiment
from parameter_rules import ParameterRule, SelectionRules
from physical_configuration import BodyPhysicalConfiguration, StagePhysicalConfiguration


def make_configuration():
    configuration = StagePhysicalConfiguration("stage-1")
    configuration.add_body(BodyPhysicalConfiguration("A", 10.0))
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
    assert stage.physical_configuration is not configuration
    assert stage.physical_configuration.get_body("A").mass == 10.0


def test_experiment_definition_applies_selections_when_building_stage():
    configuration = make_configuration()
    rules = SelectionRules()
    rules.add_rule(ParameterRule("A.mass", True, 10.0, 5.0, 20.0, 5.0))
    definition = ExperimentDefinition("test", configuration, rules)

    stage = definition.stage({"A.mass": 15.0})

    assert stage.physical_configuration.get_body("A").mass == 15.0
    assert configuration.get_body("A").mass == 10.0


def test_experiment_definition_builds_experiment():
    definition = ExperimentDefinition("test", make_configuration())

    experiment = definition.build_experiment()

    assert isinstance(experiment, Experiment)
    assert experiment.name == "test"
    assert len(experiment) == 1
    assert experiment.stages()[0].name == "test"


def test_experiment_definition_validates_inputs():
    with pytest.raises(ValueError):
        ExperimentDefinition("", make_configuration())

    with pytest.raises(TypeError):
        ExperimentDefinition("test", object())

    with pytest.raises(TypeError):
        ExperimentDefinition("test", make_configuration(), object())


def test_experiment_definition_accepts_bot_configuration():
    configuration = make_configuration()
    bot = BotConfiguration(
        "فکر می‌کنی چه اتفاقی می‌افتد؟",
        ["جذب", "نزدیک"],
    )

    definition = ExperimentDefinition(
        "gravity experiment",
        configuration,
        bot_configuration=bot,
    )

    assert definition.bot_configuration is bot


def test_experiment_definition_rejects_invalid_bot_configuration():
    with pytest.raises(TypeError):
        ExperimentDefinition(
            "gravity experiment",
            make_configuration(),
            bot_configuration=object(),
        )
