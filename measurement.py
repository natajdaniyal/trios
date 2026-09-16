"""
Measurement infrastructure.

This module stores named measured values without interpreting them.
It is intentionally independent from physics, simulation execution,
and educational logic.
"""


class MeasurementSet:
    """Ordered collection of named measurement values."""

    def __init__(self):
        self._values = {}

    def add(self, name, value):
        if not name:
            raise ValueError("Measurement name cannot be empty.")
        if name in self._values:
            raise ValueError(f"Measurement already exists: {name!r}.")

        self._values[name] = value
        return value

    def get(self, name):
        return self._values[name]

    def has(self, name):
        return name in self._values

    def items(self):
        return list(self._values.items())

    def values(self):
        return list(self._values.values())

    def names(self):
        return list(self._values.keys())

    def __len__(self):
        return len(self._values)

    def __contains__(self, name):
        return name in self._values

    def __repr__(self):
        return f"MeasurementSet(values={self._values!r})"
