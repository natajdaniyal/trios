import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from vector import Vector2
from body import Body


print("⚡ TRIOS MULTIPLE FORCES TEST")
print("============================")


passed = 0
failed = 0


body = Body(
    "Test Body",
    1,
    Vector2(0,0),
    Vector2(0,0)
)


force1 = Vector2(5,0)
force2 = Vector2(0,3)


body.apply_force(force1)
body.apply_force(force2)


if body.force.x == 5 and body.force.y == 3:
    print("✅ Multiple Forces Added")
    passed += 1
else:
    print("❌ Multiple Forces Added")
    failed += 1



body.reset_force()


if body.force.x == 0 and body.force.y == 0:
    print("✅ Force Reset After Multiple Forces")
    passed += 1
else:
    print("❌ Force Reset After Multiple Forces")
    failed += 1



print("============================")
print(f"✅ Passed : {passed}")
print(f"❌ Failed : {failed}")


if failed == 0:
    print("🟢 MULTIPLE FORCE SYSTEM HEALTHY")
else:
    print("🔴 SYSTEM NEEDS FIX")