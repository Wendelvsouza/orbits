from plot_orbits.plot import Plot
from typing import Dict, Union, List

import json


class Orbits:
    def __init__(self) -> None:
        """
        This is the constructor for the Orbits class.


        The attributes are filled in from a settings.json file which includes:

        Atributes:
        const: (Dict[str, float])
            A dictionary with the gravitational constant
            times the sun's mass - GM.

        step_euler: (Dict[str, float])
            A dictionary with the time step for
            the Euler method.

        earth_euler: (Dict[str, Union[float, list]])
            A dictionary with the initial positions, velocities, and an
            empty list to save the new positions and velocities of
            Mars for the Euler method.

        mars_euler: (Dict[str, Union[float, list]])
            dict with initiate positions, velocity and empty list to
            save new position and velocity to the mars planet to the
            method euler.


        step_runge: (Dict[str, float])
            A dictionary with the time step for the Runge-Kutta method.

        earth_runge: (Dict[str, Union[float, list]])
            A dictionary with initial positions, velocities, and an
            empty list to save the new positions and velocities of the
            Earth for the Runge-Kutta method.

        mars_runge: (Dict[str, Union[float, list]])
            A dictionary with initial positions, velocities, and an
            empty list to save the new positions and velocities of
            Mars for the Runge-Kutta method.
        """
        with open("orbits/settings.json") as json_file:
            variables: Dict[str, Union[float, list]] = json.load(json_file)

        self.const: Dict[str, float] = variables["const"]

        self.step_euler: Dict[str, float] = variables["step_euler"]
        self.earth_euler: Dict[str, Union[float, list]] = variables["earth_euler"]
        self.mars_euler: Dict[str, Union[float, list]] = variables["mars_euler"]

        self.step_runge: Dict[str, float] = variables["step_runge"]
        self.earth_runge: Dict[str, Union[float, list]] = variables["earth_runge"]
        self.mars_runge: Dict[str, Union[float, list]] = variables["mars_runge"]

    def apply_method(
        self,
        name: str,
        method_apply: Dict[str, callable],
    ) -> None:
        """
        Apply the methods accordingly with the received parameters and return
        lists that are used to call the graph_force method to generate the
        graphic related to the method."

        Parameters:

        name: (str)
                    Name of the orbit solution method to be applied.
                    'euler' or 'runge_kutta' is expected.
        method_apply: (Dict[str,str])
                    Dictionary that maps method names to corresponding class
                    instance methods.

        Atributes:

        earth_x: (List[float])
                    List of x coordinates for Earth returned by the method.
        earth_y: (List[float])
                    List of y coordinates for Earth returned by the method.
        mars_x: (List[float])
                    List of x coordinates for Mars returned by the method.
        mars_y: (List[float])
                    List of y coordinates  for Mars returned by the method.
        """

        earth_x: List[float]
        earth_y: List[float]
        mars_x: List[float]
        mars_y: List[float]

        if name == "euler":
            earth_x, earth_y, mars_x, mars_y = method_apply(
                const=self.const,
                step=self.step_euler,
                mars=self.mars_euler,
                earth=self.earth_euler,
            )
        else:
            earth_x, earth_y, mars_x, mars_y = method_apply(
                const=self.const,
                step=self.step_runge,
                mars=self.mars_runge,
                earth=self.earth_runge,
            )
        plot_euler = Plot()
        plot_euler.graph_force_grav(
            name=name, earth_x=earth_x, earth_y=earth_y, mars_x=mars_x, mars_y=mars_y
        )
