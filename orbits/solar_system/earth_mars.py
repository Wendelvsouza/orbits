from plot_orbits.plot import Plot
import json


class Orbits:
    def __init__(self) -> None:

        with open("settings.json") as json_file:
            variables = json.load(json_file)

        self.const = variables["const"]
        self.step_euler = variables["step_euler"]
        self.earth_euler = variables["earth_euler"]
        self.mars_euler = variables["mars_euler"]

        self.step_runge = variables["step_runge"]
        self.earth_runge = variables["earth_runge"]
        self.mars_runge = variables["mars_runge"]

    def apply_method(
        self,
        name,
        method_apply,
    ):
        if name == "euler":
            earth_x, earth_y, mars_x, mars_y = method_apply(
                self.const, self.step_euler, self.mars_euler, self.earth_euler
            )
        else:
            earth_x, earth_y, mars_x, mars_y = method_apply(
                self.const, self.step_runge, self.mars_runge, self.earth_runge
            )
        plot_euler = Plot()
        plot_euler.graph_force_grav(name, earth_x, earth_y, mars_x, mars_y)
