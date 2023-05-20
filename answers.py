from manim import *
import os


# Composite this shot onto P2
class Answers(Scene):
    def construct(self):
        a = Tex(r"$A(x) = 2x$")
        v = Tex(r"$V = 16$")

        g = VGroup(a, v).arrange(buff=3)
        self.play(Write(g))


if __name__ == "__main__":
    os.system(f"manim {__file__} -pqh")
