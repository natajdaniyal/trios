"""
Experiment Infrastructure Layer

Purpose
-------
Provide the generic "skeleton" for experiments:

    Experiment
        -> ExperimentStage (one or more)
            -> StagePhysicalConfiguration (from the Physical
               Configuration layer)

and, separately, a minimal placeholder for the outcome of running an
experiment:

    ExperimentResult

This layer defines experiment STRUCTURE only. It intentionally does
NOT know about:

    - the Physics Core (Body, ForceEngine, PhysicsEngine, ...),
    - Simulation execution,
    - learner predictions,
    - scoring, rewards, or correctness evaluation,
    - educational/validation logic,
    - the GUI or any game layer,
    - parameter editability rules (Parameter / Selection Rules layer).

Experiment Definition (what an experiment IS) is deliberately kept
separate from Experiment Execution (what happens when it RUNS).
This module only implements Experiment Definition / Infrastructure.
"""

from physical_configuration import StagePhysicalConfiguration


class ExperimentStage:
    """
    A single stage of an experiment.

    Holds exactly:

        - name
        - physical_configuration (a StagePhysicalConfiguration)

    This class does not execute simulations, does not compute
    physics, does not evaluate predictions, and has no notion of
    scoring, reward, or GUI.
    """

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
    """
    Represents an experiment as an ordered collection of stages.

    Holds exactly:

        - name
        - stages (ordered list of ExperimentStage)

    This class does not know about the Physics Engine, does not run
    simulations, does not produce scientific results, does not check
    predictions, and has no scoring, reward, or GUI concerns.
    """

    def __init__(self, name):
        self.name = name
        self._stages = []

    def add_stage(self, stage):
        """
        Add an ExperimentStage to this experiment.

        Raises:
            TypeError: if stage is not an ExperimentStage instance.
        """

        if not isinstance(stage, ExperimentStage):
            raise TypeError(
                "add_stage expects an ExperimentStage instance, got "
                f"{type(stage)!r}."
            )

        self._stages.append(stage)

        return stage

    def get_stage(self, index):
        """Return the ExperimentStage at index."""

        return self._stages[index]

    def stages(self):
        """Return the list of stages, in order."""

        return list(self._stages)

    def __len__(self):
        return len(self._stages)

    def __repr__(self):
        return (
            f"Experiment(name={self.name!r}, "
            f"stage_count={len(self._stages)})"
        )


class ExperimentResult:
    """
    A minimal, independent placeholder for experiment outcome data.

    The precise semantics of an experiment result (scientific
    conclusions, learner outcomes, scoring, etc.) have not been
    defined yet, so this class intentionally holds only a single,
    generic slot for result data and imposes no structure on it.
    """

    def __init__(self, data=None):
        self.data = data

    def __repr__(self):
        return f"ExperimentResult(data={self.data!r})"
