from vector import Vector2
from force import Force


class GravitationalForce(Force):

    def __init__(self, G=1.0):
        super().__init__("Gravity")
        self.G = G

    def calculate(self, body_a, body_b=None):

        if body_b is None:
            return Vector2(0, 0)

        direction = body_b.position.subtract(body_a.position)

        distance = direction.length()

        if distance == 0:
            return Vector2(0, 0)

        unit_direction = direction.normalize()

        force_magnitude = (
            self.G
            * body_a.mass
            * body_b.mass
            / (distance ** 2)
        )

        return unit_direction.multiply(force_magnitude)