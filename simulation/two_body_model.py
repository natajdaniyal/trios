from math import sqrt

from body import Body
from vector import Vector2


class TwoBodyModel:
    """
    Creates a two-body gravitational initial configuration.
    """

    def __init__(
        self,
        mass_a=10,
        mass_b=10,
        distance=10,
        G=1.0,
    ):
        self.mass_a = mass_a
        self.mass_b = mass_b
        self.distance = distance
        self.G = G

        self.body_a = None
        self.body_b = None

        self.create()

    @property
    def bodies(self):
        return [
            self.body_a,
            self.body_b,
        ]

    def create(self):
        velocity = self.calculate_orbital_velocity()

        self.body_a = Body(
            "Body A",
            self.mass_a,
            Vector2(
                -self.distance / 2,
                0
            ),
            Vector2(
                0,
                velocity
            )
        )

        self.body_b = Body(
            "Body B",
            self.mass_b,
            Vector2(
                self.distance / 2,
                0
            ),
            Vector2(
                0,
                -velocity
            )
        )

        return (
            self.body_a,
            self.body_b,
        )

    def calculate_orbital_velocity(self):
        """
        Slightly adjusted orbital velocity
        for stable two-body simulation.
        """

        total_mass = self.mass_a + self.mass_b

        radius = self.distance / 2

        base_velocity = sqrt(
            self.G * total_mass / (4 * radius)
        )

        return base_velocity * 0.9