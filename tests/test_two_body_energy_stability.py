import sys
import os


sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)


from two_body_simulation import TwoBodySimulation
from energy import EnergySystem


print("🔋 TRIOS TWO-BODY ENERGY STABILITY TEST")
print("========================================")


passed = 0
failed = 0


simulation = TwoBodySimulation(
    mass_a=1000,
    mass_b=1000,
    distance=100,
    time_step=0.01,
)


energy_system = EnergySystem(
    gravitational_constant=1
)


bodies = [
    simulation.body_a,
    simulation.body_b,
]


# --------------------------------------------------
# 1. Initial energy
# --------------------------------------------------

initial_energy = energy_system.total_energy(
    bodies
)


if initial_energy != 0:
    print("✅ Initial Energy Calculated")
    passed += 1
else:
    print("❌ Initial Energy Calculated")
    failed += 1


# --------------------------------------------------
# 2. Run simulation
# --------------------------------------------------

simulation.run(1000)


# --------------------------------------------------
# 3. Final energy
# --------------------------------------------------

final_energy = energy_system.total_energy(
    bodies
)


if final_energy != 0:
    print("✅ Final Energy Calculated")
    passed += 1
else:
    print("❌ Final Energy Calculated")
    failed += 1


# --------------------------------------------------
# 4. Energy drift
# --------------------------------------------------

energy_difference = (
    final_energy -
    initial_energy
)


relative_drift = (
    abs(energy_difference) /
    abs(initial_energy)
)


print(
    f"Initial Energy : {initial_energy}"
)

print(
    f"Final Energy   : {final_energy}"
)

print(
    f"Relative Drift : {relative_drift}"
)


# Current numerical model uses a simple integrator.
# We therefore use a conservative validation threshold.
if relative_drift < 0.001:
    print("✅ Energy Drift Within Numerical Tolerance")
    passed += 1
else:
    print("❌ Energy Drift Too Large")
    failed += 1


# --------------------------------------------------
# 5. Simulation advanced
# --------------------------------------------------

if simulation.time > 0:
    print("✅ Simulation Advanced")
    passed += 1
else:
    print("❌ Simulation Did Not Advance")
    failed += 1


print("========================================")
print(f"✅ Passed : {passed}")
print(f"❌ Failed : {failed}")


if failed == 0:
    print("🟢 TWO-BODY ENERGY STABILITY HEALTHY")
else:
    print("🔴 TWO-BODY ENERGY STABILITY NEEDS FIX")