from methods_solution.euler_runge_kutta import (
    OrbitsEulerMethod,
    OrbitsRungeKuttaMethod,
)
from solar_system.earth_mars import Orbits

if __name__ == "__main__":

    orbits = Orbits()

    OrbitsEulerMethod = OrbitsEulerMethod()

    OrbitsRungeKuttaMethod = OrbitsRungeKuttaMethod()

    methods_dict = {
        "euler": OrbitsEulerMethod.methods,
        "runge_kutta": OrbitsRungeKuttaMethod.methods,
    }

    for name in ["euler", "runge_kutta"]:
        orbits.apply_method(name, methods_dict[name])
