import pytest

from body import Body
from vector import Vector2
from sensitivity import SensitivityAnalyzer, body_state_distance, system_state_distance
from system_validation import ConservationValidator, PhysicalStateSnapshot


def make_bodies():
    return [
        Body("A", 2, Vector2(0, 0), Vector2(1, 0)),
        Body("B", 1, Vector2(2, 0), Vector2(0, 1)),
    ]


def test_physical_state_snapshot_captures_core_validation_values():
    snapshot = PhysicalStateSnapshot.capture(make_bodies())

    assert snapshot.total_energy == pytest.approx(1 + 0.5 - 1)
    assert snapshot.total_momentum == (2, 1)
    assert snapshot.angular_momentum == pytest.approx(2)
    assert snapshot.center_of_mass == pytest.approx((2 / 3, 0))


def test_conservation_validator_reports_changes():
    initial = PhysicalStateSnapshot((10, 2, 0), (2, 1), 3, (1, 2))
    final = PhysicalStateSnapshot((9, 2, 0), (2.3, 1.4), 3.5, (1.3, 2.4))

    result = ConservationValidator().compare(initial, final)

    assert result["energy_change"] == -1
    assert result["energy_error"] == 1
    assert result["momentum_change"] == pytest.approx((0.3, 0.4))
    assert result["momentum_error"] == pytest.approx(0.5)
    assert result["angular_momentum_error"] == pytest.approx(0.5)
    assert result["center_of_mass_error"] == pytest.approx(0.5)


def test_sensitivity_distance_is_zero_for_equal_states():
    bodies = make_bodies()

    assert body_state_distance(bodies[0], bodies[0]) == 0
    assert system_state_distance(bodies, bodies) == 0


def test_sensitivity_analyzer_reports_state_difference():
    reference = make_bodies()
    perturbed = make_bodies()
    perturbed[0].position = Vector2(1, 0)

    result = SensitivityAnalyzer().compare(reference, perturbed)

    assert result["state_distance"] == pytest.approx(1)


def test_system_state_distance_rejects_different_sizes():
    with pytest.raises(ValueError):
        system_state_distance(make_bodies(), make_bodies()[:1])
