import pytest

from body import Body
from physical_configuration import (
    BodyPhysicalConfiguration,
    StagePhysicalConfiguration,
)
from simulation.physical_configuration_adapter import bodies_from_configuration


def make_config():
    configuration = StagePhysicalConfiguration()
    configuration.add_body(
        BodyPhysicalConfiguration(
            name="A",
            mass=10,
            position_x=1.0,
            position_y=2.0,
            velocity_x=0.5,
            velocity_y=-0.5,
        )
    )
    configuration.add_body(
        BodyPhysicalConfiguration(
            name="B",
            mass=20,
            position_x=-3.0,
            position_y=4.0,
            velocity_x=-1.0,
            velocity_y=1.5,
        )
    )
    return configuration


def test_conversion_creates_body_objects():
    bodies = bodies_from_configuration(make_config())

    assert all(isinstance(body, Body) for body in bodies)
    assert [body.name for body in bodies] == ["A", "B"]


def test_conversion_copies_physical_values():
    bodies = bodies_from_configuration(make_config())

    assert bodies[0].mass == 10
    assert bodies[0].position.x == 1.0
    assert bodies[0].position.y == 2.0
    assert bodies[0].velocity.x == 0.5
    assert bodies[0].velocity.y == -0.5

    assert bodies[1].mass == 20
    assert bodies[1].position.x == -3.0
    assert bodies[1].position.y == 4.0
    assert bodies[1].velocity.x == -1.0
    assert bodies[1].velocity.y == 1.5


def test_conversion_creates_independent_objects():
    configuration = make_config()
    bodies = bodies_from_configuration(configuration)

    configuration.get_body("A").mass = 999
    configuration.get_body("A").position_x = 100

    assert bodies[0].mass == 10
    assert bodies[0].position.x == 1.0


def test_conversion_of_empty_configuration_returns_empty_list():
    configuration = StagePhysicalConfiguration()

    assert bodies_from_configuration(configuration) == []


def test_conversion_rejects_invalid_configuration_type():
    with pytest.raises(TypeError):
        bodies_from_configuration("not a configuration")
