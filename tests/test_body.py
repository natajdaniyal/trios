import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from body import Body
from vector import Vector2


print("🪐 TRIOS BODY TEST")
print("====================")


body = Body(
    "Test Object",
    10,
    Vector2(5, 5),
    Vector2(1, 0)
)


if body.name == "Test Object":
    print("✅ Name Works")
else:
    print("❌ Name Failed")


if body.mass == 10:
    print("✅ Mass Works")
else:
    print("❌ Mass Failed")


if body.position.x == 5 and body.position.y == 5:
    print("✅ Position Works")
else:
    print("❌ Position Failed")


if body.velocity.x == 1 and body.velocity.y == 0:
    print("✅ Velocity Works")
else:
    print("❌ Velocity Failed")


body.apply_force(Vector2(3, 0))


if body.force.x == 3:
    print("✅ Force Works")
else:
    print("❌ Force Failed")


print("====================")
print("🟢 Body System Healthy")