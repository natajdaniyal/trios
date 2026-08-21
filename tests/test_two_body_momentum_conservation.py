import sys
import os


sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)


from two_body_simulation import TwoBodySimulation
from momentum import MomentumSystem


print("🧭 TRIOS TWO-BODY MOMENTUM CONSERVATION TEST")
print("==============================================")


passed = 0
failed = 0


# --------------------------------------------------
# Test configuration
# --------------------------------------------------

mass_a = 1000
mass_b = 1000
distance = 100
time_step = 0.01
steps = 1000

simulation = TwoBodySimulation(
    mass_a=mass_a,
    mass_b=mass_b,
    distance=distance,
    time_step=time_step,
)

momentum_system = MomentumSystem()

bodies = [
    simulation.body_a,
    simulation.body_b,
]


# --------------------------------------------------
# Initial total momentum
# --------------------------------------------------

initial_momentum = momentum_system.total_momentum(
    bodies
)

initial_magnitude = (
    momentum_system.momentum_magnitude(
        initial_momentum
    )
)

print(
    f"Initial Momentum : "
    f"({initial_momentum[0]}, "
    f"{initial_momentum[1]})"
)

print(
    f"Initial Magnitude : {initial_magnitude}"
)


# --------------------------------------------------
# 1. Initial momentum
# --------------------------------------------------

initial_tolerance = 1e-12


if initial_magnitude < initial_tolerance:

    print("✅ Initial Total Momentum Is Zero")
    passed += 1

else:

    print(
        "❌ Initial Total Momentum Is Not Zero"
    )
    failed += 1


# --------------------------------------------------
# Track maximum momentum error
# --------------------------------------------------

maximum_error = 0.0


for _ in range(steps):

    simulation.step()

    current_momentum = momentum_system.total_momentum(
        bodies
    )

    current_difference = (
        current_momentum[0] -
        initial_momentum[0],
        current_momentum[1] -
        initial_momentum[1],
    )

    current_error = (
        momentum_system.momentum_magnitude(
            current_difference
        )
    )

    if current_error > maximum_error:
        maximum_error = current_error


# --------------------------------------------------
# Final momentum
# --------------------------------------------------

final_momentum = momentum_system.total_momentum(
    bodies
)

final_difference = (
    final_momentum[0] -
    initial_momentum[0],
    final_momentum[1] -
    initial_momentum[1],
)

final_error = momentum_system.momentum_magnitude(
    final_difference
)


print(
    f"Final Momentum : "
    f"({final_momentum[0]}, "
    f"{final_momentum[1]})"
)

print(
    f"Final Momentum Error : {final_error}"
)

print(
    f"Maximum Momentum Error : {maximum_error}"
)

print(
    f"Simulation Time : {simulation.time}"
)


# --------------------------------------------------
# 2. Final momentum conservation
# --------------------------------------------------

momentum_tolerance = 1e-10


if final_error < momentum_tolerance:

    print("✅ Final Momentum Conserved")
    passed += 1

else:

    print("❌ Final Momentum Drift Too Large")
    failed += 1


# --------------------------------------------------
# 3. Momentum conservation throughout simulation
# --------------------------------------------------

if maximum_error < momentum_tolerance:

    print(
        "✅ Momentum Conserved Throughout Simulation"
    )
    passed += 1

else:

    print(
        "❌ Momentum Drift Detected During Simulation"
    )
    failed += 1


# --------------------------------------------------
# 4. Simulation advanced
# --------------------------------------------------

if simulation.time > 0:

    print("✅ Simulation Advanced")
    passed += 1

else:

    print("❌ Simulation Did Not Advance")
    failed += 1


# --------------------------------------------------
# Final report
# --------------------------------------------------

print("==============================================")
print(f"✅ Passed : {passed}")
print(f"❌ Failed : {failed}")


if failed == 0:

    print(
        "🟢 TWO-BODY MOMENTUM CONSERVATION HEALTHY"
    )

else:

    print(
        "🔴 TWO-BODY MOMENTUM CONSERVATION NEEDS FIX"
    )