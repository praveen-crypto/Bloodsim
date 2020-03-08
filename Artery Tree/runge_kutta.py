import numpy as np
# RUNGEKUTTA 4th order method


def rungekutta4(f, x0, t0, tf, dt):

    t = np.arange(t0, tf, dt)
    nt = t.size

    nx = x0.size
    x = np.zeros((nx, nt))

    x[:, 0] = x0

    for k in range(nt-1):

        k1 = np.multiply(dt, f(t[k], x[:, k]))
        k2 = np.multiply(dt, f(t[k] + dt/2, x[:, k] + k1/2))
        k3 = np.multiply(dt, f(t[k] + dt/2, x[:, k] + k2/2))
        k4 = np.multiply(dt, f(t[k] + dt, x[:, k] + k3))

        test0 = k1
        test1 = 2 * k2
        test2 = 2 * k3
        test3 = k4

        dx = np.add(test0, test1)
        dx = np.add(dx, test2)
        dx = np.add(dx, test3)
        dx = np.divide(dx, 6)

        x[:, k+1] = x[:, k] + dx

    return t, x
