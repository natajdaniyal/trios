import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from vector import Vector2
from magnet import Magnet
from physics_engine import PhysicsEngine
from forces.magnetic_force import MagneticForce


def test_full_physics_chain():

    magnet_a = Magnet(
        "Magnet A",
        1,
        0,
        0,
        5,
        "N"
    )

    magnet_b = Magnet(
        "Magnet B",
        1,
        10,
        0,
        5,
        "S"
    )

    assert magnet_a.position.x == 0
    assert magnet_b.position.x == 10


    magnetic = MagneticForce(5)

    force = magnetic.calculate(
        magnet_a,
        magnet_b
    )

    assert isinstance(force, Vector2)


    magnet_a.apply_force(force)

    assert magnet_a.force.x != 0


    engine = PhysicsEngine()

    old_position = magnet_a.position.x

    engine.update(
        magnet_a
    )

    assert magnet_a.velocity.x != 0
    assert magnet_a.position.x != old_position