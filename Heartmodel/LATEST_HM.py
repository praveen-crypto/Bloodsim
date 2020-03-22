#working code
import numpy as np
import math  as m
import matplotlib.pyplot as plt
import time

# functions definition:


def Integrated_ode():
    global Aav, Amv, Apv, Atv, Gpw
    global Epua, Epuc, Epuv, Epwc, Epwv
    global yav, ymv, ypv, ytv, ypua, ypuc, ypuv, ypwa, ypwc, ypwv
    global Rav, Rmv, Rpua, Rpuc, Rpuv, Rpv, Rpwc, Rpwv, Rtv, bav, bmv, bpv, btv
    global Spua, Spuc, Spuv, Spwc, Spwv
    global Zpua, Zpuc, Zpuv, Zpwc, Zpwv
    global Caor, Cart, Ccap, Cven, Cvca
    global yaor, yart, ycap, yven, yvca
    global Raor, Rart, Rcap, Rven, Rvca
    global Saor, Sart, Scap, Sven, Svca
    global dvq, P_0d
    global dv, v, q
    global ela, era
    global plv, prv, Sla, Slv, Sra, Srv, ppc, pit, qco, Tduration, ddt, tcr

    dvq[0, 0] = q[0, 14] - q[0, 0]  # Venous volume  dvq(1)= q(15) - q(1);

    P_0d[0, 0] = v[0, 0] / Cven + Sven * dv[0, 0]  # Venous  Pressure

    dvq[0, 1] = (v[0, 0] / Cven + Sven * dv[0, 0] - Rven * q[0, 0] - v[0, 1] / Cvca - Svca * dv[0, 1]) / yven  # Venous flow

    dvq[0, 2] = q[0, 0] - q[0, 1]  # VC volume

    P_0d[0, 1] = v[0, 1] / Cvca + Svca * dv[0, 1]  # VC Pressure

    dvq[0, 3] = (v[0, 1] / Cvca - era * v[0, 2] - Rvca * q[0, 1] + Svca * dv[0, 1] - Sra * dv[0, 2] - ppc - pit) / yvca  # VC Flow

    qco = 0.0

    dvq[0, 4] = q[0, 1] + qco - q[0, 2]  # RA volume

    P_0d[0, 3] = era * v[0, 2] + Sra * dv[0, 2] + ppc + pit  # RA pressure

    dvq[0, 5] = (era * v[0, 2] - prv - Rtv * q[0, 2] - btv * q[0, 2] * np.abs(q[0, 2]) + Sra * dv[0, 2] - Srv * dv[0, 3]) / ytv  # TV flow

    dvq[0, 6] = q[0, 2] - q[0, 3]  # RV volume

    P_0d[0, 5] = prv + Srv * dv[0, 3] + ppc + pit  # RV pressure

    dvq[0, 7] = (prv - Epua * Zpua - Rpv * q[0, 3] - bpv * q[0, 3] * (np.abs(q[0, 3])) + Srv * dv[0, 3] - Spua * dv[0, 4] + ppc) / ypv  # PV flow

    dvq[0, 8] = q[0, 3] - q[0, 4] - q[0, 7]  # Pulmonary Artery volume

    P_0d[0, 7] = Epua * Zpua + Spua * dv[0, 4] + pit  # Pulmonary Artery Pressure

    dvq[0, 9] = (Epua * Zpua - Epuc * Zpuc - Rpua * q[0, 4] + Spua * dv[0, 4] - Spuc * dv[0, 5]) / ypua  # Pulmonary Artery Flow

    dvq[0, 10] = q[0, 4] - q[0, 5]  # Pulmonary Capillary volume

    P_0d[0, 9] = Epuc * Zpuc + Spuc * dv[0, 5] + pit  # Pulmonary Capillary Pressure

    dvq[0, 11] = (Epuc * Zpuc - Epuv * Zpuv - Rpuc * q[0, 5] + Spuc * dv[0, 5] - Spuv * dv[0, 6]) / ypuc  # Pulmonary Capillary Flow

    dvq[0, 12] = q[0, 5] - q[0, 6]  # Pulmonary Vein volume

    P_0d[0, 11] = Epuv * Zpuv + Spuv * dv[0, 6] + pit  # Pulmonary Vein Pressure

    dvq[0, 13] = (Epuv * Zpuv - ela * v[0, 9] - Rpuv * q[0, 6] + Spuv * dv[0, 6] - Sla * dv[0, 9] - ppc) / ypuv  # Pulmonary Vein flow

    if Gpw > 0:
        dvq[0, 14] = (Epua * Zpua - Epwc * Zpwc - q[0, 7] / gpw + Spua * dv[0, 4] - Spwc * dv[0, 7]) / ypwa  # Pulmonary Wedge ##Artery flow
    else:
        dvq[0, 14] = 0

    dvq[0, 15] = q[0, 7] - q[0, 8]  # Pulmonary Wedge capillary volume

    P_0d[0, 14] = Epwc * Zpwc + Spwc * dv[0, 7] + pit  # Pulmonary Wedge capillary Pressure

    dvq[0, 16] = (Epwc * Zpwc - Epwv * Zpwv - Rpwc * q[0, 8] + Spwc * dv[0, 7] - Spwv * dv[0, 8]) / ypwc  # Pulmonary Wedge capillary Flow

    dvq[0, 17] = q[0, 8] - q[0, 9]  # Pulmonary Wedge vein Volume

    P_0d[0, 16] = Epwv * Zpwv + Spwv * dv[0, 8] + pit  # Pulmonary Wedge vein Pressure

    dvq[0, 18] = (Epwv * Zpwv - ela * v[0, 9] - Rpwv * q[0, 9] + Spwv * dv[0, 8] - Sla * dv[0, 9] - ppc) / ypwv  # Pulmonary Wedge vein Flow

    dvq[0, 19] = q[0, 6] + q[0, 9] - q[0, 10]  # LA volume

    P_0d[0, 18] = ela * v[0, 9] + Sla * dv[0, 9] + ppc + pit  # LA Pressure

    dvq[0, 20] = (ela * v[0, 9] - plv - Rmv * q[0, 10] - bmv * q[0, 10] * np.abs(q[0, 10]) + Sla * dv[0, 9] - Slv * dv[0, 10]) / ymv  # Mitral flow

    dvq[0, 21] = q[0, 10] - q[0, 11]  # LV volume

    P_0d[0, 20] = plv + Slv * dv[0, 10] + ppc + pit  # LV Pressure

    dvq[0, 22] = (plv - v[0, 11] / Caor - Rav * q[0, 11] - (bav * q[0, 11]) * np.abs(q[0, 11]) + Slv * dv[0, 10] - Saor * dv[0, 11] + ppc + pit) / yav  # Aortic Flow

    # Adjust the state of cardiac valve
    if Aav == 0.0 and q[0, 11] <= 0.000000001:
        dvq[0, 22] = 0.0

    if np.abs(tcr - Tduration) <= ddt * 0.5 or tcr < 0.1 or (Amv == 0.0 and q[0, 10] < 0.000000001):
        dvq[0, 20] = 0.0

    if Apv == 0.0 and q[0, 3] <= 0.00000001:
        dvq[0, 7] = 0.0

    if np.abs(tcr - Tduration) <= ddt * 0.5 or tcr < 0.1 or (Atv == 0.0 and q[0, 2] <= 0.000000001):
        dvq[0, 5] = 0.0

    dvq[0, 23] = q[0, 11] - q[0, 12]  # Aorta volume

    P_0d[0, 22] = v[0, 11] / Caor + Saor * dv[0, 11]  # Aorta Presuure

    dvq[0, 24] = (v[0, 11] / Caor + Saor * dv[0, 11] - q[0, 12] * Raor - v[0, 12] / Cart - Sart * dv[0, 12]) / yaor  # Aorta Flow

    dvq[0, 25] = q[0, 12] - q[0, 13]  # Artery Volume

    P_0d[0, 24] = v[0, 12] / Cart + Sart * dv[0, 12]  # Artery Pressure

    dvq[0, 26] = (v[0, 12] / Cart + Sart * dv[0, 12] - q[0, 13] * Rart - v[0, 13] / Ccap - Scap * dv[0, 13]) / yart  # Artery Flow

    dvq[0, 27] = q[0, 13] - q[0, 14]  # Capillarya Volume

    P_0d[0, 26] = v[0, 13] / Ccap + Scap * dv[0, 13]  # Capillary Pressure

    dvq[0, 28] = (v[0, 13] / Ccap + Scap * dv[0, 13] - q[0, 14] * Rcap - v[0, 0] / Cven - Sven * dv[0, 0]) / ycap  # Capillary Pressure


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
    global tcr, ela, Elaa, tac, tar, Tduration, Elab
    tcal = tcr
    teec = tar - tac
    teer = teec
    tap = tar + teer - Tduration

    if (tcal >= 0.0 and tcal <= tap):
        ela = Elaa * 0.5 * (1.0 + np.cos(3.1415926 * (tcal + Tduration - tar) / teer)) + Elab

    if (tcal > tap and tcal <= tac):
        ela = Elab

    if (tcal > tac and tcal <= tar):
        ela = Elaa * 0.5 * (1.0 -  np.cos(3.1415926 * (tcal - tac) / teec)) + Elab

    # c if (tcal > tar. and.tcal <= (tar+teer)) then
    if (tcal > tar and tcal <= Tduration):
        ela = Elaa * 0.5 * (1.0 + np.cos(3.1415926 * (tcal - tar) / teer)) + Elab


