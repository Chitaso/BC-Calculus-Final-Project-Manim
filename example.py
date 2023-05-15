
class Example(ThreeDScene):
    def construct(self):
        resolution_fa = 100
        self.set_camera_orientation(phi=75 * DEGREES, theta=-60 * DEGREES)

        axes = ThreeDAxes(
            x_range=(0, 6, 1),
            y_range=(0, 6, 1),
            z_range=(-2, 2, 1),
            color=LIGHT_GREY
        )

        def param_trig(u, v):
            x = u
            y = v
            z = np.sin(x) + np.cos(y)
            return z

        trig_plane = OpenGLSurface(
            lambda x, y: axes.c2p(x, y, param_trig(x, y)),
            resolution=(resolution_fa, resolution_fa),
            u_range = (0, 6),
            v_range = (0, 6),
            axes = axes,
            color = '#B22222',
        )

        self.add(axes, trig_plane)
