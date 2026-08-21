import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from body import Body
from vector import Vector2
from forces.gravitational_force import GravitationalForce
from force_engine import ForceEngine
from simulation_engine import SimulationEngine


print("🌌 TRIOS TWO-BODY BACKEND TEST")
print("================================")


passed = 0
failed = 0


def check(condition, message):
    global passed, failed

    if condition:
        print(f"✅ {message}")
        passed += 1
    else:
        print(f"❌ {message}")
        failed += 1


# --------------------------------------------------
# 1. Create two bodies
# --------------------------------------------------

body_a = Body(
    "Body A",
    10,
    Vector2(-5, 0),
    Vector2(0, 1)
)

body_b = Body(
    "Body B",
    10,
    Vector2(5, 0),
    Vector2(0, -1)
)

check(
    body_a.mass == 10 and body_b.mass == 10,
    "Two Bodies Created"
)

check(
    body_a.position.x == -5 and body_b.position.x == 5,
    "Initial Positions Correct"
)


# --------------------------------------------------
# 2. Create gravitational force
# --------------------------------------------------

gravity = GravitationalForce(G=1.0)

check(
    gravity.G == 1.0,
    "Gravitational Force Created"
)


# --------------------------------------------------
# 3. Create ForceEngine
# --------------------------------------------------

force_engine = ForceEngine()

force_engine.add_body(body_a)
force_engine.add_body(body_b)
force_engine.add_force(gravity)

check(
    len(force_engine.bodies) == 2,
    "ForceEngine Contains Two Bodies"
)

check(
    len(force_engine.forces) == 1,
    "ForceEngine Contains Gravity"
)


# --------------------------------------------------
# 4. Connect ForceEngine to SimulationEngine
# --------------------------------------------------

simulation = SimulationEngine(
    bodies=[body_a, body_b],
    time_step=0.01,
    force_engine=force_engine
)

check(
    simulation.force_engine is force_engine,
    "SimulationEngine Connected To ForceEngine"
)

check(
    len(simulation.bodies) == 2,
    "Simulation Contains Two Bodies"
)


# --------------------------------------------------
# 5. Store initial state
# --------------------------------------------------

initial_velocity_a_x = body_a.velocity.x
initial_velocity_a_y = body_a.velocity.y

initial_velocity_b_x = body_b.velocity.x
initial_velocity_b_y = body_b.velocity.y

initial_position_a_x = body_a.position.x
initial_position_b_x = body_b.position.x


# --------------------------------------------------
# 6. Run one simulation step
# --------------------------------------------------

simulation.step()


# --------------------------------------------------
# 7. Verify forces affected the bodies
# --------------------------------------------------

check(
    body_a.velocity.x != initial_velocity_a_x
    or body_a.velocity.y != initial_velocity_a_y,
    "Body A Velocity Updated By Gravity"
)

check(
    body_b.velocity.x != initial_velocity_b_x
    or body_b.velocity.y != initial_velocity_b_y,
    "Body B Velocity Updated By Gravity"
)


# --------------------------------------------------
# 8. Verify positions changed
# --------------------------------------------------

check(
    body_a.position.x != initial_position_a_x
    or body_a.position.y != 0,
    "Body A Position Updated"
)

check(
    body_b.position.x != initial_position_b_x
    or body_b.position.y != 0,
    "Body B Position Updated"
)


# --------------------------------------------------
# 9. Verify equal and opposite force behavior
# --------------------------------------------------

# After PhysicsEngine.update(), Body.force is reset.
# Therefore, verify the momentum-style reaction through
# the velocity changes instead.

delta_v_a_x = body_a.velocity.x - initial_velocity_a_x
delta_v_b_x = body_b.velocity.x - initial_velocity_b_x

delta_v_a_y = body_a.velocity.y - initial_velocity_a_y
delta_v_b_y = body_b.velocity.y - initial_velocity_b_y


check(
    abs(delta_v_a_x + delta_v_b_x) < 1e-10,
    "X Acceleration Reaction Is Equal And Opposite"
)

check(
    abs(delta_v_a_y + delta_v_b_y) < 1e-10,
    "Y Acceleration Reaction Is Equal And Opposite"
)


# --------------------------------------------------
# 10. Verify simulation time
# --------------------------------------------------

check(
    simulation.time == 0.01,
    "Simulation Time Advanced"
)


print("================================")
print(f"✅ Passed : {passed}")
print(f"❌ Failed : {failed}")


if failed == 0:
    print("🟢 TWO-BODY BACKEND HEALTHY")
else:
    print("🔴 TWO-BODY BACKEND NEEDS FIX")