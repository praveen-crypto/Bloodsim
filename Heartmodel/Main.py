import numpy as np
import submain as ft
import math as m
import vandfeq as vf

global valve, Aav, Amv, Apv, Atv, Gpw
global E_cardiopul, Elaa, Elab, Elva, Elvb, Eraa, Erab, Erva, Ervb, Epua, Epuc, Epuv, Epwa, Epwc, Epwv
global yL_cardiopul, yav, ymv, ypv, ytv, ypua, ypuc, ypuv, ypwa, ypwc, ypwv
global R_cardiopul, Ra, Raa, Rav, Rca, Rda, Rmv, Rpua, Rpuc, Rpuv, Rpv, Rpwa, Rpwc, Rpwv, Rtv, Rv, Rvc, bav, bmv, bpv, btv
global S_cardiopul, Spua, Spuc, Spuv, Spwa, Spwc, Spwv
global Z_cardiopul, Zpua, Zpuc, Zpuv, Zpwa, Zpwc, Zpwv
global C_peripheral, Caor, Cart, Ccap, Cven, Cvca
global yL_peripheral, yaor, yart, ycap, yven, yvca
global R_peripheral, Raor, Rart, Rcap, Rven, Rvca
global S_peripheral, Saor, Sart, Scap, Sven, Svca
global sdvsdqdvdq, dvq, P_0d
global dvdq_cardiopul, dv, v, dq, q
global cardiac_parameter, elv, ela, erv, era, cklr, ckrl, plv, prv, Sla, Slv, Sra, Srv, ppp, ppc, pit, qco, FL, FR1, STR
global R_cardiopulc, Rav0, Rmv0, Rpv0, Rtv0, bav0, bmv0, bpv0, btv0, Rav1, Rmv1, Rpv1, Rtv1, bav1, bmv1, bpv1, btv1
global Rav2, Rmv2, Rpv2, Rtv2, bav2, bmv2, bpv2, btv2, yav0, ymv0, ypv0, ytv0, yav1, ymv1, ypv1, ytv1, yav2, ymv2, ypv2, ytv2
global n_val, m_cvst, m_cvrg, n_vrg
global timestep, Tduration, ddt, tee, tac, tar, t
global tcr

# initial values of all state equations (should be equal to number of equations in dvdqsdvdq.m file)
odic = np.array(
    [1068.2371, 52.4983, 181.7233, -41.7618, 65.0625, 0, 122.6637, 0, 67.0272, -0.3118, 135.11, -2.1737, 198.7568,
     -64.1791, 0, 2.7983, 0.1357, 2.7932, 1.1042, 68.8587, 0, 121.2539, 0, 67.3641, 41.8262, 22.0472, 56.6627, 1.8539,
     57.6473])

dv = np.zeros(shape=(1, 21))
v = np.zeros(14)
q = np.zeros(21)
resultcr = np.zeros(101)

Pit = -2.5
pit = Pit
jj = 0
kk = 0

# -----------------------------------------
Elva = 2.87  # !Peak-systolic elastance of left ventricle
Elvb = 0.06  # !Basic diastolic elastance of left ventricle
Elaa = 0.07  # !Peak-systolic elastance of left atrium
Elab = 0.075  # !Basic diastolic elastance of left atrium
Erva = 0.52  # !Peak-systolic elastance of right ventricle
Ervb = 0.043  # !Basic diastolic elastance of right ventricle
Eraa = 0.055  # !Peak-systolic elastance of right atrium
Erab = 0.06  # !Basic diastolic elastance of right atrium

Vmax = 900  # Reference volume of Frank-Starling law
Es = 45.9  # !Effective septal elastance
Vpc0 = 450  # !Reference total pericardial and cardiac volume old value 380
Vpe = 30.0  # !Pericardial volume of heart
Vcon = 40.0  # !Volume constant
Sva0 = 0.0005  # !Coefficient of cardiac viscoelasticity

# ! Cardiac valve parameters
# !(aortic valve(AV),mitral valve(MV), tricuspid valve(TV),pulmonary valve(PV))

