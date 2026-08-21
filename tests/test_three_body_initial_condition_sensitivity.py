import sys
import os
import math


sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)


from three_body_simulation import ThreeBodySimulation


print()
print(
    "🌀 TRIOS THREE-BODY INITIAL-CONDITION "
    "SENSITIVITY TEST"
)
print("==================================================")


passed = 0
failed = 0


# --------------------------------------------------
# Configuration
# --------------------------------------------------

time_step = 0.01
steps = 10000

initial_perturbation = 1e-6


# --------------------------------------------------
# Create Reference Simulation
# --------------------------------------------------

reference = ThreeBodySimulation(
    mass_a=1000,
    mass_b=1000,
    mass_c=1000,
    distance=100,
    time_step=time_step,
    G=1,
)


# --------------------------------------------------
# Create Perturbed Simulation
# --------------------------------------------------

perturbed = ThreeBodySimulation(
    mass_a=1000,
    mass_b=1000,
    mass_c=1000,
    distance=100,
    time_step=time_step,
    G=1,
)


# --------------------------------------------------
# Apply Tiny Initial Perturbation
# --------------------------------------------------

perturbed.body_a.position.x += (
    initial_perturbation
)


# --------------------------------------------------
# Measure Initial Separation
# --------------------------------------------------

def body_distance(body_a, body_b):

    dx = (
        body_a.position.x
        - body_b.position.x
    )

    dy = (
        body_a.position.y
        - body_b.position.y
    )

    return (
        dx ** 2
        + dy ** 2
    ) ** 0.5


def system_trajectory_difference(
    simulation_a,
    simulation_b,
):

    distance_a = body_distance(
        simulation_a.body_a,
        simulation_b.body_a,
    )

    distance_b = body_distance(
        simulation_a.body_b,
        simulation_b.body_b,
    )

    distance_c = body_distance(
        simulation_a.body_c,
        simulation_b.body_c,
    )

    return (
        distance_a ** 2
        + distance_b ** 2
        + distance_c ** 2
    ) ** 0.5


initial_separation = system_trajectory_difference(
    reference,
    perturbed,
)


print(
    f"Initial Perturbation : "
    f"{initial_perturbation}"
)

print(
    f"Initial Trajectory Difference : "
    f"{initial_separation}"
)


# --------------------------------------------------
# Verify Initial Perturbation
# --------------------------------------------------

if (
    initial_separation > 0
    and
    abs(
        initial_separation
        - initial_perturbation
    )
    < 1e-12
):

    print(
        "✅ Tiny Initial Perturbation Applied"
    )

    passed += 1

else:

    print(
        "❌ Initial Perturbation Is Invalid"
    )

    failed += 1


# --------------------------------------------------
# Run Both Systems
# --------------------------------------------------

max_divergence = initial_separation
max_divergence_time = 0.0

finite_state = True

sample_interval = 1000


for step in range(steps):

    reference.step()
    perturbed.step()

    divergence = system_trajectory_difference(
        reference,
        perturbed,
    )

    if divergence > max_divergence:

        max_divergence = divergence
        max_divergence_time = (
            reference.time
        )

    # ----------------------------------------------
    # Finite-State Check
    # ----------------------------------------------

    for simulation in (
        reference,
        perturbed,
    ):

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
    # Progress
    # ----------------------------------------------

    if (
        (step + 1) % sample_interval == 0
    ):

        print(
            f"Step {step + 1:5d} | "
            f"Time {reference.time:.2f} | "
            f"Divergence {divergence:.6e}"
        )


# --------------------------------------------------
# Final Divergence
# --------------------------------------------------

final_divergence = (
    system_trajectory_difference(
        reference,
        perturbed,
    )
)


print()
print(
    "=================================================="
)

print(
    "FINAL SENSITIVITY RESULTS"
)

print(
    "=================================================="
)

print(
    f"Simulation Time : "
    f"{reference.time}"
)

print(
    f"Initial Perturbation : "
    f"{initial_perturbation}"
)

print(
    f"Initial Trajectory Difference : "
    f"{initial_separation}"
)

print(
    f"Final Trajectory Difference : "
    f"{final_divergence}"
)

print(
    f"Maximum Trajectory Difference : "
    f"{max_divergence}"
)

print(
    f"Maximum Divergence Time : "
    f"{max_divergence_time}"
)


# --------------------------------------------------
# 1. Simulation Duration
# --------------------------------------------------

expected_time = (
    time_step * steps
)


if abs(
    reference.time
    - expected_time
) < 1e-9:

    print(
        "✅ Reference Simulation Completed"
    )

    passed += 1

else:

    print(
        "❌ Reference Simulation Time Invalid"
    )

    failed += 1


if abs(
    perturbed.time
    - expected_time
) < 1e-9:

    print(
        "✅ Perturbed Simulation Completed"
    )

    passed += 1

else:

    print(
        "❌ Perturbed Simulation Time Invalid"
    )

    failed += 1


# --------------------------------------------------
# 2. Finite State
# --------------------------------------------------

if finite_state:

    print(
        "✅ Both Systems Remained Numerically Finite"
    )

    passed += 1

else:

    print(
        "❌ Non-Finite State Detected"
    )

    failed += 1


# --------------------------------------------------
# 3. Trajectories Are No Longer Identical
# --------------------------------------------------

if final_divergence > initial_separation:

    print(
        "✅ Small Initial Difference Produced "
        "Larger Final Trajectory Difference"
    )

    passed += 1

else:

    print(
        "❌ No Measurable Trajectory Amplification"
    )

    failed += 1


# --------------------------------------------------
# 4. Sensitivity Amplification
# --------------------------------------------------

amplification_factor = (
    max_divergence
    /
    initial_separation
)


print(
    f"Maximum Amplification Factor : "
    f"{amplification_factor}"
)


if amplification_factor > 1.0:

    print(
        "✅ Initial Perturbation Was Amplified"
    )

    passed += 1

else:

    print(
        "❌ Initial Perturbation Was Not Amplified"
    )

    failed += 1


# --------------------------------------------------
# 5. Detectable Divergence
# --------------------------------------------------

if max_divergence > 1e-6:

    print(
        "✅ Trajectory Divergence Is "
        "Numerically Detectable"
    )

    passed += 1

else:

    print(
        "❌ Trajectory Divergence Is "
        "Too Small To Detect"
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
        "🟢 THREE-BODY INITIAL-CONDITION "
        "SENSITIVITY HEALTHY"
    )

else:

    print(
        "🔴 THREE-BODY INITIAL-CONDITION "
        "SENSITIVITY FAILED"
    )