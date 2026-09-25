
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

        self._resolve_collisions()
        self.time += self.physics_engine.time_step

    def _resolve_collisions(self):
        for index, body_a in enumerate(self.bodies):
            radius_a = float(getattr(body_a, "collision_radius", 0.0) or 0.0)
            if radius_a <= 0:
                continue
            for body_b in self.bodies[index + 1:]:
                radius_b = float(getattr(body_b, "collision_radius", 0.0) or 0.0)
                if radius_b <= 0:
                    continue
                delta = body_b.position.subtract(body_a.position)
                distance = delta.length()
                minimum_distance = radius_a + radius_b
                if distance >= minimum_distance:
                    continue
                normal = body_a.position.__class__(1, 0) if distance == 0 else delta.multiply(1 / distance)
                overlap = minimum_distance - distance
                total_radius = radius_a + radius_b
                body_a.position = body_a.position.add(normal.multiply(-overlap * radius_b / total_radius))
                body_b.position = body_b.position.add(normal.multiply(overlap * radius_a / total_radius))
                relative_normal_speed = ((body_b.velocity.x - body_a.velocity.x) * normal.x + (body_b.velocity.y - body_a.velocity.y) * normal.y)
                if relative_normal_speed < 0:
                    body_a.velocity = body_a.velocity.add(normal.multiply(-relative_normal_speed * radius_b / total_radius))
                    body_b.velocity = body_b.velocity.add(normal.multiply(relative_normal_speed * radius_a / total_radius))

    def run(self, steps):
        """Run the simulation for a given number of steps."""
        for _ in range(steps):
            self.step()