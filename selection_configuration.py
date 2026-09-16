"""
Selection / Physical Configuration bridge.

Applies validated parameter selections to a physical configuration without
adding selection-rule concepts to the Physical Configuration layer.
"""

from physical_configuration import BodyPhysicalConfiguration, StagePhysicalConfiguration
from parameter_rules import SelectionRules


_PARAMETER_FIELDS = {
    "mass",
    "position_x",
    "position_y",
    "velocity_x",
    "velocity_y",
}


def configuration_from_selection(configuration, rules, selections=None):
    """Return a new physical configuration using validated selections.

    Unselected parameters keep their existing physical values. Every supplied
    selection must have a corresponding rule and pass that rule's validation.
    """

    if not isinstance(configuration, StagePhysicalConfiguration):
        raise TypeError("configuration must be a StagePhysicalConfiguration instance.")

    if not isinstance(rules, SelectionRules):
        raise TypeError("rules must be a SelectionRules instance.")

    if selections is None:
        selections = {}

    if not isinstance(selections, dict):
        raise TypeError("selections must be a dictionary.")

    result = StagePhysicalConfiguration(stage_name=configuration.stage_name)

    for body in configuration.bodies():
        values = body.as_dict()
        for parameter_name, value in selections.items():
            parts = parameter_name.split(".", 1)
            if len(parts) != 2 or parts[0] != body.name or parts[1] not in _PARAMETER_FIELDS:
                continue
            rule = rules.get_rule(parameter_name)
            if rule is None:
                raise ValueError(f"No selection rule exists for '{parameter_name}'.")
            rule.validate(value)
            values[parts[1]] = value

        result.add_body(
            BodyPhysicalConfiguration(
                name=values["name"],
                mass=values["mass"],
                position_x=values["position_x"],
                position_y=values["position_y"],
                velocity_x=values["velocity_x"],
                velocity_y=values["velocity_y"],
            )
        )

    return result
