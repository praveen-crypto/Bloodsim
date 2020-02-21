import numpy as np

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
global timestep, Tduration, ddt, tee, tcr, tac, tar, t
global odic

# functions definition:

def Ecal(EEE, ZZZ, vol):
    EcalR = EEE * np.exp(vol / ZZZ)

    return EcalR
def Lvecal():
    global Elva, Elvb
    global elv, FL
    global tee, tcr
    tcal = tcr

    if tcal <= tee:
        elv = FL * Elva * 0.5 * (1.0 - np.cos(3.1415926 * tcal / tee)) + Elvb / FL
    else:
        if tcal <= 1.5 * tee:
            elv = FL * Elva * 0.5 * (1.0 + np.cos(3.1415926 * (tcal - tee) / (0.5 * tee))) + Elvb / FL
        else:
            elv = Elvb / FL
def Laecal():
    global tcr, ela, Elaa, tap, Tduration
    global teec
    global teer

    tcal = tcr
    teec = tar - tac
    teer = teec
    tap = tar + teer - Tduration

    if (tcal >= 0.0 and tcal <= tap):
        ela = Elaa * 0.5 * (1.0 + np.cos(3.1415926 * (tcal + Tduration - tar) / teer)) + Elab

    if (tcal > tap and tcal <= tac):
        ela = Elab

    if (tcal > tac and tcal <= tar):
        ela = Elaa * 0.5 * (1.0 - np.cos(3.1415926 * (tcal - tac) / teec)) + Elab

    # c if (tcal > tar. and.tcal <= (tar+teer)) then
    if (tcal > tar and tcal <= Tduration):
        ela = Elaa * 0.5 * (1.0 + np.cos(3.1415926 * (tcal - tar) / teer)) + Elab
def rvecal():
    global tcr, FR1,Erva,tee,Ervb
    global erv
    tcal = tcr
    if tcal <= tee:
        erv = FR1 * Erva * 0.5 * (1.0 - np.cos(3.1415926 * tcal / tee)) + Ervb / FR1
    else:
        if tcal <= 1.5 * tee:
            erv = FR1 * Erva * 0.5 * (1.0 + np.cos(2.0 * 3.1415926 * (tcal - tee) / tee)) + Ervb / FR1
        else:
            erv = Ervb / FR1
def raecal():
    global teer,Eraa,Erab
    global tar, tac, tcr
    global era,Tduration

    eec = tar - tac
    teer = teec
    tcal = tcr

    tap = tar + teer - Tduration

    if 0 <= tcal <= tap:
        era = Eraa * 0.5 * (1.0 + np.cos(3.1415926 * (tcal + Tduration - tar) / teer)) + Erab

    if tap < tcal <= tac:
        era = Erab

    if tcal > tac and tcal <= tar:
        era = Eraa * 0.5 * (1.0 - np.cos(3.1415926 * (tcal - tac) / teec)) + Erab

    if tcal > tar and tcal <= Tduration:
        era = Eraa * 0.5 * (1.0 + np.cos(3.1415926 * (tcal - tar) / teer)) + Erab
def rungekutta(subresultcr) :
    #call dvdqsdvsdq % == == == == == = make a note........................
    dvdqsdvsdq()
    dfl[0, :29] = dvq[0, :29]

    #do i = 0, 28
    #dfl(i) = dvq(i + 1)
    #end do

    dq[0, :7] = dfl[0, 1:14:2]
    dq[0, 8:15] = dfl[0, 15:29:2]

    dv[0, :7] = dfl[0, 1:13:2]
    dv[0, 8:14] = dfl[0, 16:28:2]

    for nrk in np.arange(4):
        subrukruk[nrk, :29] = np.multiply(ddt, dfl[0, :29])

        if nrk == 1:
            Aav = AAav()
            Amv = AAmv()
            Apv = AApv()
            Atv = AAtv()

        if nrk < 4 :
            inter[0, :29] = np.multiply(0.5, (subrukuk[nrk, :29]))
        else :
            inter[0, :29] = subrukuk[nrk, :29]

    inter[0, :29] = np.multiply(0.5, (subrukuk[nrk,1:29]))
    newpara[0, :29] = np.multiply(subresultcr[0, :29] + inter[0, :29])


    q[0, :7] = newpara[0, 1:14:2]
    q[0, 8:15]= newpara[0, 15:29:2]


    v[0, :7] = newpara[0, 0:13:2]
    v[0, 8:14] = newpara[0, 16:28:2]


v = np.zeros(shape=(1,14))
q = np.zeros(shape=(1, 21))
dvq = np.zeros(shape=(1, 29))
diffv = np.zeros(shape=(1, 14))
resultcr = np.zeros(shape=(1, 101))
dv = np.zeros(shape=(1, 21))

