import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from vector import Vector2
from magnet import Magnet
from physics_engine import PhysicsEngine
from forces.magnetic_force import MagneticForce

print("🌌 TRIOS FULL PHYSICS CHAIN TEST")
print("================================")

passed = 0
failed = 0


# 1) Create magnets

magnet_a = Magnet(
    "Magnet A",
    1,
    0,
    0,
    5,
    "N"
)

magnet_b = Magnet(
    "Magnet B",
    1,
    10,
    0,
    5,
    "S"
)

if magnet_a.position.x == 0 and magnet_b.position.x == 10:
    print("✅ Magnets Created")
    passed += 1
else:
    print("❌ Magnets Created")
    failed += 1


# 2) Calculate magnetic force

magnetic = MagneticForce(5)

force = magnetic.calculate(
    magnet_a,
    magnet_b
)

if isinstance(force, Vector2):
    print("✅ Magnetic Force Generated")
    passed += 1
else:
    print("❌ Magnetic Force Generated")
    failed += 1


# 3) Apply force

magnet_a.apply_force(force)

if magnet_a.force.x != 0:
    print("✅ Force Applied")
    passed += 1
else:
    print("❌ Force Applied")
    failed += 1


# 4) Physics update

engine = PhysicsEngine()

old_position = magnet_a.position.x

engine.update(
    magnet_a
)


# 5) Check movement

if magnet_a.velocity.x != 0:
    print("✅ Velocity Changed")
    passed += 1
else:
    print("❌ Velocity Changed")
    failed += 1

if magnet_a.position.x != old_position:
    print("✅ Position Changed")
    passed += 1
else:
    print("❌ Position Changed")
    failed += 1


print("================================")
print(f"✅ Passed : {passed}")
print(f"❌ Failed : {failed}")

if failed == 0:
    print("🟢 TRIOS PHYSICS CORE FULLY HEALTHY")
else:
    print("🔴 CORE NEEDS FIX")
