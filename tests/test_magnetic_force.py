import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from magnet import Magnet
from forces.magnetic_force import MagneticForce


print("🧲 TRIOS MAGNETIC FORCE TEST")
print("============================")


passed = 0
failed = 0


# ساخت آهنرباها

magnet_a = Magnet(
    "North Magnet",
    10,
    0,
    0,
    5,
    "N"
)


magnet_b = Magnet(
    "South Magnet",
    10,
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


# تست وجود نیرو

if force is not None:
    print("✅ Magnetic Force Calculated")
    passed += 1
else:
    print("❌ Magnetic Force Calculated")
    failed += 1



# تست برداری بودن نیرو

if hasattr(force, "x") and hasattr(force, "y"):
    print("✅ Force Returns Vector")
    passed += 1
else:
    print("❌ Force Returns Vector")
    failed += 1



# تست جهت جذب

if force.x > 0:
    print("✅ Attraction Direction Works")
    passed += 1
else:
    print("❌ Attraction Direction Works")
    failed += 1



print("============================")
print(f"✅ Passed : {passed}")
print(f"❌ Failed : {failed}")


if failed == 0:
    print("🟢 MAGNETIC FORCE HEALTHY")
else:
    print("🔴 MAGNETIC FORCE NEEDS FIX")