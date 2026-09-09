"""
Adapter between Physical Configuration and simulation Body objects.

This module converts a StagePhysicalConfiguration into the concrete
Body instances expected by the simulation layer. It does not run a
simulation and does not define any physics rules.
"""

from body import Body
from vector import Vector2
from physical_configuration import StagePhysicalConfiguration


def bodies_from_configuration(configuration):
    """
    Create fresh Body objects from a StagePhysicalConfiguration.

    The conversion copies only the physical initial-condition values:

        name, mass, position.x, position.y, velocity.x, velocity.y

    The returned Body objects are independent from the configuration's
    BodyPhysicalConfiguration objects.
    """

    if not isinstance(configuration, StagePhysicalConfiguration):
        raise TypeError(
            "bodies_from_configuration expects a "
            "StagePhysicalConfiguration instance, got "
            f"{type(configuration)!r}."
        )

    bodies = []

    for body_configuration in configuration.bodies():
        bodies.append(
            Body(
                body_configuration.name,
                body_configuration.mass,
                Vector2(
                    body_configuration.position_x,
                    body_configuration.position_y,
                ),
                Vector2(
                    body_configuration.velocity_x,
                    body_configuration.velocity_y,
                ),
            )
        )

    return bodies
