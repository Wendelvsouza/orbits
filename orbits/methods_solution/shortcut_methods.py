from typing import Dict, Union, Tuple


class Shortcut:

    def div_calculator(self, distance_A: float, distance_B: float) -> float:

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

        if id == 1:
            earth[x] = earth[y]
        else:
            mars[x] = mars[y]
