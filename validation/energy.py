class EnergySystem:
    """
    Calculates physical energy values for bodies.

    Supports:
    - Kinetic Energy
    - Gravitational Potential Energy
    - Total System Energy
    """

    def __init__(self, gravitational_constant=1):
        self.G = gravitational_constant

    def kinetic_energy(self, body):
        """
        KE = 1/2 * m * v^2
        """

        if body is None:
            return 0

        if body.velocity is None:
            return 0

        velocity_squared = (
            body.velocity.x ** 2 +
            body.velocity.y ** 2
        )

        return 0.5 * body.mass * velocity_squared

    def potential_energy(self, body_a, body_b):
        """
        PE = -G * m1 * m2 / r
        """

        if body_a is None or body_b is None:
            return 0

        dx = body_b.position.x - body_a.position.x
        dy = body_b.position.y - body_a.position.y

        distance = (
            dx ** 2 +
            dy ** 2
        ) ** 0.5

        if distance == 0:
            return 0

        return (
            -self.G *
            body_a.mass *
            body_b.mass /
            distance
        )

    def total_energy(self, bodies):
        """
        Calculates total energy of the system.

        Includes:
        - Kinetic energy of all bodies
        - Pairwise gravitational potential energy
        """

        if bodies is None:
            return 0

        total = 0

        valid_bodies = [
            body for body in bodies
            if body is not None
        ]

        for body in valid_bodies:
            total += self.kinetic_energy(body)

        for i in range(len(valid_bodies)):
            for j in range(i + 1, len(valid_bodies)):
                total += self.potential_energy(
                    valid_bodies[i],
                    valid_bodies[j]
                )

        return total