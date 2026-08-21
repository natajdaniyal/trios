import sys
import os


sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)


from two_body_simulation import TwoBodySimulation


print("🌌 TRIOS TWO-BODY STABILITY TEST")
print("================================")


passed = 0
failed = 0


simulation = TwoBodySimulation(
    mass_a=1000,
    mass_b=1000,
    distance=100,
    time_step=0.01,
)


# 1. Bodies exist

if (
    simulation.body_a is not None
    and simulation.body_b is not None
):
    print("✅ Two Bodies Created")
    passed += 1
else:
    print("❌ Two Bodies Created")
    failed += 1


# 2. Initial distance

initial_distance = (
    simulation.distance_between_bodies()
)


if abs(initial_distance - 100) < 0.01:
    print("✅ Initial Distance Correct")
    passed += 1
else:
    print("❌ Initial Distance Incorrect")
    failed += 1


# 3. Run simulation

simulation.run(1000)


# 4. Time advanced

if simulation.time > 0:
    print("✅ Simulation Time Advanced")
    passed += 1
else:
    print("❌ Simulation Time Failed")
    failed += 1


# 5. Bodies moved

if (
    simulation.body_a.position.y != 0
    or simulation.body_b.position.y != 0
):
    print("✅ Orbital Motion Detected")
    passed += 1
else:
    print("❌ No Orbital Motion")
    failed += 1


# 6. Distance safety

final_distance = (
    simulation.distance_between_bodies()
)


if 20 < final_distance < 300:
    print("✅ Orbit Distance Stable")
    passed += 1
else:
    print("❌ Orbit Distance Unstable")
    failed += 1



print("================================")
print(f"✅ Passed : {passed}")
print(f"❌ Failed : {failed}")


if failed == 0:
    print("🟢 TWO-BODY STABILITY HEALTHY")
else:
    print("🔴 TWO-BODY STABILITY NEEDS FIX")