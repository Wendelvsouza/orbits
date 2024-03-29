from interface.methods import MethodsInterface
from typing import Dict, Union


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

        acceleration = (
            -const * position_1 / divisor_a + gm * (position_2 - position_3) / divisor_b
        )

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
    ) -> tuple:

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


class OrbitsEulerMethod(MethodsInterface):

    def methods(
        self,
        const: Dict[str, float],
        step: Dict[str, float],
        mars: Dict[str, Union[float, list]],
        earth: Dict[str, Union[float, list]],
    ) -> tuple:
        shortcut = Shortcut()

        for _ in range(9000):

            shortcut.save_position_list(earth=earth, mars=mars)

            div_a = shortcut.div_calculator(
                distance_A=earth["x_earth"], distance_B=earth["y_earth"]
            )
            div_b = shortcut.div_calculator(
                distance_A=mars["x_mars"], distance_B=mars["y_mars"]
            )
            div_a_b = shortcut.div_calculator(
                distance_A=mars["x_mars"] - earth["x_earth"],
                distance_B=mars["y_mars"] - earth["y_earth"],
            )

            acceleration_ax = shortcut.acceleration_calculator(
                const=const["GM"],
                position_1=earth["x_earth"],
                divisor_a=div_a,
                gm=earth["Gm_a"],
                position_2=mars["x_mars"],
                position_3=earth["x_earth"],
                divisor_b=div_a_b,
            )

            acceleration_ay = shortcut.acceleration_calculator(
                const=const["GM"],
                position_1=earth["y_earth"],
                divisor_a=div_a,
                gm=earth["Gm_a"],
                position_2=mars["y_mars"],
                position_3=earth["y_earth"],
                divisor_b=div_a_b,
            )
            acceleration_bx = shortcut.acceleration_calculator(
                const=const["GM"],
                position_1=mars["x_mars"],
                divisor_a=div_b,
                gm=mars["Gm_b"],
                position_2=mars["x_mars"],
                position_3=earth["x_earth"],
                divisor_b=div_a_b,
            )
            acceleration_by = shortcut.acceleration_calculator(
                const=const["GM"],
                position_1=mars["y_mars"],
                divisor_a=div_b,
                gm=mars["Gm_b"],
                position_2=mars["y_mars"],
                position_3=earth["y_earth"],
                divisor_b=div_a_b,
            )

            shortcut.update_velocity_position(
                id=1,
                mars=mars,
                earth=earth,
                acceleration_ax=acceleration_ax,
                acceleration_ay=acceleration_ay,
                acceleration_bx=acceleration_bx,
                acceleration_by=acceleration_by,
                step=step["dt_euler"],
                var1="velocity_x_earth",
                var2="velocity_y_earth",
                var3="velocity_x_mars",
                var4="velocity_y_mars",
                var5="x_earth",
                var6="y_earth",
                var7="x_mars",
                var8="y_mars",
            )

        return shortcut.save_position_list(earth, mars)


