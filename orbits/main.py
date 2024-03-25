from methods_solution.euler_runge_kutta import (
    Orbits_euler_method,
    Orbits_runge_kutta_method,
)
from solar_system.earth_mars import Orbits

if __name__ == "__main__":

    orbits = Orbits()

    orbits_euler_method = Orbits_euler_method()

    orbits_runge_kutta_method = Orbits_runge_kutta_method()

    methods_dict = {
        "euler": orbits_euler_method.methods,
        "runge_kutta": orbits_runge_kutta_method.methods,
    }

    for name in ["euler", "runge_kutta"]:
        orbits.apply_method(name, methods_dict[name])
