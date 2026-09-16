class CenterOfMassSystem:
    """
    Calculates the center of mass of a 2D body system.

    The center of mass is a validation/measurement quantity. This class
    reads physical state only and does not modify bodies or simulations.
    """

    def body_weighted_position(self, body):
        """Return the mass-weighted position contribution of one body."""
        if body is None:
            return (0, 0, 0)

        return (
            body.mass * body.position.x,
            body.mass * body.position.y,
            body.mass,
        )

    def total_mass(self, bodies):
        """Return the total mass of the system."""
        if bodies is None:
            return 0

        return sum(
            body.mass
            for body in bodies
            if body is not None
        )

    def center_of_mass(self, bodies):
        """Return the system center of mass as ``(x, y)``."""
        if bodies is None:
            return (0, 0)

        weighted_x = 0
        weighted_y = 0
        total_mass = 0

        for body in bodies:
            if body is None:
                continue

            weighted_x += body.mass * body.position.x
            weighted_y += body.mass * body.position.y
            total_mass += body.mass

        if total_mass == 0:
            return (0, 0)

        return (
            weighted_x / total_mass,
            weighted_y / total_mass,
        )
