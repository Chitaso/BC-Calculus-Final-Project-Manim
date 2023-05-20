import os
from manim import *


class ReimannPart(VMobject):
    def __init__(self, lower_bound, upper_bound, **kwargs):
        super().__init__(**kwargs)

        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

        temp = (upper_bound * 2) ** 0.5
        prism = Prism(dimensions=[upper_bound - lower_bound, temp, temp], fill_opacity=1, stroke_opacity=1,
                      stroke_width=1, stroke_color=BLACK).move_to(
            [lower_bound + (upper_bound - lower_bound) / 2, 0, 0]).rotate(PI / 4, axis=RIGHT)
        self.add(prism)

    def split(self, n_parts=2):  # Returns [from_obj], [to_obj]
        step = round((self.upper_bound - self.lower_bound) / n_parts, 3)

        return [self.copy() for _ in range(n_parts - 1)] + [self], [
            ReimannPart(self.lower_bound + i * step, self.lower_bound + (i + 1) * step) for i in range(n_parts)]


class ReimannSum(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(x_range=[-5, 5, 1], y_range=[-5, 5, 1], z_range=[-5, 5, 1])

        x_label = axes.get_x_axis_label(Tex("x"))
        y_label = axes.get_y_axis_label(Tex("y")).shift(UP * 1.8).rotate(3 * PI / 2)
        z_label = axes.get_z_axis_label(Tex("z"))

        self.set_camera_orientation(zoom=0.5)
        self.play(FadeIn(axes), FadeIn(x_label), FadeIn(y_label), FadeIn(z_label))

        self.move_camera(phi=75 * DEGREES, theta=-80 * DEGREES, zoom=1.2, run_time=1.5)

        self.wait(0.5)

        parts = [ReimannPart(i / 8, (i + 1) / 8) for i in range(32)]
        self.play(AnimationGroup(*[FadeIn(i) for i in parts], lag_ratio=0.1))
        self.wait(0.5)

        self.play(FadeOut(VGroup(axes, x_label, y_label, z_label)))

        shape = VGroup(*parts)
        self.play(shape.animate.move_to([0, 0, 0]))

        self.wait(0.5)

        n = 6
        for i, j, k, l in zip(parts + [None] * (n - 1), [None] + parts + [None] * (n - 2),
                              [None] * (n - 2) + parts + [None], [None] * (n - 1) + parts):
            anims = []

            if i:
                anims.append(i.animate.set_color("#ACE2EE"))
            if j:
                anims.append(j.animate.set_color(WHITE))
            if k:
                anims.append(k.animate.set_color("#ACE2EE"))
            if l:
                anims.append(l.animate.set_color(BLUE).set_stroke(BLACK))

            self.play(*anims, run_time=0.032)

        self.wait(0.5)


if __name__ == "__main__":
    os.system(f"manim {__file__} -pqh")
