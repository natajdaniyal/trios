import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from body import Body
from force import Force
from vector import Vector2
from forces.gravitational_force import GravitationalForce


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


print("🌌 TRIOS GRAVITATIONAL FORCE TEST")
print("================================")


# 1. Creation and inheritance
gravity = GravitationalForce(G=1.0)

check(
    "Gravitational Force Creation",
    isinstance(gravity, GravitationalForce)
)

check(
    "Force Inheritance",
    isinstance(gravity, Force)
)


# 2. Basic gravitational calculation
body_a = Body(
    "A",
    2,
    position=Vector2(0, 0)
)

body_b = Body(
    "B",
    3,
    position=Vector2(2, 0)
)

force_ab = gravity.calculate(body_a, body_b)

expected_magnitude = (1.0 * 2 * 3) / (2 ** 2)

check(
    "Force Returns Vector2",
    isinstance(force_ab, Vector2)
)

check(
    "Correct Force Magnitude",
    abs(force_ab.length() - expected_magnitude) < 1e-9
)


# 3. Correct direction
check(
    "Correct Force Direction",
    abs(force_ab.x - expected_magnitude) < 1e-9
    and abs(force_ab.y) < 1e-9
)


# 4. Newton's Third Law
force_ba = gravity.calculate(body_b, body_a)

check(
    "Equal And Opposite Forces",
    abs(force_ab.x + force_ba.x) < 1e-9
    and abs(force_ab.y + force_ba.y) < 1e-9
)


# 5. Configurable G
gravity_custom = GravitationalForce(G=2.0)

custom_force = gravity_custom.calculate(body_a, body_b)

expected_custom_magnitude = (2.0 * 2 * 3) / (2 ** 2)

check(
    "Configurable Gravitational Constant",
    abs(custom_force.length() - expected_custom_magnitude) < 1e-9
)


# 6. Zero distance safety
body_c = Body(
    "C",
    5,
    position=Vector2(0, 0)
)

zero_distance_force = gravity.calculate(body_a, body_c)

check(
    "Zero Distance Safety",
    zero_distance_force.x == 0
    and zero_distance_force.y == 0
)


# 7. None body safety
none_force = gravity.calculate(body_a)

check(
    "Missing Second Body Safety",
    none_force.x == 0
    and none_force.y == 0
)


print("================================")
print(f"✅ Passed : {passed}")
print(f"❌ Failed : {failed}")

if failed == 0:
    print("🟢 GRAVITATIONAL FORCE HEALTHY")
else:
    print("🔴 GRAVITATIONAL FORCE NEEDS FIX")