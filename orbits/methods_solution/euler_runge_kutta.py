from interface.methods import MethodsInterface


class Orbits_euler_method(MethodsInterface):

    def methods(self, const, step, mars, earth) -> list:
        for i in range(19000):
            earth["pos_a_x"].append(earth["x_a"])
            earth["pos_a_y"].append(earth["y_a"])

            mars["pos_b_x"].append(mars["x_b"])
            mars["pos_b_y"].append(mars["y_b"])

            div_b = (mars["x_b"] ** 2 + mars["y_b"] ** 2) ** (3 / 2)
            div_a = (earth["x_a"] ** 2 + earth["y_a"] ** 2) ** (3 / 2)
            div_a_b = (
                (mars["x_b"] - earth["x_a"]) ** 2 + (mars["y_b"] - earth["y_a"]) ** 2
            ) ** (3 / 2)

            acceleration_ax = (
                -const["GM"] * earth["x_a"] / div_a
                + earth["Gm_a"] * (mars["x_b"] - earth["x_a"]) / div_a_b
            )
            acceleration_ay = (
                -const["GM"] * earth["y_a"] / div_a
                + earth["Gm_a"] * (mars["y_b"] - earth["y_a"]) / div_a_b
            )

            acceleration_bx = (
                -const["GM"] * mars["x_b"] / div_b
                - mars["Gm_b"] * (mars["x_b"] - earth["x_a"]) / div_a_b
            )
            acceleration_by = (
                -const["GM"] * mars["y_b"] / div_b
                - mars["Gm_b"] * (mars["y_b"] - earth["y_a"]) / div_a_b
            )

            earth["vx_a"] += acceleration_ax * step["dt_euler"]
            earth["vy_a"] += acceleration_ay * step["dt_euler"]

            mars["vx_b"] += acceleration_bx * step["dt_euler"]
            mars["vy_b"] += acceleration_by * step["dt_euler"]

            earth["x_a"] += earth["vx_a"] * step["dt_euler"]
            earth["y_a"] += earth["vy_a"] * step["dt_euler"]

            mars["x_b"] += mars["vx_b"] * step["dt_euler"]
            mars["y_b"] += mars["vy_b"] * step["dt_euler"]

        return (
            earth["pos_a_x"],
            earth["pos_a_y"],
            mars["pos_b_x"],
            mars["pos_b_y"],
        )


class Orbits_runge_kutta_method(MethodsInterface):

    def methods(self, const, step, mars, earth) -> list:

        for _ in range(358000):

            x_b0 = mars["x_b"]
            y_b0 = mars["y_b"]
            vx_b0 = mars["vx_b"]
            vy_b0 = mars["vy_b"]

            x_a0 = earth["x_a"]
            y_a0 = earth["y_a"]
            vx_a0 = earth["vx_a"]
            vy_a0 = earth["vy_a"]

            earth["pos_c_x"].append(earth["x_a"])

            earth["pos_c_y"].append(earth["y_a"])

            mars["pos_d_x"].append(mars["x_b"])
            mars["pos_d_y"].append(mars["y_b"])

            div_b = (mars["x_b"] ** 2 + mars["y_b"] ** 2) ** (3 / 2)
            div_a = (earth["x_a"] ** 2 + earth["y_a"] ** 2) ** (3 / 2)
            div_a_b = (
                (mars["x_b"] - earth["x_a"]) ** 2 + (mars["y_b"] - earth["y_a"]) ** 2
            ) ** (3 / 2)

            acceleration_ax = (
                -const["GM"] * earth["x_a"] / div_a
                + earth["Gm_a"] * (mars["x_b"] - earth["x_a"]) / div_a_b
            )
            acceleration_ay = (
                -const["GM"] * earth["y_a"] / div_a
                + earth["Gm_a"] * (mars["y_b"] - earth["y_a"]) / div_a_b
            )

            acceleration_bx = (
                -const["GM"] * mars["x_b"] / div_b
                - mars["Gm_b"] * (mars["x_b"] - earth["x_a"]) / div_a_b
            )
            acceleration_by = (
                -const["GM"] * mars["y_b"] / div_b
                - mars["Gm_b"] * (mars["y_b"] - earth["y_a"]) / div_a_b
            )

            earth["vx_a"] += acceleration_ax * step["dt_runge_kutta"] / 2
            earth["vy_a"] += acceleration_ay * step["dt_runge_kutta"] / 2

            mars["vx_b"] += acceleration_bx * step["dt_runge_kutta"] / 2
            mars["vy_b"] += acceleration_by * step["dt_runge_kutta"] / 2

            earth["x_a"] += earth["vx_a"] * step["dt_runge_kutta"] / 2
            mars["x_b"] += mars["vx_b"] * step["dt_runge_kutta"] / 2

            earth["y_a"] += earth["vy_a"] * step["dt_runge_kutta"] / 2
            mars["y_b"] += mars["vy_b"] * step["dt_runge_kutta"] / 2

            div_b = (mars["x_b"] ** 2 + mars["y_b"] ** 2) ** (3 / 2)
            div_a = (earth["x_a"] ** 2 + earth["y_a"] ** 2) ** (3 / 2)
            div_a_b = (
                (mars["x_b"] - earth["x_a"]) ** 2 + (mars["y_b"] - earth["y_a"]) ** 2
            ) ** (3 / 2)

            acceleration_ax = (
                -const["GM"] * earth["x_a"] / div_a
                + earth["Gm_a"] * (mars["x_b"] - earth["x_a"]) / div_a_b
            )
            acceleration_ay = (
                -const["GM"] * earth["y_a"] / div_a
                + earth["Gm_a"] * (mars["y_b"] - earth["y_a"]) / div_a_b
            )

            acceleration_bx = (
                -const["GM"] * mars["x_b"] / div_b
                - mars["Gm_b"] * (mars["x_b"] - earth["x_a"]) / div_a_b
            )
            acceleration_by = (
                -const["GM"] * mars["y_b"] / div_b
                - mars["Gm_b"] * (mars["y_b"] - earth["y_a"]) / div_a_b
            )

            earth["vx_a"] = vx_a0 + acceleration_ax * step["dt_runge_kutta"]
            earth["vy_a"] = vy_a0 + acceleration_ay * step["dt_runge_kutta"]

            mars["vx_b"] = vx_b0 + acceleration_bx * step["dt_runge_kutta"]
            mars["vy_b"] = vy_b0 + acceleration_by * step["dt_runge_kutta"]

            earth["x_a"] = x_a0 + earth["vx_a"] * step["dt_runge_kutta"]
            mars["x_b"] = x_b0 + mars["vx_b"] * step["dt_runge_kutta"]

            earth["y_a"] = y_a0 + earth["vy_a"] * step["dt_runge_kutta"]
            mars["y_b"] = y_b0 + mars["vy_b"] * step["dt_runge_kutta"]

        return (
            earth["pos_c_x"],
            earth["pos_c_y"],
            mars["pos_d_x"],
            mars["pos_d_y"],
        )
