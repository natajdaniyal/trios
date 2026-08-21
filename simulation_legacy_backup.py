def update_position(body, dt):
    body.x += body.vx * dt
    body.y += body.vy * dt


def simulate(bodies, steps):
    for step in range(steps):
        print("🌌 Step", step)

        for body in bodies:
            update_position(body, 1)

            print(
                body.name,
                "Position:",
                round(body.x, 2),
                round(body.y, 2)
            )

        print("----------------")