bav = 0.000025  # !Bernoulli's resistance of AV
bmv = 0.000016  # !Bernoulli's resistance of MV
btv = 0.000016  # !Bernoulli's resistance of TV
bpv = 0.000025  # !Bernoulli's resistance of PV
Rav = 0.005  # !Viscous resistance of AV
Rmv = 0.005  # !Viscous resistance of MV
Rtv = 0.005  # !Viscous resistance of TV
Rpv = 0.005  # !Viscous resistance of PV
yav = 0.0005  # !Inertance of AV
ymv = 0.0002  # !Inertance of MV
ytv = 0.0002  # !Inertance of TV
ypv = 0.0005  # !Inertance of PV

# ! Pulmonary circulation
Epua0 = 0.02
Epuc0 = 0.02
Epuv0 = 0.02
Epwc0 = 0.7
Epwv0 = 0.7
Rpua = 0.04
Rpuc = 0.04
Rpuv = 0.005
Rpwa = 0.0005
Rpwc = 0.4
Rpwv = 0.4
ypua = 0.0005
ypuc = 0.0005
ypuv = 0.0005
ypwa = 0.0005
ypwc = 0.0005
ypwv = 0.0005
Zpua = 20.0
Zpuc = 60.0
Zpuv = 200.0
Zpwa = 1.0
Zpwc = 1.0
Zpwv = 1.0
Spua = 0.01
Spuc = 0.01
Spuv = 0.01
Spwa = 0.01
Spwc = 0.01
Spwv = 0.01

# ! Peripheral circulation
Caor = 0.9
Cart = 0.3
Ccap = 0.06
Cven = 100.0
Cvca = 30.0

yaor = 0.005
yart = 0.001
ycap = 0.0005
yven = 0.0005
yvca = 0.0005

Raor = 0.03
Rart = 0.75
Rcap = 0.35
Rven = 0.07
Rvca = 0.001

Saor = 0.01
Sart = 0.01
Scap = 0.01
Sven = 0.01
Svca = 0.01
qco = 0.0

# -----------------------------------------
Tduration = 0.65  # input('Please specify cardiac duration(s)')
dt = 0.001  # input('Please specify time step(s)')

# tee = 0.3*sqrt(Tduration) #!Moment when ventricular contractility reaches the peak
tee = 0.31  # !Moment when ventricular contractility reaches the peak

tac = 0.34  # Tduration - 0.02*tee - 0.02* (Tduration/0.855)# !Moment when atrium begins to contract

tar = Tduration - 0.02 * (Tduration / 0.855)  # !Moment when atrium begins to relax
ddt = dt

ncycle = 10  # input('how many cardiac cycles to run ?')

ntotal = ((ncycle) * Tduration / dt)

