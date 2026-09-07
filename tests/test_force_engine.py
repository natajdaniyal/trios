import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from body import Body
from force import Force
from force_engine import ForceEngine
from vector import Vector2


class TestForce(Force):
    def __init__(self, vector):
        super().__init__("TestForce")
        self.vector = vector

    def calculate(self, body_a, body_b=None):
        return self.vector


def test_force_engine_creation():
    engine = ForceEngine()

    assert engine.bodies == []
    assert engine.forces == []


def test_add_body():
    engine = ForceEngine()
    body = Body("A", 1.0, Vector2(0, 0), Vector2(0, 0))

    engine.add_body(body)

    assert body in engine.bodies
    assert len(engine.bodies) == 1


def test_add_force():
    engine = ForceEngine()
    force = TestForce(Vector2(1, 0))

    engine.add_force(force)

    assert force in engine.forces
    assert len(engine.forces) == 1


def test_add_invalid_force():
    engine = ForceEngine()

    try:
        engine.add_force("not a force")
        assert False
    except TypeError:
        assert True


def test_pair_calculation():
    engine = ForceEngine()

    body_a = Body("A", 1.0, Vector2(0, 0), Vector2(0, 0))
    body_b = Body("B", 1.0, Vector2(10, 0), Vector2(0, 0))

    force = TestForce(Vector2(5, 0))

    engine.add_body(body_a)
    engine.add_body(body_b)
    engine.add_force(force)

    engine.calculate_forces()

    assert body_a.force.x == 5
    assert body_a.force.y == 0

    assert body_b.force.x == -5
    assert body_b.force.y == 0


def test_equal_and_opposite_forces():
    engine = ForceEngine()

    body_a = Body("A", 1.0, Vector2(0, 0), Vector2(0, 0))
    body_b = Body("B", 1.0, Vector2(10, 0), Vector2(0, 0))

    force = TestForce(Vector2(3, 4))

    engine.add_body(body_a)
    engine.add_body(body_b)
    engine.add_force(force)

    engine.calculate_forces()

    assert body_a.force.x == -body_b.force.x
    assert body_a.force.y == -body_b.force.y


def test_multiple_bodies():
    engine = ForceEngine()

    body_a = Body("A", 1.0, Vector2(0, 0), Vector2(0, 0))
    body_b = Body("B", 1.0, Vector2(1, 0), Vector2(0, 0))
    body_c = Body("C", 1.0, Vector2(0, 1), Vector2(0, 0))

    force = TestForce(Vector2(1, 0))

    engine.add_body(body_a)
    engine.add_body(body_b)
    engine.add_body(body_c)
    engine.add_force(force)

    engine.calculate_forces()

    assert body_a.force.x == 2
    assert body_a.force.y == 0

    assert body_b.force.x == 0
    assert body_b.force.y == 0

    assert body_c.force.x == -2
    assert body_c.force.y == 0


def test_multiple_forces():
    engine = ForceEngine()

    body_a = Body("A", 1.0, Vector2(0, 0), Vector2(0, 0))
    body_b = Body("B", 1.0, Vector2(10, 0), Vector2(0, 0))

    force_1 = TestForce(Vector2(2, 0))
    force_2 = TestForce(Vector2(0, 3))

    engine.add_body(body_a)
    engine.add_body(body_b)

    engine.add_force(force_1)
    engine.add_force(force_2)

    engine.calculate_forces()

    assert body_a.force.x == 2
    assert body_a.force.y == 3

    assert body_b.force.x == -2
    assert body_b.force.y == -3


def test_clear_bodies():
    engine = ForceEngine()

    body = Body("A", 1.0, Vector2(0, 0), Vector2(0, 0))

    engine.add_body(body)
    engine.clear_bodies()

    assert engine.bodies == []


def test_clear_forces():
    engine = ForceEngine()

    force = TestForce(Vector2(1, 0))

    engine.add_force(force)
    engine.clear_forces()

    assert engine.forces == []