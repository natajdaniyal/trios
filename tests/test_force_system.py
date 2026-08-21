import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from vector import Vector2
from body import Body
from force import Force
from magnet import Magnet
from forces.magnetic_force import MagneticForce


print("⚡ TRIOS FORCE SYSTEM FULL TEST")
print("================================")

passed = 0
failed = 0


# Test 1: Force creation

try:
    force = Force("Base Force")

    if force.name == "Base Force":
        print("✅ Base Force Creation")
        passed += 1
    else:
        print("❌ Base Force Creation")
        failed += 1

except Exception:
    print("❌ Base Force Creation")
    failed += 1


# Test 2: MagneticForce inheritance

try:
    magnetic = MagneticForce(5)

    if isinstance(magnetic, Force):
        print("✅ Magnetic Force Inheritance")
        passed += 1
    else:
        print("❌ Magnetic Force Inheritance")
        failed += 1

except Exception:
    print("❌ Magnetic Force Inheritance")
    failed += 1


# Test 3: MagneticForce returns Vector2

try:
    magnet_a = Magnet(
        "A",
        1,
        0,
        0,
        2,
        "N"
    )

    magnet_b = Magnet(
        "B",
        1,
        10,
        0,
        2,
        "S"
    )

    result = magnetic.calculate(
        magnet_a,
        magnet_b
    )

    if isinstance(result, Vector2):
        print("✅ Force Returns Vector")
        passed += 1
    else:
        print("❌ Force Returns Vector")
        failed += 1

except Exception:
    print("❌ Force Returns Vector")
    failed += 1


# Test 4: Force applied to body

try:
    body = Body(
        "Test",
        1
    )

    body.apply_force(
        Vector2(10, 0)
    )

    if body.force.x == 10:
        print("✅ Force Applied To Body")
        passed += 1
    else:
        print("❌ Force Applied To Body")
        failed += 1

except Exception:
    print("❌ Force Applied To Body")
    failed += 1


# Test 5: Force reset

try:
    body.reset_force()

    if body.force.x == 0 and body.force.y == 0:
        print("✅ Force Reset")
        passed += 1
    else:
        print("❌ Force Reset")
        failed += 1

except Exception:
    print("❌ Force Reset")
    failed += 1


print("================================")
print(f"✅ Passed : {passed}")
print(f"❌ Failed : {failed}")

if failed == 0:
    print("🟢 FORCE SYSTEM PERFECT")
else:
    print("🔴 FORCE SYSTEM NEEDS FIX")