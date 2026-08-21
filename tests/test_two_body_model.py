import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from two_body_model import TwoBodyModel


print("🌌 TRIOS TWO-BODY MODEL TEST")
print("================================")


passed = 0
failed = 0


model = TwoBodyModel()

body_a, body_b = model.create()


# Test 1: Bodies created
if body_a is not None and body_b is not None:
    print("✅ Two Bodies Created")
    passed += 1
else:
    print("❌ Two Bodies Created")
    failed += 1


# Test 2: Names
if body_a.name == "Body A" and body_b.name == "Body B":
    print("✅ Body Names Correct")
    passed += 1
else:
    print("❌ Body Names Correct")
    failed += 1


# Test 3: Masses
if body_a.mass == 10 and body_b.mass == 10:
    print("✅ Masses Correct")
    passed += 1
else:
    print("❌ Masses Correct")
    failed += 1


# Test 4: Initial positions
if (
    body_a.position.x == -5
    and body_a.position.y == 0
    and body_b.position.x == 5
    and body_b.position.y == 0
):
    print("✅ Initial Positions Correct")
    passed += 1
else:
    print("❌ Initial Positions Correct")
    failed += 1


# Test 5: Initial velocities exist
if (
    body_a.velocity.y > 0
    and body_b.velocity.y < 0
):
    print("✅ Orbital Velocities Assigned")
    passed += 1
else:
    print("❌ Orbital Velocities Assigned")
    failed += 1


# Test 6: Opposite velocities
if (
    body_a.velocity.y == -body_b.velocity.y
):
    print("✅ Equal And Opposite Velocities")
    passed += 1
else:
    print("❌ Equal And Opposite Velocities")
    failed += 1


print("================================")
print(f"✅ Passed : {passed}")
print(f"❌ Failed : {failed}")


if failed == 0:
    print("🟢 TWO-BODY MODEL HEALTHY")
else:
    print("🔴 TWO-BODY MODEL NEEDS FIX")