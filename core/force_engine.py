from force import Force


class ForceEngine:
    """
    Manages bodies and forces, calculates pairwise interactions,
    and applies the resulting forces to the bodies.
    """

    def __init__(self):
        self.bodies = []
        self.forces = []

    def add_body(self, body):
        """Add a body to the force system."""
        self.bodies.append(body)

    def add_force(self, force):
        """Add a force model to the force system."""
        if not isinstance(force, Force):
            raise TypeError("force must be an instance of Force")

        self.forces.append(force)

    def clear_bodies(self):
        """Remove all bodies from the force system."""
        self.bodies.clear()

    def clear_forces(self):
        """Remove all force models from the force system."""
        self.forces.clear()

    def calculate_forces(self):
        """
        Calculate and apply all pairwise forces.

        Each pair of bodies is processed only once.
        For every calculated force F_AB:
            force on A = F_AB
            force on B = -F_AB
        """

        for i in range(len(self.bodies)):
            body_a = self.bodies[i]

            for j in range(i + 1, len(self.bodies)):
                body_b = self.bodies[j]

                for force in self.forces:
                    force_vector = force.calculate(body_a, body_b)

                    body_a.apply_force(force_vector)
                    body_b.apply_force(force_vector.multiply(-1))

    def apply_forces(self):
        """
        Alias for calculate_forces().

        Kept as a clear public entry point for the force-application step.
        """
        self.calculate_forces()

    def step(self):
        """Calculate and apply all forces for the current timestep."""
        self.calculate_forces()