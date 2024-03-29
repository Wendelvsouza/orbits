from interface.methods import MethodsInterface
from methods_solution.shortcut_methods import Shortcut
from typing import Tuple


class OrbitsRungeKuttaMethod(MethodsInterface):

    def call(self, const, step, mars, earth) -> Tuple[float]:
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

        return shortcut.save_position_list(earth, mars)
