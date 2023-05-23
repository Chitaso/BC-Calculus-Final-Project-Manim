from manim import *
import os


class ProblemStatement(Scene):
    def construct(self):
        # tex = Tex(
        #     r"``The Solid'' lies between the planes perpendicular to the x-axis at $x=0$ and $x=4$. The cross sections perpendicular to x-axis between these planes run from $y=-\sqrt{x}$ to $y=\sqrt{x}$. Find the formula for $A(x)$ of the cross section if it is a square with diagonal in xy plane. Then find $V$.").scale(0.75)
        tex = Tex(
            r"A solid lies between the planes perpendicular to the $x$ axis at $x=0$ and $x=4$. Cross sections perpendicular to the $x$ axis between them are squares whose diagonals run from $y=-\sqrt{x}$ to $y=\sqrt{x}$. Find the formula for the area of the cross section $A(x)$, then find the volume $V$.").scale(
            0.75)

        # tex = Tex(r"``The Solid'' lies between the planes perpendicular\\to the x-axis at $x=0$ and $x=4$.").scale(0.75)
        # tex = Tex(r"Cross sections perpendicular to x-axis between them are\\squares whose diagonals run from $y=-\sqrt{x}$ to $y=\sqrt{x}$").scale(0.75)
        self.play(Write(tex, run_time=2))
        self.wait(0.5)
        self.play(FadeOut(tex))
        self.wait(0.5)


if __name__ == "__main__":
    os.system(f"manim {__file__} -pqh")
