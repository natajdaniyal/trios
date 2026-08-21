import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from body import Body
from vector import Vector2
from physics_engine import PhysicsEngine


print("⚙️ TRIOS PHYSICS ENGINE TEST")
print("============================")


body = Body(
    "Test Body",
    10,
    Vector2(0,0),
    Vector2(0,0)
)


engine = PhysicsEngine()


body.apply_force(
    Vector2(10,0)
)


engine.update(body)


if body.velocity.x == 1:
    print("✅ Acceleration Works")
else:
    print("❌ Acceleration Failed")


if body.position.x == 1:
    print("✅ Movement Works")
else:
    print("❌ Movement Failed")


if body.force.x == 0:
    print("✅ Force Reset Works")
else:
    print("❌ Force Reset Failed")


print("============================")
print("🟢 Physics Engine Healthy")