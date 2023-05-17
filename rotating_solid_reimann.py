import os
from manim import *


class ReimannPart(VMobject):
    def __init__(self, lower_bound, upper_bound, **kwargs):
        super().__init__(**kwargs)

        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

        temp = (upper_bound / 2) ** 0.5
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

        self.move_camera(phi=75 * DEGREES, theta=-75 * DEGREES, zoom=1.2, run_time=1.5)

        self.wait(0.5)

        parts = [ReimannPart(0, 4)]
        self.play(*[FadeIn(i) for i in parts])
        self.wait(0.5)

        for i in range(5):
            temp = []
            anims = []

            for p in parts:
                a, b = p.split()
                temp += b
                anims += [ReplacementTransform(*i) for i in zip(a, b)]

            parts = temp

            self.play(*anims)
            self.wait(1)

        self.wait(0.3)

        self.play(FadeOut(VGroup(axes, x_label, y_label, z_label)))

        shape = VGroup(*parts)
        self.play(shape.animate.move_to([0, 0, 0]))

        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(40)

if __name__ == "__main__":
    os.system(f"manim {__file__} -pqh")
