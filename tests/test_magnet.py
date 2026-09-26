import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from magnet import Magnet


print("🧲 TRIOS MAGNET TEST")
print("===================")


passed = 0
failed = 0


magnet = Magnet(
    "Red Magnet",
    1,
    0,
    0,
    10,
    "N"
)


if magnet.name == "Red Magnet":
    print("✅ Name Works")
    passed += 1
else:
    print("❌ Name Failed")
    failed += 1


if magnet.strength == 10:
    print("✅ Strength Works")
    passed += 1
else:
    print("❌ Strength Failed")
    failed += 1


if magnet.is_north():
    print("✅ North Pole Works")
    passed += 1
else:
    print("❌ North Pole Failed")
    failed += 1


if magnet.position.x == 0:
    print("✅ Position Works")
    passed += 1
else:
    print("❌ Position Failed")
    failed += 1

two_pole_magnet = Magnet(
    "Two Pole Magnet",
    1,
    0,
    0,
    10,
    "N",
    left_pole="S",
    right_pole="N",
)

if (two_pole_magnet.left_pole, two_pole_magnet.right_pole) == ("S", "N"):
    print("✅ Two-Pole Configuration Works")
    passed += 1
else:
    print("❌ Two-Pole Configuration Failed")
    failed += 1



print("===================")
print(f"✅ Passed : {passed}")
print(f"❌ Failed : {failed}")


if failed == 0:
    print("🟢 MAGNET SYSTEM HEALTHY")
else:
    print("🔴 MAGNET SYSTEM NEEDS FIX")