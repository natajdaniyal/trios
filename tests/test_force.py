import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from force import Force
from body import Body
from vector import Vector2


print("⚡ TRIOS FORCE SYSTEM TEST")
print("=========================")


force = Force("Base Force")


if force.name == "Base Force":
    print("✅ Force Name Works")


body = Body(
    "Test Body",
    5
)


force.apply(
    body,
    Vector2(10,0)
)


if body.force.x == 10:
    print("✅ Force Apply Works")
else:
    print("❌ Force Apply Failed")


result = force.calculate(body)


if result.x == 0 and result.y == 0:
    print("✅ Calculate Works")
else:
    print("❌ Calculate Failed")


print("=========================")
print("🟢 Force System Healthy")