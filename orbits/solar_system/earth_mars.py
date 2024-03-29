from plot_orbits.plot import Plot
from typing import Dict, Union, List

import json


class Orbits:
    def __init__(self) -> None:

        with open("settings.json") as json_file:
            variables: Dict[str, Union[float, list]] = json.load(json_file)

        self.const: Dict[str, float] = variables["const"]

        self.step_euler: Dict[str, float] = variables["step_euler"]
        self.earth_euler: Dict[str, Union[float, list]] = variables["earth_euler"]
        self.mars_euler: Dict[str, Union[float, list]] = variables["mars_euler"]

        self.step_runge: Dict[str, float] = variables["step_runge"]
        self.earth_runge: Dict[str, Union[float, list]] = variables["earth_runge"]
        self.mars_runge: Dict[str, Union[float, list]] = variables["mars_runge"]

    def apply_method(
        self,
        name: str,
        method_apply: dict,
    ) -> None:
        earth_x: List[float]
        earth_y: List[float]
        mars_x: List[float]
        mars_y: List[float]

        if name == "euler":
            earth_x, earth_y, mars_x, mars_y = method_apply(
                const=self.const,
                step=self.step_euler,
                mars=self.mars_euler,
                earth=self.earth_euler,
            )
        else:
            earth_x, earth_y, mars_x, mars_y = method_apply(
                const=self.const,
                step=self.step_runge,
                mars=self.mars_runge,
                earth=self.earth_runge,
            )
        plot_euler = Plot()
        plot_euler.graph_force_grav(
            name=name, earth_x=earth_x, earth_y=earth_y, mars_x=mars_x, mars_y=mars_y
        )
