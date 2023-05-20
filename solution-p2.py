from manim import *
import os


class RiemannObject(VMobject):
    def __init__(self, lower_bound, upper_bound, num_parts, **kwargs):
        super().__init__(**kwargs)

        for i in range(num_parts):
            ub = (i + 1) * (upper_bound - lower_bound) / num_parts
            lb = i * (upper_bound - lower_bound) / num_parts

            temp = (ub * 2) ** 0.5
            prism = Prism(dimensions=[ub - lb, temp, temp], fill_opacity=1, stroke_opacity=1,
                          stroke_width=1, stroke_color=BLACK).move_to(
                [lb + (ub - lb) / 2, 0, 0]).rotate(PI / 4, axis=RIGHT)
            self.add(prism)

    def generate_sum_effect(self):  # TODO - figure out better sum effect
        n = 4
        for i, j, k, l in zip(self.submobjects + [None] * (n - 1), [None] + self.submobjects + [None] * (n - 2),
                              [None] * (n - 2) + self.submobjects + [None], [None] * (n - 1) + self.submobjects):
            p = []

            if i:
                p.append(i.animate.set_color("#ACE2EE"))
            if j:
                p.append(j.animate.set_color(WHITE))
            if k:
                p.append(k.animate.set_color("#ACE2EE"))
            if l:
                p.append(l.animate.set_color(BLUE).set_stroke(BLACK))

            yield p


class FinalSolutionP2(ThreeDScene):
    def construct(self):
        # Positioning camera
        self.move_camera(phi=75 * DEGREES, theta=-75 * DEGREES, frame_center=[2.2, 1.8, -4], zoom=0.4, run_time=0.01)

        # Fading in the things
        axes = ThreeDAxes(x_range=[-5, 5, 1], y_range=[-5, 5, 1], z_range=[-5, 5, 1])

        x_label = axes.get_x_axis_label(Tex("x"))
        y_label = axes.get_y_axis_label(Tex("y")).shift(UP * 1.8).rotate(3 * PI / 2)
        z_label = axes.get_z_axis_label(Tex("z")).rotate(PI / 2).shift([-0.3, 0.5, 0])

        riemann = RiemannObject(0, 4, 32)
        self.play(FadeIn(axes), FadeIn(x_label), FadeIn(y_label), FadeIn(z_label), FadeIn(riemann))

        self.wait(0.5)


        # Showing off A(x) and dx
        random_piece = Prism(dimensions=[0.125, 2.82842712, 2.82842712], fill_opacity=1, stroke_opacity=1,
                             stroke_width=1, stroke_color=BLACK)
        side_label = Tex("$A(x)$").rotate(PI / 2).rotate(PI / 2, axis=UP).flip(axis=UP).flip(axis=RIGHT)
        dx_label = Tex(r"$\mathrm{d}\!\mathop{x}$").rotate(PI / 2, axis=RIGHT).move_to([0, -1.4, -1.6]).scale(0.5)

        VGroup(random_piece, side_label, dx_label).move_to([13, 3, 0]).scale(2).rotate(
            PI / 3 - 30 * DEGREES).rotate(-2 * DEGREES, axis=UP)  # Positioning things

        riemann.submobjects[18].save_state()

        self.play(Wiggle(riemann.submobjects[18]))
        self.play(Transform(riemann.submobjects[18], random_piece))

        self.wait(0.5)
        self.play(Write(side_label))
        self.wait(0.5)
        self.play(Write(dx_label))
        self.wait(0.5)

        self.play(FadeOut(side_label), FadeOut(dx_label), run_time=0.5)
        self.play(Restore(riemann.submobjects[18]))

        self.wait(0.5)

        # Showing sum effect
        for i in riemann.generate_sum_effect():
            self.play(*i, run_time=0.032)

        self.wait(0.5)

        note = Tex(r"I hope you can composite shots :)\\Manim is too full of bugs in 3d").shift(RIGHT * 4.5 + UP * 3).scale(0.5)
        self.add_fixed_in_frame_mobjects(note)

        self.wait(0.5)

        # Actually solving the problem
        # sol_1 = Tex(r"$V = \int \! A(x) \, \mathrm{d}x$").shift(RIGHT * 4.5 + UP * 3)
        # sol_2 = Tex(r"$V = \int_0^4 \! A(x) \, \mathrm{d}x$").shift(RIGHT * 4.5 + UP * 3)
        # sol_3 = Tex(r"$V = \int_0^4 \! 2x \, \mathrm{d}x$").shift(RIGHT * 4.5 + UP * 3)
        # self.camera.add_fixed_in_frame_mobjects(sol_1, sol_2, sol_3)
        #
        # self.play(Write(sol_1))
        # self.wait(0.5)
        # self.play(FadeIn(sol_2), FadeOut(sol_1))
        # self.wait(0.5)
        # self.play(FadeIn(sol_3), FadeOut(sol_2))
        # self.wait(0.5)

        # sol_1_p1 = Tex(r"$V = \int$").shift(RIGHT * 4.5 + UP * 3)
        # sol_1_p2 = Tex(r"$A(x)$").next_to(sol_1_p1, RIGHT).shift(0.2 * LEFT)
        # sol_1_p3 = Tex(r"$\mathrm{d}x$").next_to(sol_1_p2, RIGHT).shift(0.1 * LEFT)
        #
        # self.camera.add_fixed_in_frame_mobjects(sol_1_p1, sol_1_p2, sol_1_p3)
        # self.play(Write(sol_1_p1), Write(sol_1_p2), Write(sol_1_p3))
        #
        # self.wait(0.5)
        #
        # sol_2_p1 = Tex(r"$V = \int_0^4$").shift(RIGHT * 4.5 + UP * 3)
        # self.play(TransformMatchingShapes(sol_1_p1, sol_2_p1),
        #           sol_1_p2.animate.next_to(sol_2_p1, RIGHT).shift(0.21 * LEFT),
        #           sol_1_p3.animate.next_to(sol_1_p2, RIGHT).shift(0.05 * LEFT), run_time=1)
        # self.wait(0.5)
        #
        # sol_3_p1 = Tex(r"$2x$").shift(RIGHT * 4.5 + UP * 3)
        # # self.camera.add_fixed_in_frame_mobjects(sol_3_p1)
        #
        # self.play(Transform(sol_1_p2, sol_3_p1), sol_1_p3.animate.next_to(sol_3_p1, RIGHT).shift(0.05 * LEFT),
        #           run_time=1)
        #
        # self.wait(0.5)

        # sol_4 = Tex(r"$V = x^2 \big|_0^4$").shift(RIGHT * 4.5 + UP * 2.3)
        # self.camera.add_fixed_in_frame_mobjects(sol_4)
        #
        # self.play(Write(sol_4))


if __name__ == "__main__":
    os.system(f"manim {__file__} -pqh")
