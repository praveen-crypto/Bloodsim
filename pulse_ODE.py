import numpy as np


def pulsegen(t, x, R1, L, R2, C, clock, it):
    i1 = np.interp(t, clock, it)

    xdot = [[0.0], [0.0]]

    xdot[0] = -R1 / L * x[0] + R1 * i1 / L

    xdot[1] = -x[1] / (R2 * C) + i1 / C

    return xdot
