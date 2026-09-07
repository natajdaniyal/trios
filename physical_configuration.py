"""
Physical Configuration Layer (Architecture Layer 3)

Purpose
-------
Represent the physical initial condition of one or more bodies for a
single experiment stage, independently of:

    - the user interface,
    - experiment definition, objective, or prediction,
    - experiment execution and results,
    - parameter editability rules (Layer 4 - Parameter / Selection Rules).

Each experiment stage is expected to own its own independent
StagePhysicalConfiguration instance. Two stages never share or inherit
physical state from one another; a value set in one stage's
configuration has no effect on any other stage's configuration.

This module intentionally does NOT know about:

    - experiments or the ordered sequence of stages inside them,
    - learner predictions,
    - simulation execution,
    - whether a physical value is editable or fixed by the learner.

Those responsibilities belong to higher layers (Parameter / Selection
Rules, Experiment Infrastructure) and are out of scope here on purpose.
"""


class BodyPhysicalConfiguration:
    """
    The physical initial condition of a single body.

    Holds exactly the physical values identified by the architecture
    for the Physical Configuration layer:

        mass, position.x, position.y, velocity.x, velocity.y

    This class carries no notion of editability, ownership, or
    experiment/stage context. It is a plain physical value holder,
    on purpose, so that "what the value is" stays separate from
    "who is allowed to change it".
    """

    def __init__(
        self,
        name,
        mass,
        position_x=0.0,
        position_y=0.0,
        velocity_x=0.0,
        velocity_y=0.0,
    ):
        if not name:
            raise ValueError(
                "BodyPhysicalConfiguration requires a non-empty name."
            )

        if mass is None or mass <= 0:
            raise ValueError(
                f"BodyPhysicalConfiguration '{name}' requires mass > 0, "
                f"got {mass!r}."
            )

        self.name = name
        self.mass = mass

        self.position_x = position_x
        self.position_y = position_y

        self.velocity_x = velocity_x
        self.velocity_y = velocity_y

    def as_dict(self):
        """
        Return the physical values as a plain dictionary.

        Useful for serialization, logging, or comparison, without
        exposing any editability or experiment semantics.
        """

        return {
            "name": self.name,
            "mass": self.mass,
            "position_x": self.position_x,
            "position_y": self.position_y,
            "velocity_x": self.velocity_x,
            "velocity_y": self.velocity_y,
        }

    def __eq__(self, other):
        if not isinstance(other, BodyPhysicalConfiguration):
            return NotImplemented

        return self.as_dict() == other.as_dict()

    def __repr__(self):
        return (
            f"BodyPhysicalConfiguration(name={self.name!r}, "
            f"mass={self.mass!r}, "
            f"position=({self.position_x!r}, {self.position_y!r}), "
            f"velocity=({self.velocity_x!r}, {self.velocity_y!r}))"
        )


class StagePhysicalConfiguration:
    """
    The complete physical configuration of ONE experiment stage.

    A stage's physical configuration is a collection of independent
    BodyPhysicalConfiguration entries, one per body involved in that
    stage. Different stages of the same experiment are expected to
    each hold their own StagePhysicalConfiguration instance; this
    class performs no sharing or inheritance between stages -
    creating a new instance always starts empty.

    This class does not know:

        - the name/position of the stage inside an experiment,
        - editable/fixed rules for any parameter,
        - how the configuration is later turned into a running
          simulation or an experiment result.
    """

    def __init__(self, stage_name=None):
        self.stage_name = stage_name
        self._bodies = {}

    def add_body(self, body_configuration):
        """
        Add a BodyPhysicalConfiguration to this stage.

        Raises:
            TypeError: if body_configuration is not a
                BodyPhysicalConfiguration instance.
            ValueError: if a body with the same name already exists
                in this stage.
        """

        if not isinstance(body_configuration, BodyPhysicalConfiguration):
            raise TypeError(
                "add_body expects a BodyPhysicalConfiguration instance, "
                f"got {type(body_configuration)!r}."
            )

        if body_configuration.name in self._bodies:
            raise ValueError(
                f"A body named '{body_configuration.name}' already "
                f"exists in this stage configuration."
            )

        self._bodies[body_configuration.name] = body_configuration

        return body_configuration

    def get_body(self, name):
        """Return the BodyPhysicalConfiguration for name, or None."""

        return self._bodies.get(name)

    def has_body(self, name):
        return name in self._bodies

    def body_names(self):
        return list(self._bodies.keys())

    def bodies(self):
        return list(self._bodies.values())

    def __len__(self):
        return len(self._bodies)

    def __contains__(self, name):
        return name in self._bodies

    def __repr__(self):
        return (
            f"StagePhysicalConfiguration(stage_name={self.stage_name!r}, "
            f"bodies={self.body_names()!r})"
        )
