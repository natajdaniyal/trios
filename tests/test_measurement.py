import pytest

from measurement import MeasurementSet


def test_measurement_set_starts_empty():
    measurements = MeasurementSet()

    assert len(measurements) == 0
    assert measurements.items() == []


def test_measurement_set_add_and_get():
    measurements = MeasurementSet()

    measurements.add("energy", 12.5)

    assert measurements.get("energy") == 12.5
    assert measurements.has("energy")
    assert "energy" in measurements


def test_measurement_set_preserves_insertion_order():
    measurements = MeasurementSet()

    measurements.add("energy", 1)
    measurements.add("momentum", 2)

    assert measurements.names() == ["energy", "momentum"]
    assert measurements.items() == [("energy", 1), ("momentum", 2)]


def test_measurement_set_rejects_empty_name():
    measurements = MeasurementSet()

    with pytest.raises(ValueError):
        measurements.add("", 1)


def test_measurement_set_rejects_duplicate_name():
    measurements = MeasurementSet()
    measurements.add("energy", 1)

    with pytest.raises(ValueError):
        measurements.add("energy", 2)
