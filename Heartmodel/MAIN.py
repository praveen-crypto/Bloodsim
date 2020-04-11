import numpy as np
import integrated_ode as so
import datetime
from scipy.integrate import solve_ivp
from Heartmodel import CARDIAC


def calc(HR, PF):
    nn = datetime.datetime.now()
    branch_list = open('DB/branch_list.txt', 'r')
    b = branch_list.readlines()
    rlctru = np.genfromtxt('DB/RLCtru.csv', delimiter=",")
    eqn_no = np.genfromtxt('DB/eqn_no.txt', delimiter='')

    print("main executed")
    Rs = rlctru[:, 0]
    L = rlctru[:, 1]
    C = rlctru[:, 2]
    Rp = rlctru[:, 3]

    f = open("RLCtru.csv", "w")
    f.truncate()
    f.close()

    HR = int(HR)
    PF = int(PF)

    dt = 0.001
    Td = 60 / HR
    ncycle = 10

    es = ncycle * Td - 0.1
    clock = np.arange(0.0, es, dt)
    print(es)

    T = 60 / HR
    R1 = 0.11
    L = 0.011
    R2 = 1.11
    C = 0.91

    pressure, flow = CARDIAC.lumped(HR, ncycle, dt)
    print(len(clock))
    print(len(pressure))
    system_initial = np.zeros(256)

    clock1 = np.arange(0, 10, 0.001)
    system_finder = lambda t, x: so.integrated_ode(t, x, pressure[:len(clock)], np.arange(0, es, dt))
    sol = solve_ivp(system_finder, [0, es], system_initial, method='Radau', t_eval=np.arange(0, es, dt))
    t = sol.t
    x = sol.y

    return t, x


if __name__ == "__main__":
    import STENOSIS
    import matplotlib.pyplot as plt

    STENOSIS.steno(0, 0)
    c, p = calc(75, 450)
    plt.plot(c, p[1, :])
