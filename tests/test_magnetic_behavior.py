import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from magnet import Magnet
from forces.magnetic_force import MagneticForce


print("🧲 TRIOS MAGNETIC BEHAVIOR TEST")
print("================================")


passed = 0
failed = 0


force = MagneticForce(10)


# آهنربای شمال و جنوب (جذب)

north = Magnet(
    "North Magnet",
    1,
    0,
    0,
    5,
    "N"
)


south = Magnet(
    "South Magnet",
    1,
    10,
    0,
    5,
    "S"
)


attract_force = force.calculate(
    north,
    south
)


if attract_force.x > 0:
    print("✅ Opposite Poles Attract")
    passed += 1
else:
    print("❌ Opposite Poles Attract")
    failed += 1



# دو قطب شمال (دفع)

north2 = Magnet(
    "North Magnet 2",
    1,
    10,
    0,
    5,
    "N"
)


repel_force = force.calculate(
    north,
    north2
)


if repel_force.x < 0:
    print("✅ Same Poles Repel")
    passed += 1
else:
    print("❌ Same Poles Repel")
    failed += 1



# تست اینکه خروجی بردار است

if hasattr(attract_force, "x") and hasattr(attract_force, "y"):
    print("✅ Force Returns Vector")
    passed += 1
else:
    print("❌ Force Returns Vector")
    failed += 1



print("================================")
print(f"✅ Passed : {passed}")
print(f"❌ Failed : {failed}")


if failed == 0:
    print("🟢 MAGNETIC BEHAVIOR HEALTHY")
else:
    print("🔴 MAGNETIC BEHAVIOR NEEDS FIX")