import numpy as np
import math


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
       ela = Elaa * 0.5 * (1.0 - np.cos(3.1415926 * (tcal - tac) / teec)) + Elab

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
   intee = prv - Epua * Zpua
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

global  DL_O2, CtCO2,_ao, CtCO2_pa, alphaCO2, DL_CO2

odic = [80, 3565, 3300, -80, -5.6, 3565, 134.08, 125.95, 106.26, 13.21, 19.967, 36.26, 96.1, 34.92, 19.486, 36.499, 66.54, 67, 1068.2371, 52.4983, 181.7233, -41.7618, 65.0625, 0, 122.6637, 0, 67.0272, -0.3118, 135.11, -2.1737, 198.7568, -64.1791, 0, 2.7983, 0.1357, 2.7932, 1.1042, 68.8587, 0, 121.2539, 0, 67.3641, 41.8262, 22.0472, 56.6627, 1.8539, 57.6473]

dv = np.zeros(shape=(2, 21))
q = np.zeros(shape=(2, 101))
v = np.zeros(shape=(2, 101))
result = np.zeros(shape=(2, 101))
#P_0d = np.zeros(shape=(2, 101))
#diffv = np.zeros(shape=(2, 14))
resultcr = np.zeros(shape=(2, 101))
#dv = np.zeros(shape=(2, 21))
#MyResult = np.zeros(shape=(100000, 28))
#MyResult1 = np.zeros(shape=(100000, 29))




Pit = -2.5

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

Vmax = 900.0  # Reference volume of Frank-Starling law
Es = 45.9  # !Effective septal elastance
Vpc0 = 380.0  # !Reference total pericardial and cardiac volume
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
FRC = 3.9


VT = 0.5
Rv = 1650
TLC = 5550
VD = 185
RespR = 10
Ac = 7.09 / 1.36
Al = 0.2 / 1.36
As = 2.2 / (1.36*1000)
Au = 0.34 / (1.36*1000)
Bc = 37.3 / 1.36
Bcp = 3.73 / 1.36
Bl = -0.5 / 1.36
Bs = 0.02 / (1.36*1000)
Cve = 0.5*(1.36*1000)
Kc_air = 0.21 / (1.36*1000)
Kl = 1 / 1000
Ks = -10.9
Ku = 0.46 / math.pow(1.36*10, 6)
Rve = 1 / (1.36*1000)
Vstar = 5.3*1000
Vcmax = 0.185*1000
A = -2.17
B = 5.6
f = 15
tau = 0.1
f1 = f / 60


####################GasExchange##############
Tbody = 300
Pstp = 760
Tstp = 273
nH = 3.5
P50_O2 = 26.5
CHb = 0.0000204
Hcrit = 0.45
alphaO2 = 1.36E-09
Vpcmax = 0.07125*1000
Visf = 48000
PS1 = 166.67
Vcytox = 0.21
Kcytox = 1.00E-12
P50_CO2 = 250
alphaCO2 = 3.26E-08
RQ = 0.8
Pao = 760
PH2O = 47
tweight = 60
r_Pao_O2 = 2.10E-01
r_Pao_CO2 = 0.0003


#CO2flux = 0
#O2flux = 0

#---------------------------------------
Tduration = 0.8
dt = 0.002
tee = 0.3 * math.sqrt(Tduration)
tac = Tduration - 0.5 * tee - 0.02 * (Tduration / 0.855)
tar = Tduration - 0.02 * (Tduration / 0.855)
ddt = dt
ncycle = 10
ntotal = ((ncycle) * Tduration)

