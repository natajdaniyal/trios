import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from vector import Vector2
from body import Body
from angular_momentum import AngularMomentumSystem


print("🧭 TRIOS ANGULAR MOMENTUM SYSTEM TEST")
print("====================================")


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


system = AngularMomentumSystem()

check(
    "Angular Momentum System Created",
    system is not None
)


body_a = Body(
    name="A",
    mass=2,
    position=Vector2(3, 0),
    velocity=Vector2(0, 4)
)

l_a = system.body_angular_momentum(body_a)

check(
    "Single Body Angular Momentum Correct",
    abs(l_a - 24) < 1e-9
)


body_b = Body(
    name="B",
    mass=1,
    position=Vector2(0, 5),
    velocity=Vector2(2, 0)
)

l_b = system.body_angular_momentum(body_b)

check(
    "Angular Momentum Direction Correct",
    abs(l_b + 10) < 1e-9
)


total = system.total_angular_momentum(
    [body_a, body_b]
)

check(
    "Total Angular Momentum Correct",
    abs(total - 14) < 1e-9
)


magnitude = system.angular_momentum_magnitude(-10)

check(
    "Angular Momentum Magnitude Correct",
    magnitude == 10
)


body_zero = Body(
    name="Zero",
    mass=5,
    position=Vector2(0, 0),
    velocity=Vector2(0, 0)
)

zero_l = system.body_angular_momentum(body_zero)

check(
    "Zero Angular Momentum Safety",
    zero_l == 0
)


print("====================================")
print(f"✅ Passed : {passed}")
print(f"❌ Failed : {failed}")

if failed == 0:
    print("🟢 ANGULAR MOMENTUM SYSTEM HEALTHY")
else:
    print("🔴 ANGULAR MOMENTUM SYSTEM FAILED")