from force import Force
from vector import Vector2


class MagneticForce(Force):

    def __init__(self, strength):
        super().__init__("Magnetic Force")
        self.strength = strength

    def calculate(self, magnet_a, magnet_b):
        """
        Calculate the magnetic force between two magnets.

        Opposite poles -> attraction
        Same poles -> repulsion
        """

        direction = Vector2(
            magnet_b.position.x - magnet_a.position.x,
            magnet_b.position.y - magnet_a.position.y
        )

        distance = direction.length()

        if distance == 0:
            return Vector2(0, 0)

        direction = direction.normalize()

        # Magnets have finite size.  Do not let the point-like 1/r^2
        # model produce an effectively infinite impulse when bodies get
        # very close; the collision model already treats this distance
        # as the physical contact scale.
        collision_distance = (
            float(getattr(magnet_a, "collision_radius", 0.0) or 0.0)
            + float(getattr(magnet_b, "collision_radius", 0.0) or 0.0)
        )
        effective_distance = max(distance, collision_distance)

        force_value = (
            self.strength
            * magnet_a.strength
            * magnet_b.strength
        ) / (effective_distance * effective_distance)

        if magnet_a.pole == magnet_b.pole:
            direction = direction.multiply(-1)

        return direction.multiply(force_value)