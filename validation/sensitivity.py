"""Utilities for measuring sensitivity between two simulation outcomes."""

from math import hypot


def body_state_distance(body_a, body_b):
    """Return Euclidean distance across position and velocity state."""
    if body_a is None or body_b is None:
        raise ValueError("Both bodies are required.")

    position_delta = hypot(
        body_a.position.x - body_b.position.x,
        body_a.position.y - body_b.position.y,
    )
    velocity_delta = hypot(
        body_a.velocity.x - body_b.velocity.x,
        body_a.velocity.y - body_b.velocity.y,
    )

    return hypot(position_delta, velocity_delta)


def system_state_distance(bodies_a, bodies_b):
    """Return the combined state distance for two comparable body systems."""
    if bodies_a is None or bodies_b is None:
        raise ValueError("Both body collections are required.")

    bodies_a = list(bodies_a)
    bodies_b = list(bodies_b)

    if len(bodies_a) != len(bodies_b):
        raise ValueError("Body collections must contain the same number of bodies.")

    total_squared = 0
    for body_a, body_b in zip(bodies_a, bodies_b):
        distance = body_state_distance(body_a, body_b)
        total_squared += distance ** 2

    return total_squared ** 0.5


class SensitivityAnalyzer:
    """Compare two completed physical outcomes without interpreting them."""

    def compare(self, reference_bodies, perturbed_bodies):
        return {
            "state_distance": system_state_distance(
                reference_bodies,
                perturbed_bodies,
            )
        }
