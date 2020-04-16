def dvdqsdvsdq11():
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
    global cardiac_parameter, elv, ela, erv, era, cklr, ckrl, plv, prv, Sla, Slv, Sra, Srv, ppp, ppc, pit, Pit, qco, FL, FR1, STR
    global R_cardiopulc, Rav0, Rmv0, Rpv0, Rtv0, bav0, bmv0, bpv0, btv0, Rav1, Rmv1, Rpv1, Rtv1, bav1, bmv1, bpv1, btv1
    global Rav2, Rmv2, Rpv2, Rtv2, bav2, bmv2, bpv2, btv2, yav0, ymv0, ypv0, ytv0, yav1, ymv1, ypv1, ytv1, yav2, ymv2, ypv2, ytv2
    global n_val, m_cvst, m_cvrg, n_vrg
    global timestep, Tduration, ddt, tcr, tee, tac, tar
    global odic
    global Pao_O2, Pao_CO2, Vpc, Vsc, CtO2_ao, CtO2_pa, CtO2_isf, Visf, Qdotup
    global Rve, tau, Pplc, VD, Pstp, Tbody, O2flux, Tstp, CO2flux, tweight
    global Rc, Rs, Ru, Pcw, Pl, Pmus, Pc, Pve, Vcw, Ppl, PA, Qdotco, Qdotsm, Alvflux, Qdotve, Qdotca, Qdotdc, Qdoted
    global alphaO2, Hcrit, CHb, dSHbO2dPO2_ao, PS1, V_O2, V_CO2, dSHbO2dPO2_pa, dSHbCO2dPCO2_ao, dSHbCO2dPCO2_pa

    dvq[0, 0] = Qdotco - Qdotsm
    dvq[0, 1] = (q[0, 5] - q[0, 1]) / tau
    dvq[0, 2] = Qdotsm - Qdotve - Alvflux
    dvq[0, 4] = (Pplc - q[0, 4]) / 0.0001
    dvq[0, 5] = Qdotsm + Qdotco - Qdotsm - Alvflux

    if Qdotup > 0:
        dvq[0, 6] = (Qdotup * Pao_O2 - Qdotco * q[0, 6]) / 185
    else:
        dvq[0, 7] = (Qdotup * q[0, 7] - Qdotco * q[0, 7]) / 185

    if (Qdotup > 0 and Qdotsm > 0):
        dvq[0, 7] = (Qdotco*q[0, 6] - Qdotsm*q[0, 7] - q[0, 7] * (Qdotco-Qdotsm)) / q[0, 0]
    elif (Qdotup > 0 and Qdotsm < 0):
        dvq[0, 7] = (Qdotco * q[0, 6] - Qdotsm * q[0, 8] - q[0, 7] * (Qdotco - Qdotsm)) / q[0, 0]
    elif (Qdotup < 0 and Qdotsm > 0):
        dvq[0, 7] = (Qdotco * q[0, 7] - Qdotsm * q[0, 7] - q[0, 7] * (Qdotco - Qdotsm)) / q[0, 0]
    else:
        dvq[0, 7] = (Qdotco * q[0, 7] - Qdotsm * q[0, 8] - q[0, 7] * (Qdotco - Qdotsm)) / q[0, 0]

    if Qdotsm > 0:
        dvq[0, 8] = (Qdotsm * q[0, 7] - (760 * 300 / 273) * O2flux - (Qdotsm - Alvflux) * q[0, 8]) / q[0, 2]
    else:
        dvq[0, 8] = (Qdotsm * q[0, 8] - (760 * 300 / 273) * O2flux - (Qdotsm - Alvflux) * q[0, 8]) / q[0, 2]

    if Qdotup > 0:
        dvq[0, 9] = (Qdotup * Pao_CO2 - Qdotco * q[0, 9]) / 185
    else:
        dvq[0, 9] = (Qdotup * q[0, 9] - Qdotco * q[0, 10]) / 185

    if (Qdotup > 0 and Qdotsm > 0):
        dvq[0, 10] = (Qdotco * q[0, 9] - Qdotsm * q[0, 10] - q[0, 10] * (Qdotco - Qdotsm)) / q[0, 0]
    elif (Qdotup > 0 and Qdotsm < 0):
        dvq[0, 10] = (Qdotco * q[0, 9] - Qdotsm * q[0, 11] - q[0, 10] * (Qdotco - Qdotsm)) / q[0, 0]
    elif Qdotup < 0 and Qdotsm > 0:
        dvq[0, 10] = (Qdotco * q[0, 10] - Qdotsm * q[0, 10] - q[0, 10] * (Qdotco - Qdotsm)) / q[0, 0]
    else:
        dvq[0, 10] = (Qdotco * q[0, 10] - Qdotsm * q[0, 11] - q[0, 10] * (Qdotco - Qdotsm)) / q[0, 0]

    if (Qdotsm > 0):
        dvq[0, 11] = (Qdotsm * q[0, 10] - (760 * 300 / 273) * (CO2flux) - q[0, 11] * (Qdotsm - Alvflux)) / q[0, 2]
    else:
        dvq[0, 11] = (Qdotsm * q[0, 11] - (760 * 300 / 273) * (CO2flux) - q[0, 11] * (Qdotsm - Alvflux)) / q[0, 2]




    dvq[0, 12] = (q[0, 23] * (CtO2_pa - CtO2_ao) + DL_O2 * (q[0, 8] - q[0, 12])) / (v[0, 5] * (alphaO2 + Hcrit * CHb * dSHbO2dPO2_ao))

    dvq[0, 13] = (q[0, 32] * (CtO2_ao - CtO2_pa) + PS1 * tweight * alphaO2 * (q[0, 14] - q[0, 13])) / (
                (v[0, 13]) * (alphaO2 + Hcrit * CHb * dSHbO2dPO2_pa))

    dvq[0, 14] = PS1 * tweight * (q[0, 13] - q[0, 14]) / Visf - V_O2 / (alphaO2 * Visf)

    dvq[0, 15] = (q[0, 23] * (CtCO2_pa - CtCO2_ao) + DL_CO2 * (q[0, 11] - q[0, 15])) / (
                v[0, 5] * (alphaCO2 + Hcrit * CHb * dSHbCO2dPCO2_ao))

    dvq[0, 16] = (q[0, 32] * (CtCO2_ao - CtCO2_pa) + PS1 * tweight * alphaCO2 * (q[0, 17] - q[0, 16])) / (
                (v[0, 13]) * (alphaCO2 + Hcrit * CHb * dSHbCO2dPCO2_pa))

    dvq[0, 17] = PS1 * tweight * (q[0, 16] - q[0, 17]) / Visf + V_CO2 / (alphaCO2 * Visf)


    dvq[0, 18] = q[0, 32] - q[0, 18]

    P_0d[0, 0] = v[0, 0] / Cven + Sven * dv[0, 0]

    dvq[0, 19] = (v[0, 0] / Cven + Sven * dv[0, 0] - Rven * q[0, 18] - v[0, 1] / Cvca - Svca * dv[0, 1]) / yven

    dvq[0, 20] = q[0, 18] - q[0, 19]

    P_0d[0, 1] = v[0, 1] / Cvca + Svca * dv[0, 1]

    dvq[0, 21] = (v[0, 1] / Cvca - era * v[0, 2] - Rvca * q[0, 19] + Svca * dv[0, 1] - Sra * dv[0, 2] - ppc - pit) / yvca

    qco = 0.0

    dvq[0, 22] = q[0, 19] + qco - q[0, 20]

    P_0d[0, 3] = era * v[0, 2] + Sra * dv[0, 2] + ppc + pit

    dvq[0, 23] = (era * v[0, 2] - prv - Rtv * q[0, 20] - btv * q[0, 20] * abs(q[0, 20]) + Sra * dv[0, 2] - Srv * dv[0, 3]) / ytv

    dvq[0, 24] = q[0, 20] - q[0, 21]

    P_0d[0, 5] = prv + Srv * dv[0, 3] + ppc + pit

    dvq[0, 25] = (prv - Epua * Zpua - Rpv * q[0, 21] - bpv * q[0, 21] * (abs(q[0, 21])) + Srv * dv[0, 3] - Spua * dv[0, 4] + ppc) / ypv

    dvq[0, 26] = q[0, 21] - q[0, 24] - q[0, 25]

    P_0d[0, 7] = Epua * Zpua + Spua * dv[0, 4] + pit

    dvq[0, 27] = (Epua * Zpua - Epuc * Zpuc - Rpua * q[0, 22] + Spua * dv[0, 4] - Spuc * dv[0, 5]) / ypua

    dvq[0, 28] = q[0, 22] - q[0, 23]

    P_0d[0, 9] = Epuc * Zpuc + Spuc * dv[0, 5] + pit

    dvq[0, 29] = (Epuc * Zpuc - Epuv * Zpuv - Rpuc * q[0, 23] + Spuc * dv[0, 5] - Spuv * dv[0, 6]) / ypuc

    dvq[0, 30] = q[0, 23] - q[0, 24]

    P_0d[0, 11] = Epuv * Zpuv + Spuv * dv[0, 6] + pit

    dvq[0, 31] = (Epuv * Zpuv - ela * v[0, 9] - Rpuv * q[0, 24] + Spuv * dv[0, 6] - Sla * dv[0, 9] - ppc) / ypuv


    if(Gpw>0):
        dvq[0, 32]= (Epua * Zpua - Epwc * Zpwc - q[0, 25] / gpw + Spua * dv[0, 4] - Spwc * dv[0, 7]) / ypwa
    else:
        dvq[0, 32] = 0


    dvq[0, 33]=q[0, 25]-q[0, 26]

    P_0d[0, 14] = Epwc * Zpwc + Spwc * dv[0, 7] + pit

    dvq[0, 34]=(Epwc * Zpwc - Epwv * Zpwv - Rpwc *q[0, 26] + Spwc * dv[0, 7] - Spwv * dv[0, 8]) / ypwc

    dvq[0, 35] = q[0, 26] - q[0, 27]

    P_0d[0, 16] = Epwv * Zpwv + Spwv * dv[0, 8] + pit

    dvq[0, 36] = (Epwv * Zpwv - ela * v[0, 9] - Rpwv * q[0, 27] + Spwv * dv[0, 8] - Sla * dv[0, 9] - ppc) / ypwv

    dvq[0, 37] = q[0, 24] + q[0, 27] - q[0, 28]

    P_0d[0, 18] = ela * v[0, 9] + Sla * dv[0, 9] + ppc + pit

    dvq[0, 38] = (ela * v[0, 9] - plv - Rmv * q[0, 28] - bmv * q[0, 28] * np.abs(q[0, 28]) + Sla * dv[0, 9] - Slv * dv[0, 10]) / ymv

    dvq[0, 39] = q[0, 28] - q[0, 29]

    P_0d[0, 20] = plv + Slv * dv[0, 10] + ppc + pit

    dvq[0, 40] = (plv-v[0, 11] / Caor - Rav * q[0, 29] - (bav * q[0, 29]) * np.abs(q[0, 29]) + Slv * dv(11) - Saor * dv[0, 11] + ppc + pit) / yav

    #% Adjust the state of cardiac valve
    if Aav == 0.0 and q[0, 29] <= 0.000000001:
        dvq[0, 40] = 0.0

    if np.abs (tcr - Tduration) <= ddt * 0.5 or tcr < 0.1 or (Amv == 0.0 and q[0, 28] < 0.000000001):
        dvq[0, 38] = 0.0

    if Apv==0.0 and q[0, 21] <= 0.00000001:
        dvq[0, 25] = 0.0

    if abs(tcr - Tduration) <= ddt*0.5 or tcr<0.1 or (Atv == 0.0 and q(21) <= 0.000000001):
        dvq[0, 23] = 0.0

    dvq[0, 41] = q[0, 29] - q[0, 30]

    P_0d[0, 22] = v(12) / Caor + Saor * dv[0, 11]  # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%changed%%%%%%%%%%%%%%%%%%%%%%

    dvq[0, 42] = ( v[0, 11] / Caor + Saor * dv[0, 11] - q[0, 30] * Raor - v[0, 12] / Cart - Sart * dv[0, 12])/yaor

    dvq[0, 43] = q[0, 30] - q[0, 31]

    P_0d[0, 24] = v[0, 12] / Cart + Sart * dv[0, 12]

    dvq[0, 44] = ( v[0, 12] / Cart + Sart * dv[0, 12] - q[0, 31] * Rart - v[0, 13] / Ccap -  Scap * dv[0, 13]) / yart

    dvq[0, 45] = q[0, 31] - q[0, 32]

    P_0d[0, 26] = v[0, 13] / Ccap + Scap * dv[0, 13]

    dvq[0, 46] = (v[0, 13] / Ccap + Scap * dv[0, 13] - q[0, 32] * Rcap - v[0 ,0]/ Cven - Sven * dv[0, 0])/ycap

