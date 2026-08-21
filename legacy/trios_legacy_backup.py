class Body:
    def __init__(self, name, mass, x, y, vx, vy):
        self.name = name
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def show(self):
        print("Body:", self.name)
        print("Mass:", self.mass)
        print("Position:", self.x, self.y)
        print("Velocity:", self.vx, self.vy)
        print("----------------")


body1 = Body("A", 100, 0, 0, 0, 1)
body2 = Body("B", 10, 10, 0, 0, -1)
body3 = Body("C", 1, 5, 5, -1, 0)


print("🌌 Trios Universe")
print()

body1.show()
body2.show()
body3.show()
import math


def distance(body1, body2):
    dx = body2.x - body1.x
    dy = body2.y - body1.y

    return math.sqrt(dx**2 + dy**2)


print("Distance between A and B:")
print(distance(body1, body2))

print("Distance between A and C:")
print(distance(body1, body3))
import math


def gravitational_force(body1, body2):
    r = distance(body1, body2)
    G = 1

    force = G * (body1.mass * body2.mass) / (r**2)

    return force


print("Gravity A-B:")
print(gravitational_force(body1, body2))

print("Gravity A-C:")
print(gravitational_force(body1, body3))
def force_direction(body1, body2):
    dx = body2.x - body1.x
    dy = body2.y - body1.y

    return dx, dy


print("Direction A to B:")
print(force_direction(body1, body2))

print("Direction A to C:")
print(force_direction(body1, body3))