# initial values of all state equations (should be equal to number of equations in dvdqsdvdq.m file)
odic = np.array([1068.2371, 52.4983, 181.7233, -41.7618, 65.0625, 0, 122.6637, 0, 67.0272, -0.3118, 135.11, -2.1737, 198.7568,
                 -64.1791, 0, 2.7983, 0.1357, 2.7932, 1.1042, 68.8587, 0, 121.2539, 0, 67.3641, 41.8262, 22.0472, 56.6627, 1.8539,
                 57.6473])

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
for nstep in np.arange(ntotal):
    if nstep == 0:
        tcr = 0.0
        ppc = 0.0
        result = np.zeros(shape=(1, 101))
        result[0, :29] = odic

        for i in np.arange(14):
            if i <= 6:
                v[0, i] = result[0, 2 * i]
            else:
                v[0, i] = result[0, 2 * i +1]

        for i in np.arange(15):
            if i <= 6:
                q[0, i] = result[0, 2 * i +1]
            else:
                q[0, i] = result[0, 2 * i]

        STR = 1.0
        FL = 1.0
        FR1 = 1.0
        Gpw = 0.0

        Aav = 0.0
        Amv = 0.0
        Apv = 0.0
        Atv = 0.0

        Pit = -2.5
        P_0d = np.zeros(shape=(1, 101))

        # fid60  =  fopen('0Dresult.txt','a+')
        # fid63  =  fopen('0Dpress.txt','a+')


    # ==========================================================================================
    # --------------------------------------
    # c*-----------------------Start computation----------------------*c
    ncount = 0
    ncountadd = ncount + 1
    resultcr[0, :101] = result[0, :101]
    tcr = np.remainder(np.multiply(nstep, dt), Tduration)
    t = np.multiply(nstep, dt)

    # c.... Compute the pulmonary elastances
    Epua = Ecal(Epua0, Zpua, v[0, 4])
    Epuc = Ecal(Epuc0, Zpuc, v[0, 5])
    Epuv = Ecal(Epuv0, Zpuv, v[0, 6])
    Epwc = Ecal(Epwc0, Zpwc, v[0, 7])
    Epwv = Ecal(Epwv0, Zpwv, v[0, 8])

    # c.....Update nolinear cardiac parameters

    if tcr == 0.0:
        FL = np.subtract(1.0, np.divide(result[0, 21], Vmax))  # Left ventricle scaling factor
        FR1 = np.subtract(1.0, np.divide(result[0, 6], Vmax))  # Right ventricle scaling factor

    Lvecal()  # LV elastance function calling
    Laecal()  # LA elastance function calling
    rvecal()  # RV elastance function calling
    raecal()  # RA elastance function calling

    # Spetum cross talk pressure calculations
    cklr = erv / (Es + erv)
    ckrl = elv / (Es + elv)

    ppp1 = np.multiply(np.multiply(np.multiply(np.add(np.multiply(np.multiply(ckrl, Es), v[0, 10]), ckrl), ckrl), Es), v[0, 3])#plv=(ckrl*Es*v(11)+ckrl*cklr*Es*v(4))/(1.0-cklr)
    plv = np.divide(ppp1, np.subtract(1.0, cklr))
    prv = np.divide(np.multiply(np.multiply(np.multiply(np.add(np.multiply(np.multiply(ckrl, Es), v[0, 3]), ckrl), ckrl), Es), v[0, 10]), np.subtract(1.0, cklr))

    # All cardiac chambers viscoelastance calculation
    Sla = np.multiply(np.multiply(Sva0, v[0, 9]), ela)   #Sla = Sva0 * v[10] * ela
    Slv = np.multiply(Sva0, plv)                       #Slv = Sva0 * plv
    Sra = np.multiply(np.multiply(Sva0, v[0, 2]), era)    #Sra = Sva0 * v[3] * era
    Srv = np.multiply(Sva0, prv)                       #Srv = Sva0 * prv

    # Pericardium pressure calculations

    ppp = np.divide(np.subtract(np.add(np.add(np.add(np.add(v[0, 2], v[0, 3]), v[0, 9]), v[0, 10]), Vpe), Vpc0), Vcon)#ppp = (v[3] + v[4] + v[10] + v[11] + Vpe - Vpc0) / Vcon
    ppc = np.exp(ppp)
    # c....Update dv and state equation function calling

    #dvdqsdvsdq()#dvdqsdvsdq();  # = == == == == == == == == == == == == == = >> make a note.............................

    diffv[0, :7] = dvq[0, 0:13:2]
    diffv[0, 8:14] = dvq[0, 16:28:2]
    dv[0, :14] = diffv[0, 0:14]

    # c.....Implement fourth - order Runge - Kutta method

    rukuk = rungekutta(resultcr)

    # c.....Update variables with Runge-Kutta method

    for i in np.arange(29):
        result[ncountadd, i] = np.divide(np.add(result[ncount, i] ,np.add(rukuk[:i], np.add(np.multiply(2.0, np.add(rukuk[2, i], rukuk[3,i]))), rukuk[4,i])), 6)

    delta = 0.00000001

    # update all four cardiac valve flow as zero when they were closed

    if Aav == 0.0 and resultcr[22] <= delta:
        resultcr[22] = 0.0
        result[ncountadd, 22] = 0.0
        q[11] = 0.0

    if np.absolute(tcr - Tduration) <= ddt * 0.5 or tcr < 0.1 or Amv == 0.0 and resultcr[20] <= delta:
        resultcr[20] = 0.0
        resultcr[ncountadd, 20] = 0.0
        q[10] = 0.0

    if Apv == 0.0 and resultcr[7] <= delta:
        resultcr[7] = 0.0
        resultcr[ncountadd, 7] = 0.0
        q[3] = 0.0

    if np.absolute(tcr - Tduration) <= ddt * 0.5 or tcr < 0.1 or Atv == 0.0 and resultcr[5] <= delta:
        resultcr[5] = 0.0
        result[ncountadd, 5] = 0.0
        q[2] = 0.0

    # c.....Update q() and v() to be used at next time
    v[:7] = result[ncountadd, 0:13:2]
    v[8:14] = result[ncountadd, 16:28:2]

    q[: 7] = result[ncountadd, 1:14:2]
    q[8: 15] = result[ncountadd, 15:29:2]
    q[16: 21] = result[ncountadd, 30:35:1]

    result[0, :29] = result[1, :29]

    # load calculated hemodynamic variables in an array

    jj += 1

    # MyResult(jj,1:27)=P_0d(1:27);
    # MyResult1(jj,1:30)=result(1,1:29);

    MyResult[jj - 1, 0:26] = P_0d[0, 26]
    MyResult[jj - 1, 0:28] = result[0, 0:28]

    # Update the initial conditions for next cardiac cycle






