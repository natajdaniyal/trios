import sys
import os


sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)


from two_body_simulation import TwoBodySimulation
from energy import EnergySystem


print("🕐 TRIOS TWO-BODY TIME-STEP SENSITIVITY TEST")
print("============================================")


passed = 0
failed = 0


energy_system = EnergySystem(
    gravitational_constant=1
)


# --------------------------------------------------
# Test configuration
# --------------------------------------------------

mass_a = 1000
mass_b = 1000
distance = 100

total_time = 10.0

time_steps = [
    0.02,
    0.01,
    0.005,
]


results = []


# --------------------------------------------------
# Run simulations
# --------------------------------------------------

for time_step in time_steps:

    simulation = TwoBodySimulation(
        mass_a=mass_a,
        mass_b=mass_b,
        distance=distance,
        time_step=time_step,
    )

    bodies = [
        simulation.body_a,
        simulation.body_b,
    ]

    initial_energy = energy_system.total_energy(
        bodies
    )

    steps = int(
        round(
            total_time /
            time_step
        )
    )

    simulation.run(steps)

    final_energy = energy_system.total_energy(
        bodies
    )

    energy_difference = (
        final_energy -
        initial_energy
    )

    relative_drift = (
        abs(energy_difference) /
        abs(initial_energy)
    )

    results.append(
        {
            "time_step": time_step,
            "steps": steps,
            "initial_energy": initial_energy,
            "final_energy": final_energy,
            "relative_drift": relative_drift,
            "simulation_time": simulation.time,
        }
    )


# --------------------------------------------------
# Print results
# --------------------------------------------------

for result in results:

    print()
    print(
        f"dt = {result['time_step']}"
    )

    print(
        f"Steps           : {result['steps']}"
    )

    print(
        f"Initial Energy  : {result['initial_energy']}"
    )

    print(
        f"Final Energy    : {result['final_energy']}"
    )

    print(
        f"Relative Drift  : {result['relative_drift']}"
    )

    print(
        f"Simulation Time : {result['simulation_time']}"
    )


# --------------------------------------------------
# 1. Initial energy validity
# --------------------------------------------------

all_initial_energy_valid = all(
    result["initial_energy"] != 0
    for result in results
)


if all_initial_energy_valid:

    print()
    print("✅ Initial Energy Valid For All Time Steps")
    passed += 1

else:

    print()
    print("❌ Initial Energy Invalid")
    failed += 1


# --------------------------------------------------
# 2. Equal physical simulation duration
# --------------------------------------------------

all_times_correct = all(
    abs(
        result["simulation_time"] -
        total_time
    ) < 1e-12
    for result in results
)


if all_times_correct:

    print("✅ Equal Physical Duration Maintained")
    passed += 1

else:

    print("❌ Physical Durations Are Not Equal")
    failed += 1


# --------------------------------------------------
# 3. All simulations advanced
# --------------------------------------------------

all_simulations_advanced = all(
    result["simulation_time"] > 0
    for result in results
)


if all_simulations_advanced:

    print("✅ All Simulations Advanced")
    passed += 1

else:

    print("❌ One Or More Simulations Did Not Advance")
    failed += 1


# --------------------------------------------------
# 4. Energy drift decreases with smaller dt
# --------------------------------------------------

drifts = [
    result["relative_drift"]
    for result in results
]


drift_decreases = (
    drifts[1] < drifts[0]
    and
    drifts[2] < drifts[1]
)


if drift_decreases:

    print("✅ Energy Drift Decreases As Time Step Decreases")
    passed += 1

else:

    print("❌ Energy Drift Does Not Decrease Consistently")
    failed += 1


# --------------------------------------------------
# 5. Finest time step is within validation threshold
# --------------------------------------------------

finest_drift = drifts[-1]


if finest_drift < 0.0001:

    print("✅ Finest Time Step Has Low Energy Drift")
    passed += 1

else:

    print("❌ Finest Time Step Energy Drift Too Large")
    failed += 1


# --------------------------------------------------
# Final report
# --------------------------------------------------

print()
print("============================================")
print(f"✅ Passed : {passed}")
print(f"❌ Failed : {failed}")


if failed == 0:

    print(
        "🟢 TWO-BODY TIME-STEP SENSITIVITY HEALTHY"
    )

else:

    print(
        "🔴 TWO-BODY TIME-STEP SENSITIVITY NEEDS FIX"
    )