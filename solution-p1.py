from manim import *
import os


class FinalSolutionP1(ThreeDScene):
    def construct(self):
        # Setting up Axes
        axes = ThreeDAxes(x_range=[-5, 5, 1], y_range=[-5, 5, 1], z_range=[-5, 5, 1])

        x_label = axes.get_x_axis_label(Tex("x"))
        y_label = axes.get_y_axis_label(Tex("y")).shift(UP * 1.8).rotate(3 * PI / 2)
        z_label = axes.get_z_axis_label(Tex("z")).rotate(PI / 2).shift([-0.3, 0.5, 0])

        self.set_camera_orientation(zoom=0.5)
        self.play(FadeIn(axes), FadeIn(x_label), FadeIn(y_label), FadeIn(z_label))
        self.wait(0.5)

        # Draw Initial Function on 2D
        sqrt_x = ParametricFunction(lambda t: np.array((t, t ** 0.5, 0)), t_range=np.array([0, 4]), fill_opacity=0,
                                    color=BLUE)

        sqrt_x_label = Tex(r"$y = \sqrt{x}$").move_to([2, 2.5, 0])

        neg_sqrt_x = ParametricFunction(lambda t: np.array((t, -t ** 0.5, 0)), t_range=np.array([0, 4]), fill_opacity=0,
                                        color=BLUE)
        neg_sqrt_x_label = Tex(r"$y = -\sqrt{x}$").move_to([2, -2.5, 0])

        self.play(Write(sqrt_x), Write(neg_sqrt_x), FadeIn(sqrt_x_label), FadeIn(neg_sqrt_x_label))

        self.wait(1)

        # Draw Vertical Lines
        x_0 = Dot3D([2.3, 0, 0])
        x_0_label = Tex("$x_0$").move_to([1.7, 0.5, 0])
        self.play(FadeIn(x_0), FadeIn(x_0_label))

        self.wait(0.5)

        upper_func = ParametricFunction(lambda t: np.array((2.3, t, 0)), t_range=np.array([0, 1.51657509]),
                                        fill_opacity=0, color="#C83200")
        lower_func = ParametricFunction(lambda t: np.array((2.3, -t, 0)), t_range=np.array([0, 1.51657509]),
                                        fill_opacity=0, color="#C83200")

        self.play(Write(upper_func), Write(lower_func), FadeOut(x_0))

        self.wait(0.5)

        # Get Diagonal Length
        x_0_label_c = x_0_label.copy()
        line_len_top = Tex(r"$\sqrt{x_0}$").move_to([3, 0.70, 0])
        line_len_bottom = Tex(r"$\sqrt{x_0}$").move_to([3, -0.70, 0])

        self.play(ReplacementTransform(x_0_label, line_len_top), ReplacementTransform(x_0_label_c, line_len_bottom))

        self.wait(0.5)

        line_len_total = Tex(r"$2\sqrt{x_0}$").move_to([3.1, 0.7, 0])
        self.play(line_len_bottom.animate.move_to([3, 0.70, 0]))
        self.remove(line_len_bottom)
        self.play(TransformMatchingShapes(line_len_top, line_len_total))

        self.wait(0.5)

        # Draw Square
        self.move_camera(phi=75 * DEGREES, theta=-10 * DEGREES, zoom=0.75, run_time=1.5)
        self.play(FadeOut(sqrt_x_label), FadeOut(neg_sqrt_x_label), FadeOut(line_len_total))

        square = ParametricFunction(lambda t: np.array(
            (2.3, 1.51657509 * ((t - 1) if t < 2 else (3 - t)),
             1.51657509 * (t if t < 1 else ((2 - t) if t < 3 else (t - 4))))), t_range=[0, 4], fill_opacity=0,
                                    color=WHITE).set_shade_in_3d(True)

        self.play(Write(square))

        temp_remove = VGroup(axes, neg_sqrt_x, sqrt_x, x_label, y_label, z_label)
        diagonal = VGroup(upper_func, lower_func)

        square_group = VGroup(square, diagonal)

        self.wait(0.5)
        self.move_camera(phi=PI / 2, theta=0, zoom=0.75, run_time=1,
                         added_anims=[FadeOut(temp_remove), diagonal.animate.set_color(WHITE)])

        self.play(square_group.animate.rotate(45 * DEGREES, axis=RIGHT).move_to([7, -2.7, 0]))

        line_len_explain = Tex(r"$2\sqrt{x_0}$").move_to([7, -3.1, 0.4]).rotate(PI / 2).rotate(PI / 2, axis=UP).scale(
            0.7)
        s_len = Tex(r"$S$").move_to([7, -2.7, -1.3]).rotate(PI / 2).rotate(PI / 2, axis=UP).scale(0.7)
        s_len_real = Tex(r"$\sqrt{2x}$").move_to([7, -2.7, -1.3]).rotate(PI / 2).rotate(PI / 2, axis=UP).scale(0.7)

        self.play(FadeIn(line_len_explain), FadeIn(s_len))

        # Finding Side Length and A(x)
        line_len_explain_real = Tex(r"$2\sqrt{x}$").move_to([7, -3.1, 0.4]).rotate(PI / 2).rotate(PI / 2,
                                                                                                  axis=UP).scale(
            0.7)
        self.play(ReplacementTransform(line_len_explain, line_len_explain_real))

        sol_s_1 = Tex(r"$\sqrt{2}S = 2\sqrt{x}$").rotate(PI / 2).rotate(PI / 2, axis=UP).scale(0.7).move_to(
            [7, 1.8, 1.3])
        sol_s_2 = Tex(r"$S = \frac{2\sqrt{x}}{\sqrt{2}}$").rotate(PI / 2).rotate(PI / 2, axis=UP).scale(0.7).move_to(
            [7, 1.8, 0.6])
        sol_s_3 = Tex(r"$S = \sqrt{2x}$").rotate(PI / 2).rotate(PI / 2, axis=UP).scale(0.7).move_to([7, 1.8, 0.6])

        self.play(FadeIn(sol_s_1))
        self.wait(1)
        self.play(FadeIn(sol_s_2))
        self.wait(1)
        self.play(ReplacementTransform(sol_s_2, sol_s_3))
        self.wait(1)

        self.play(ReplacementTransform(s_len, s_len_real))

        self.wait(0.5)

        sol_a_1 = Tex(r"$A(x) = S^2$").rotate(PI / 2).rotate(PI / 2, axis=UP).scale(0.7).move_to(
            [7, 1.8, -0.8])
        sol_a_2 = Tex(r"$A(x) = (\sqrt{2x})^2$").rotate(PI / 2).rotate(PI / 2, axis=UP).scale(0.7).move_to(
            [7, 1.8, -0.8])
        sol_a_3 = Tex(r"$A(x) = 2x$").rotate(PI / 2).rotate(PI / 2, axis=UP).scale(0.7).move_to(
            [7, 1.8, -0.8])

        self.play(FadeIn(sol_a_1))
        self.wait(1)
        self.play(TransformMatchingShapes(sol_a_1, sol_a_2))
        self.wait(1)
        self.play(TransformMatchingShapes(sol_a_2, sol_a_3))
        self.wait(1)

        a_answer_box = Rectangle(height=0.75, width=2.35).rotate(PI / 2).rotate(PI / 2, axis=UP).scale(0.7).move_to(
            [7, 1.8, -0.8])
        self.play(Write(a_answer_box))

        self.wait(1)

        self.play(
            FadeOut(VGroup(square_group, s_len_real, line_len_explain_real, sol_s_1, sol_s_3, sol_a_3, a_answer_box)))

        self.wait(1)


if __name__ == "__main__":
    os.system(f"manim {__file__} -pqh")
