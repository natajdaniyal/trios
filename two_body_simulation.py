from body import Body
from vector import Vector2
from forces.gravitational_force import GravitationalForce
from force_engine import ForceEngine
from physics_engine import PhysicsEngine


class TwoBodySimulation:
    """
    Basic two-body orbital simulation.

    Creates two bodies with initial orbital conditions
    and updates their motion using gravity.
    """

    def __init__(
        self,
        mass_a=1000,
        mass_b=1000,
        distance=100,
        time_step=0.01,
    ):

        self.body_a = Body(
            "Body A",
            mass_a,
            Vector2(
                -distance / 2,
                0
            ),
            Vector2(
                0,
                -1
            )
        )

        self.body_b = Body(
            "Body B",
            mass_b,
            Vector2(
                distance / 2,
                0
            ),
            Vector2(
                0,
                1
            )
        )

        self.physics_engine = PhysicsEngine(
            time_step
        )

        self.force_engine = ForceEngine()

        self.gravity = GravitationalForce(
            G=1
        )

        self.force_engine.add_body(
            self.body_a
        )

        self.force_engine.add_body(
            self.body_b
        )

        self.force_engine.add_force(
            self.gravity
        )

        self.time = 0


    def step(self):

        # Calculate gravitational interaction
        self.force_engine.calculate_forces()

        # Update motion
        self.physics_engine.update(
            self.body_a
        )

        self.physics_engine.update(
            self.body_b
        )

        self.time += self.physics_engine.time_step


    def run(self, steps):

        for _ in range(steps):
            self.step()


    def distance_between_bodies(self):

        dx = (
            self.body_a.position.x
            -
            self.body_b.position.x
        )

        dy = (
            self.body_a.position.y
            -
            self.body_b.position.y
        )

        return (
            dx ** 2 +
            dy ** 2
        ) ** 0.5