from manim import *
import os


# General Storyboard
# Short Clip of Showing Problem
# Short Clip of Solid Spinning
# Show this File
# Do a cut when it asks to cut & cut back
# Show off IRL model for like 1s at the end lol

class Solution(ThreeDScene):
    def construct(self):
        # Setting us Axes
        axes = ThreeDAxes(x_range=[-5, 5, 1], y_range=[-5, 5, 1], z_range=[-5, 5, 1])

        x_label = axes.get_x_axis_label(Tex("x"))
        y_label = axes.get_y_axis_label(Tex("y")).shift(UP * 1.8).rotate(3 * PI / 2)
        z_label = axes.get_z_axis_label(Tex("z"))

        self.set_camera_orientation(zoom=0.5)
        self.play(FadeIn(axes), FadeIn(x_label), FadeIn(y_label), FadeIn(z_label))
        self.wait(0.5)

        self.move_camera(phi=75 * DEGREES, theta=-75 * DEGREES, zoom=0.75, run_time=1.5)
        self.wait(0.5)

        plane1 = Surface(lambda u, v: np.array((0, u, v)), u_range=np.array((-4, 4)), v_range=np.array((-4, 4)),
                         checkerboard_colors=None, fill_opacity=0.3)
        plane2 = Surface(lambda u, v: np.array((4, u, v)), u_range=np.array((-4, 4)), v_range=np.array((-4, 4)),
                         checkerboard_colors=None, fill_opacity=0.3)

        self.play(FadeIn(plane1), FadeIn(plane2))

        self.wait(0.5)

        self.move_camera(phi=0, theta=-90 * DEGREES, zoom=0.5)

        # Draw Initial Function on 2D
        sqrt_x = ParametricFunction(lambda t: np.array((t, t ** 0.5, 0)), t_range=np.array([0, 4]), fill_opacity=0,
                                    color=BLUE)
        neg_sqrt_x = ParametricFunction(lambda t: np.array((t, -t ** 0.5, 0)), t_range=np.array([0, 4]), fill_opacity=0,
                                        color=BLUE)
        self.play(Write(sqrt_x), Write(neg_sqrt_x))

        self.wait(1.5)

        # Show off 3D
        self.move_camera(phi=75 * DEGREES, theta=-10 * DEGREES, zoom=0.75, run_time=1.5)

        self.wait(1)

        # Draw the Square's Diagonal
        diagonal = ParametricFunction(lambda t: np.array((4, t, 0)), t_range=np.array([-2, 2]), fill_opacity=0,
                                      color="#C83200")

        # TODO - do we need to show that the plane is perpendicular?

        self.play(Write(diagonal))
        self.wait(0.3)

        self.move_camera(phi=PI / 2, theta=0, zoom=0.75, run_time=1)

        # Draw the actual Square
        square = ParametricFunction(lambda t: np.array(
            (4, 2 * ((t - 1) if t < 2 else (3 - t)), 2 * ((t if t < 1 else ((2 - t) if t < 3 else (t - 4)))))),
                                    t_range=[0, 4], fill_opacity=0, color=BLUE)
        self.play(Write(square))
        self.wait(0.3)

        self.wait(1)

        self.play(FadeOut(plane1), FadeOut(plane2))

        g = VGroup(square, diagonal)

        self.play(FadeOut(axes), FadeOut(x_label), FadeOut(y_label), FadeOut(z_label), FadeOut(sqrt_x),
                  FadeOut(neg_sqrt_x), g.animate.set_color(WHITE))

        self.play(g.animate.rotate(45 * DEGREES, axis=RIGHT))

        self.wait(2)  # DO SOME MORE ANIMATION WORK HERE

        self.play(g.animate.rotate(-45 * DEGREES, axis=RIGHT))

        self.wait(0.5)  # DO A CUT HERE AND PLAY DIFFERENT ANIMATION OF finding A(x)

        self.play(FadeIn(axes), FadeIn(x_label), FadeIn(y_label), FadeIn(z_label), FadeIn(sqrt_x), FadeIn(neg_sqrt_x),
                  FadeOut(diagonal), square.animate.set_color(BLUE))
        self.move_camera(phi=75 * DEGREES, theta=-75 * DEGREES, zoom=0.75, run_time=1.5)

        self.wait(0.5)

        # Draw the other 2 Functions
        z_sqrt_x = ParametricFunction(lambda t: np.array((t, 0, t ** 0.5)), t_range=np.array([0, 4]), fill_opacity=0,
                                      color=BLUE)
        z_neg_sqrt_x = ParametricFunction(lambda t: np.array((t, 0, -t ** 0.5)), t_range=np.array([0, 4]),
                                          fill_opacity=0, color=BLUE)
        self.play(Write(z_sqrt_x), Write(z_neg_sqrt_x))

        self.wait(0.5)

        # TODO - make the shape better?
        # Draw the shape
        # t = u
        # x = v
        surface = Surface(lambda x, t: np.array(
            (x, x ** 0.5 * ((t - 1) if t < 2 else (3 - t)),
             (x ** 0.5) * (t if t < 1 else ((2 - t) if t < 3 else (t - 4))))), u_range=np.array([0, 4]),
                          v_range=np.array([0, 4]), should_make_jagged=True, resolution=(64, 64),
                          checkerboard_colors=None)
        sqrt_2_div_2 = 0.707106781
        surface2 = Surface(lambda u, v: np.array((4, (u - v) * sqrt_2_div_2, (u + v) * sqrt_2_div_2)),
                           u_range=np.array([-1.41421356, 1.41421356]), v_range=np.array([-1.41421356, 1.41421356]),
                           checkerboard_colors=None)

        self.play(Write(surface), Write(surface2))


if __name__ == "__main__":
    os.system(f"manim {__file__} -pqm")
