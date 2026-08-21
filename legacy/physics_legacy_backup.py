import math

def distance(body1, body2):
    dx = body2.x - body1.x
    dy = body2.y - body1.y

    return math.sqrt(dx**2 + dy**2)


def gravitational_force(body1, body2):
    r = distance(body1, body2)
    G = 1

    return G * (body1.mass * body2.mass) / (r**2)