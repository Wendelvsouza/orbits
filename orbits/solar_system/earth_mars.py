from plot_orbits.plot import Plot
import json


class Orbits:
    def __init__(self) -> None:

        # Abrindo e lendo o arquivo JSON
        with open("settings.json") as json_file:
            variables = json.load(json_file)

        # Agora a variável dados contém os dados do arquivo JSON e pode ser utilizada

        self.const = variables["const"]
        self.step = variables["step"]
        self.earth = variables["earth"]
        self.mars = variables["mars"]

    def apply_euler_method(self, euler_method):
        name = "euler"
        earth_x, earth_y, mars_x, mars_y = euler_method(
            self.const, self.step, self.mars, self.earth
        )
        plot_euler = Plot()
        plot_euler.graph_force_grav(name, earth_x, earth_y, mars_x, mars_y)

    def apply_runge_kutta_method(self, runge_kutta_method):
        name = "runge_kutta"
        earth_x, earth_y, mars_x, mars_y = runge_kutta_method(
            self.const, self.step, self.mars, self.earth
        )
        plot_runge = Plot()
        plot_runge.graph_force_grav(name, earth_x, earth_y, mars_x, mars_y)
