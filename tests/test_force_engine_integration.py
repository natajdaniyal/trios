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


print("⚙️ TRIOS FORCE ENGINE INTEGRATION TEST")
print("====================================")


passed = 0
failed = 0


magnet_a = Magnet(
    "Magnet A",
    10,
    0,
    0,
    5,
    "N"
)


magnet_b = Magnet(
    "Magnet B",
    10,
    10,
    0,
    5,
    "S"
)


magnetic = MagneticForce(5)


force = magnetic.calculate(
    magnet_a,
    magnet_b
)


magnet_a.apply_force(force)


if magnet_a.force.x != 0 or magnet_a.force.y != 0:
    print("✅ Force Reached Magnet")
    passed += 1
else:
    print("❌ Force Reached Magnet")
    failed += 1



engine = PhysicsEngine()


engine.update(
    magnet_a
)



if magnet_a.velocity.x != 0:
    print("✅ Velocity Updated")
    passed += 1
else:
    print("❌ Velocity Updated")
    failed += 1



if magnet_a.position.x != 0:
    print("✅ Position Updated")
    passed += 1
else:
    print("❌ Position Updated")
    failed += 1



print("====================================")
print(f"✅ Passed : {passed}")
print(f"❌ Failed : {failed}")


if failed == 0:
    print("🟢 FORCE ENGINE CONNECTION HEALTHY")
else:
    print("🔴 INTEGRATION NEEDS FIX")