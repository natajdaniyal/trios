import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from two_body_model import TwoBodyModel
from energy import EnergySystem


print("🌌 TRIOS TWO-BODY ENERGY TEST")
print("================================")


passed = 0
failed = 0


# Create two-body system

model = TwoBodyModel()


if model:
    print("✅ Two Body Model Created")
    passed += 1
else:
    print("❌ Two Body Model Created")
    failed += 1



bodies = model.bodies


if len(bodies) == 2:
    print("✅ Two Bodies Loaded")
    passed += 1
else:
    print("❌ Two Bodies Loaded")
    failed += 1



# Create energy system

energy = EnergySystem()


if energy:
    print("✅ Energy System Created")
    passed += 1
else:
    print("❌ Energy System Created")
    failed += 1



# Calculate initial energy

initial_energy = energy.total_energy(bodies)


if initial_energy != 0:
    print("✅ Initial Energy Calculated")
    passed += 1
else:
    print("❌ Initial Energy Calculated")
    failed += 1



# Check kinetic energy exists

kinetic = 0

for body in bodies:
    kinetic += energy.kinetic_energy(body)


if kinetic > 0:
    print("✅ Kinetic Energy Exists")
    passed += 1
else:
    print("❌ Kinetic Energy Exists")
    failed += 1



# Check potential energy exists

potential = energy.potential_energy(
    bodies[0],
    bodies[1]
)


if potential < 0:
    print("✅ Gravitational Potential Energy Exists")
    passed += 1
else:
    print("❌ Gravitational Potential Energy Exists")
    failed += 1



print("================================")
print(f"✅ Passed : {passed}")
print(f"❌ Failed : {failed}")


if failed == 0:
    print("🟢 TWO-BODY ENERGY HEALTHY")
else:
    print("🔴 TWO-BODY ENERGY NEEDS FIX")