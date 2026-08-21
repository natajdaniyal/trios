class MomentumSystem:
    """
    Calculates linear momentum for physical bodies.

    Linear momentum:
        p = m * v

    Supports:
    - Momentum of a single body
    - Total momentum of a multi-body system
    - Momentum magnitude
    """

    def __init__(self):
        pass

    def body_momentum(self, body):
        """
        Calculates the linear momentum of one body.

        Returns:
            Tuple[px, py]
        """

        if body is None:
            return (0, 0)

        if body.velocity is None:
            return (0, 0)

        px = body.mass * body.velocity.x
        py = body.mass * body.velocity.y

        return (px, py)

    def total_momentum(self, bodies):
        """
        Calculates the total linear momentum of a system.

        Returns:
            Tuple[px, py]
        """

        if bodies is None:
            return (0, 0)

        total_px = 0
        total_py = 0

        for body in bodies:

            if body is None:
                continue

            momentum = self.body_momentum(body)

            total_px += momentum[0]
            total_py += momentum[1]

        return (
            total_px,
            total_py,
        )

    def momentum_magnitude(self, momentum):
        """
        Calculates the magnitude of a momentum vector.
        """

        if momentum is None:
            return 0

        px = momentum[0]
        py = momentum[1]

        return (
            px ** 2 +
            py ** 2
        ) ** 0.5