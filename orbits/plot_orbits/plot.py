import matplotlib.pyplot as plt


class Plot:
    """
    This class creates a plot using the received parameters.

    '''

    Parameters
    ----------
    name : str
        The name of the method used (either Euler or Runge-Kutta).
    earth_x : list
        A list containing the positions of Earth on the X-axis.
    earth_y : list
        A list containing the positions of Earth on the Y-axis.
    mars_x : list
        A list containing the positions of Mars on the X-axis.
    mars_y : list
        A list containing the positions of Mars on the Y-axis.
    """

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
