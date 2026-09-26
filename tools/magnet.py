from body import Body
from vector import Vector2


class Magnet(Body):

    def __init__(
        self,
        name,
        mass,
        x,
        y,
        strength,
        pole,
        left_pole=None,
        right_pole=None,
    ):
        super().__init__(
            name,
            mass,
            Vector2(x, y),
            Vector2(0, 0)
        )

        self.strength = strength
        self.pole = pole
        self.collision_radius = 0.62

        # Two-pole configuration is optional for legacy callers. Experiment
        # scenarios provide both poles explicitly so the Physics Core can use
        # the same physical orientation that the UI displays.
        if (left_pole is None) != (right_pole is None):
            raise ValueError("left_pole and right_pole must be provided together.")

        if left_pole is not None:
            if left_pole not in {"N", "S"} or right_pole not in {"N", "S"}:
                raise ValueError("Magnet poles must be 'N' or 'S'.")
            if left_pole == right_pole:
                raise ValueError("A bar magnet must have opposite left and right poles.")
            self.left_pole = left_pole
            self.right_pole = right_pole
            self.pole_offset = 0.5


    def is_north(self):
        return self.pole == "N"


    def is_south(self):
        return self.pole == "S"