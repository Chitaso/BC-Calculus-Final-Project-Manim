from manim import *
import os


# Composite this shot onto P2
class FinalSolutionP2Composite(Scene):
    def construct(self):
        # Actually solving the problem
        sol_1 = Tex(r"$V = \int \! A(x) \, \mathrm{d}x$").shift(RIGHT * 3.2 + UP * 1.8)
        sol_2 = Tex(r"$V = \int\limits_0^4 \! A(x) \, \mathrm{d}x$").move_to(sol_1)
        sol_3 = Tex(r"$V = \int\limits_0^4 \! 2x \, \mathrm{d}x$").move_to(sol_2)

        self.play(Write(sol_1))
        self.wait(0.5)
        self.play(TransformMatchingShapes(sol_1, sol_2))
        self.wait(0.5)
        self.play(TransformMatchingShapes(sol_2, sol_3))
        self.wait(0.5)

        sol_4 = Tex(r"$V = x^2 \Big|_0^4$").next_to(sol_1, DOWN).shift(LEFT * 0.45)
        self.play(Write(sol_4))
        self.wait(0.5)

        sol_5 = Tex(r"$V = \left(4\right)^2 - \left(0\right)^2$").next_to(sol_4, DOWN).shift(RIGHT * 0.7)
        self.play(Write(sol_5))
        self.wait(0.5)

        sol_6 = Tex(r"$V = 16 - 0$").next_to(sol_4, DOWN).align_to(sol_5, LEFT).shift(DOWN * 0.08)
        self.play(TransformMatchingShapes(sol_5, sol_6))
        self.wait(0.5)

        sol_7 = Tex(r"$V = 16$").next_to(sol_4, DOWN).align_to(sol_5, LEFT).shift(DOWN * 0.08)
        self.play(TransformMatchingShapes(sol_6, sol_7))
        self.wait(0.5)

        box = Rectangle(width=1.8, height=0.8).move_to(sol_7)
        self.play(Write(box))
        self.wait(0.5)

        self.play(FadeOut(sol_3), FadeOut(sol_4), FadeOut(sol_7), FadeOut(box))

        self.wait(0.5)


if __name__ == "__main__":
    os.system(f"manim {__file__} -pqh")
