from math import sqrt

from body import Body
from vector import Vector2


class ThreeBodyModel:
    """
    Creates a three-body gravitational initial configuration
    using an equilateral-triangle central configuration.

    The three bodies are placed at the vertices of an equilateral
    triangle with side length = distance.

    The configuration is shifted so that the center of mass is at
    the origin.

    Initial velocities are tangential to the circular motion around
    the center of mass and are derived from the gravitational dynamics.
    """

    def __init__(
        self,
        mass_a=10,
        mass_b=10,
        mass_c=10,
        distance=10,
        G=1.0,
    ):
        self.mass_a = mass_a
        self.mass_b = mass_b
        self.mass_c = mass_c
        self.distance = distance
        self.G = G

        self.body_a = None
        self.body_b = None
        self.body_c = None

        self.create()

    @property
    def bodies(self):
        return [
            self.body_a,
            self.body_b,
            self.body_c,
        ]

    def create(self):
        positions = self.calculate_initial_positions()
        angular_velocity = self.calculate_angular_velocity()

        self.body_a = Body(
            "Body A",
            self.mass_a,
            positions[0],
            self.calculate_velocity(
                positions[0],
                angular_velocity
            )
        )

        self.body_b = Body(
            "Body B",
            self.mass_b,
            positions[1],
            self.calculate_velocity(
                positions[1],
                angular_velocity
            )
        )

        self.body_c = Body(
            "Body C",
            self.mass_c,
            positions[2],
            self.calculate_velocity(
                positions[2],
                angular_velocity
            )
        )

        return (
            self.body_a,
            self.body_b,
            self.body_c,
        )

    def calculate_initial_positions(self):
        """
        Create an equilateral triangle and shift it so that
        the center of mass is at the origin.
        """

        height = sqrt(3) * self.distance / 2

        raw_a = Vector2(
            0,
            2 * height / 3
        )

        raw_b = Vector2(
            -self.distance / 2,
            -height / 3
        )

        raw_c = Vector2(
            self.distance / 2,
            -height / 3
        )

        total_mass = (
            self.mass_a +
            self.mass_b +
            self.mass_c
        )

        center_x = (
            self.mass_a * raw_a.x +
            self.mass_b * raw_b.x +
            self.mass_c * raw_c.x
        ) / total_mass

        center_y = (
            self.mass_a * raw_a.y +
            self.mass_b * raw_b.y +
            self.mass_c * raw_c.y
        ) / total_mass

        return [
            Vector2(
                raw_a.x - center_x,
                raw_a.y - center_y
            ),
            Vector2(
                raw_b.x - center_x,
                raw_b.y - center_y
            ),
            Vector2(
                raw_c.x - center_x,
                raw_c.y - center_y
            ),
        ]

    def calculate_angular_velocity(self):
        """
        Angular velocity of the equilateral three-body
        central configuration.

        omega^2 = G * M / distance^3
        """

        total_mass = (
            self.mass_a +
            self.mass_b +
            self.mass_c
        )

        return sqrt(
            self.G * total_mass / self.distance ** 3
        )

    def calculate_velocity(self, position, angular_velocity):
        """
        Tangential velocity for counter-clockwise rotation:

            vx = -omega * y
            vy =  omega * x
        """

        return Vector2(
            -angular_velocity * position.y,
            angular_velocity * position.x
        )