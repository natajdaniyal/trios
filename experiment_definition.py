from experiment_infrastructure import Experiment, ExperimentStage
from parameter_rules import SelectionRules
from physical_configuration import StagePhysicalConfiguration
from selection_configuration import configuration_from_selection


class ExperimentDefinition:
    def __init__(self, name, physical_configuration, selection_rules=None):
        if not name:
            raise ValueError("Experiment name cannot be empty.")
        if not isinstance(physical_configuration, StagePhysicalConfiguration):
            raise TypeError("physical_configuration must be a StagePhysicalConfiguration.")
        if selection_rules is None:
            selection_rules = SelectionRules()
        if not isinstance(selection_rules, SelectionRules):
            raise TypeError("selection_rules must be a SelectionRules instance.")

        self.name = name
        self.physical_configuration = physical_configuration
        self.selection_rules = selection_rules

    def stage(self, selections=None):
        configuration = configuration_from_selection(
            self.physical_configuration,
            self.selection_rules,
            selections,
        )
        return ExperimentStage(self.name, configuration)

    def build_experiment(self, selections=None):
        experiment = Experiment(self.name)
        experiment.add_stage(self.stage(selections))
        return experiment
