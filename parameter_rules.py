"""
Parameter / Selection Rules Layer (Architecture Layer 4).

Defines the rules for which physical parameter values are allowed in an
experiment. It does not store or modify physical configuration values.
"""

from math import isclose
from numbers import Real


class ParameterRule:
    """Rules governing one numeric physical parameter."""

    def __init__(self, name, editable, default, minimum=None, maximum=None, step=None):
        if not name:
            raise ValueError("ParameterRule requires a non-empty name.")
        if not isinstance(editable, bool):
            raise TypeError("editable must be a bool.")

        self.name = name
        self.editable = editable
        self.default = default
        self.minimum = minimum
        self.maximum = maximum
        self.step = step
        self._validate_definition()

    def _validate_definition(self):
        for field_name, value in (
            ("default", self.default),
            ("minimum", self.minimum),
            ("maximum", self.maximum),
            ("step", self.step),
        ):
            if value is not None and (
                not isinstance(value, Real) or isinstance(value, bool)
            ):
                raise TypeError(f"{field_name} must be a number or None.")

        if self.minimum is not None and self.maximum is not None and self.minimum > self.maximum:
            raise ValueError("minimum must be <= maximum.")
        if self.minimum is not None and self.default < self.minimum:
            raise ValueError("default must be >= minimum.")
        if self.maximum is not None and self.default > self.maximum:
            raise ValueError("default must be <= maximum.")
        if self.step is not None and self.step <= 0:
            raise ValueError("step must be > 0.")

    def is_editable(self):
        return self.editable

    def validate(self, value):
        if not isinstance(value, Real) or isinstance(value, bool):
            raise ValueError(f"Invalid value for parameter '{self.name}'.")
        if not self.editable and not isclose(value, self.default):
            raise ValueError(
                f"Parameter '{self.name}' is fixed and must remain at its default value."
            )
        if self.minimum is not None and value < self.minimum:
            raise ValueError(f"Value for '{self.name}' is below minimum.")
        if self.maximum is not None and value > self.maximum:
            raise ValueError(f"Value for '{self.name}' is above maximum.")
        if self.step is not None:
            origin = self.minimum if self.minimum is not None else self.default
            steps = (value - origin) / self.step
            if not isclose(steps, round(steps)):
                raise ValueError(f"Value for '{self.name}' does not match step.")
        return True

    def __repr__(self):
        return (
            f"ParameterRule(name={self.name!r}, editable={self.editable!r}, "
            f"default={self.default!r}, minimum={self.minimum!r}, "
            f"maximum={self.maximum!r}, step={self.step!r})"
        )


class SelectionRules:
    """Ordered collection of ParameterRule objects for one configuration."""

    def __init__(self):
        self._rules = {}

    def add_rule(self, rule):
        if not isinstance(rule, ParameterRule):
            raise TypeError("add_rule expects a ParameterRule instance.")
        if rule.name in self._rules:
            raise ValueError(f"A rule named '{rule.name}' already exists.")
        self._rules[rule.name] = rule
        return rule

    def get_rule(self, name):
        return self._rules.get(name)

    def has_rule(self, name):
        return name in self._rules

    def rules(self):
        return list(self._rules.values())

    def __len__(self):
        return len(self._rules)

    def __contains__(self, name):
        return name in self._rules
