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
print("🕐 TRIOS THREE-BODY TIME-STEP SENSITIVITY TEST")
print("==================================================")


passed = 0
failed = 0


energy_system = EnergySystem(
    gravitational_constant=1
)


# --------------------------------------------------
# Configuration
# --------------------------------------------------

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

    steps = int(
        total_time / time_step
    )

    simulation = ThreeBodySimulation(
        mass_a=1000,
        mass_b=1000,
        mass_c=1000,
        distance=100,
        time_step=time_step,
        G=1,
    )

    initial_energy = (
        energy_system.total_energy(
            simulation.bodies
        )
    )

    for _ in range(steps):
        simulation.step()

    final_energy = (
        energy_system.total_energy(
            simulation.bodies
        )
    )

    absolute_drift = abs(
        final_energy
        - initial_energy
    )

    relative_drift = (
        absolute_drift
        /
        abs(initial_energy)
    )

    results.append(
        {
            "dt": time_step,
            "steps": steps,
            "initial_energy": initial_energy,
            "final_energy": final_energy,
            "absolute_drift": absolute_drift,
            "relative_drift": relative_drift,
            "simulation_time": simulation.time,
        }
    )


# --------------------------------------------------
# Print Results
# --------------------------------------------------

for result in results:

    print()
    print(
        f"dt = {result['dt']}"
    )

    print(
        f"Steps           : "
        f"{result['steps']}"
    )

    print(
        f"Initial Energy  : "
        f"{result['initial_energy']}"
    )

    print(
        f"Final Energy    : "
        f"{result['final_energy']}"
    )

    print(
        f"Absolute Drift  : "
        f"{result['absolute_drift']}"
    )

    print(
        f"Relative Drift  : "
        f"{result['relative_drift']}"
    )

    print(
        f"Simulation Time : "
        f"{result['simulation_time']}"
    )


# --------------------------------------------------
# 1. Initial Energy Consistency
# --------------------------------------------------

initial_energies = [
    result["initial_energy"]
    for result in results
]


initial_energy_tolerance = 1e-9


if all(
    abs(
        energy
        - initial_energies[0]
    )
    < initial_energy_tolerance
    for energy in initial_energies
):

    print()
    print(
        "✅ Initial Energy Valid For "
        "All Time Steps"
    )

    passed += 1

else:

    print()
    print(
        "❌ Initial Energy Inconsistent"
    )

    failed += 1


# --------------------------------------------------
# 2. Equal Physical Duration
# --------------------------------------------------

simulation_times = [
    result["simulation_time"]
    for result in results
]


duration_tolerance = 1e-9


if all(
    abs(
        simulation_time
        - total_time
    )
    < duration_tolerance
    for simulation_time in simulation_times
):

    print(
        "✅ Equal Physical Duration Maintained"
    )

    passed += 1

else:

    print(
        "❌ Physical Duration Mismatch"
    )

    failed += 1


# --------------------------------------------------
# 3. All Simulations Advanced
# --------------------------------------------------

if all(
    result["steps"] > 0
    and result["simulation_time"] > 0
    for result in results
):

    print(
        "✅ All Simulations Advanced"
    )

    passed += 1

else:

    print(
        "❌ Simulation Advancement Failed"
    )

    failed += 1


# --------------------------------------------------
# 4. Energy Drift Improves With Smaller dt
# --------------------------------------------------

drift_large = results[0]["relative_drift"]
drift_medium = results[1]["relative_drift"]
drift_small = results[2]["relative_drift"]


print()
print(
    f"Drift dt=0.02  : {drift_large}"
)

print(
    f"Drift dt=0.01  : {drift_medium}"
)

print(
    f"Drift dt=0.005 : {drift_small}"
)


if (
    drift_medium < drift_large
    and
    drift_small < drift_medium
):

    print(
        "✅ Energy Drift Decreases As "
        "Time Step Decreases"
    )

    passed += 1

else:

    print(
        "❌ Energy Drift Does Not "
        "Decrease Consistently"
    )

    failed += 1


# --------------------------------------------------
# 5. Finest Time Step Validation
# --------------------------------------------------

if drift_small < 1e-4:

    print(
        "✅ Finest Time Step Has "
        "Low Energy Drift"
    )

    passed += 1

else:

    print(
        "❌ Finest Time Step Drift "
        "Exceeds Validation Threshold"
    )

    failed += 1


# --------------------------------------------------
# Final Report
# --------------------------------------------------

print("==================================================")
print(
    f"✅ Passed : {passed}"
)

print(
    f"❌ Failed : {failed}"
)


if failed == 0:

    print(
        "🟢 THREE-BODY TIME-STEP "
        "SENSITIVITY HEALTHY"
    )

else:

    print(
        "🔴 THREE-BODY TIME-STEP "
        "SENSITIVITY FAILED"
    )