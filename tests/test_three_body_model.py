import os
import sys
from math import sqrt

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from three_body_model import ThreeBodyModel


print("🌌 TRIOS THREE-BODY MODEL TEST")
print("================================")


passed = 0
failed = 0


def check(name, condition):
    global passed, failed

    if condition:
        print(f"✅ {name}")
        passed += 1
    else:
        print(f"❌ {name}")
        failed += 1


# ---------------------------------------------------------
# Create model
# ---------------------------------------------------------

model = ThreeBodyModel()

check(
    "Three Body Model Created",
    model is not None
)


# ---------------------------------------------------------
# Check body count
# ---------------------------------------------------------

bodies = model.bodies

check(
    "Exactly Three Bodies Exist",
    len(bodies) == 3
)


# ---------------------------------------------------------
# Check names
# ---------------------------------------------------------

check(
    "Body Names Correct",
    (
        bodies[0].name == "Body A"
        and bodies[1].name == "Body B"
        and bodies[2].name == "Body C"
    )
)


# ---------------------------------------------------------
# Check masses
# ---------------------------------------------------------

check(
    "Masses Correct",
    (
        bodies[0].mass == model.mass_a
        and bodies[1].mass == model.mass_b
        and bodies[2].mass == model.mass_c
    )
)


# ---------------------------------------------------------
# Check pairwise distances
# ---------------------------------------------------------

ab = bodies[0].position.subtract(
    bodies[1].position
).length()

ac = bodies[0].position.subtract(
    bodies[2].position
).length()

bc = bodies[1].position.subtract(
    bodies[2].position
).length()

tolerance = 1e-9

check(
    "Equilateral Triangle Geometry Correct",
    (
        abs(ab - model.distance) < tolerance
        and abs(ac - model.distance) < tolerance
        and abs(bc - model.distance) < tolerance
    )
)


# ---------------------------------------------------------
# Check center of mass
# ---------------------------------------------------------

total_mass = (
    bodies[0].mass
    + bodies[1].mass
    + bodies[2].mass
)

center_x = (
    bodies[0].mass * bodies[0].position.x
    + bodies[1].mass * bodies[1].position.x
    + bodies[2].mass * bodies[2].position.x
) / total_mass

center_y = (
    bodies[0].mass * bodies[0].position.y
    + bodies[1].mass * bodies[1].position.y
    + bodies[2].mass * bodies[2].position.y
) / total_mass

check(
    "Center Of Mass At Origin",
    (
        abs(center_x) < tolerance
        and abs(center_y) < tolerance
    )
)


# ---------------------------------------------------------
# Check initial velocities
# ---------------------------------------------------------

velocity_values_valid = all(
    body.velocity.length() > 0
    for body in bodies
)

check(
    "Initial Velocities Assigned",
    velocity_values_valid
)


# ---------------------------------------------------------
# Check total linear momentum
# ---------------------------------------------------------

total_px = sum(
    body.mass * body.velocity.x
    for body in bodies
)

total_py = sum(
    body.mass * body.velocity.y
    for body in bodies
)

check(
    "Initial Total Momentum Is Zero",
    (
        abs(total_px) < tolerance
        and abs(total_py) < tolerance
    )
)


print("================================")
print(f"✅ Passed : {passed}")
print(f"❌ Failed : {failed}")

if failed == 0:
    print("🟢 THREE-BODY MODEL HEALTHY")
else:
    print("🔴 THREE-BODY MODEL FAILED")