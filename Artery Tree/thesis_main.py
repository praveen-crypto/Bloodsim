import numpy as np
import runge_kutta as r_k
import pulse_ode as po
import integrated_ode as so
import datetime
from scipy.integrate import solve_ivp
from Heartmodel import CARDIAC

def calc(HR, PF):
   # try:
        #nn = datetime.datetime.now()
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
        dt = 0.00015
        Td = 60/HR

        ncycle = 10
        es = ncycle*Td-0.1
        clock = np.arange(0.0, es, dt)

        T = 60 / HR
        x1 = PF * (np.square(np.sin(3.14 * t3 / (0.3))))
        x2 = np.floor(t3 + 0.7)
        it = np.multiply((1 - x2), x1)
        R1 = 0.11
        L = 0.011
        R2 = 1.11
        C = 0.91

        pressure, flow = CARDIAC.lumped()
        print(len(clock))
        print(len(pressure))
        system_initial = np.zeros(256)

        clock1 = np.arange(0,10,0.001)
        system_finder = lambda t, x: so.integrated_ode(t, x, pressure[1000:11000], clock1)
        sol = solve_ivp(system_finder,[0, 10],system_initial,method='Radau',t_eval=np.arange(0, 10, 0.001))
        t = sol.t
        x = sol.y

        return (t, x)
    #except:
       # return (-1,-10000)

if __name__ == "__main__":
    import stenosis
    import matplotlib.pyplot as plt
    stenosis.steno(0, 0)
    c,p = calc(72, 360)
    plt.plot(c, p[1][:])