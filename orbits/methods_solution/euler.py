from interface.methods import MethodsInterface
from typing import Dict, Union, Tuple
from methods_solution.shortcut_methods import Shortcut


class OrbitsEulerMethod(MethodsInterface):

    def call(
        self,
        const: Dict[str, float],
        step: Dict[str, float],
        mars: Dict[str, Union[float, list]],
        earth: Dict[str, Union[float, list]],
    ) -> Tuple[float]:
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
