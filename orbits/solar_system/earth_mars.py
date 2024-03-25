from plot_orbits.plot import Plot
import json


class Orbits:
    def __init__(self) -> None:

        with open("settings.json") as json_file:
            variables = json.load(json_file)

        self.const = variables["const"]
        self.step = variables["step"]
        self.earth = variables["earth"]
        self.mars = variables["mars"]

    def apply_method(
        self,
        name,
        method_apply,
    ):
        earth_x, earth_y, mars_x, mars_y = method_apply(
            self.const, self.step, self.mars, self.earth
        )
        plot_euler = Plot()
        plot_euler.graph_force_grav(name, earth_x, earth_y, mars_x, mars_y)