def Rvecal():
    global tcr, FR1, Erva, tee, Ervb
    global erv
    tcal = tcr

    if tcal <= tee:
        erv = FR1 * Erva * 0.5 * (1.0 - np.cos(3.1415926 * tcal / tee)) + Ervb / FR1
    else:
        if tcal <= 1.5 * tee:
            erv = FR1 * Erva * 0.5 * (1.0 + np.cos(2.0 * 3.1415926 * (tcal - tee) / tee)) + Ervb / FR1
        else:
            erv = Ervb / FR1


def Raecal():
    global Eraa, Erab
    global tar, tac, tcr
    global era, Tduration
    teec = tar - tac
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


def AAav():
    global Caor, dv, v
    global plv, Slv, ppc

    intee = plv + Slv * dv[0, 10] + ppc - v[0, 11] / Caor

    if intee > 0.0:
        AAav = 4.0
    else:
        AAav = 0.0

    return AAav


def AAmv():
    global v, ela, plv

    intee = ela * v[0, 9] - plv

    if intee > 0.0:
        AAmv = 4.0
    else:
        AAmv = 0.0
    return AAmv


def AApv():
    global Epua, Zpua, prv

    intee = prv - Epua * Zpua;

    if intee > 0.0:
        AApv = 4.0
    else:
        AApv = 0.0
    return AApv