# -----------------------------------------
for nstep in np.arange(1, ntotal + 1):
    if nstep == 1:
        tcr = 0.0
        ppc = 0.0
        result = np.zeros(shape=(101))
        result[0:29] = odic  # xlsread('0DIC_28.xls',1,'A1:A29')

        for i in range(14):
            if i <= 6:
                v[i] = result[2  * i ]
            else:
                v[i] = result[2 * i + 1]

        for i in range(1, 15):
            if i <= 7:
                q[i] = result[2 * i]
            else:
                q[i] = result[2 * i - 1]

        STR = 1.0
        FL  = 1.0
        FR1 = 1.0
        Gpw = 0.0

        Aav = 0.0
        Amv = 0.0
        Apv = 0.0
        Atv = 0.0

        Pit = -2.5
        P_0d = np.zeros(shape=(101))

        # fid60  =  fopen('0Dresult.txt','a+')
        # fid63  =  fopen('0Dpress.txt','a+')


    # ==========================================================================================

    # --------------------------------------
    # c*-----------------------Start computation----------------------*c
    ncount = 1
    ncountadd = ncount + 1
    resultcr[0: 100] = result[0, 0:100]
    tcr = np.remainder((nstep * dt), Tduration)
    t = np.multiply(nstep, dt)

    # c.... Compute the pulmonary elastances
    Epua = ft.Ecal(Epua0, Zpua, v[4])
    Epuc = ft.Ecal(Epuc0, Zpuc, v[5])
    Epuv = ft.Ecal(Epuv0, Zpuv, v[6])
    Epwc = ft.Ecal(Epwc0, Zpwc, v[7])
    Epwv = ft.Ecal(Epwv0, Zpwv, v[8])

    # c.....Update nolinear cardiac parameters
    if tcr == 0.0:
        FL = 1.0 - np.divide(result[0, 21], Vmax)  # Left ventricle scaling factor
        FR1 = 1.0 - np.divide(result[0, 6], Vmax)  # Right ventricle scaling factor

    Lvecal()  # LV elastance function calling
    Laecal()  # LA elastance function calling
    rvecal()  # RV elastance function calling
    raecal()  # RA elastance function calling

    # Spetum cross talk pressure calculations
    cklr = erv / (Es + erv)
    ckrl = elv / (Es + elv)

    plv = np.divide(ppp, np.subtract(1.0, cklr))
    prv = np.divide(np.multiply(np.multiply(np.multiply(np.add(np.multiply(np.multiply(ckrl, Es), v[3]), ckrl), ckrl), Es), v[10]), np.subtract(1.0, cklr))

    # All cardiac chambers viscoelastance calculation
    Sla =  np.multiply(np.multiply(Sva0, v[9]), ela)   #Sla = Sva0 * v[10] * ela
    Slv = np.multiply(Sva0, plv)                       #Slv = Sva0 * plv
    Sra = np.multiply(np.multiply(Sva0, v[2]), era)    #Sra = Sva0 * v[3] * era
    Srv = np.multiply(Sva0, prv)                       #Srv = Sva0 * prv
    # Pericardium pressure calculations
    ppp = np.divide(np.subtract(np.add(np.add(np.add(np.add(v[2], v[3]), vp[9]), v[10]), Vpe), Vpc0), Vcon)#ppp = (v[3] + v[4] + v[10] + v[11] + Vpe - Vpc0) / Vcon
    ppc = m.exp(ppp)
    # c....Update dv and state equation function calling

    dvdqsdvsdq()#dvdqsdvsdq();  # = == == == == == == == == == == == == == = >> make a note.............................

    diffv[0: 6] = dvq[0: 1: 12]
    diffv[7: 13] = dvq[15: 1: 27]
    dv[0: 13] = diffv[0: 13]
    # c.....Implement fourth - order Runge - Kutta method

    rukuk = rungekutta(resultcr)

    # c.....Update variables with Runge-Kutta method

    for i in range(1, 29):
        result[ncountadd, i] = np.divide(np.add(result[ncount, i], np.add(
            (rukuk[1, i], np.add(np.multiply(2.0, (np.add(rukuk[2, i] + rukuk[3, i]))), rukuk[4, i])))), 6)

    # c.....Specify blood flows through cardiac valves

    delta = 0.00000001
    # update all four cardiac valve flow as zero when they were closed

    if (Aav == 0.0 and resultcr[22] <= delta):
        resultcr[22] = 0.0
        result[ncountadd - 1, 22] = 0.0
        q[11] = 0.0

    if (abs(tcr - Tduration) <= ddt * 0.5 or tcr < 0.1 or (Amv == 0.0 and resultcr[20] <= delta)):
        resultcr[20] = 0.0
        resultcr[ncountadd - 1, 20] = 0.0
        q[10] = 0.0

    if (Apv == 0.0 and resultcr[7] <= delta):
        resultcr[7] = 0.0
        resultcr[ncountadd - 1, 7] = 0.0
        q[3] = 0.0

    if (np.absolute(tcr - Tduration) <= ddt * 0.5 or tcr < 0.1 or (Atv == 0.0 and resultcr[5] <= delta)):
        resultcr[5] = 0.0
        result[ncountadd - 1, 5] = 0.0
        q[2] = 0.0

    # c.....Update q() and v() to be used at next time step
    v[0: 6] = result[ncountadd - 1, 0: 1: 12]
    v[7: 13] = result[ncountadd - 1, 15: 1: 27]

    q[0: 6] = result[ncountadd - 1, 1: 1: 13]
    q[7: 14] = result[ncountadd - 1, 14: 1: 28]
    q[15: 20] = result[ncountadd - 1, 29: 0:34]

    result[0, 0: 28] = result[1, 0: 28]

    # load calculated hemodynamic variables in an array

    jj += 1

    # MyResult(jj,1:27)=P_0d(1:27);
    # MyResult1(jj,1:30)=result(1,1:29);

    MyResult[jj - 1, 0:26] = P_0d[0, 26]
    MyResult[jj - 1, 0:28] = result[0, 0:28]

    # Update the initial conditions for next cardiac cycle

    if nstep == ntotal:
        odic_new = result[0, 0:28]
t = np.arange(0, 6.499, 0.001)
T = np.transpose(t)
Pa_1 = MyResult1[:, 23]

F_1 = MyResult1[:, 22]





