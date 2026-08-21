import sys
import os
import math


sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)


from three_body_simulation import ThreeBodySimulation
from energy import EnergySystem
from momentum import MomentumSystem
from angular_momentum import AngularMomentumSystem


print()
print("🌌 TRIOS THREE-BODY LONG-DURATION STABILITY TEST")
print("==================================================")


passed = 0
failed = 0


# --------------------------------------------------
# Configuration
# --------------------------------------------------

time_step = 0.01
steps = 10000
expected_time = time_step * steps

energy_tolerance = 0.01
momentum_tolerance = 1e-7
angular_momentum_tolerance = 1e-7
center_of_mass_tolerance = 1e-7


# --------------------------------------------------
# Systems
# --------------------------------------------------

simulation = ThreeBodySimulation(
    mass_a=1000,
    mass_b=1000,
    mass_c=1000,
    distance=100,
    time_step=time_step,
    G=1,
)


energy_system = EnergySystem(
    gravitational_constant=1
)

momentum_system = MomentumSystem()

angular_momentum_system = AngularMomentumSystem()


# --------------------------------------------------
# Initial State
# --------------------------------------------------

initial_energy = (
    energy_system.total_energy(
        simulation.bodies
    )
)

initial_momentum = (
    momentum_system.total_momentum(
        simulation.bodies
    )
)

initial_momentum_magnitude = (
    momentum_system.momentum_magnitude(
        initial_momentum
    )
)

initial_angular_momentum = (
    angular_momentum_system.total_angular_momentum(
        simulation.bodies
    )
)


def calculate_center_of_mass():

    total_mass = (
        simulation.body_a.mass
        + simulation.body_b.mass
        + simulation.body_c.mass
    )

    center_x = (
        simulation.body_a.mass
        * simulation.body_a.position.x
        + simulation.body_b.mass
        * simulation.body_b.position.x
        + simulation.body_c.mass
        * simulation.body_c.position.x
    ) / total_mass

    center_y = (
        simulation.body_a.mass
        * simulation.body_a.position.y
        + simulation.body_b.mass
        * simulation.body_b.position.y
        + simulation.body_c.mass
        * simulation.body_c.position.y
    ) / total_mass

    return center_x, center_y


def center_of_mass_magnitude():

    center_x, center_y = calculate_center_of_mass()

    return (
        center_x ** 2
        + center_y ** 2
    ) ** 0.5


initial_center_of_mass = calculate_center_of_mass()


print(
    f"Initial Energy : {initial_energy}"
)

print(
    f"Initial Momentum : {initial_momentum}"
)

print(
    f"Initial Angular Momentum : "
    f"{initial_angular_momentum}"
)

print(
    f"Initial Center Of Mass : "
    f"{initial_center_of_mass}"
)

print(
    f"Target Simulation Time : "
    f"{expected_time}"
)


# --------------------------------------------------
# Long-Duration Simulation
# --------------------------------------------------

max_energy_relative_drift = 0.0
max_momentum_error = 0.0
max_angular_momentum_error = 0.0
max_center_of_mass_magnitude = 0.0

finite_state = True

sample_interval = 1000


for step in range(steps):

    simulation.step()

    # ----------------------------------------------
    # Energy
    # ----------------------------------------------

    current_energy = (
        energy_system.total_energy(
            simulation.bodies
        )
    )

    energy_error = abs(
        current_energy
        - initial_energy
    )

    if abs(initial_energy) > 0:

        energy_relative_drift = (
            energy_error
            /
            abs(initial_energy)
        )

    else:

        energy_relative_drift = 0.0

    if (
        energy_relative_drift
        >
        max_energy_relative_drift
    ):

        max_energy_relative_drift = (
            energy_relative_drift
        )

    # ----------------------------------------------
    # Momentum
    # ----------------------------------------------

    current_momentum = (
        momentum_system.total_momentum(
            simulation.bodies
        )
    )

    current_momentum_magnitude = (
        momentum_system.momentum_magnitude(
            current_momentum
        )
    )

    momentum_error = (
        current_momentum_magnitude
        -
        initial_momentum_magnitude
    )

    momentum_error = abs(
        momentum_error
    )

    if momentum_error > max_momentum_error:

        max_momentum_error = momentum_error

    # ----------------------------------------------
    # Angular Momentum
    # ----------------------------------------------

    current_angular_momentum = (
        angular_momentum_system.total_angular_momentum(
            simulation.bodies
        )
    )

    angular_momentum_error = abs(
        current_angular_momentum
        - initial_angular_momentum
    )

    if (
        angular_momentum_error
        >
        max_angular_momentum_error
    ):

        max_angular_momentum_error = (
            angular_momentum_error
        )

    # ----------------------------------------------
    # Center Of Mass
    # ----------------------------------------------

    current_center_of_mass_magnitude = (
        center_of_mass_magnitude()
    )

    if (
        current_center_of_mass_magnitude
        >
        max_center_of_mass_magnitude
    ):

        max_center_of_mass_magnitude = (
            current_center_of_mass_magnitude
        )

    # ----------------------------------------------
    # Finite-State Check
    # ----------------------------------------------

    for body in simulation.bodies:

        values = [
            body.position.x,
            body.position.y,
            body.velocity.x,
            body.velocity.y,
            body.force.x,
            body.force.y,
        ]

        if not all(
            math.isfinite(value)
            for value in values
        ):

            finite_state = False

    # ----------------------------------------------
    # Progress Samples
    # ----------------------------------------------

    if (
        (step + 1) % sample_interval == 0
    ):

        print(
            f"Step {step + 1:5d} | "
            f"Time {simulation.time:.2f} | "
            f"Energy Drift "
            f"{energy_relative_drift:.3e} | "
            f"COM "
            f"{current_center_of_mass_magnitude:.3e}"
        )


