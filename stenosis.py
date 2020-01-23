import numpy as np; import csv
import math as m

def steno(p, value):
    RLCtru = np.zeros(shape=(128,4))
    D = np.zeros(shape=(128))                            #easier to type # creating empty arrays of size 128,1
    mu = 0.04                                            #blood viscosity
    rho = 1.05                                           #blood density
    G0 = 0.6                                             #Reflection coefficient
    pi = m.pi                                            #value of pi

    p = int(p)
    value = int(value)

    D[p] = value
    print(D[p])
    print('stenosis activated')
    at = np.genfromtxt('arterytree.txt', delimiter=',')

    l = at[:, 0]                                          #assigning E with dataframe of 3rd column of a variable
    r = at[:, 1]                                          #assigning E with dataframe of 3rd column of a variable
    h = at[:, 2]                                          #assigning E with dataframe of 3rd column of a variable
    E = np.multiply(at[:, 3], 10e+5)                      #assigning E with dataframe of 3rd column of a variable    E = a(:,4).*10^6;

    RLCtru[:, 0] = np.true_divide(8*mu*l, np.power(pi*np.multiply(np.subtract(r, D), r), 4))   #8*mu*l ./ (pi*(r-D.*r).^4);

    RLCtru[:, 1] = np.true_divide(np.multiply(l, rho), ((pi*np.power(np.multiply(np.subtract(r, D), r), 2))))   # l.*rho ./ ((pi*(r-D.*r).^2))

    RLCtru[:, 2] = np.multiply(np.multiply(3*pi, l), np.true_divide(np.power(np.multiply(np.subtract(r, D), r), 3), np.multiply(2*E, h)))  #3*pi.*l .* (r-D.*r).^3./(2*E.*h)

    #c0 = np.dtype(object)
    c0 = np.true_divide(np.multiply(E, h), rho*(np.multiply(np.subtract(r, D), r)))    #(E.*h./(rho*(r-D.*r))).^0.5
    c0 = np.sign(c0) * (np.abs(c0)) ** (1 / 2)

    R0 =  np.true_divide(rho*c0, np.power(pi*np.multiply(np.subtract(r, D), r), 2 ))     #rho*c0./(pi*(r-D.*r).^2)

    RLCtru[:, 3] = R0 *(1+G0)/(1-G0)

    np.savetxt("RLCtru.csv", RLCtru,delimiter=",")
    print('Finished')

if __name__ == "__main__":
    steno(2, 0)