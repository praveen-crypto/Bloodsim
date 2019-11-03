import numpy as np
import scipy
from scipy.integrate import RK45
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import pulse_ODE as p
import integrated_ODE as iode

def cal(HR, PF):
    try:
        branch_list = open('branch_list.txt', 'r')
        b = branch_list.readlines()
        rlcval = np.genfromtxt('rlcval.txt', delimiter = ',')
        eqn_no = np.genfromtxt('eqn_no.txt', delimiter = '')
        Ts = 0.01
        clock = np.arange(0,15,Ts,dtype=np.float64)

        HR = int(HR)
        PF = int(PF)

        T = 60/HR
        t1 = clock/T
        t2 = t1-np.floor(t1,dtype=np.float64)
        t3 = T*t2
        x1 = PF*(np.square(np.sin(3.14*t3/(0.3),dtype=np.float64),dtype=np.float64))
        x2 = np.floor(t3 + 0.7,dtype=np.float64)
        it = np.multiply((1-x2),x1,dtype=np.float64)
        R1 = 0.11
        L = 0.011
        R2 = 1.11
        C = 0.91
        x2 = np.array([0.0,0.0],dtype=np.float64)
        pulse_out = odeint(p.pulsegen,x2,clock,args=(R1,L,R2,C,clock,it),rtol=1e-3,atol=1e-6,tfirst=True)
        pu = it.transpose()
        pulse = (pu - pulse_out[:,0]) * R1+pulse_out[:,1]
        #plt.plot(clock,pulse)
        #plt.show()

        Rs = rlcval[:,0]
        L = rlcval[:,1]
        C = rlcval[:,2]
        Rp = rlcval[:,3]
        x0 = np.zeros(256,dtype=np.float64)

        '''output = odeint(iode.integrated_ode,x0,clock,args=(pulse,clock),rtol=1e-3,atol=1e-6,tfirst=True)
        a = output[:,200]
        plt.plot(clock,a)
        plt.show()'''
        return (clock, pulse)
    except:
        return (-1,-10000)

if __name__=="__main__":
    pass
    c,p=cal(60,430)
    print(c)
    print(p)