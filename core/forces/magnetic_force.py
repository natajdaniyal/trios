from force import Force
from vector import Vector2


class MagneticForce(Force):

    def __init__(self, strength):
        super().__init__("Magnetic Force")
        self.strength = strength

    @staticmethod
    def _pole_position(magnet, side):
        offset = float(getattr(magnet, "pole_offset", 0.0) or 0.0)
        x_offset = offset if side == "right" else -offset
        return Vector2(
            magnet.position.x + x_offset,
            magnet.position.y,
        )

    @staticmethod
    def _single_pole_force(
        magnet_a,
        pole_a,
        position_a,
        magnet_b,
        pole_b,
        position_b,
        base_strength,
    ):
        direction = Vector2(
            position_b.x - position_a.x,
            position_b.y - position_a.y,
        )
        distance = direction.length()

        if distance == 0:
            return Vector2(0, 0)

        direction = direction.normalize()

        collision_distance = (
            float(getattr(magnet_a, "collision_radius", 0.0) or 0.0)
            + float(getattr(magnet_b, "collision_radius", 0.0) or 0.0)
        )
        effective_distance = max(
            distance,
            collision_distance,
            0.1,
        )

        force_value = base_strength / (
            effective_distance * effective_distance
        )

        # Opposite poles attract; like poles repel.
        if pole_a == pole_b:
            direction = direction.multiply(-1)

        return direction.multiply(force_value)

    def _calculate_two_pole_force(self, magnet_a, magnet_b):
        base_strength = (
            self.strength
            * magnet_a.strength
            * magnet_b.strength
        )

        # Educational bar magnets are represented by their two poles.
        # For the translational force, use the poles that face each other
        # along the line joining the magnet centers. This keeps the physical
        # rule explicit:
        #   N-N / S-S -> repulsion
        #   N-S / S-N -> attraction
        dx = magnet_b.position.x - magnet_a.position.x
        if dx >= 0:
            side_a = "right"
            side_b = "left"
        else:
            side_a = "left"
            side_b = "right"

        pole_a = (
            magnet_a.right_pole
            if side_a == "right"
            else magnet_a.left_pole
        )
        pole_b = (
            magnet_b.right_pole
            if side_b == "right"
            else magnet_b.left_pole
        )

        return self._single_pole_force(
            magnet_a,
            pole_a,
            self._pole_position(magnet_a, side_a),
            magnet_b,
            pole_b,
            self._pole_position(magnet_b, side_b),
            base_strength,
        )

    def calculate(self, magnet_a, magnet_b):
        """
        Calculate the magnetic force between two magnets.

        Educational magnets use two finite poles when left_pole/right_pole
        are configured. This keeps the Physics Core consistent with the
        two-pole magnets displayed by the experiment UI.

        Opposite poles -> attraction
        Same poles -> repulsion
        """

        if (
            hasattr(magnet_a, "left_pole")
            and hasattr(magnet_a, "right_pole")
            and hasattr(magnet_b, "left_pole")
            and hasattr(magnet_b, "right_pole")
        ):
            return self._calculate_two_pole_force(magnet_a, magnet_b)

        # Backward-compatible single-pole model for legacy body types.
        direction = Vector2(
            magnet_b.position.x - magnet_a.position.x,
            magnet_b.position.y - magnet_a.position.y,
        )

        distance = direction.length()

        if distance == 0:
            return Vector2(0, 0)

        direction = direction.normalize()

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
