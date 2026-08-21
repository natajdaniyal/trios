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
    "🌀 TRIOS THREE-BODY QUANTITATIVE "
    "SENSITIVITY ANALYSIS"
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

sample_interval = 100


# --------------------------------------------------
# Helpers
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


# --------------------------------------------------
# Create Systems
# --------------------------------------------------

reference = ThreeBodySimulation(
    mass_a=1000,
    mass_b=1000,
    mass_c=1000,
    distance=100,
    time_step=time_step,
    G=1,
)


perturbed = ThreeBodySimulation(
    mass_a=1000,
    mass_b=1000,
    mass_c=1000,
    distance=100,
    time_step=time_step,
    G=1,
)


# --------------------------------------------------
# Apply Tiny Perturbation
# --------------------------------------------------

perturbed.body_a.position.x += (
    initial_perturbation
)


initial_difference = (
    system_trajectory_difference(
        reference,
        perturbed,
    )
)


print(
    f"Initial Perturbation : "
    f"{initial_perturbation}"
)

print(
    f"Initial Difference    : "
    f"{initial_difference}"
)


# --------------------------------------------------
# Collect Divergence Samples
# --------------------------------------------------

samples = []

finite_state = True


for step in range(steps):

    reference.step()
    perturbed.step()

    if (
        (step + 1) % sample_interval
        == 0
    ):

        current_time = reference.time

        divergence = (
            system_trajectory_difference(
                reference,
                perturbed,
            )
        )

        samples.append(
            (
                current_time,
                divergence,
            )
        )

        print(
            f"Time {current_time:7.2f} | "
            f"Divergence {divergence:.6e}"
        )

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


# --------------------------------------------------
# Final Difference
# --------------------------------------------------

final_time = reference.time

final_difference = (
    system_trajectory_difference(
        reference,
        perturbed,
    )
)


# --------------------------------------------------
# Finite-Time Divergence Rate
#
# lambda = ln(D_final / D_initial) / T
#
# This is a finite-time diagnostic.
# It is NOT by itself a proof of chaos.
# --------------------------------------------------

if (
    initial_difference > 0
    and
    final_difference > 0
):

    finite_time_rate = (
        math.log(
            final_difference
            /
            initial_difference
        )
        /
        final_time
    )

else:

    finite_time_rate = 0.0


amplification_factor = (
    final_difference
    /
    initial_difference
)


# --------------------------------------------------
# Log-Divergence Fit
# --------------------------------------------------

fit_times = []
fit_logs = []


for time, divergence in samples:

    if divergence > 0:

        fit_times.append(time)
        fit_logs.append(
            math.log(divergence)
        )


def linear_regression_slope(
    x_values,
    y_values,
):

    n = len(x_values)

    if n < 2:

        return 0.0

    mean_x = (
        sum(x_values)
        / n
    )

    mean_y = (
        sum(y_values)
        / n
    )

    numerator = 0.0
    denominator = 0.0

    for x, y in zip(
        x_values,
        y_values,
    ):

        numerator += (
            (x - mean_x)
            *
            (y - mean_y)
        )

        denominator += (
            (x - mean_x) ** 2
        )

    if denominator == 0:

        return 0.0

    return numerator / denominator


log_divergence_slope = (
    linear_regression_slope(
        fit_times,
        fit_logs,
    )
)


# --------------------------------------------------
# R² of Log-Divergence Fit
# --------------------------------------------------

if len(fit_times) >= 2:

    mean_log = (
        sum(fit_logs)
        /
        len(fit_logs)
    )

    predicted_logs = []

    for time in fit_times:

        predicted_logs.append(
            fit_logs[0]
            +
            log_divergence_slope
            * (
                time
                - fit_times[0]
            )
        )

    ss_total = 0.0
    ss_residual = 0.0

    for actual, predicted in zip(
        fit_logs,
        predicted_logs,
    ):

        ss_total += (
            actual
            - mean_log
        ) ** 2

        ss_residual += (
            actual
            - predicted
        ) ** 2

    if ss_total > 0:

        r_squared = (
            1
            -
            (
                ss_residual
                /
                ss_total
            )
        )

    else:

        r_squared = 0.0

else:

    r_squared = 0.0


# --------------------------------------------------
# Final Report
# --------------------------------------------------

print()
print(
    "=================================================="
)

print(
    "QUANTITATIVE SENSITIVITY RESULTS"
)

print(
    "=================================================="
)

print(
    f"Simulation Time : "
    f"{final_time}"
)

print(
    f"Initial Difference : "
    f"{initial_difference}"
)

print(
    f"Final Difference : "
    f"{final_difference}"
)

print(
    f"Amplification Factor : "
    f"{amplification_factor}"
)

print(
    f"Finite-Time Divergence Rate : "
    f"{finite_time_rate}"
)

print(
    f"Log-Divergence Slope : "
    f"{log_divergence_slope}"
)

print(
    f"Log-Divergence R² : "
    f"{r_squared}"
)


# --------------------------------------------------
# 1. Simulation Completed
# --------------------------------------------------

expected_time = (
    time_step
    * steps
)


if abs(
    final_time
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
# 2. Finite-State Validation
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
# 3. Amplification
# --------------------------------------------------

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
# 4. Positive Finite-Time Divergence Rate
# --------------------------------------------------

if finite_time_rate > 0:

    print(
        "✅ Finite-Time Divergence Rate Is Positive"
    )

    passed += 1

else:

    print(
        "❌ Finite-Time Divergence Rate Is Not Positive"
    )

    failed += 1


# --------------------------------------------------
# 5. Positive Log-Divergence Slope
# --------------------------------------------------

if log_divergence_slope > 0:

    print(
        "✅ Log-Divergence Shows Positive Growth"
    )

    passed += 1

else:

    print(
        "❌ Log-Divergence Growth Is Not Positive"
    )

    failed += 1


# --------------------------------------------------
# 6. Detectable Divergence
# --------------------------------------------------

if final_difference > 1e-6:

    print(
        "✅ Final Trajectory Divergence "
        "Is Numerically Detectable"
    )

    passed += 1

else:

    print(
        "❌ Final Trajectory Divergence "
        "Is Too Small"
    )

    failed += 1


# --------------------------------------------------
# 7. Interpretation Guard
# --------------------------------------------------

print()
print(
    "ℹ️ Positive divergence indicates "
    "sensitivity to initial conditions."
)

print(
    "ℹ️ This test does NOT by itself prove chaos."
)

passed += 1


# --------------------------------------------------
# Final Report
# --------------------------------------------------

print()
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
        "🟢 THREE-BODY QUANTITATIVE "
        "SENSITIVITY HEALTHY"
    )

else:

    print(
        "🔴 THREE-BODY QUANTITATIVE "
        "SENSITIVITY FAILED"
    )