import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from body import Body
from vector import Vector2
from simulation_engine import SimulationEngine

print("🌌 TRIOS SIMULATION ENGINE TEST")
print("================================")

passed = 0
failed = 0

body_a = Body(
    "Body A",
    10,
    Vector2(0, 0),
    Vector2(0, 0)
)

simulation = SimulationEngine([body_a])

if len(simulation.bodies) == 1:
    print("✅ Body Added")
    passed += 1
else:
    print("❌ Body Added")
    failed += 1

body_a.apply_force(Vector2(10, 0))

simulation.step()

if body_a.velocity.x == 1:
    print("✅ Simulation Step Updated Velocity")
    passed += 1
else:
    print("❌ Simulation Step Updated Velocity")
    failed += 1

if body_a.position.x == 1:
    print("✅ Simulation Step Updated Position")
    passed += 1
else:
    print("❌ Simulation Step Updated Position")
    failed += 1

if simulation.time == 1:
    print("✅ Simulation Time Updated")
    passed += 1
else:
    print("❌ Simulation Time Updated")
    failed += 1

simulation.add_body(
    Body(
        "Body B",
        5,
        Vector2(10, 0),
        Vector2(0, 0)
    )
)

if len(simulation.bodies) == 2:
    print("✅ Second Body Added")
    passed += 1
else:
    print("❌ Second Body Added")
    failed += 1

print("================================")
print(f"✅ Passed : {passed}")
print(f"❌ Failed : {failed}")

if failed == 0:
    print("🟢 SIMULATION ENGINE HEALTHY")
else:
    print("🔴 SIMULATION ENGINE NEEDS FIX")