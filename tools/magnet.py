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
        pole
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


    def is_north(self):
        return self.pole == "N"


    def is_south(self):
        return self.pole == "S"