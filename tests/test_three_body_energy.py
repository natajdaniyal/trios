import sys
import os


sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)


from three_body_simulation import ThreeBodySimulation
from energy import EnergySystem


print()
print("🔋 TRIOS THREE-BODY ENERGY VALIDATION TEST")
print("==================================================")


passed = 0
failed = 0


energy_system = EnergySystem(
    gravitational_constant=1
)


# --------------------------------------------------
# 1. Energy System Created
# --------------------------------------------------

if isinstance(
    energy_system,
    EnergySystem
):

    print("✅ Energy System Created")
    passed += 1

else:

    print("❌ Energy System Creation Failed")
    failed += 1


# --------------------------------------------------
# 2. Initial Three-Body Energy
# --------------------------------------------------

simulation = ThreeBodySimulation(
    mass_a=1000,
    mass_b=1000,
    mass_c=1000,
    distance=100,
    time_step=0.01,
    G=1,
)


initial_energy = energy_system.total_energy(
    simulation.bodies
)


print(
    f"Initial Energy : {initial_energy}"
)


if initial_energy != 0:

    print("✅ Initial Total Energy Calculated")
    passed += 1

else:

    print("❌ Initial Total Energy Is Zero")
    failed += 1


# --------------------------------------------------
# 3. Energy Components Exist
# --------------------------------------------------

kinetic_total = 0.0

for body in simulation.bodies:

    kinetic_total += (
        energy_system.kinetic_energy(body)
    )


potential_ab = (
    energy_system.potential_energy(
        simulation.body_a,
        simulation.body_b
    )
)

potential_ac = (
    energy_system.potential_energy(
        simulation.body_a,
        simulation.body_c
    )
)

potential_bc = (
    energy_system.potential_energy(
        simulation.body_b,
        simulation.body_c
    )
)


print(
    f"Initial Kinetic Energy : {kinetic_total}"
)

print(
    f"Initial Potential AB   : {potential_ab}"
)

print(
    f"Initial Potential AC   : {potential_ac}"
)

print(
    f"Initial Potential BC   : {potential_bc}"
)


if (
    kinetic_total > 0
    and
    potential_ab < 0
    and
    potential_ac < 0
    and
    potential_bc < 0
):

    print("✅ Energy Components Valid")
    passed += 1

else:

    print("❌ Energy Components Invalid")
    failed += 1


# --------------------------------------------------
# 4. Total Energy Consistency
# --------------------------------------------------

expected_total_energy = (
    kinetic_total
    + potential_ab
    + potential_ac
    + potential_bc
)


energy_difference = abs(
    initial_energy
    - expected_total_energy
)


print(
    f"Expected Total Energy : "
    f"{expected_total_energy}"
)

print(
    f"Initial Energy Error  : "
    f"{energy_difference}"
)


if energy_difference < 1e-9:

    print("✅ Total Energy Calculation Consistent")
    passed += 1

else:

    print("❌ Total Energy Calculation Inconsistent")
    failed += 1


# --------------------------------------------------
# 5. Energy Evolution
# --------------------------------------------------

initial_energy_reference = initial_energy

max_relative_drift = 0.0

steps = 1000


for _ in range(steps):

    simulation.step()

    current_energy = energy_system.total_energy(
        simulation.bodies
    )

    absolute_error = abs(
        current_energy
        - initial_energy_reference
    )

    if abs(initial_energy_reference) > 0:

        relative_drift = (
            absolute_error
            /
            abs(initial_energy_reference)
        )

    else:

        relative_drift = 0.0

    if relative_drift > max_relative_drift:

        max_relative_drift = relative_drift


final_energy = energy_system.total_energy(
    simulation.bodies
)


final_absolute_error = abs(
    final_energy
    - initial_energy_reference
)


final_relative_drift = (
    final_absolute_error
    /
    abs(initial_energy_reference)
)


print()
print(
    f"Final Energy : {final_energy}"
)

print(
    f"Final Absolute Drift : "
    f"{final_absolute_error}"
)

print(
    f"Final Relative Drift : "
    f"{final_relative_drift}"
)

print(
    f"Maximum Relative Drift : "
    f"{max_relative_drift}"
)

print(
    f"Simulation Time : "
    f"{simulation.time}"
)


# --------------------------------------------------
# 6. Numerical Energy Stability
# --------------------------------------------------

# This is a validation threshold for the current
# integrator and simulation conditions.
#
# It does NOT mean energy is mathematically exact.

drift_tolerance = 0.01


if max_relative_drift < drift_tolerance:

    print(
        "✅ Three-Body Energy Drift "
        "Within Validation Tolerance"
    )

    passed += 1

else:

    print(
        "❌ Three-Body Energy Drift "
        "Exceeded Validation Tolerance"
    )

    failed += 1


# --------------------------------------------------
# 7. Energy Remains Finite
# --------------------------------------------------

if (
    abs(initial_energy) < float("inf")
    and
    abs(final_energy) < float("inf")
):

    print("✅ Energy Remains Finite")
    passed += 1

else:

    print("❌ Invalid Energy Detected")
    failed += 1


# --------------------------------------------------
# Final Report
# --------------------------------------------------

print("==================================================")
print(f"✅ Passed : {passed}")
print(f"❌ Failed : {failed}")


if failed == 0:

    print(
        "🟢 THREE-BODY ENERGY VALIDATION HEALTHY"
    )

else:

    print(
        "🔴 THREE-BODY ENERGY VALIDATION FAILED"
    )