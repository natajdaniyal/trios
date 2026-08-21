import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from magnet import Magnet
from forces.magnetic_force import MagneticForce
from physics_engine import PhysicsEngine


print("🧲 TRIOS MAGNET PHYSICS INTEGRATION TEST")
print("========================================")


passed = 0
failed = 0


# ساخت دو آهنربا

magnet_a = Magnet(
    "North Magnet",
    1,
    0,
    0,
    5,
    "N"
)


magnet_b = Magnet(
    "South Magnet",
    1,
    10,
    0,
    5,
    "S"
)


# ساخت نیروی مغناطیسی

magnetic_force = MagneticForce(10)


force = magnetic_force.calculate(
    magnet_a,
    magnet_b
)


# اعمال نیرو

magnet_a.apply_force(force)


if magnet_a.force.x != 0:
    print("✅ Magnetic Force Applied")
    passed += 1
else:
    print("❌ Magnetic Force Applied")
    failed += 1



# موتور فیزیک

engine = PhysicsEngine()


old_position = magnet_a.position.x


engine.update(
    magnet_a
)



if magnet_a.velocity.x != 0:
    print("✅ Magnet Velocity Changed")
    passed += 1
else:
    print("❌ Magnet Velocity Changed")
    failed += 1



if magnet_a.position.x != old_position:
    print("✅ Magnet Moved")
    passed += 1
else:
    print("❌ Magnet Moved")
    failed += 1



print("========================================")
print(f"✅ Passed : {passed}")
print(f"❌ Failed : {failed}")


if failed == 0:
    print("🟢 MAGNET PHYSICS INTEGRATION HEALTHY")
else:
    print("🔴 INTEGRATION NEEDS FIX")