import math


class Vector2:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


    def add(self, other):
        return Vector2(
            self.x + other.x,
            self.y + other.y
        )


    def subtract(self, other):
        return Vector2(
            self.x - other.x,
            self.y - other.y
        )


    def multiply(self, value):
        return Vector2(
            self.x * value,
            self.y * value
        )


    def length(self):
        return math.sqrt(
            self.x ** 2 + self.y ** 2
        )


    def normalize(self):

        length = self.length()

        if length == 0:
            return Vector2(0, 0)

        return Vector2(
            self.x / length,
            self.y / length
        )


    def __str__(self):
        return f"({self.x}, {self.y})"