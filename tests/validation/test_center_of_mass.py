from body import Body
from vector import Vector2
from center_of_mass import CenterOfMassSystem


def test_center_of_mass_system_creation():
    assert isinstance(CenterOfMassSystem(), CenterOfMassSystem)


def test_total_mass():
    bodies = [
        Body("A", 2, Vector2(0, 0)),
        Body("B", 3, Vector2(10, 0)),
    ]

    system = CenterOfMassSystem()

    assert system.total_mass(bodies) == 5


def test_center_of_mass():
    bodies = [
        Body("A", 2, Vector2(0, 0)),
        Body("B", 3, Vector2(10, 0)),
    ]

    system = CenterOfMassSystem()

    assert system.center_of_mass(bodies) == (6, 0)


def test_center_of_mass_two_dimensions():
    bodies = [
        Body("A", 1, Vector2(0, 0)),
        Body("B", 1, Vector2(2, 4)),
    ]

    system = CenterOfMassSystem()

    assert system.center_of_mass(bodies) == (1, 2)


def test_center_of_mass_none_and_empty_safety():
    system = CenterOfMassSystem()

    assert system.center_of_mass(None) == (0, 0)
    assert system.center_of_mass([]) == (0, 0)
    assert system.total_mass(None) == 0
    assert system.total_mass([]) == 0
