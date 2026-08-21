import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from vector import Vector2


def test_vector_length():
    vector = Vector2(3, 4)

    assert vector.length() == 5


def test_vector_addition():
    vector_a = Vector2(3, 4)
    vector_b = Vector2(1, 2)

    result = vector_a.add(vector_b)

    assert result.x == 4
    assert result.y == 6


def test_vector_subtraction():
    vector_a = Vector2(5, 7)
    vector_b = Vector2(2, 3)

    result = vector_a.subtract(vector_b)

    assert result.x == 3
    assert result.y == 4


def test_vector_multiplication():
    vector = Vector2(3, 4)

    result = vector.multiply(2)

    assert result.x == 6
    assert result.y == 8


def test_vector_normalization():
    vector = Vector2(3, 4)

    result = vector.normalize()

    assert abs(result.x - 0.6) < 1e-9
    assert abs(result.y - 0.8) < 1e-9