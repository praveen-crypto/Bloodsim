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
global S_peripheral, Saor, Sart, Scap, Sven
global sdvsdqdvdq, dvq, P_0d
global dvdq_cardiopul, dv, v, dq, q
global cardiac_parameter, elv, ela, erv, era, cklr, ckrl, plv, prv, Sla, Slv, Sra, Srv, ppp, ppc, pit, qco, FL, FR1, STR
global R_cardiopulc, Rav0, Rmv0, Rpv0, Rtv0, bav0, bmv0, bpv0, btv0, Rav1, Rmv1, Rpv1, Rtv1, bav1, bmv1, bpv1, btv1
global Rav2, Rmv2, Rpv2, Rtv2, bav2, bmv2, bpv2, btv2, yav0, ymv0, ypv0, ytv0, yav1, ymv1, ypv1, ytv1, yav2, ymv2, ypv2, ytv2
global n_val, m_cvst, m_cvrg, n_vrg
global timestep, Tduration, ddt, tcr, tee, tac, tar, t



def dvdqsdvsdq():



    dvq[0] = q[14] - q[0]  # Venous volume

    P_0d[0] = v[0] / Cven + Sven * dv[0]  # Venous  Pressure

    dvq[1] = [v[0] / Cven + Sven * dv[0] - Rven * q[0] - v[1] / Cvca - Svca * dv[1]] / yven  # Venous flow

    dvq[2] = q[0] - q[1]  # VC volume

    P_0d[1] = v[1] / Cvca + Svca * dv[1]  # VC Pressure

    dvq[3] = [v[1] / Cvca - era * v[2] - Rvca * q[1] + Svca * dv[1] - Sra * dv[2] - ppc - pit] / yvca  # VC Flow

    qco = 0.0

    dvq[4] = q[1] + qco - q[2]  # RA volume

    P_0d[3] = era * v[2] + Sra * dv[2] + ppc + pit  # RA pressure

    dvq[5] = [era * v[2] - prv - Rtv * q[2] - btv * q[2] * abs[q[2]] + Sra * dv[2] - Srv * dv[3]] / ytv  # TV flow
    # ============================================
    dvq[6] = q[2] - q[3]  # RV volume

    P_0d[5] = prv + Srv * dv[3] + ppc + pit  # RV pressure

    dvq[7] = [prv - Epua * Zpua - Rpv * q[3] - bpv * q[3] * [abs[q[3]]] + Srv * dv[3] - Spua * dv[
        4] + ppc] / ypv  # PV flow

    dvq[8] = q[3] - q[4] - q[7]  # Pulmonary Artery volume

    P_0d[7] = Epua * Zpua + Spua * dv[4] + pit  # Pulmonary Artery Pressure

    dvq[9] = [Epua * Zpua - Epuc * Zpuc - Rpua * q[4] + Spua * dv[4] - Spuc * dv[5]] / ypua  # Pulmonary Artery Flow
    # =========================================================
    dvq[10] = q[4] - q[5]  # Pulmonary Capillary volume

    P_0d[9] = Epuc * Zpuc + Spuc * dv[5] + pit  # Pulmonary Capillary Pressure

    dvq[11] = [Epuc * Zpuc - Epuv * Zpuv - Rpuc * q[5] + Spuc * dv[5] - Spuv * dv[6]] / ypuc  # Pulmonary Capillary Flow

    dvq[12] = q[5] - q[6]  # Pulmonary Vein volume

    P_0d[11] = Epuv * Zpuv + Spuv * dv[6] + pit  # Pulmonary Vein Pressure

    dvq[13] = [Epuv * Zpuv - ela * v[9] - Rpuv * q[6] + Spuv * dv[6] - Sla * dv[9] - ppc] / ypuv  # Pulmonary Vein flow

    if [Gpw > 0]:
        dvq[14] = [Epua * Zpua - Epwc * Zpwc - q[7] / gpw + Spua * dv[4] - Spwc * dv[
            7]] / ypwa  # Pulmonary Wedge ##Artery flow
    else:
        dvq[14] = 0

    dvq[15] = q[7] - q[8]  # Pulmonary Wedge capillary volume

    P_0d[14] = Epwc * Zpwc + Spwc * dv[7] + pit  # Pulmonary Wedge capillary Pressure

    dvq[16] = [Epwc * Zpwc - Epwv * Zpwv - Rpwc * q[8] + Spwc * dv[7] - Spwv * dv[
        8]] / ypwc  # Pulmonary Wedge capillary Flow

    dvq[17] = q[8] - q[9]  # Pulmonary Wedge vein Volume

    P_0d[16] = Epwv * Zpwv + Spwv * dv[8] + pit  # Pulmonary Wedge vein Pressure

    dvq[18] = [Epwv * Zpwv - ela * v[9] - Rpwv * q[9] + Spwv * dv[8] - Sla * dv[
        9] - ppc] / ypwv  # Pulmonary Wedge vein Flow

    dvq[19] = q[6] + q[9] - q[10]  # LA volume

    P_0d[18] = ela * v[9] + Sla * dv[9] + ppc + pit  # LA Pressure

    dvq[20] = [ela * v[9] - plv - Rmv * q[10] - bmv * q[10] * abs[q[10]] + Sla * dv[9] - Slv * dv[
        10]] / ymv  # Mitral flow

    dvq[21] = q[10] - q[11]  # LV volume

    P_0d[20] = plv + Slv * dv[10] + ppc + pit  # LV Pressure

    dvq[22] = [plv - v[11] / Caor - Rav * q[11] - [bav * q[11]] * abs[q[11]] + Slv * dv[10] - Saor * dv[
        11] + ppc + pit] / yav  # Aortic Flow

    # Adjust the state of cardiac valve
    if Aav == 0.0 and q[12] <= 0.000000001:
        dvq[22] = 0.

    if (abs(tcr - Tduration) <= ddt * 0.5 or tcr < 0.1) or (Amv == 0.0 and q[10] < 0.000000001):
        dvq[20] = 0.0

    if Apv == 0.0 and q[3] <= 0.00000001:
        dvq[7] = 0.0

    if abs(tcr - Tduration) <= ddt * 0.5 or tcr < 0.1 or (Atv == 0.0 and q[2] <= 0.000000001):
        dvq[5] = 0.0

    dvq[23] = q[11] - q[12]  # Aorta volume

    P_0d[22] = v[11] / Caor + Saor * dv[11]  # Aorta Presuure

    dvq[24] = [v[11] / Caor + Saor * dv[11] - q[12] * Raor - v[12] / Cart - Sart * dv[12]] / yaor  # Aorta Flow
    dvq[25] = q[12] - q[13]  # Artery Volume

    P_0d[24] = v[12] / Cart + Sart * dv[12]  # Artery Pressure

    dvq[26] = [v[12] / Cart + Sart * dv[12] - q[13] * Rart - v[13] / Ccap - Scap * dv[13]] / yart  # Artery Flow

    dvq[27] = q[13] - q[14]  # Capillarya Volume

    P_0d[26] = v[13] / Ccap + Scap * dv[13]  # Capillary Pressure

    dvq[28] = [v[13] / Ccap + Scap * dv[13] - q[14] * Rcap - v[0] / Cven - Sven * dv[0]] / ycap  # Capillary Pressure
