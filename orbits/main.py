from methods_solution.euler import OrbitsEulerMethod
from methods_solution.runge_kutta import OrbitsRungeKuttaMethod

from solar_system.earth_mars import Orbits

if __name__ == "__main__":

    orbits = Orbits()

    OrbitsEulerMethod = OrbitsEulerMethod()

    OrbitsRungeKuttaMethod = OrbitsRungeKuttaMethod()

    methods_dict = {
        "euler": OrbitsEulerMethod.call,
        "runge_kutta": OrbitsRungeKuttaMethod.call,
    }

    for name in ["euler", "runge_kutta"]:
        orbits.apply_method(
            name, methods_dict[name]
        )  # Loop to apply Euler's method and the RK method
