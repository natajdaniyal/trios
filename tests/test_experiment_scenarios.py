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
