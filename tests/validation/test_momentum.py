import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from body import Body
from vector import Vector2
from momentum import MomentumSystem


print("🧭 TRIOS MOMENTUM SYSTEM TEST")
print("================================")


passed = 0
failed = 0

body_a = Body(
    "Body A",
    2,
    Vector2(0, 0),
    Vector2(3, 4)
)

body_b = Body(
    "Body B",
    5,
    Vector2(10, 0),
    Vector2(-2, 1)
)

momentum_system = MomentumSystem()

if isinstance(momentum_system, MomentumSystem):
    print("✅ Momentum System Created")
    passed += 1
else:
    print("❌ Momentum System Creation Failed")
    failed += 1

momentum_a = momentum_system.body_momentum(body_a)
expected_a = (6, 8)

if momentum_a == expected_a:
    print("✅ Single Body Momentum Correct")
    passed += 1
else:
    print(
        f"❌ Single Body Momentum Incorrect "
        f"(Expected: {expected_a}, Got: {momentum_a})"
    )
    failed += 1

momentum_b = momentum_system.body_momentum(body_b)
expected_b = (-10, 5)

if momentum_b == expected_b:
    print("✅ Second Body Momentum Correct")
    passed += 1
else:
    print(
        f"❌ Second Body Momentum Incorrect "
        f"(Expected: {expected_b}, Got: {momentum_b})"
    )
    failed += 1

total_momentum = momentum_system.total_momentum([body_a, body_b])
expected_total = (-4, 13)

if total_momentum == expected_total:
    print("✅ Total System Momentum Correct")
    passed += 1
else:
    print(
        f"❌ Total System Momentum Incorrect "
        f"(Expected: {expected_total}, Got: {total_momentum})"
    )
    failed += 1

magnitude = momentum_system.momentum_magnitude((3, 4))

if magnitude == 5:
    print("✅ Momentum Magnitude Correct")
    passed += 1
else:
    print(
        f"❌ Momentum Magnitude Incorrect "
        f"(Expected: 5, Got: {magnitude})"
    )
    failed += 1

empty_momentum = momentum_system.total_momentum(None)
none_body_momentum = momentum_system.body_momentum(None)

if empty_momentum == (0, 0) and none_body_momentum == (0, 0):
    print("✅ Momentum Safety Behavior Correct")
    passed += 1
else:
    print("❌ Momentum Safety Behavior Incorrect")
    failed += 1

print("================================")
print(f"✅ Passed : {passed}")
print(f"❌ Failed : {failed}")

if failed == 0:
    print("🟢 MOMENTUM SYSTEM HEALTHY")
else:
    print("🔴 MOMENTUM SYSTEM NEEDS FIX")