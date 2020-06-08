import numpy as np
import runge_kutta as r_k
import pulse_ode as po
import integrated_ode as so
import os
from scipy.integrate import solve_ivp

def calc(HR, PF):
    try:
        #nn = datetime.datetime.now()
        path = os.path.join('DBS', 'RLCtru.txt')
        rlctru = np.genfromtxt(path, delimiter=',')
        Rs = rlctru[:, 0]
        L = rlctru[:, 1]
        C = rlctru[:, 2]
        Rp = rlctru[:, 3]
        f = open(path, 'w')
        f.truncate()
        f.close()
        HR = int(HR)
        PF = int(PF)
        dt = 0.001
        st = 0
        et = 10
        clock = np.arange(st, et, dt)
        T = 60 / HR
        t1 = clock / T
        t2 = t1 - np.floor(t1)
        t3 = np.multiply(T, t2)
        x1 = PF * (np.square(np.sin(3.14 * t3 / 0.3)))
        x2 = np.floor(t3 + 0.7)
        R1 = 0.11
        L = 0.011
        R2 = 1.11
        C = 0.91
        it = np.multiply((1 - x2), x1)
        # GENERATION OF PULSE
        # initial value
        pulse_initial = np.zeros(2)
        pulse_generator = lambda t, x: po.pulsegen(t, x, R1, L, R2, C, clock, it)  # input for solver function
        t, x = r_k.rungekutta4(pulse_generator, pulse_initial, st, et, dt)
        pu = it.transpose()  # plotting the output
        pulse = (pu - x[0, :]) * R1 + x[1, :]
        system_initial = np.zeros(256)
        system_finder = lambda t, x: so.integrated_ode(t, x, pulse, clock)
        sol = solve_ivp(system_finder, [st, et], system_initial, method='Radau', t_eval=np.arange(st, et, dt))
        to = sol.t
        xo = sol.y
        t = to[:7500]
        x = xo[:, 2500:]
        return t, x
    except:
        return -1, -10000


if __name__ == "__main__":
    import STENOSIS
    import matplotlib.pyplot as plt
    stn_dat = {'0': None, '1': 3, '7': 4, '13': 6, '3': 7, '11': 20, '10': 0, '51': 0, '46': 0,
                '74': 0, '56': None, '70': 0, '62': 0, '63': 0, '108': 0, '109': 0,
                '102': 0, '107': 0, '96': 0, '92': 55}
    STENOSIS.steno(0.04, 1.05, 0.6, **stn_dat)
    c, p = calc(72, 450)
    plt.plot(c, p[0, :])


