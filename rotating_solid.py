import os

from manim import *


class RotatingSolid(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(x_range=[-5, 5, 1], y_range=[-5, 5, 1], z_range=[-5, 5, 1])

        x_label = axes.get_x_axis_label(Tex("x"))
        y_label = axes.get_y_axis_label(Tex("y")).shift(UP * 1.8).rotate(3 * PI / 2)
        z_label = axes.get_z_axis_label(Tex("z"))

        self.set_camera_orientation(zoom=0.5)
        self.play(FadeIn(axes), FadeIn(x_label), FadeIn(y_label), FadeIn(z_label))

        self.move_camera(phi=75 * DEGREES, theta=-110 * DEGREES, zoom=0.75, run_time=1.5)
        self.begin_ambient_camera_rotation(rate=0.2)

        self.wait(0.5)

        sqrt_x = ParametricFunction(lambda t: np.array((t, t ** 0.5, 0)), t_range=np.array([0, 4]), fill_opacity=0,
                                    color=BLUE).set_shade_in_3d(True)
        neg_sqrt_x = ParametricFunction(lambda t: np.array((t, -t ** 0.5, 0)), t_range=np.array([0, 4]), fill_opacity=0,
                                        color=BLUE).set_shade_in_3d(True)
        z_sqrt_x = ParametricFunction(lambda t: np.array((t, 0, t ** 0.5)), t_range=np.array([0, 4]), fill_opacity=0,
                                      color=BLUE).set_shade_in_3d(True)
        z_neg_sqrt_x = ParametricFunction(lambda t: np.array((t, 0, -t ** 0.5)), t_range=np.array([0, 4]),
                                          fill_opacity=0, color=BLUE).set_shade_in_3d(True)

        self.play(Write(sqrt_x), Write(neg_sqrt_x), Write(z_sqrt_x), Write(z_neg_sqrt_x))

        square = ParametricFunction(lambda t: np.array(
            (4, 2 * ((t - 1) if t < 2 else (3 - t)), 2 * ((t if t < 1 else ((2 - t) if t < 3 else (t - 4)))))),
                                    t_range=[0, 4], fill_opacity=0, color=BLUE).set_shade_in_3d(True)
        self.play(Write(square))

        self.wait(0.5)

        surface = Surface(lambda x, t: np.array(
            (x, x ** 0.5 * ((t - 1) if t < 2 else (3 - t)),
             (x ** 0.5) * (t if t < 1 else ((2 - t) if t < 3 else (t - 4))))), u_range=np.array([0, 4]),
                          v_range=np.array([0, 4]), should_make_jagged=True, resolution=(64, 64),
                          checkerboard_colors=None)

        sqrt_2_div_2 = 0.707106781
        surface2 = Surface(lambda u, v: np.array((4, (u - v) * sqrt_2_div_2, (u + v) * sqrt_2_div_2)),
                           u_range=np.array([-1.41421356, 1.41421356]), v_range=np.array([-1.41421356, 1.41421356]), checkerboard_colors=None)
        self.play(Write(surface), Write(surface2))

        self.wait(40)


if __name__ == "__main__":
    os.system(f"manim {__file__} -pqk")
