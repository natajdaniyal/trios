from vector import Vector2


class PhysicsEngine:

    def __init__(self, time_step=1):
        self.time_step = time_step


    def update(self, body):

        # a = F / m
        acceleration = body.force.multiply(
            1 / body.mass
        )


        # v = v + a*t
        body.velocity = body.velocity.add(
            acceleration.multiply(self.time_step)
        )


        # x = x + v*t
        body.position = body.position.add(
            body.velocity.multiply(self.time_step)
        )


        # آماده برای نیروهای مرحله بعد
        body.reset_force()