def AAtv():
    global era, v, prv

    intee = era * v[0, 2] - prv

    if intee > 0.0:
        AAtv = 4.0
    else:
        AAtv = 0.0
    return AAtv


def rungekutta(subresultcr):
    global Aav, Amv, Apv, Atv, dvq
    global dv, v, dq, q, ddt

    # call Integrated_ode % == == == == == = make a note........................
    Integrated_ode()

    # Declaration of variables
    dfl = np.zeros(shape=(2, 30))
    dq = np.zeros(shape=(2, 15))
    subrukuk = np.zeros(shape=(4, 29))
    inter = np.zeros(shape=(2, 29))
    newpara = np.zeros(shape=(2, 29))

    # -------------------------------------------------------------------------
    dfl[0, :29] = dvq[0, :29]
    dq[0, :7] = dfl[0, 1:14:2]
    dq[0, 7:15] = dfl[0, 14:29:2]
    dv[0, :7] = dfl[0, 0:13:2]
    dv[0, 7:14] = dfl[0, 15:28:2]


    for nrk in np.arange(4):
        subrukuk[nrk, :29] = np.multiply(ddt, dfl[0, :29])

        if nrk == 0:
            Aav = AAav()
            Amv = AAmv()
            Apv = AApv()
            Atv = AAtv()

        if nrk < 3:
            inter[0, :29] = np.multiply(0.5, subrukuk[nrk, 0:29])
        else:
            inter[0, :29] = subrukuk[nrk, 0:29]

    inter[0, 0:29] = np.multiply(0.5, subrukuk[nrk, 0:29])
    newpara[0, 0:29] = np.add(subresultcr[0, 0:29], inter[0, 0:29])

    q[0, :7] = newpara[0, 1:14:2]
    q[0, 7:15] = newpara[0, 14:29:2]

    v[0, :7] = newpara[0, 0:13:2]
    v[0, 7:14] = newpara[0, 15:28:2]

    return subrukuk

# End of function definition ----------------------------------

