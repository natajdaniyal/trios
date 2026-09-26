import pytest

from experiment_scenarios import (
    build_experiment_one_scenario,
    build_opposite_poles_scenario,
    build_same_poles_scenario,
    build_three_magnets_scenario,
)


def test_opposite_poles_scenario_has_two_magnets_and_attracts():
    simulation = build_opposite_poles_scenario()
    assert len(simulation.bodies) == 2

    left, right = simulation.bodies
    initial_left = left.position.x
    simulation.step()

    assert left.position.x > initial_left


def test_same_poles_scenario_has_two_magnets_and_repels():
    simulation = build_same_poles_scenario()
    assert len(simulation.bodies) == 2

    left, right = simulation.bodies
    initial_left = left.position.x
    simulation.step()

    assert left.position.x < initial_left


def test_three_magnets_scenario_has_three_magnets():
    simulation = build_three_magnets_scenario()
    assert len(simulation.bodies) == 3


def test_unknown_scenario_is_rejected():
    with pytest.raises(ValueError, match="Unknown Experiment 1 scenario"):
        build_experiment_one_scenario("unknown")


def test_magnets_cannot_penetrate_each_other_during_simulation():
    simulation = build_opposite_poles_scenario(positions={"A": -0.25, "B": 0.25})
    simulation.step()
    left, right = simulation.bodies
    distance = right.position.subtract(left.position).length()
    assert distance >= (left.collision_radius + right.collision_radius) - 1e-9


def test_three_magnet_setup_is_not_symmetric():
    simulation = build_three_magnets_scenario()
    assert len({round(body.position.y, 6) for body in simulation.bodies}) == 3


def test_magnetic_force_is_bounded_for_nearby_finite_size_magnets():
    simulation = build_three_magnets_scenario(
        positions={
            "A": {"x": -1.0, "y": 0.0},
            "B": {"x": 0.0, "y": 0.5},
            "C": {"x": 1.0, "y": 0.0},
        }
    )

    for _ in range(220):
        simulation.step()

    maximum_coordinate = max(
        abs(body.position.x)
        for body in simulation.bodies
    ) + max(
        abs(body.position.y)
        for body in simulation.bodies
    )

    assert maximum_coordinate < 10.0
