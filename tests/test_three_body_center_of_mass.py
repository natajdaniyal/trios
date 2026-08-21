import sys
import os


sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)


from three_body_simulation import ThreeBodySimulation


print()
print("🌌 TRIOS THREE-BODY CENTER OF MASS TEST")
print("==================================================")


passed = 0
failed = 0


def calculate_center_of_mass(simulation):

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


def center_of_mass_magnitude(center_of_mass):

    x = center_of_mass[0]
    y = center_of_mass[1]

    return (
        x ** 2
        + y ** 2
    ) ** 0.5


# --------------------------------------------------
# 1. Equal-Mass Initial Center Of Mass
# --------------------------------------------------

simulation = ThreeBodySimulation(
    mass_a=1000,
    mass_b=1000,
    mass_c=1000,
    distance=100,
    time_step=0.01,
)


initial_center_of_mass = calculate_center_of_mass(
    simulation
)

initial_magnitude = center_of_mass_magnitude(
    initial_center_of_mass
)


print(
    f"Initial Center Of Mass : "
    f"{initial_center_of_mass}"
)

print(
    f"Initial Magnitude : "
    f"{initial_magnitude}"
)


if initial_magnitude < 1e-9:

    print("✅ Initial Center Of Mass At Origin")
    passed += 1

else:

    print(
        "❌ Initial Center Of Mass Is Not At Origin"
    )
    failed += 1


# --------------------------------------------------
# 2. Equal-Mass Center Of Mass Stability
# --------------------------------------------------

max_magnitude = 0.0

steps = 1000


for _ in range(steps):

    simulation.step()

    current_center_of_mass = (
        calculate_center_of_mass(simulation)
    )

    current_magnitude = center_of_mass_magnitude(
        current_center_of_mass
    )

    if current_magnitude > max_magnitude:

        max_magnitude = current_magnitude


final_center_of_mass = calculate_center_of_mass(
    simulation
)

final_magnitude = center_of_mass_magnitude(
    final_center_of_mass
)


print(
    f"Final Center Of Mass : "
    f"{final_center_of_mass}"
)

print(
    f"Final Magnitude : "
    f"{final_magnitude}"
)

print(
    f"Maximum Center Of Mass Magnitude : "
    f"{max_magnitude}"
)

print(
    f"Simulation Time : "
    f"{simulation.time}"
)


tolerance = 1e-6


if final_magnitude < tolerance:

    print(
        "✅ Final Center Of Mass Remains Near Origin"
    )
    passed += 1

else:

    print(
        "❌ Final Center Of Mass Drift Detected"
    )
    failed += 1


if max_magnitude < tolerance:

    print(
        "✅ Center Of Mass Stable Throughout Simulation"
    )
    passed += 1

else:

    print(
        "❌ Center Of Mass Stability Failed"
    )
    failed += 1


# --------------------------------------------------
# 3. Unequal-Mass Initial Center Of Mass
# --------------------------------------------------

unequal_simulation = ThreeBodySimulation(
    mass_a=800,
    mass_b=1200,
    mass_c=1600,
    distance=100,
    time_step=0.01,
)


unequal_initial_center_of_mass = (
    calculate_center_of_mass(
        unequal_simulation
    )
)

unequal_initial_magnitude = (
    center_of_mass_magnitude(
        unequal_initial_center_of_mass
    )
)


print()
print(
    f"Unequal Mass Initial Center Of Mass : "
    f"{unequal_initial_center_of_mass}"
)

print(
    f"Unequal Mass Initial Magnitude : "
    f"{unequal_initial_magnitude}"
)


if unequal_initial_magnitude < tolerance:

    print(
        "✅ Unequal-Mass Center Of Mass At Origin"
    )
    passed += 1

else:

    print(
        "❌ Unequal-Mass Center Of Mass "
        "Is Not At Origin"
    )
    failed += 1


# --------------------------------------------------
# 4. Unequal-Mass Center Of Mass Stability
# --------------------------------------------------

unequal_max_magnitude = 0.0

for _ in range(500):

    unequal_simulation.step()

    current_center_of_mass = (
        calculate_center_of_mass(
            unequal_simulation
        )
    )

    current_magnitude = center_of_mass_magnitude(
        current_center_of_mass
    )

    if current_magnitude > unequal_max_magnitude:

        unequal_max_magnitude = current_magnitude


unequal_final_center_of_mass = (
    calculate_center_of_mass(
        unequal_simulation
    )
)

unequal_final_magnitude = (
    center_of_mass_magnitude(
        unequal_final_center_of_mass
    )
)


print(
    f"Unequal Mass Final Center Of Mass : "
    f"{unequal_final_center_of_mass}"
)

print(
    f"Unequal Mass Final Magnitude : "
    f"{unequal_final_magnitude}"
)

print(
    f"Unequal Mass Maximum Magnitude : "
    f"{unequal_max_magnitude}"
)

print(
    f"Unequal Mass Simulation Time : "
    f"{unequal_simulation.time}"
)


if unequal_final_magnitude < tolerance:

    print(
        "✅ Unequal-Mass Center Of Mass "
        "Remains Near Origin"
    )
    passed += 1

else:

    print(
        "❌ Unequal-Mass Center Of Mass "
        "Drift Detected"
    )
    failed += 1


if unequal_max_magnitude < tolerance:

    print(
        "✅ Unequal-Mass Center Of Mass "
        "Stable Throughout Simulation"
    )
    passed += 1

else:

    print(
        "❌ Unequal-Mass Center Of Mass "
        "Stability Failed"
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
        "🟢 THREE-BODY CENTER OF MASS HEALTHY"
    )

else:

    print(
        "🔴 THREE-BODY CENTER OF MASS FAILED"
    )