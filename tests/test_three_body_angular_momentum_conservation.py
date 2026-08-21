import sys
import os


sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)


from three_body_simulation import ThreeBodySimulation
from angular_momentum import AngularMomentumSystem


print()
print(
    "🧭 TRIOS THREE-BODY ANGULAR MOMENTUM "
    "CONSERVATION TEST"
)
print("==================================================")


passed = 0
failed = 0


angular_momentum_system = AngularMomentumSystem()


# --------------------------------------------------
# 1. Angular Momentum System Created
# --------------------------------------------------

if isinstance(
    angular_momentum_system,
    AngularMomentumSystem
):

    print("✅ Angular Momentum System Created")
    passed += 1

else:

    print(
        "❌ Angular Momentum System Creation Failed"
    )

    failed += 1


# --------------------------------------------------
# 2. Initial Three-Body Angular Momentum
# --------------------------------------------------

simulation = ThreeBodySimulation(
    mass_a=1000,
    mass_b=1000,
    mass_c=1000,
    distance=100,
    time_step=0.01,
)


initial_angular_momentum = (
    angular_momentum_system.total_angular_momentum(
        simulation.bodies
    )
)

initial_magnitude = (
    angular_momentum_system.angular_momentum_magnitude(
        initial_angular_momentum
    )
)


print(
    f"Initial Angular Momentum : "
    f"{initial_angular_momentum}"
)

print(
    f"Initial Magnitude : "
    f"{initial_magnitude}"
)


if abs(initial_magnitude) > 0:

    print(
        "✅ Initial Angular Momentum Exists"
    )

    passed += 1

else:

    print(
        "❌ Initial Angular Momentum Is Zero"
    )

    failed += 1


# --------------------------------------------------
# 3. Angular Momentum Conservation
# --------------------------------------------------

initial_value = initial_angular_momentum

max_error = 0.0

steps = 1000


for _ in range(steps):

    simulation.step()

    current_angular_momentum = (
        angular_momentum_system.total_angular_momentum(
            simulation.bodies
        )
    )

    error = abs(
        current_angular_momentum
        - initial_value
    )

    if error > max_error:

        max_error = error


final_angular_momentum = (
    angular_momentum_system.total_angular_momentum(
        simulation.bodies
    )
)

final_error = abs(
    final_angular_momentum
    - initial_value
)


print(
    f"Final Angular Momentum   : "
    f"{final_angular_momentum}"
)

print(
    f"Final Angular Momentum Error : "
    f"{final_error}"
)

print(
    f"Maximum Angular Momentum Error : "
    f"{max_error}"
)

print(
    f"Simulation Time : "
    f"{simulation.time}"
)


tolerance = 1e-9


if final_error < tolerance:

    print(
        "✅ Final Angular Momentum Conserved"
    )

    passed += 1

else:

    print(
        "❌ Final Angular Momentum "
        "Conservation Failed"
    )

    failed += 1


if max_error < tolerance:

    print(
        "✅ Angular Momentum Conserved "
        "Throughout Simulation"
    )

    passed += 1

else:

    print(
        "❌ Angular Momentum Drift Detected"
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


unequal_initial_angular_momentum = (
    angular_momentum_system.total_angular_momentum(
        unequal_mass_simulation.bodies
    )
)


for _ in range(500):

    unequal_mass_simulation.step()


unequal_final_angular_momentum = (
    angular_momentum_system.total_angular_momentum(
        unequal_mass_simulation.bodies
    )
)

unequal_error = abs(
    unequal_final_angular_momentum
    - unequal_initial_angular_momentum
)


print()
print(
    f"Unequal Mass Initial Angular Momentum : "
    f"{unequal_initial_angular_momentum}"
)

print(
    f"Unequal Mass Final Angular Momentum   : "
    f"{unequal_final_angular_momentum}"
)

print(
    f"Unequal Mass Angular Momentum Error   : "
    f"{unequal_error}"
)


if unequal_error < tolerance:

    print(
        "✅ Angular Momentum Conserved "
        "With Unequal Masses"
    )

    passed += 1

else:

    print(
        "❌ Unequal-Mass Angular Momentum "
        "Conservation Failed"
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
        "🟢 THREE-BODY ANGULAR MOMENTUM "
        "CONSERVATION HEALTHY"
    )

else:

    print(
        "🔴 THREE-BODY ANGULAR MOMENTUM "
        "CONSERVATION FAILED"
    )