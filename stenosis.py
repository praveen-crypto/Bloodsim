import numpy as np
import pandas as pd;       import math as m

RLCtru = np.zeros(shape=(128,4))
D = stenosis = 40 #np.zeros(shape=(128,1))                 #easier to type # creating empty arrays of size 128,1
mu = 0.04                                              #blood viscosity
rho = 1.05                                             #blood density
G0 = 0.6                                               #Reflection coefficient
pi = m.pi                                              # value of pi

at = np.genfromtxt('arterytree.txt', delimiter=',')

l = at[:, 0]                                            #assigning E with dataframe of 3rd column of a variable
r = at[:, 1]                                            #assigning E with dataframe of 3rd column of a variable
h = at[:, 2]                                            #assigning E with dataframe of 3rd column of a variable
E = np.multiply(at[:, 3], 10^6)                         #assigning E with dataframe of 3rd column of a variable

RLC = np.divide(8*mu*l, np.power(pi*np.multiply(r-D, r), 4))   #8*mu*l ./ (pi*(r-D.*r).^4);
RLCtru[:, 0] = RLC[0, :]


RLC1 = np.divide(np.multiply(l, rho), ((pi*np.power(np.multiply(r-D, r), 2))))    #l.*rho./((pi*(r-D.*r).^2))
RLCtru[:, 1] = RLC1[0, :]


RLC2 = np.multiply(np.multiply(3*pi, l), np.divide(np.power(np.multiply(r-D, r), 3), np.multiply(2*E, h)))  #3*pi.*l  .* (r-D.*r).^3./(2*E.*h)
RLCtru[:, 2] = RLC2[0, :]

c0 = np.zeros(shape=(128, 1))
c01 = np.power(np.divide(np.multiply(E, h), rho*(np.multiply(r-D, r))), 0.5)     #(E.*h./(rho*(r-D.*r))).^0.5
c0[:, 0] = c01[0, :]

R0 = np.zeros(shape=(128, 1))
R01 =  np.divide(rho*c0[:, 0], np.power(pi*np.multiply(r-D, r), 2 ))     #rho*c0./(pi*(r-D.*r).^2)
R0[:, 0] = R01[0, :]

RLC3 = R0 *(1+G0)/(1-G0)
RLCtru[:, 3] = RLC3[:, 0]