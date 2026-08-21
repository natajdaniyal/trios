class AngularMomentumSystem:
    """
    Computes angular momentum for bodies in a 2D system.

    For a body:
        Lz = x * py - y * px

    where:
        p = m * v

    Therefore:
        Lz = m * (x * vy - y * vx)

    The system only measures angular momentum.
    It does not modify bodies, forces, or simulation state.
    """

    def body_angular_momentum(self, body):
        """
        Calculate the angular momentum of a single body.

        Returns:
            float: Angular momentum around the origin.
        """
        mass = body.mass
        x = body.position.x
        y = body.position.y
        vx = body.velocity.x
        vy = body.velocity.y

        px = mass * vx
        py = mass * vy

        return x * py - y * px

    def total_angular_momentum(self, bodies):
        """
        Calculate the total angular momentum of a collection of bodies.

        Each body's angular momentum is calculated once and summed.

        Returns:
            float: Total angular momentum around the origin.
        """
        return sum(
            self.body_angular_momentum(body)
            for body in bodies
        )

    def angular_momentum_magnitude(self, angular_momentum):
        """
        Return the magnitude of a scalar 2D angular momentum value.

        Returns:
            float: Absolute angular momentum.
        """
        return abs(angular_momentum)