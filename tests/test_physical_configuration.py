
import os
import sys

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

import pytest

from physical_configuration import (
    BodyPhysicalConfiguration,
    StagePhysicalConfiguration,
)


def make_body(name="A", mass=10):
    return BodyPhysicalConfiguration(
        name=name,
        mass=mass,
        position_x=1.0,
        position_y=2.0,
        velocity_x=0.5,
        velocity_y=-0.5,
    )


def test_body_configuration_stores_values():
    body = make_body()

    assert body.name == "A"
    assert body.mass == 10
    assert body.position_x == 1.0
    assert body.position_y == 2.0
    assert body.velocity_x == 0.5
    assert body.velocity_y == -0.5


def test_body_configuration_rejects_invalid_mass():
    with pytest.raises(ValueError):
        BodyPhysicalConfiguration(name="A", mass=0)

    with pytest.raises(ValueError):
        BodyPhysicalConfiguration(name="A", mass=-5)


def test_body_configuration_requires_name():
    with pytest.raises(ValueError):
        BodyPhysicalConfiguration(name="", mass=10)


def test_body_configuration_as_dict_and_equality():
    body_1 = make_body("A", 10)
    body_2 = make_body("A", 10)
    body_3 = make_body("A", 999)

    assert body_1 == body_2
    assert body_1 != body_3

    assert body_1.as_dict() == {
        "name": "A",
        "mass": 10,
        "position_x": 1.0,
        "position_y": 2.0,
        "velocity_x": 0.5,
        "velocity_y": -0.5,
    }


def test_stage_configuration_starts_empty():
    stage = StagePhysicalConfiguration(stage_name="Stage 1")

    assert len(stage) == 0
    assert stage.body_names() == []


def test_stage_configuration_add_and_get_body():
    stage = StagePhysicalConfiguration(stage_name="Stage 1")

    body_a = make_body("A", 10)
    stage.add_body(body_a)

    assert stage.has_body("A")
    assert stage.get_body("A") is body_a
    assert stage.get_body("missing") is None
    assert len(stage) == 1
    assert "A" in stage


def test_stage_configuration_rejects_duplicate_body_name():
    stage = StagePhysicalConfiguration()
    stage.add_body(make_body("A"))

    with pytest.raises(ValueError):
        stage.add_body(make_body("A"))


def test_stage_configuration_rejects_non_body_configuration():
    stage = StagePhysicalConfiguration()

    with pytest.raises(TypeError):
        stage.add_body("not a body configuration")


def test_multiple_bodies_in_one_stage():
    stage = StagePhysicalConfiguration(stage_name="Stage 1")

    stage.add_body(make_body("A", 10))
    stage.add_body(make_body("B", 20))
    stage.add_body(make_body("C", 30))

    assert stage.body_names() == ["A", "B", "C"]
    assert len(stage) == 3


def test_stages_are_independent_of_each_other():
    stage_1 = StagePhysicalConfiguration(stage_name="Stage 1")

    stage_1.add_body(
        BodyPhysicalConfiguration(
            "A",
            mass=10,
            position_x=0,
            position_y=0,
        )
    )

    stage_1.add_body(
        BodyPhysicalConfiguration(
            "B",
            mass=20,
            position_x=5,
            position_y=0,
        )
    )

    stage_1.add_body(
        BodyPhysicalConfiguration(
            "C",
            mass=30,
            position_x=0,
            position_y=5,
        )
    )

    stage_2 = StagePhysicalConfiguration(stage_name="Stage 2")

    stage_2.add_body(
        BodyPhysicalConfiguration(
            "A",
            mass=100,
            position_x=50,
            position_y=50,
        )
    )

    stage_2.add_body(
        BodyPhysicalConfiguration(
            "B",
            mass=200,
            position_x=-50,
            position_y=50,
        )
    )

    stage_2.add_body(
        BodyPhysicalConfiguration(
            "C",
            mass=300,
            position_x=0,
            position_y=-50,
        )
    )

    assert stage_1.get_body("A").mass == 10
    assert stage_1.get_body("A").position_x == 0

    assert stage_2.get_body("A").mass == 100
    assert stage_2.get_body("A").position_x == 50

    stage_2.get_body("A").mass = 999

    assert stage_1.get_body("A").mass == 10


def test_two_stage_configurations_can_hold_same_body_names_independently():
    stage_1 = StagePhysicalConfiguration()
    stage_2 = StagePhysicalConfiguration()

    stage_1.add_body(make_body("A", 1))
    stage_2.add_body(make_body("A", 2))

    assert stage_1.get_body("A").mass == 1
    assert stage_2.get_body("A").mass == 2