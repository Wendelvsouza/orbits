import matplotlib.pyplot as plt


class Plot:

    def graph_force_grav(
        self,
        name,
        terra_x,
        terra_y,
        mars_x,
        mars_y,
    ):

        plt.figure()

        plt.plot(terra_x, terra_y, label="Earth")
        plt.plot(mars_x, mars_y, label="Mars")
        plt.title(f"Orbit_{name}")
        plt.xlabel("Position(x in 10**2meters)")
        plt.ylabel("Position(y in 10**2meters)")
        plt.legend()
        plt.savefig(f"method_{name}_orbit_plot.jpeg")
