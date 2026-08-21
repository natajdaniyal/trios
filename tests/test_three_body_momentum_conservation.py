import sys
import os


sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)


from three_body_simulation import ThreeBodySimulation
from momentum import MomentumSystem


print()
print("🧭 TRIOS THREE-BODY MOMENTUM CONSERVATION TEST")
print("==================================================")


passed = 0
failed = 0


momentum_system = MomentumSystem()


# --------------------------------------------------
# 1. Momentum System Created
# --------------------------------------------------

if isinstance(momentum_system, MomentumSystem):

    print("✅ Momentum System Created")
    passed += 1

else:

    print("❌ Momentum System Creation Failed")
    failed += 1


# --------------------------------------------------
# 2. Initial Three-Body Momentum
# --------------------------------------------------

simulation = ThreeBodySimulation(
    mass_a=1000,
    mass_b=1000,
    mass_c=1000,
    distance=100,
    time_step=0.01,
)


initial_momentum = momentum_system.total_momentum(
    simulation.bodies
)

initial_magnitude = momentum_system.momentum_magnitude(
    initial_momentum
)


print(
    f"Initial Momentum : {initial_momentum}"
)

print(
    f"Initial Magnitude : {initial_magnitude}"
)


if initial_magnitude < 1e-9:

    print("✅ Initial Total Momentum Is Zero")
    passed += 1

else:

    print(
        "❌ Initial Total Momentum Is Not Zero "
        f"(Got: {initial_momentum})"
    )

    failed += 1


# --------------------------------------------------
# 3. Momentum Conservation Throughout Simulation
# --------------------------------------------------

max_momentum_error = 0.0

steps = 1000


for _ in range(steps):

    simulation.step()

    current_momentum = momentum_system.total_momentum(
        simulation.bodies
    )

    current_magnitude = momentum_system.momentum_magnitude(
        current_momentum
    )

    if current_magnitude > max_momentum_error:

        max_momentum_error = current_magnitude


final_momentum = momentum_system.total_momentum(
    simulation.bodies
)

final_magnitude = momentum_system.momentum_magnitude(
    final_momentum
)


print(
    f"Final Momentum   : {final_momentum}"
)

print(
    f"Final Magnitude  : {final_magnitude}"
)

print(
    f"Maximum Momentum Error : {max_momentum_error}"
)

print(
    f"Simulation Time : {simulation.time}"
)


tolerance = 1e-9


if final_magnitude < tolerance:

    print("✅ Final Momentum Conserved")
    passed += 1

else:

    print(
        "❌ Final Momentum Conservation Failed "
        f"(Magnitude: {final_magnitude})"
    )

    failed += 1


if max_momentum_error < tolerance:

    print("✅ Momentum Conserved Throughout Simulation")
    passed += 1

else:

    print(
        "❌ Momentum Drift Detected "
        f"(Maximum Error: {max_momentum_error})"
    )

    failed += 1


# --------------------------------------------------
# 4. Unequal-Mass Validation
# --------------------------------------------------

unequal_mass_simulation = ThreeBodySimulation(
    mass_a=800,
    mass_b=1200,
    mass_c=1600,
    distance=100,
    time_step=0.01,
)


unequal_initial_momentum = (
    momentum_system.total_momentum(
        unequal_mass_simulation.bodies
    )
)

unequal_initial_magnitude = (
    momentum_system.momentum_magnitude(
        unequal_initial_momentum
    )
)


for _ in range(500):

    unequal_mass_simulation.step()


unequal_final_momentum = (
    momentum_system.total_momentum(
        unequal_mass_simulation.bodies
    )
)

unequal_final_magnitude = (
    momentum_system.momentum_magnitude(
        unequal_final_momentum
    )
)


print()
print(
    f"Unequal Mass Initial Momentum : "
    f"{unequal_initial_momentum}"
)

print(
    f"Unequal Mass Final Momentum   : "
    f"{unequal_final_momentum}"
)

print(
    f"Unequal Mass Final Magnitude  : "
    f"{unequal_final_magnitude}"
)


if unequal_initial_magnitude < tolerance:

    print(
        "✅ Unequal-Mass Initial Momentum Is Zero"
    )

    passed += 1

else:

    print(
        "❌ Unequal-Mass Initial Momentum Is Not Zero "
        f"(Magnitude: {unequal_initial_magnitude})"
    )

    failed += 1


if unequal_final_magnitude < tolerance:

    print(
        "✅ Momentum Conserved With Unequal Masses"
    )

    passed += 1

else:

    print(
        "❌ Unequal-Mass Momentum Conservation Failed "
        f"(Magnitude: {unequal_final_magnitude})"
    )

    failed += 1


# --------------------------------------------------
# Final Report
# --------------------------------------------------

print("==================================================")
print(f"✅ Passed : {passed}")
print(f"❌ Failed : {failed}")


if failed == 0:

    print(
        "🟢 THREE-BODY MOMENTUM CONSERVATION HEALTHY"
    )

else:

    print(
        "🔴 THREE-BODY MOMENTUM CONSERVATION NEEDS FIX"
    )