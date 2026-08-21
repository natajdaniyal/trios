import os
import sys


# Add project root to Python import path
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


from three_body_simulation import ThreeBodySimulation


def test_three_body_creation():
    simulation = ThreeBodySimulation()

    assert simulation.body_a is not None
    assert simulation.body_b is not None
    assert simulation.body_c is not None

    assert len(simulation.bodies) == 3

    print("✅ Three Body Simulation Created")


def test_body_masses():
    simulation = ThreeBodySimulation(
        mass_a=1000,
        mass_b=2000,
        mass_c=3000,
    )

    assert simulation.body_a.mass == 1000
    assert simulation.body_b.mass == 2000
    assert simulation.body_c.mass == 3000

    print("✅ Body Masses Correct")


def test_initial_geometry():
    distance = 100

    simulation = ThreeBodySimulation(
        distance=distance
    )

    ab = simulation.distance_ab()
    ac = simulation.distance_ac()
    bc = simulation.distance_bc()

    tolerance = 1e-9

    assert abs(ab - distance) < tolerance
    assert abs(ac - distance) < tolerance
    assert abs(bc - distance) < tolerance

    print("✅ Equilateral Initial Geometry Correct")


def test_center_of_mass():
    simulation = ThreeBodySimulation()

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

    tolerance = 1e-9

    assert abs(center_x) < tolerance
    assert abs(center_y) < tolerance

    print("✅ Center Of Mass At Origin")


def test_initial_total_momentum():
    simulation = ThreeBodySimulation()

    px = (
        simulation.body_a.mass
        * simulation.body_a.velocity.x
        + simulation.body_b.mass
        * simulation.body_b.velocity.x
        + simulation.body_c.mass
        * simulation.body_c.velocity.x
    )

    py = (
        simulation.body_a.mass
        * simulation.body_a.velocity.y
        + simulation.body_b.mass
        * simulation.body_b.velocity.y
        + simulation.body_c.mass
        * simulation.body_c.velocity.y
    )

    tolerance = 1e-9

    assert abs(px) < tolerance
    assert abs(py) < tolerance

    print("✅ Initial Total Momentum Is Zero")


def test_initial_distances_are_equal():
    simulation = ThreeBodySimulation(
        distance=100
    )

    ab = simulation.distance_ab()
    ac = simulation.distance_ac()
    bc = simulation.distance_bc()

    tolerance = 1e-9

    assert abs(ab - ac) < tolerance
    assert abs(ac - bc) < tolerance

    print("✅ Initial Pairwise Distances Are Equal")


def test_simulation_time_advances():
    time_step = 0.01

    simulation = ThreeBodySimulation(
        time_step=time_step
    )

    assert simulation.time == 0

    simulation.step()

    assert abs(
        simulation.time - time_step
    ) < 1e-12

    print("✅ Simulation Time Advances")


def test_bodies_move_after_step():
    simulation = ThreeBodySimulation(
        time_step=0.01
    )

    initial_positions = [
        (
            simulation.body_a.position.x,
            simulation.body_a.position.y,
        ),
        (
            simulation.body_b.position.x,
            simulation.body_b.position.y,
        ),
        (
            simulation.body_c.position.x,
            simulation.body_c.position.y,
        ),
    ]

    simulation.step()

    final_positions = [
        (
            simulation.body_a.position.x,
            simulation.body_a.position.y,
        ),
        (
            simulation.body_b.position.x,
            simulation.body_b.position.y,
        ),
        (
            simulation.body_c.position.x,
            simulation.body_c.position.y,
        ),
    ]

    assert initial_positions != final_positions

    print("✅ Bodies Move After Simulation Step")


def test_pairwise_distances_remain_valid():
    simulation = ThreeBodySimulation(
        time_step=0.01
    )

    simulation.step()

    ab = simulation.distance_ab()
    ac = simulation.distance_ac()
    bc = simulation.distance_bc()

    assert ab > 0
    assert ac > 0
    assert bc > 0

    assert isinstance(ab, float)
    assert isinstance(ac, float)
    assert isinstance(bc, float)

    print("✅ Pairwise Distances Remain Valid")


def test_run_advances_multiple_steps():
    time_step = 0.01
    steps = 10

    simulation = ThreeBodySimulation(
        time_step=time_step
    )

    simulation.run(steps)

    expected_time = (
        time_step * steps
    )

    assert abs(
        simulation.time - expected_time
    ) < 1e-12

    print("✅ Multi-Step Simulation Works")


def main():
    print()
    print("🌌 TRIOS THREE-BODY SIMULATION TEST")
    print("=" * 50)

    tests = [
        test_three_body_creation,
        test_body_masses,
        test_initial_geometry,
        test_center_of_mass,
        test_initial_total_momentum,
        test_initial_distances_are_equal,
        test_simulation_time_advances,
        test_bodies_move_after_step,
        test_pairwise_distances_remain_valid,
        test_run_advances_multiple_steps,
    ]

    passed = 0

    for test in tests:
        test()
        passed += 1

    print("=" * 50)
    print(
        f"✅ PASSED: {passed}/{len(tests)}"
    )
    print(
        "🟢 THREE-BODY SIMULATION TEST HEALTHY"
    )


if __name__ == "__main__":
    main()