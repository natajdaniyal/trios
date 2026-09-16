from experiment_infrastructure import ExperimentStage
from parameter_rules import SelectionRules
from physical_configuration import StagePhysicalConfiguration


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

    def stage(self):
        return ExperimentStage(self.name, self.physical_configuration)
