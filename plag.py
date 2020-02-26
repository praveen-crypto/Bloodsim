import numpy as np

plv = 7.280601607170047
Slv= 0.0036403008035850236
ppc = 0.34853033782078907;pit = -2.5
Saor =  0.01;Sart =  0.01
Scap = 0.01;Sven = 0.01
Caor = 0.95;Ccap =  0.06
Cart = 0.45
Cven = 100.0
Rav = 0.0005
Raor = 0.08
Rart =   0.8; Rcap = 0.35
yav =  0.0005; bav = 0.000025
yaor = 0.015;yart = 0.05 ; ycap = 0.0005

#array declaration
v11 =0.067; v12 = 22.0472;
v13 = 0.0019; v0=1068.2371
dv11 = 0 ; dv12=0 ; dv13 =0; dv0 =0;dv10 =0
q11 = 0; q12 = 41.8262;q13 = 56.6627;q14=57.6473

dvq22 = (plv - v11) / Caor - Rav * q11 - bav * q11 * 0.0 + Slv * dv10 - Saor * dv11 + ppc + pit / yav
dvq24 = (v11 / Caor + Saor * dv11 - q12 * Raor - v12 / Cart - Sart * dv12) / yaor
dvq26 = (v12 / Cart + Sart * dv12 - q13 * Rart - v13 / Ccap - Scap * dv13) / yart
dvq28 = (v13 / Ccap + Scap * dv13 - q14 * Rcap - v0 / Cven - Sven * dv0) / ycap
print('22 =',dvq22)
print('24 =', dvq24)
print('26 =',dvq26)
print('28 =', dvq28 )