# --------------------------------------------------
# Final State
# --------------------------------------------------

final_energy = (
    energy_system.total_energy(
        simulation.bodies
    )
)

final_momentum = (
    momentum_system.total_momentum(
        simulation.bodies
    )
)

final_angular_momentum = (
    angular_momentum_system.total_angular_momentum(
        simulation.bodies
    )
)

final_center_of_mass = calculate_center_of_mass()


final_energy_relative_drift = (
    abs(
        final_energy
        - initial_energy
    )
    /
    abs(initial_energy)
)

final_momentum_magnitude = (
    momentum_system.momentum_magnitude(
        final_momentum
    )
)

final_angular_momentum_error = abs(
    final_angular_momentum
    - initial_angular_momentum
)

final_center_of_mass_magnitude = (
    center_of_mass_magnitude()
)


print()
print("==================================================")
print("FINAL LONG-DURATION RESULTS")
print("==================================================")

print(
    f"Final Simulation Time : "
    f"{simulation.time}"
)

print(
    f"Final Energy : "
    f"{final_energy}"
)

print(
    f"Final Relative Energy Drift : "
    f"{final_energy_relative_drift}"
)

print(
    f"Maximum Relative Energy Drift : "
    f"{max_energy_relative_drift}"
)

print(
    f"Final Momentum : "
    f"{final_momentum}"
)

print(
    f"Maximum Momentum Error : "
    f"{max_momentum_error}"
)

print(
    f"Final Angular Momentum : "
    f"{final_angular_momentum}"
)

print(
    f"Maximum Angular Momentum Error : "
    f"{max_angular_momentum_error}"
)

print(
    f"Final Center Of Mass : "
    f"{final_center_of_mass}"
)

print(
    f"Maximum Center Of Mass Magnitude : "
    f"{max_center_of_mass_magnitude}"
)


# --------------------------------------------------
# 1. Simulation Duration
# --------------------------------------------------

if abs(
    simulation.time
    - expected_time
) < 1e-9:

    print(
        "✅ Long-Duration Simulation Completed"
    )

    passed += 1

else:

    print(
        "❌ Simulation Duration Incorrect"
    )

    failed += 1


# --------------------------------------------------
# 2. Finite State
# --------------------------------------------------

if finite_state:

    print(
        "✅ All Physical State Values Remained Finite"
    )

    passed += 1

else:

    print(
        "❌ Non-Finite Physical State Detected"
    )

    failed += 1


# --------------------------------------------------
# 3. Energy Stability
# --------------------------------------------------

if (
    max_energy_relative_drift
    <
    energy_tolerance
):

    print(
        "✅ Long-Duration Energy Drift "
        "Within Validation Tolerance"
    )

    passed += 1

else:

    print(
        "❌ Long-Duration Energy Drift "
        "Exceeded Validation Tolerance"
    )

    failed += 1


# --------------------------------------------------
# 4. Momentum Stability
# --------------------------------------------------

if (
    max_momentum_error
    <
    momentum_tolerance
):

    print(
        "✅ Long-Duration Momentum "
        "Conservation Stable"
    )

    passed += 1

else:

    print(
        "❌ Long-Duration Momentum "
        "Drift Detected"
    )

    failed += 1


# --------------------------------------------------
# 5. Angular Momentum Stability
# --------------------------------------------------

if (
    max_angular_momentum_error
    <
    angular_momentum_tolerance
):

    print(
        "✅ Long-Duration Angular Momentum "
        "Conservation Stable"
    )

    passed += 1

else:

    print(
        "❌ Long-Duration Angular Momentum "
        "Drift Detected"
    )

    failed += 1


# --------------------------------------------------
# 6. Center Of Mass Stability
# --------------------------------------------------

if (
    max_center_of_mass_magnitude
    <
    center_of_mass_tolerance
):

    print(
        "✅ Long-Duration Center Of Mass "
        "Remained Stable"
    )

    passed += 1

else:

    print(
        "❌ Long-Duration Center Of Mass "
        "Drift Detected"
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

print("==================================================")


if failed == 0:

    print(
        "🟢 THREE-BODY LONG-DURATION "
        "STABILITY HEALTHY"
    )

else:

    print(
        "🔴 THREE-BODY LONG-DURATION "
        "STABILITY FAILED"
    )