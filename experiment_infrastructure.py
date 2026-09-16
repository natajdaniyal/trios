"""
Experiment Infrastructure Layer

Purpose
-------
Provide the generic "skeleton" for experiments:

    Experiment
        -> ExperimentStage (one or more)
            -> StagePhysicalConfiguration (from the Physical
               Configuration layer)

and, separately, a minimal container for the outcome of running an
experiment:

    ExperimentResult

This layer defines experiment STRUCTURE only. It intentionally does
NOT know about the Physics Core, Simulation execution, learner
predictions, scoring, rewards, educational logic, or GUI behavior.
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
    """Container for generic experiment data and measured values."""

    def __init__(self, data=None, measurements=None):
        self.data = data
        self.measurements = (
            MeasurementSet() if measurements is None else measurements
        )

        if not isinstance(self.measurements, MeasurementSet):
            raise TypeError("measurements must be a MeasurementSet instance.")

    def add_measurement(self, name, value):
        return self.measurements.add(name, value)

    def get_measurement(self, name):
        return self.measurements.get(name)

    def has_measurement(self, name):
        return self.measurements.has(name)

    def __repr__(self):
        return (
            f"ExperimentResult(data={self.data!r}, "
            f"measurements={self.measurements!r})"
        )
