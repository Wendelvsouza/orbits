from interface.methods import MethodsInterface


class shortcut:

    def div_calculator(self, distance_A, distance_B) -> float:

        div = ((distance_A) ** 2 + (distance_B) ** 2) ** (3 / 2)

        return div

    def acceleration_calculator(
        self, const, position_1, divisor_a, Gm_a, position_2, position_3, divisor_b
    ) -> float:

        acceleration = (
            -const * position_1 / divisor_a
            + Gm_a * (position_2 - position_3) / divisor_b
        )

        return acceleration

    def update_velocity_position(
        self,
        mars,
        earth,
        acceleration_ax,
        acceleration_ay,
        acceleration_bx,
        acceleration_by,
        step,
    ):
        earth["velocity_x_earth"] = earth["velocity_x_earth"] + acceleration_ax * step
        earth["velocity_y_earth"] = earth["velocity_y_earth"] + acceleration_ay * step

        mars["velocity_x_mars"] = mars["velocity_x_mars"] + acceleration_bx * step
        mars["velocity_y_mars"] = mars["velocity_y_mars"] + acceleration_by * step
        earth["x_earth"] = earth["x_earth"] + earth["velocity_x_earth"] * step
        earth["y_earth"] = earth["y_earth"] + earth["velocity_y_earth"] * step

        mars["x_mars"] = mars["x_mars"] + mars["velocity_x_mars"] * step
        mars["y_mars"] = mars["y_mars"] + mars["velocity_y_mars"] * step

    def update_velocity_position_2(
        self,
        mars,
        earth,
        acceleration_ax,
        acceleration_ay,
        acceleration_bx,
        acceleration_by,
        step,
    ):
        earth["velocity_x_earth"] = earth["velocity_x_earth0"] + acceleration_ax * step
        earth["velocity_y_earth"] = earth["velocity_y_earth0"] + acceleration_ay * step

        mars["velocity_x_mars"] = mars["velocity_x_mars0"] + acceleration_bx * step
        mars["velocity_y_mars"] = mars["velocity_y_mars0"] + acceleration_by * step

        earth["x_earth"] = earth["x_earth0"] + earth["velocity_x_earth"] * step
        mars["x_mars"] = mars["x_mars0"] + mars["velocity_x_mars"] * step

        earth["y_earth"] = earth["y_earth0"] + earth["velocity_y_earth"] * step
        mars["y_mars"] = mars["y_mars0"] + mars["velocity_y_mars"] * step

    def save_positions(self, earth, mars):

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


class Orbits_euler_method(MethodsInterface):
    shortcut_instance = shortcut()

    def methods(self, const, step, mars, earth) -> tuple:
        shortcut_instance = shortcut()
        for _ in range(19000):

            shortcut_instance.save_positions(earth, mars)

            div_a = shortcut_instance.div_calculator(earth["x_earth"], earth["y_earth"])
            div_b = shortcut_instance.div_calculator(mars["x_mars"], mars["y_mars"])
            div_a_b = shortcut_instance.div_calculator(
                mars["x_mars"] - earth["x_earth"], mars["y_mars"] - earth["y_earth"]
            )

            acceleration_ax = shortcut_instance.acceleration_calculator(
                const["GM"],
                earth["x_earth"],
                div_a,
                earth["Gm_a"],
                mars["x_mars"],
                earth["x_earth"],
                div_a_b,
            )
            acceleration_ay = shortcut_instance.acceleration_calculator(
                const["GM"],
                earth["y_earth"],
                div_a,
                earth["Gm_a"],
                mars["y_mars"],
                earth["y_earth"],
                div_a_b,
            )
            acceleration_bx = shortcut_instance.acceleration_calculator(
                const["GM"],
                mars["x_mars"],
                div_b,
                mars["Gm_b"],
                mars["x_mars"],
                earth["x_earth"],
                div_a_b,
            )
            acceleration_by = shortcut_instance.acceleration_calculator(
                const["GM"],
                mars["y_mars"],
                div_b,
                mars["Gm_b"],
                mars["y_mars"],
                earth["y_earth"],
                div_a_b,
            )

            shortcut_instance.update_velocity_position(
                mars,
                earth,
                acceleration_ax,
                acceleration_ay,
                acceleration_bx,
                acceleration_by,
                step["dt_euler"],
            )

        return shortcut_instance.save_positions(earth, mars)


