
from physics_engine import PhysicsEngine
from force_engine import ForceEngine


class SimulationEngine:

    def __init__(
        self,
        bodies=None,
        time_step=1,
        force_engine=None,
    ):
        self.bodies = []
        self.physics_engine = PhysicsEngine(time_step)
        self.force_engine = force_engine or ForceEngine()
        self.time = 0

        if bodies:
            for body in bodies:
                self.add_body(body)

    def add_body(self, body):
        """Add a body to both simulation and force systems."""
        self.bodies.append(body)
        self.force_engine.add_body(body)

    def add_force(self, force):
        """Add a force model to the force engine."""
        self.force_engine.add_force(force)

    def step(self):
        """
        Advance the simulation by one timestep.

        1. Calculate all current forces.
        2. Apply those forces to the bodies.
        3. Update each body's motion.
        4. Advance simulation time.
        """
        self.force_engine.calculate_forces()

        for body in self.bodies:
            self.physics_engine.update(body)

        self.time += self.physics_engine.time_step

    def run(self, steps):
        """Run the simulation for a given number of steps."""
        for _ in range(steps):
            self.step()