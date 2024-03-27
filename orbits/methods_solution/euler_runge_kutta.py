from interface.methods import MethodsInterface


class shortcut:

    def div_calculator(self, x_mars, y_mars, x_earth, y_earth) -> list:
        div_b = (x_mars**2 + y_mars**2) ** (3 / 2)
        div_a = (x_earth**2 + y_earth**2) ** (3 / 2)
        div_a_b = ((x_mars - x_earth) ** 2 + (y_mars - y_earth) ** 2) ** (3 / 2)

        return [div_a, div_b, div_a_b]

    def acceleration_calculator(
        self, const, mars, earth, div_a, div_b, div_a_b
    ) -> tuple:

        acceleration_ax = (
            -const["GM"] * earth["x_earth"] / div_a
            + earth["Gm_a"] * (mars["x_mars"] - earth["x_earth"]) / div_a_b
        )
        acceleration_ay = (
            -const["GM"] * earth["y_earth"] / div_a
            + earth["Gm_a"] * (mars["y_mars"] - earth["y_earth"]) / div_a_b
        )

        acceleration_bx = (
            -const["GM"] * mars["x_mars"] / div_b
            - mars["Gm_b"] * (mars["x_mars"] - earth["x_earth"]) / div_a_b
        )
        acceleration_by = (
            -const["GM"] * mars["y_mars"] / div_b
            - mars["Gm_b"] * (mars["y_mars"] - earth["y_earth"]) / div_a_b
        )

        return (acceleration_ax, acceleration_ay, acceleration_bx, acceleration_by)

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
        earth["velocity_x_earth"] += acceleration_ax * step
        earth["velocity_y_earth"] += acceleration_ay * step

        mars["velocity_x_mars"] += acceleration_bx * step
        mars["velocity_y_mars"] += acceleration_by * step
        earth["x_earth"] += earth["velocity_x_earth"] * step
        earth["y_earth"] += earth["velocity_y_earth"] * step

        mars["x_mars"] += mars["velocity_x_mars"] * step
        mars["y_mars"] += mars["velocity_y_mars"] * step

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
        for i in range(19000):

            shortcut_instance.save_positions(earth, mars)

            div_a, div_b, div_a_b = shortcut_instance.div_calculator(
                mars["x_mars"], mars["y_mars"], earth["x_earth"], earth["y_earth"]
            )

            acceleration_ax, acceleration_ay, acceleration_bx, acceleration_by = (
                shortcut_instance.acceleration_calculator(
                    const, mars, earth, div_a, div_b, div_a_b
                )
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

        for _ in range(358000):

            x_mars0 = mars["x_mars"]
            y_mars0 = mars["y_mars"]
            velocity_x_mars0 = mars["velocity_x_mars"]
            velocity_y_mars0 = mars["velocity_y_mars"]

            x_earth0 = earth["x_earth"]
            y_earth0 = earth["y_earth"]
            velocity_x_earth0 = earth["velocity_x_earth"]
            velocity_y_earth0 = earth["velocity_y_earth"]

            earth["new_position_earth_x"].append(earth["x_earth"])

            earth["new_position_earth_y"].append(earth["y_earth"])

            mars["new_position_mars_x"].append(mars["x_mars"])
            mars["new_position_mars_y"].append(mars["y_mars"])

            div_b = (mars["x_mars"] ** 2 + mars["y_mars"] ** 2) ** (3 / 2)
            div_a = (earth["x_earth"] ** 2 + earth["y_earth"] ** 2) ** (3 / 2)
            div_a_b = (
                (mars["x_mars"] - earth["x_earth"]) ** 2
                + (mars["y_mars"] - earth["y_earth"]) ** 2
            ) ** (3 / 2)

            acceleration_ax = (
                -const["GM"] * earth["x_earth"] / div_a
                + earth["Gm_a"] * (mars["x_mars"] - earth["x_earth"]) / div_a_b
            )
            acceleration_ay = (
                -const["GM"] * earth["y_earth"] / div_a
                + earth["Gm_a"] * (mars["y_mars"] - earth["y_earth"]) / div_a_b
            )

            acceleration_bx = (
                -const["GM"] * mars["x_mars"] / div_b
                - mars["Gm_b"] * (mars["x_mars"] - earth["x_earth"]) / div_a_b
            )
            acceleration_by = (
                -const["GM"] * mars["y_mars"] / div_b
                - mars["Gm_b"] * (mars["y_mars"] - earth["y_earth"]) / div_a_b
            )

            earth["velocity_x_earth"] += acceleration_ax * step["dt_runge_kutta"] / 2
            earth["velocity_y_earth"] += acceleration_ay * step["dt_runge_kutta"] / 2

            mars["velocity_x_mars"] += acceleration_bx * step["dt_runge_kutta"] / 2
            mars["velocity_y_mars"] += acceleration_by * step["dt_runge_kutta"] / 2

            earth["x_earth"] += earth["velocity_x_earth"] * step["dt_runge_kutta"] / 2
            mars["x_mars"] += mars["velocity_x_mars"] * step["dt_runge_kutta"] / 2

            earth["y_earth"] += earth["velocity_y_earth"] * step["dt_runge_kutta"] / 2
            mars["y_mars"] += mars["velocity_y_mars"] * step["dt_runge_kutta"] / 2

            div_b = (mars["x_mars"] ** 2 + mars["y_mars"] ** 2) ** (3 / 2)
            div_a = (earth["x_earth"] ** 2 + earth["y_earth"] ** 2) ** (3 / 2)
            div_a_b = (
                (mars["x_mars"] - earth["x_earth"]) ** 2
                + (mars["y_mars"] - earth["y_earth"]) ** 2
            ) ** (3 / 2)

            acceleration_ax = (
                -const["GM"] * earth["x_earth"] / div_a
                + earth["Gm_a"] * (mars["x_mars"] - earth["x_earth"]) / div_a_b
            )
            acceleration_ay = (
                -const["GM"] * earth["y_earth"] / div_a
                + earth["Gm_a"] * (mars["y_mars"] - earth["y_earth"]) / div_a_b
            )

            acceleration_bx = (
                -const["GM"] * mars["x_mars"] / div_b
                - mars["Gm_b"] * (mars["x_mars"] - earth["x_earth"]) / div_a_b
            )
            acceleration_by = (
                -const["GM"] * mars["y_mars"] / div_b
                - mars["Gm_b"] * (mars["y_mars"] - earth["y_earth"]) / div_a_b
            )

            earth["velocity_x_earth"] = (
                velocity_x_earth0 + acceleration_ax * step["dt_runge_kutta"]
            )
            earth["velocity_y_earth"] = (
                velocity_y_earth0 + acceleration_ay * step["dt_runge_kutta"]
            )

            mars["velocity_x_mars"] = (
                velocity_x_mars0 + acceleration_bx * step["dt_runge_kutta"]
            )
            mars["velocity_y_mars"] = (
                velocity_y_mars0 + acceleration_by * step["dt_runge_kutta"]
            )

            earth["x_earth"] = (
                x_earth0 + earth["velocity_x_earth"] * step["dt_runge_kutta"]
            )
            mars["x_mars"] = x_mars0 + mars["velocity_x_mars"] * step["dt_runge_kutta"]

            earth["y_earth"] = (
                y_earth0 + earth["velocity_y_earth"] * step["dt_runge_kutta"]
            )
            mars["y_mars"] = y_mars0 + mars["velocity_y_mars"] * step["dt_runge_kutta"]

        return (
            earth["new_position_earth_x"],
            earth["new_position_earth_y"],
            mars["new_position_mars_x"],
            mars["new_position_mars_y"],
        )