class Orbits_runge_kutta_method(MethodsInterface):

    def methods(self, const, step, mars, earth) -> tuple:
        shortcut_instance = shortcut()

        for _ in range(358000):

            shortcut_instance.save_positions(earth, mars)

            div_a = shortcut_instance.div_calculator(earth["x_earth"], earth["y_earth"])
            div_b = shortcut_instance.div_calculator(mars["x_mars"], mars["y_mars"])
            div_a_b = shortcut_instance.div_calculator(
                mars["x_mars"] - earth["x_earth"], mars["y_mars"] - earth["y_earth"]
            )

            acceleration_ax = shortcut_instance.acceleration_calculator(
                const["GM"],
                earth["x_earth"],
                div_a,
                earth["Gm_a"],
                mars["x_mars"],
                earth["x_earth"],
                div_a_b,
            )
            acceleration_ay = shortcut_instance.acceleration_calculator(
                const["GM"],
                earth["y_earth"],
                div_a,
                earth["Gm_a"],
                mars["y_mars"],
                earth["y_earth"],
                div_a_b,
            )
            acceleration_bx = shortcut_instance.acceleration_calculator(
                const["GM"],
                mars["x_mars"],
                div_b,
                mars["Gm_b"],
                mars["x_mars"],
                earth["x_earth"],
                div_a_b,
            )
            acceleration_by = shortcut_instance.acceleration_calculator(
                const["GM"],
                mars["y_mars"],
                div_b,
                mars["Gm_b"],
                mars["y_mars"],
                earth["y_earth"],
                div_a_b,
            )

            shortcut_instance.update_velocity_position(
                mars,
                earth,
                acceleration_ax,
                acceleration_ay,
                acceleration_bx,
                acceleration_by,
                step["dt_runge_kutta"] / 2,
            )

            div_a = shortcut_instance.div_calculator(earth["x_earth"], earth["y_earth"])
            div_b = shortcut_instance.div_calculator(mars["x_mars"], mars["y_mars"])
            div_a_b = shortcut_instance.div_calculator(
                mars["x_mars"] - earth["x_earth"], mars["y_mars"] - earth["y_earth"]
            )

            acceleration_ax = shortcut_instance.acceleration_calculator(
                const["GM"],
                earth["x_earth"],
                div_a,
                earth["Gm_a"],
                mars["x_mars"],
                earth["x_earth"],
                div_a_b,
            )
            acceleration_ay = shortcut_instance.acceleration_calculator(
                const["GM"],
                earth["y_earth"],
                div_a,
                earth["Gm_a"],
                mars["y_mars"],
                earth["y_earth"],
                div_a_b,
            )
            acceleration_bx = shortcut_instance.acceleration_calculator(
                const["GM"],
                mars["x_mars"],
                div_b,
                mars["Gm_b"],
                mars["x_mars"],
                earth["x_earth"],
                div_a_b,
            )
            acceleration_by = shortcut_instance.acceleration_calculator(
                const["GM"],
                mars["y_mars"],
                div_b,
                mars["Gm_b"],
                mars["y_mars"],
                earth["y_earth"],
                div_a_b,
            )

            shortcut_instance.update_velocity_position_2(
                mars,
                earth,
                acceleration_ax,
                acceleration_ay,
                acceleration_bx,
                acceleration_by,
                step["dt_runge_kutta"],
            )

        return shortcut_instance.save_positions(earth, mars)
