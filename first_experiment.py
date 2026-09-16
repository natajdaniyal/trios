"""Minimal end-to-end experiment proving the current TRIOS architecture."""

from experiment_execution import run_experiment
from experiment_infrastructure import Experiment, ExperimentStage
from parameter_rules import ParameterRule, SelectionRules
from physical_configuration import BodyPhysicalConfiguration, StagePhysicalConfiguration
from selection_configuration import configuration_from_selection


EXPERIMENT_NAME = "جرم جسم A و حرکت گرانشی"


def build_first_experiment():
    """Build the fixed physical scenario and its allowed selection rules."""
    configuration = StagePhysicalConfiguration(stage_name="stage-1")
    configuration.add_body(
        BodyPhysicalConfiguration(
            name="A",
            mass=10.0,
            position_x=0.0,
            position_y=0.0,
            velocity_x=0.0,
            velocity_y=0.0,
        )
    )
    configuration.add_body(
        BodyPhysicalConfiguration(
            name="B",
            mass=10.0,
            position_x=1.0,
            position_y=0.0,
            velocity_x=0.0,
            velocity_y=0.0,
        )
    )

    rules = SelectionRules()
    rules.add_rule(
        ParameterRule(
            "A.mass",
            editable=True,
            default=10.0,
            minimum=5.0,
            maximum=20.0,
            step=5.0,
        )
    )

    return Experiment(EXPERIMENT_NAME), configuration, rules


def run_first_experiment(mass_a=10.0):
    """Apply the selected mass and execute one simulation step."""
    experiment, configuration, rules = build_first_experiment()
    selected_configuration = configuration_from_selection(
        configuration,
        rules,
        {"A.mass": mass_a},
    )

    experiment.add_stage(ExperimentStage("stage-1", selected_configuration))
    return run_experiment(experiment, steps_per_stage=1, time_step=0.01)
