import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from body import Body
from vector import Vector2
from energy import EnergySystem


print("🔋 TRIOS ENERGY SYSTEM TEST")
print("================================")


passed = 0
failed = 0


# Test 1: Create bodies

body_a = Body(
    "Body A",
    10,
    Vector2(0, 0),
    Vector2(2, 0)
)


body_b = Body(
    "Body B",
    20,
    Vector2(10, 0),
    Vector2(-1, 0)
)


if body_a and body_b:
    print("✅ Bodies Created")
    passed += 1
else:
    print("❌ Bodies Created")
    failed += 1



# Test 2: Create energy system

energy = EnergySystem(
    gravitational_constant=1
)


if energy:
    print("✅ Energy System Created")
    passed += 1
else:
    print("❌ Energy System Created")
    failed += 1



# Test 3: Kinetic energy

ke = energy.kinetic_energy(body_a)


expected_ke = 0.5 * 10 * (2 ** 2)


if ke == expected_ke:
    print("✅ Kinetic Energy Correct")
    passed += 1
else:
    print("❌ Kinetic Energy Incorrect")
    failed += 1



# Test 4: Potential energy

pe = energy.potential_energy(
    body_a,
    body_b
)


expected_pe = -1 * 10 * 20 / 10


if pe == expected_pe:
    print("✅ Potential Energy Correct")
    passed += 1
else:
    print("❌ Potential Energy Incorrect")
    failed += 1



# Test 5: Total energy

total = energy.total_energy(
    [
        body_a,
        body_b
    ]
)


expected_total = (
    energy.kinetic_energy(body_a)
    +
    energy.kinetic_energy(body_b)
    +
    energy.potential_energy(body_a, body_b)
)


if total == expected_total:
    print("✅ Total Energy Correct")
    passed += 1
else:
    print("❌ Total Energy Incorrect")
    failed += 1



# Test 6: Zero distance safety

body_c = Body(
    "Body C",
    5,
    Vector2(0, 0),
    Vector2(0, 0)
)


zero_test = energy.potential_energy(
    body_a,
    body_c
)


if zero_test == 0:
    print("✅ Zero Distance Safety")
    passed += 1
else:
    print("❌ Zero Distance Safety")
    failed += 1



print("================================")
print(f"✅ Passed : {passed}")
print(f"❌ Failed : {failed}")


if failed == 0:
    print("🟢 ENERGY SYSTEM HEALTHY")
else:
    print("🔴 ENERGY SYSTEM NEEDS FIX")