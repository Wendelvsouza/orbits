from methods_solution.euler_runge_kutta import (
    Orbits_euler_method,
    Orbits_runge_kutta_method,
)
from solar_system.earth_mars import Orbits

if __name__ == "__main__":

    orbits = Orbits()

    orbits_euler_method = Orbits_euler_method()

    orbits_runge_kutta_method = Orbits_runge_kutta_method()

    orbits.apply_euler_method(orbits_euler_method.methods)

    orbits.apply_runge_kutta_method(orbits_runge_kutta_method.methods)
