import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from vector import Vector2
from body import Body
from physics_engine import PhysicsEngine


print("⚙️ TRIOS ENGINE STABILITY TEST")
print("==============================")


passed = 0
failed = 0


body = Body(
    "Stable Body",
    1,
    Vector2(0,0),
    Vector2(1,0)
)


engine = PhysicsEngine()


start_position = body.position.x


# چند مرحله آپدیت

for i in range(5):
    engine.update(body)


# بررسی حرکت

if body.position.x != start_position:
    print("✅ Multiple Updates Work")
    passed += 1
else:
    print("❌ Multiple Updates Work")
    failed += 1


# بررسی اینکه موتور کرش نکرده

if body.velocity.x != 0:
    print("✅ Engine Remains Active")
    passed += 1
else:
    print("❌ Engine Remains Active")
    failed += 1



print("==============================")
print(f"✅ Passed : {passed}")
print(f"❌ Failed : {failed}")


if failed == 0:
    print("🟢 ENGINE STABILITY HEALTHY")
else:
    print("🔴 ENGINE NEEDS FIX")