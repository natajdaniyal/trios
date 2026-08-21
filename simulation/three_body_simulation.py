import math

from body import Body
from vector import Vector2
from forces.gravitational_force import GravitationalForce
from force_engine import ForceEngine
from physics_engine import PhysicsEngine


class ThreeBodySimulation:
    """
    Basic three-body gravitational simulation.

    Creates three bodies in an equilateral-triangle configuration
    with circular rotating initial conditions and updates their
    motion using pairwise gravity.
    """

    def __init__(
        self,
        mass_a=1000,
        mass_b=1000,
        mass_c=1000,
        distance=100,
        time_step=0.01,
        G=1,
    ):
        self.G = G

        # ---------------------------------------------------------
        # 1. Create equilateral-triangle geometry
        # ---------------------------------------------------------
        height = (
            math.sqrt(3)
            * distance
            / 2
        )

        raw_position_a = Vector2(
            -distance / 2,
            -height / 3,
        )

        raw_position_b = Vector2(
            distance / 2,
            -height / 3,
        )

        raw_position_c = Vector2(
            0,
            2 * height / 3,
        )

        # ---------------------------------------------------------
        # 2. Shift geometry to the true center of mass
        # ---------------------------------------------------------
        total_mass = (
            mass_a
            + mass_b
            + mass_c
        )

        center_of_mass_x = (
            mass_a * raw_position_a.x
            + mass_b * raw_position_b.x
            + mass_c * raw_position_c.x
        ) / total_mass

        center_of_mass_y = (
            mass_a * raw_position_a.y
            + mass_b * raw_position_b.y
            + mass_c * raw_position_c.y
        ) / total_mass

        position_a = Vector2(
            raw_position_a.x - center_of_mass_x,
            raw_position_a.y - center_of_mass_y,
        )

        position_b = Vector2(
            raw_position_b.x - center_of_mass_x,
            raw_position_b.y - center_of_mass_y,
        )

        position_c = Vector2(
            raw_position_c.x - center_of_mass_x,
            raw_position_c.y - center_of_mass_y,
        )

        # ---------------------------------------------------------
        # 3. Calculate common angular velocity
        #
        # For an equilateral three-body configuration:
        #
        # omega² = G * M / distance³
        # ---------------------------------------------------------
        omega_squared = (
            G
            * total_mass
            / (distance ** 3)
        )

        omega = math.sqrt(
            omega_squared
        )

        # ---------------------------------------------------------
        # 4. Tangential velocities
        #
        # v = omega × r
        #
        # In 2D:
        # vx = -omega * y
        # vy =  omega * x
        # ---------------------------------------------------------
        velocity_a = Vector2(
            -omega * position_a.y,
            omega * position_a.x,
        )

        velocity_b = Vector2(
            -omega * position_b.y,
            omega * position_b.x,
        )

        velocity_c = Vector2(
            -omega * position_c.y,
            omega * position_c.x,
        )

        # ---------------------------------------------------------
        # 5. Create bodies
        # ---------------------------------------------------------
        self.body_a = Body(
            "Body A",
            mass_a,
            position_a,
            velocity_a,
        )

        self.body_b = Body(
            "Body B",
            mass_b,
            position_b,
            velocity_b,
        )

        self.body_c = Body(
            "Body C",
            mass_c,
            position_c,
            velocity_c,
        )

        # Convenient collection
        self.bodies = [
            self.body_a,
            self.body_b,
            self.body_c,
        ]

        # ---------------------------------------------------------
        # 6. Physics infrastructure
        # ---------------------------------------------------------
        self.physics_engine = PhysicsEngine(
            time_step
        )

        self.force_engine = ForceEngine()

        self.gravity = GravitationalForce(
            G=G
        )

        # ---------------------------------------------------------
        # 7. Register bodies
        # ---------------------------------------------------------
        self.force_engine.add_body(
            self.body_a
        )

        self.force_engine.add_body(
            self.body_b
        )

        self.force_engine.add_body(
            self.body_c
        )

        # ---------------------------------------------------------
        # 8. Register gravity
        # ---------------------------------------------------------
        self.force_engine.add_force(
            self.gravity
        )

        self.time = 0

    # -------------------------------------------------------------
    # Simulation Step
    # -------------------------------------------------------------
    def step(self):

        # Calculate all pairwise gravitational interactions
        self.force_engine.calculate_forces()

        # Update all three bodies
        self.physics_engine.update(
            self.body_a
        )

        self.physics_engine.update(
            self.body_b
        )

        self.physics_engine.update(
            self.body_c
        )

        # Advance simulation time
        self.time += (
            self.physics_engine.time_step
        )

    # -------------------------------------------------------------
    # Run Simulation
    # -------------------------------------------------------------
    def run(self, steps):

        for _ in range(steps):
            self.step()

    # -------------------------------------------------------------
    # Pairwise Distances
    # -------------------------------------------------------------
    def distance_ab(self):

        dx = (
            self.body_a.position.x
            - self.body_b.position.x
        )

        dy = (
            self.body_a.position.y
            - self.body_b.position.y
        )

        return (
            dx ** 2
            + dy ** 2
        ) ** 0.5

    def distance_ac(self):

        dx = (
            self.body_a.position.x
            - self.body_c.position.x
        )

        dy = (
            self.body_a.position.y
            - self.body_c.position.y
        )

        return (
            dx ** 2
            + dy ** 2
        ) ** 0.5

    def distance_bc(self):

        dx = (
            self.body_b.position.x
            - self.body_c.position.x
        )

        dy = (
            self.body_b.position.y
            - self.body_c.position.y
        )

        return (
            dx ** 2
            + dy ** 2
        ) ** 0.5