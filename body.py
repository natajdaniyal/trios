from vector import Vector2


class Body:

    def __init__(
        self,
        name,
        mass,
        position=None,
        velocity=None
    ):

        self.name = name
        self.mass = mass

        self.position = position or Vector2(0, 0)

        self.velocity = velocity or Vector2(0, 0)

        self.force = Vector2(0, 0)


    def apply_force(self, force):

        self.force = self.force.add(force)


    def reset_force(self):

        self.force = Vector2(0, 0)


    def __str__(self):

        return (
            f"{self.name} | "
            f"Mass: {self.mass} | "
            f"Position: {self.position}"
        )