for nstep in np.arange(0, ntotal, ddt):
   if nstep == 0:
       tcr = 0
       ppc = 0.0
       result = np.zeros(shape=(2, 101))

       result[0, :47] = odic

       for i in np.arange(18):
           if i < 6:
               q[0, i] = result[0, i]
           #else:
            #   q[0, i] = result[0, 2*i-1]

       q[0, 18:25] = result[0, 19:32:2]
       q[0, 25:33] = result[0, 32:47:2]

       v[0, :7] = result[0, 18:31:2]
       v[0, 7:14] = result[0, 33:46:2]

       STR = 1.0
       FL = 1.0
       FR1 = 1.0
       Gpw = 0.0

       Aav = 0.0
       Amv = 0.0
       Apv = 0.0
       Atv = 0.0

       P_0d = np.zeros(shape=(2, 101))

   ncount = 1
   ncountadd = ncount + 1
   resultcr[0, :47] = result[0, :47]
   tcr = math.remainder(nstep, Tduration)
   tresp = math.remainder(nstep, 4)

   pit = Pit
   Epua = Ecal(Epua0, Zpua, v[0, 4])
   Epuc = Ecal(Epuc0, Zpuc, v[0, 5])
   Epuv = Ecal(Epuv0, Zpuv, v[0, 6])
   Epwc = Ecal(Epwc0, Zpwc, v[0, 7])
   Epwv = Ecal(Epwv0, Zpwv, v[0, 8])

   if tcr == 0.0:
       Fl = 1.0 - (result[0, 30] / Vmax)
       FR1 = 1.0 - (result[0, 25] / Vmax)

   Lvecal()
   Laecal()
   Rvecal()
   Raecal()

   cklr = erv / (Es + erv)
   ckrl = elv / (Es + elv)
   plv = (ckrl*Es*v[0, 10] + ckrl*cklr*Es*v[0, 3]) / (1.0 - cklr)
   prv = (cklr*Es*v[0, 3] + cklr*ckrl*Es*v[0, 10]) / (1.0 - ckrl)

   Sla = Sva0 * v[0, 9] * ela
   Slv = Sva0 * plv
   Sra = Sva0 * v[0, 2] * era
   Srv = Sva0 * prv
   ppp = (v[0, 2] + v[0, 3] + v[0, 9] + v[0, 10] + Vpe - Vpc0) / Vcon
   ppc = math.exp(ppp)

   Vcw = q[0, 2] + VD
   aa = Vcmax / q[0, 0]
   bb = 1 / aa
   Rco = 0
   if (q[0, 0] > Vcmax):
       Rc = Kc_air + Rco
   else:
       Rc = Kc_air * math.pow((Vcmax / q[0, 0]), 2) + Rco

   al = q[0, 2] - Rv
   a2 = Ks * al
   a3 = Vstar - Rv
   a4 = math.exp((a2/a3))
   Rs = As * a4 + Bs
   Ru = Au + Ku * abs(q[0, 1])

   pcw = (A* np.sin(2*math.pi*f1*tresp) - B)
   Pl = Al * math.exp((Kl*q[0, 2])) + Bl

   if bb < 0.5:
       Pc = Ac - Bc * math.pow((q[0, 0]/Vcmax - 0.7), 2)
   else:
       Pc = Ac - Bc * math.pow((0.5 - 0.7), 2) - Bcp * math.log((Vcmax/q[0, 0] - 0.999), 10)

   Pve = q[0, 3] / Cve
   Ppl = pcw
   Pit = Ppl
   pit = Pit

   Pbs = 0
   PplmmHg = Ppl
   Pmouth = Pbs

   Pplc = Ppl
   PA = Ppl + Pve + Pl

   Pcc = Pplc + Pc
   Ps = Pcc - PA
   Qdotco = (Pmouth-Pcc) / (Ru+Rc)
   Qdotup = Qdotco
   Qdotve = Pve/Rve
   Qdotsm = Ps/Rs

   PD = Qdotup * Ru
   Qdotca = Pc + Ppl - PA/Rs
   Qdotdc = PD-Pc-Ppl/Rc
   Qdoted = Qdotdc

   Vpc = 114+5* np.sin((math.pi/0.855)*tcr)
   Vsc = 300 + 14 * np.sin((math.pi / 0.855) * tcr)

   if v[0, 5] > 155:
       DL_O2 = ((0.397 /22400)+((0.0085/22400 )*q[0, 12])-((0.00013/22400 )*math.pow(q[0, 12], 2)))+((5.1e-7)/22400 *math.pow(q[0, 12], 3))
   else:
       DL_O2 = (math.sqrt(v[0, 5] / 155)) * ((0.397 / 22400) + ((0.0085 / 22400) * q[0, 12]) - ((0.00013 / 22400) * math.pow(q[0, 12], 2))) + ((5.1e-7) / 22400 * math.pow(q[0, 12], 3))

   if v[0, 5] > 155:
       DL_CO2 = (16.67 / 22400)
   else:
       DL_CO2 = (math.sqrt(v[0, 5] / 155)) * (16.67 / 22400)

   O2flux = DL_O2[q[0, 8]-q[0, 12]]*22400
   CO2flux = DL_CO2(q[0, 11] - q[0, 15])*22400
   Alvflux = (760 * 300 / ((PA + (760)) * 273)) * (O2flux + CO2flux)

   PD = Qdotup * Ru
   PDc = Qdotco * Rc + Pcc
   Pup = Qdotup * (Ru + Rc)

   SHbO2_ao = (math.pow(q[0, 12] / P50_O2), nH) / (math.pow((q[0, 12] / P50_O2), nH) + 1)
   SHbO2_pa = (math.pow(q[0, 13] / P50_O2), nH) / (math.pow((q[0, 13] / P50_O2), nH) + 1)
   SHbO2_aoISR = SHbO2_ao * 100

   dSHbO2dPO2_ao = nH * math.pow(q[0, 12], -1) * math.pow((q[0, 12] / P50_O2), nH) / math.pow((math.pow((q[0, 12] / P50_O2), nH) + 1), 2)
   dSHbO2dPO2_pa = nH * math.pow(q[0, 13], -1) * math.pow((q[0, 13] / P50_O2), nH) / math.pow((math.pow((q[0, 13] / P50_O2), nH) + 1), 2)

   CtO2_ao = alphaO2 * q[0, 12] + CHb * SHbO2_ao * Hcrit
   CtO2_pa = alphaO2 * q[0, 13] + CHb * SHbO2_pa * Hcrit
   CtO2_isf = alphaO2 * q[0, 14]

   if q[0, 14] <= 0:
       V_O2 = 0
   else:
       V_O2 = (Vcytox * tweight * alphaO2 * q[0, 14]) / (Kcytox + (alphaO2 * q[0, 14]))

   SHbCO2_ao = (q[0, 15] / P50_CO2) / ((q[0, 15] / P50_CO2) + 1)
   SHbCO2_pa = (q[0, 16] / P50_CO2) / ((q[0, 16] / P50_CO2) + 1)
   dSHbCO2dPCO2_ao = math.pow(q[0, 15], -1) * (q[0, 15] / P50_CO2) / math.pow(((q[0, 15] / P50_CO2) + 1), 2)
   dSHbCO2dPCO2_pa = math.pow(q[0, 16], -1) * (q[0, 16] / P50_CO2) / math.pow(((q[0, 16] / P50_CO2) + 1), 2)

   CtCO2_ao = alphaCO2 * q[0, 15] + CHb * SHbCO2_ao * Hcrit
   CtCO2_pa = alphaCO2 * q[0, 16] + CHb * SHbCO2_pa * Hcrit
   CtCO2_isf = alphaCO2 * q[0, 17]

   V_CO2 = 0.8 * V_O2
   Pao_O2 = (Pao - PH2O) * r_Pao_O2
   Pao_CO2 = (Pao - PH2O) * r_Pao_CO2

   Pmouth_CO2 = q[0, 9]

   dvdqsdvsdq11()

   diffq[0, :18] = dvq[0, :18]
   diffv[0, :7] = dvq[0, 18:30:2]
   diffv[0, 7:13] = dvq[0, 33:45:2]
   dv[0, :14] = diffv[0, :14]
   rukuk = ngekutta11(resultcr)

   for i in np.arange(47):
       result[ncountadd, i] = result[ncount, i]+(rukuk[0,i]+2.0*(rukuk[1,i]+rukuk[2,i])+(rukuk[3,i])) / 6.0

   delta = 0.00000001

   if ((Aav == 0.0) and (resultcr[0, 22] <= delta)):
       resultcr[0, 40] = 0.0
       result[ncountadd, 40] = 0.0
       q[29] = 0.0

   if (abs(tcr-Tduration) <= ddt*0.5 or tcr<0.1 or (Amv == 0 and resultcr[0, 38] <= delta)):
       resultcr[0, 38] = 0.0
       result[ncountadd, 38] = 0.0
       q[28] = 0.0

   if ((Apv == 0.0) and (resultcr[0, 25] <= delta)):
       resultcr[0, 25] = 0.0
       result[ncountadd, 25] = 0.0
       q[21] = 0.0

   if (abs(tcr - Tduration) <= ddt * 0.5 or tcr < 0.1 or (Atv == 0.0 and resultcr[0, 23] <= delta)):
       resultcr[0, 23] = 0.0
       result[ncountadd, 23] = 0.0
       q[20] = 0.0

   q[0, :18] = result[ncountadd, 1:18]
   q[0, 18:24] = result[ncountadd, 19:31:2]
   q[0, 25:32] = result[ncountadd, 32:46:2]

   v[0, :7] = result[ncountadd, 18:30:2]
   v[0, 7:13] = result[ncountadd, 33:45:2]

   result[0, :47] = result[1, :47]

   jj = jj + 1

   MyResult[jj, 0] = CO2flux
   MyResult[jj, 1] = O2flux
   MyResult[jj, 2] = Qdoted
   MyResult[jj, 3] = Ppl

   MyResult1[jj, :47] = result[0, :47]
   MyResult1[jj, 47] = tcr
   MyResult2[jj, :27] = P_0d[0, :27]

   if nstep == ntotal:
       odic_new = result[0, :47]