class OrbitsRungeKuttaMethod(MethodsInterface):

    def methods(self, const, step, mars, earth) -> tuple:
        shortcut = Shortcut()

        for _ in range(89000):

            shortcut.save_variables(
                id=1, earth=earth, mars=mars, x="x_earth0", y="x_earth"
            )
            shortcut.save_variables(
                id=1, earth=earth, mars=mars, x="y_earth0", y="y_earth"
            )
            shortcut.save_variables(
                id=1,
                earth=earth,
                mars=mars,
                x="velocity_x_earth0",
                y="velocity_x_earth",
            )
            shortcut.save_variables(
                id=1,
                earth=earth,
                mars=mars,
                x="velocity_y_earth0",
                y="velocity_y_earth",
            )
            shortcut.save_variables(
                id=0, earth=earth, mars=mars, x="x_mars0", y="x_mars"
            )
            shortcut.save_variables(
                id=0, earth=earth, mars=mars, x="y_mars0", y="y_mars"
            )
            shortcut.save_variables(
                id=0, earth=earth, mars=mars, x="velocity_x_mars0", y="velocity_x_mars"
            )
            shortcut.save_variables(
                id=0, earth=earth, mars=mars, x="velocity_y_mars0", y="velocity_y_mars"
            )

            [
                earth["position_earth_x"],
                earth["position_earth_y"],
                mars["position_mars_x"],
                mars["position_mars_y"],
            ] = shortcut.save_position_list(earth=earth, mars=mars)

            div_a = shortcut.div_calculator(
                distance_A=earth["x_earth"], distance_B=earth["y_earth"]
            )

            div_b = shortcut.div_calculator(
                distance_A=mars["x_mars"], distance_B=mars["y_mars"]
            )
            div_a_b = shortcut.div_calculator(
                distance_A=mars["x_mars"] - earth["x_earth"],
                distance_B=mars["y_mars"] - earth["y_earth"],
            )

            acceleration_ax = shortcut.acceleration_calculator(
                const=const["GM"],
                position_1=earth["x_earth"],
                divisor_a=div_a,
                gm=earth["Gm_a"],
                position_2=mars["x_mars"],
                position_3=earth["x_earth"],
                divisor_b=div_a_b,
            )

            acceleration_ay = shortcut.acceleration_calculator(
                const=const["GM"],
                position_1=earth["y_earth"],
                divisor_a=div_a,
                gm=earth["Gm_a"],
                position_2=mars["y_mars"],
                position_3=earth["y_earth"],
                divisor_b=div_a_b,
            )
            acceleration_bx = shortcut.acceleration_calculator(
                const=const["GM"],
                position_1=mars["x_mars"],
                divisor_a=div_b,
                gm=mars["Gm_b"],
                position_2=mars["x_mars"],
                position_3=earth["x_earth"],
                divisor_b=div_a_b,
            )
            acceleration_by = shortcut.acceleration_calculator(
                const=const["GM"],
                position_1=mars["y_mars"],
                divisor_a=div_b,
                gm=mars["Gm_b"],
                position_2=mars["y_mars"],
                position_3=earth["y_earth"],
                divisor_b=div_a_b,
            )

            shortcut.update_velocity_position(
                id=1,
                mars=mars,
                earth=earth,
                acceleration_ax=acceleration_ax,
                acceleration_ay=acceleration_ay,
                acceleration_bx=acceleration_bx,
                acceleration_by=acceleration_by,
                step=step["dt_runge_kutta"] / 2,
                var1="velocity_x_earth",
                var2="velocity_y_earth",
                var3="velocity_x_mars",
                var4="velocity_y_mars",
                var5="x_earth",
                var6="y_earth",
                var7="x_mars",
                var8="y_mars",
            )

            div_a = shortcut.div_calculator(
                distance_A=earth["x_earth"], distance_B=earth["y_earth"]
            )

            div_b = shortcut.div_calculator(
                distance_A=mars["x_mars"], distance_B=mars["y_mars"]
            )
            div_a_b = shortcut.div_calculator(
                distance_A=mars["x_mars"] - earth["x_earth"],
                distance_B=mars["y_mars"] - earth["y_earth"],
            )

            acceleration_ax = shortcut.acceleration_calculator(
                const=const["GM"],
                position_1=earth["x_earth"],
                divisor_a=div_a,
                gm=earth["Gm_a"],
                position_2=mars["x_mars"],
                position_3=earth["x_earth"],
                divisor_b=div_a_b,
            )
            acceleration_ay = shortcut.acceleration_calculator(
                const=const["GM"],
                position_1=earth["y_earth"],
                divisor_a=div_a,
                gm=earth["Gm_a"],
                position_2=mars["y_mars"],
                position_3=earth["y_earth"],
                divisor_b=div_a_b,
            )
            acceleration_bx = shortcut.acceleration_calculator(
                const=const["GM"],
                position_1=mars["x_mars"],
                divisor_a=div_b,
                gm=mars["Gm_b"],
                position_2=mars["x_mars"],
                position_3=earth["x_earth"],
                divisor_b=div_a_b,
            )
            acceleration_by = shortcut.acceleration_calculator(
                const=const["GM"],
                position_1=mars["y_mars"],
                divisor_a=div_b,
                gm=mars["Gm_b"],
                position_2=mars["y_mars"],
                position_3=earth["y_earth"],
                divisor_b=div_a_b,
            )

            shortcut.update_velocity_position(
                id=0,
                mars=mars,
                earth=earth,
                acceleration_ax=acceleration_ax,
                acceleration_ay=acceleration_ay,
                acceleration_bx=acceleration_bx,
                acceleration_by=acceleration_by,
                step=step["dt_runge_kutta"],
                var1="velocity_x_earth",
                var2="velocity_y_earth",
                var3="velocity_x_mars",
                var4="velocity_y_mars",
                var5="x_earth",
                var6="y_earth",
                var7="x_mars",
                var8="y_mars",
                varA="velocity_x_earth0",
                varB="velocity_y_earth0",
                varC="velocity_x_mars0",
                varD="velocity_y_mars0",
                varE="x_earth0",
                varF="y_earth0",
                varG="x_mars0",
                varH="y_mars0",
            )

        return (
            earth["position_earth_x"],
            earth["position_earth_y"],
            mars["position_mars_x"],
            mars["position_mars_y"],
        )