def main():
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
    global timestep, Tduration, ddt, tee, tcr, tac, tar, t, odic

    v = np.zeros(shape=(2, 14))
    q = np.zeros(shape=(2, 21))
    dvq = np.zeros(shape=(2, 29))
    result = np.zeros(shape=(2, 101))
    P_0d = np.zeros(shape=(2, 101))
    diffv = np.zeros(shape=(2, 14))
    resultcr = np.zeros(shape=(2, 101))
    dv = np.zeros(shape=(2, 21))
    MyResult = np.zeros(shape=(100000, 28))
    MyResult1 = np.zeros(shape=(100000, 29))

    # initial values of all state equations (should be equal to number of equations in dvdqsdvdq.m file)
    odic = np.array(
        [1068.2371, 52.4983, 181.7233, -41.7618, 65.0625, 0, 122.6637, 0, 67.0272, -0.3118, 135.1100, -2.1737, 198.7568,
         -64.1791, 0, 2.7983, 0.1357, 2.7932, 1.1042, 68.8587, 0, 121.2539, 0, 67.3641, 41.8262, 22.0472, 56.6627,
         1.8539, 57.6473])

    Pit = -2.5
    pit = Pit
    jj = 0

    # --------------------------------------------------------------------------------
    Elva = 2.87   # !Peak-systolic elastance of left ventricle
    Elvb = 0.06   # !Basic diastolic elastance of left ventricle
    Elaa = 0.07   # !Peak-systolic elastance of left atrium
    Elab = 0.075  # !Basic diastolic elastance of left atrium
    Erva = 0.52   # !Peak-systolic elastance of right ventricle
    Ervb = 0.043  # !Basic diastolic elastance of right ventricle
    Eraa = 0.055  # !Peak-systolic elastance of right atrium
    Erab = 0.06   # !Basic diastolic elastance of right atrium

    Vmax = 900     # Reference volume of Frank-Starling law
    Es = 45.9      # !Effective septal elastance
    Vpc0 = 380.0   # !Reference total pericardial and cardiac volume old value 380
    Vpe = 30.0     # !Pericardial volume of heart
    Vcon = 40.0    # !Volume constant
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
    Epua0 = 0.0200
    Epuc0 = 0.0200
    Epuv0 = 0.0200
    Epwc0 = 0.7000
    Epwv0 = 0.7000
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
    yaor = 0.015
    yart = 0.05
    ycap = 0.0005
    yven = 0.0005
    yvca = 0.0005
    Raor = 0.08
    Rart = 0.8
    Rcap = 0.35
    Rven = 0.07
    Rvca = 0.001
    Saor = 0.01
    Sart = 0.01
    Scap = 0.01
    Sven = 0.01
    Svca = 0.01
    qco = 0.0

    # ------------------------------------------------------------------------------------------------
    Tduration = 1/65  # input('Please specify cardiac duration(s)')
    dt = 0.0001  # input'Please specify time step(s)')
    tee = 0.3*np.sqrt(Tduration) #!Moment when ventricular contractility reaches the peak
    tac = Tduration - 0.5 * tee - 0.02 * (Tduration/0.855)  # !Moment when atrium begins to contract
    tar = Tduration - 0.02 * (Tduration / 0.855)  # !Moment when atrium begins to relax
    ddt = dt
    ncycle = 0 #GET INPUT FORM USER THROUGH TEXTBOX
    ntotal = ((ncycle) * Tduration / dt)
    ntotal = int(ntotal)

    # ------------------------------------------------------------------------
    for nstep in np.arange(ntotal):
        if nstep == 0:
            tcr = 0.0
            ppc = 0.0
            cn =0

            i = 0
            for i in range(29):
                result[0, i] = odic[i]

            i = 0
            for i in np.arange(14):
                if i <= 6:
                    v[0, i] = result[0, 2 * i]
                else:
                    v[0, i] = result[0, 2 * i + 1]

            i =0
            for i in np.arange(15):
                if i <= 6:
                    q[0, i] = result[0, 2 * i + 1]
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

            # fid60  =  fopen('0Dresult.txt','a+')
            # fid63  =  fopen('0Dpress.txt','a+')

        # ----------------------Start computation---------------------------
        ncount = 0
        ncountadd = ncount + 1

        cn += 1
        tcr = cn * dt % Tduration

        print('tcr of ', cn,':', tcr)
        t = cn * dt

        # c.... Compute the pulmonary elastances
        Epua = Ecal(Epua0, Zpua, v[0, 4])
        Epuc = Ecal(Epuc0, Zpuc, v[0, 5])
        Epuv = Ecal(Epuv0, Zpuv, v[0, 6])
        Epwc = Ecal(Epwc0, Zpwc, v[0, 7])
        Epwv = Ecal(Epwv0, Zpwv, v[0, 8])

        # c.....Update nolinear cardiac parameters
        if tcr == 0.0:
            FL = 1.0 - (result[0, 21] / Vmax)  # Left ventricle scaling factor
            FR1 = 1.0 - (result[0, 6] / Vmax)  # Right ventricle scaling factor

        Lvecal()  # LV elastance function calling
        Laecal()  # LA elastance function calling
        Rvecal()  # RV elastance function calling
        Raecal()  # RA elastance function calling

        # Spetum cross talk pressure calculations
        cklr = erv / (Es + erv)
        ckrl = elv / (Es + elv)
        plv = ckrl * Es * v[0, 10] + ckrl * cklr * Es * v[0, 3] / (1.0 - cklr)
        prv = cklr * Es * v[0, 3] + ckrl * cklr * Es * v[0, 10] / (1.0 - ckrl)

        # All cardiac chambers viscoelastance calculation
        Sla = Sva0 * v[0, 9] * ela
        Slv = Sva0 * plv
        Sra = Sva0 * v[0, 2] * era
        Srv = Sva0 * prv

        # Pericardium pressure calculations
        ppp = (v[0, 2] + v[0, 3] + v[0, 9] + v[0, 10] + Vpe - Vpc0) / Vcon
        ppc = np.exp(ppp)

        # c....Update dv and state equation function calling
        Integrated_ode()  # = == == == == == == == == == == == == == = >> make a note.............................

        diffv[0, :7] = dvq[0, 0:13:2]
        diffv[0, 7:14] = dvq[0, 15:28:2]
        dv[0, :14] = diffv[0, :14]

        # c.....Implement fourth - order Runge - Kutta method
        resultcr[0, :101] = result[0, :101]
        rukuk = rungekutta(resultcr)

        # c.....Update variables with Runge-Kutta method
        for j in np.arange(29):
            result[ncountadd, j] = result[ncount, j] + (rukuk[0, j] + 2.0 * (rukuk[1, j] + rukuk[2, j]) + rukuk[3, j]) / 6.0

        delta = 0.00000001

        # update all four cardiac valve flow as zero when they were closed
        if (Aav == 0.0 and resultcr[0, 22] <= delta):
            resultcr[0, 22] = 0.0
            result[ncountadd, 22] = 0.0
            q[0, 11] = 0.0

        if (np.abs(tcr - Tduration) <= ddt * 0.5 or tcr < 0.1 or (Amv == 0.0 and resultcr[0, 20]) <= delta):
            resultcr[0, 20] = 0.0
            resultcr[ncountadd, 20] = 0.0
            q[0, 10] = 0.0

        if (Apv == 0.0) and (resultcr[0, 7] <= delta):
            resultcr[0, 7] = 0.0
            resultcr[ncountadd, 7] = 0.0
            q[0, 3] = 0.0

        if np.abs(tcr - Tduration) <= ddt * 0.5 or tcr < 0.1 or Atv == 0.0 and resultcr[0, 5] <= delta:
            resultcr[0, 5] = 0.0
            result[ncountadd, 5] = 0.0
            q[0, 2] = 0.0

        # c.....Update q() and v() to be used at next time
        v[0, :7] = result[ncountadd, 0:13:2]
        v[0, 7:14] = result[ncountadd, 15:28:2]

        q[0, : 7] = result[ncountadd, 1:14:2]
        q[0, 7: 15] = result[ncountadd, 14:29:2]
        q[0, 15: 21] = result[ncountadd, 29:35:1]
        result[0, :29] = result[1, :29]

        # load calculated hemodynamic variables in an array
        jj += 1
        print('Value of JJ:', jj - 1)
        MyResult[jj - 1, :27] = P_0d[0, :27]
        MyResult1[jj - 1, :29] = result[0, :29]

        # Update the initial conditions for next cardiac cycle
        if nstep+1 == ntotal:
            odic_new = result[0, :29]

    stp_sz = Tduration * ncycle
    t = np.arange(0, stp_sz, dt)
    T = t
    Pa_1 = MyResult1[:ntotal, 23]  #23
    F_1 = MyResult1[:ntotal, 22]   #22

    plt.figure()
    plt.plot(T, F_1, label='Flow')
    lg = plt.legend()

    plt.figure()
    plt.plot(T, Pa_1, label='Pressure')
    lg = plt.legend()
    plt.show()

if __name__ == "__main__":
    main()