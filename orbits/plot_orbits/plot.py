import matplotlib.pyplot as plt


class Plot:

    def graph_force_grav(
        self,
        name: str,
        earth_x: list,
        earth_y: list,
        mars_x: list,
        mars_y: list,
    ) -> None:

        plt.figure()

        plt.plot(earth_x, earth_y, label="Earth")
        plt.plot(mars_x, mars_y, label="Mars")
        plt.title(f"Orbit_{name}")
        plt.xlabel("Position(x in 10**2meters)")
        plt.ylabel("Position(y in 10**2meters)")
        plt.legend()
        plt.savefig(f"method_{name}_orbit_plot.jpeg")
