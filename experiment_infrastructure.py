"""
Experiment Infrastructure Layer

Defines experiment structure and generic result containers. It does not
know about physics, simulation execution, learner behavior, or GUI logic.
"""

from measurement import MeasurementSet
from physical_configuration import StagePhysicalConfiguration


class ExperimentStage:
    """A single stage containing a name and physical configuration."""

    def __init__(self, name, physical_configuration):
        if not isinstance(physical_configuration, StagePhysicalConfiguration):
            raise TypeError(
                "ExperimentStage requires physical_configuration to be a "
                "StagePhysicalConfiguration instance, got "
                f"{type(physical_configuration)!r}."
            )

        self.name = name
        self.physical_configuration = physical_configuration

    def __repr__(self):
        return (
            f"ExperimentStage(name={self.name!r}, "
            f"physical_configuration={self.physical_configuration!r})"
        )


class Experiment:
    """Represents an experiment as an ordered collection of stages."""

    def __init__(self, name):
        self.name = name
        self._stages = []

    def add_stage(self, stage):
        if not isinstance(stage, ExperimentStage):
            raise TypeError(
                "add_stage expects an ExperimentStage instance, got "
                f"{type(stage)!r}."
            )

        self._stages.append(stage)
        return stage

    def get_stage(self, index):
        return self._stages[index]

    def stages(self):
        return list(self._stages)

    def __len__(self):
        return len(self._stages)

    def __repr__(self):
        return (
            f"Experiment(name={self.name!r}, "
            f"stage_count={len(self._stages)})"
        )


class ExperimentResult:
    """Container for generic experiment data, measurements, and validations."""

    def __init__(self, data=None, measurements=None, validations=None):
        self.data = data
        self.measurements = (
            MeasurementSet() if measurements is None else measurements
        )
        self.validations = {} if validations is None else validations

        if not isinstance(self.measurements, MeasurementSet):
            raise TypeError("measurements must be a MeasurementSet instance.")
        if not isinstance(self.validations, dict):
            raise TypeError("validations must be a dict instance.")

    def add_measurement(self, name, value):
        return self.measurements.add(name, value)

    def get_measurement(self, name):
        return self.measurements.get(name)

    def has_measurement(self, name):
        return self.measurements.has(name)

    def add_validation(self, name, value):
        if not name:
            raise ValueError("Validation name cannot be empty.")
        if name in self.validations:
            raise ValueError(f"Validation already exists: {name!r}.")

        self.validations[name] = value
        return value

    def get_validation(self, name):
        return self.validations[name]

    def has_validation(self, name):
        return name in self.validations

    def __repr__(self):
        return (
            f"ExperimentResult(data={self.data!r}, "
            f"measurements={self.measurements!r}, "
            f"validations={self.validations!r})"
        )
