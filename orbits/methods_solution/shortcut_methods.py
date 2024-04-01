from typing import Dict, Union, Tuple


class Shortcut:
    """
    This class is a shortcut to perform the mathematical calculations of each
    method.

    Methods:
        div_calculator(distance_A: float,distance_B: float)
            Calculates the division result of two distances.

        acceleration_calculator(
            self,
            const: float,
            position_1: float,
            divisor_a: float,
            gm: float,
            position_2: float,
            position_3: float,
            divisor_b: float,
        ) -> float:
            Calculates the acceleration based on the given parameters.

        update_velocity_position(
            self,
            id: int,
            mars: Dict[str, Union[float, list]],
            earth: Dict[str, Union[float, list]],
            acceleration_ax: float,
            acceleration_ay: float,
            acceleration_bx: float,
            acceleration_by: float,
            step: float,
            var1: str,
            var2: str,
            var3: str,
            var4: str,
            var5: str,
            var6: str,
            var7: str,
            var8: str,
            **kwargs
        )
            Updates the velocity and position of the planets.

        save_position_list(
            self,
            earth: Dict[str, Union[float, list]],
            mars: Dict[str, Union[float, list]]
        )
            Stores and returns the positions of Mars and Earth.

        save_variables(
            self,
            id: int,
            earth: Dict[str, Union[float, list]],
            mars: Dict[str, Union[float, list]],
            x: str,
            y: str,
        )
            Saves the given variables depending on the given ID.
    """

    def div_calculator(self, distance_A: float, distance_B: float) -> float:
        """
        Calculates the specific mathematical expression incorporating two
        distances.

            distance_A: float
                Position of the Earth planet
            distance_B: float
                Position of the Mars planet

        Returns:
            Calculated value as per the formula, which is a float.
        """

        div = ((distance_A) ** 2 + (distance_B) ** 2) ** (3 / 2)

        return div

    def acceleration_calculator(
        self,
        const: float,
        position_1: float,
        divisor_a: float,
        gm: float,
        position_2: float,
        position_3: float,
        divisor_b: float,
    ) -> float:
        """
        Calculates acceleration based on input parameters and a
        predetermined formula.

        Parameters:
            const: float
                Represents a gravitational constant in the calculation.

            position_1, position_2, position_3: float
                Represent coordinates involved in the calculation.

            divisor_a, divisor_b: float
                Represent distances involved in the calculation.

            gm: float
                The variable gm represents the product of the gravitational
                constant and the mass of the planets Earth or Mars.

        Returns:
            Computed acceleration value as a float.

            Raises:
            ZeroDivisionError if any of the denominators are zero.
        """

        try:
            acceleration = (
                -const * position_1 / divisor_a
                + gm * (position_2 - position_3) / divisor_b
            )
        except ZeroDivisionError:
            print("Cannot divide by zero")
        return acceleration

    def update_velocity_position(
        self,
        id: int,
        mars: Dict[str, Union[float, list]],
        earth: Dict[str, Union[float, list]],
        acceleration_ax: float,
        acceleration_ay: float,
        acceleration_bx: float,
        acceleration_by: float,
        step: float,
        var1: str,
        var2: str,
        var3: str,
        var4: str,
        var5: str,
        var6: str,
        var7: str,
        var8: str,
        **kwargs
    ) -> None:
        """
        This function updates the positions and velocities of the Earth and
        Mars.

        Parameters:
            id: int
                An identifier which determines how the other inputs are
                processed.
            mars, earth: Dict[str, Union[float,list]]
                These are dictionaries representing the respective planets.
                acceleration_ax, acceleration_ay (floats): Accelerations of Earth
                along the x and y axis respectively.

            acceleration_bx, acceleration_by (floats):
                Accelerations of Mars along the x and y axis respectively.

            step (float):
                This represents the discrete time step in the
                calculation.

            var1, var2, var3, var4, var5, var6, var7, var8 (strs):
                Variables which are part of the calculation for position
                and velocity update.

            **kwargs:
                A dictionary containing any additional variables
                required. If "id" is not 1, these variables will be fetched
                from kwargs.
        """

        if id == 1:
            varA = var1
            varB = var2
            varC = var3
            varD = var4
            varE = var5
            varF = var6
            varG = var7
            varH = var8

        else:

            varA = kwargs["varA"]
            varB = kwargs["varB"]
            varC = kwargs["varC"]
            varD = kwargs["varD"]
            varE = kwargs["varE"]
            varF = kwargs["varF"]
            varG = kwargs["varG"]
            varH = kwargs["varH"]

        earth[var1] = earth[varA] + acceleration_ax * step
        earth[var2] = earth[varB] + acceleration_ay * step

        mars[var3] = mars[varC] + acceleration_bx * step
        mars[var4] = mars[varD] + acceleration_by * step

        earth[var5] = earth[varE] + earth[var1] * step
        earth[var6] = earth[varF] + earth[var2] * step

        mars[var7] = mars[varG] + mars[var3] * step
        mars[var8] = mars[varH] + mars[var4] * step

    def save_position_list(
        self, earth: Dict[str, Union[float, list]], mars: Dict[str, Union[float, list]]
    ) -> Tuple[float]:
        """
        Updates the lists of positions for the Earth and Mars planets and returns a tuple with these lists.

        Parameters:
            earth (dict):
                A dictionary representing Earth, containing current x, y
                coordinates and lists to store the history of these
                positions.

            mars (dict):
                A dictionary representing Mars, containing current x, y
                coordinates and lists to store the history of these
                positions.

        Returns:
                A tuple containing four lists that represent the
                positional history x and y for Earth and Mars, in that
                order.
        """

        earth["position_earth_x"].append(earth["x_earth"])

        earth["position_earth_y"].append(earth["y_earth"])
        mars["position_mars_x"].append(mars["x_mars"])
        mars["position_mars_y"].append(mars["y_mars"])

        return (
            earth["position_earth_x"],
            earth["position_earth_y"],
            mars["position_mars_x"],
            mars["position_mars_y"],
        )

    def save_variables(
        self,
        id: int,
        earth: Dict[str, Union[float, list]],
        mars: Dict[str, Union[float, list]],
        x: str,
        y: str,
    ) -> None:
        """
        Stores the value of a variable from the earth or mars dictionaries
        into another variable in the same dictionary based on the given id.

        Parameters:
            id (int):
                An identifier which determines whether to perform the operation
                on 'earth' or 'mars'. If id is 1, the operation will be performed
                on 'earth', otherwise it will be performed on 'mars'.

            earth (dict):
                A dictionary representing Earth, with its attributes represented
                as key-value pairs.

            mars (dict):
                A dictionary representing Mars, with its attributes
                represented as key-value pairs.

            x (str):
                The key in the dictionary where the value should be stored.

            y (str):
                The key in the dictionary which value should be copied.
        """
        if id == 1:
            earth[x] = earth[y]
        else:
            mars[x] = mars[y]
