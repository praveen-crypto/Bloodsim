import numpy as np
import math as m


def steno(M, R, G, **data):
    #s = datetime.datetime.now()
    RLCtru = np.zeros(shape=(128,4))
    D = np.zeros(shape=(128))                            #easier to type # creating empty arrays of size 128,0
    mu = M                                               #0.04  #blood viscosity
    rho = R                                              #1.05       #blood density
    G0 =  G                                              #0.6   #Reflection coefficient
    pi = m.pi                                            #value of pi
    pos = []
    values = []
    for keys, value in data.items():
        #print(keys,value)
        pos.append(int(keys))
        if value is None:
            values.append(0)
        else: values.append(value)
    j = 0
    for i in pos:
        D[i] = values[j]
        j = j +1
    at = np.genfromtxt('DB/arterytree.txt', delimiter=',')
    l = at[:, 0]                                          #assigning l with dataframe of 0th col of a variable
    r = at[:, 1]                                          #assigning r with dataframe of 1st col of a variable
    h = at[:, 2]                                          #assigning h with dataframe of 2nd col of a variable
    E = np.multiply(at[:, 3], 10e+5)                      #assigning E with dataframe of 3rd col of a variable
    RLCtru[:, 0] = np.true_divide(8*mu*l, np.power(pi*np.multiply(np.subtract(r, D), r), 4))   #8*mu*l ./ (pi*(r-D.*r).^4);
    RLCtru[:, 1] = np.true_divide(np.multiply(l, rho), ((pi*np.power(np.multiply(np.subtract(r, D), r), 2))))   # l.*rho ./ ((pi*(r-D.*r).^2))
    RLCtru[:, 2] = np.multiply(np.multiply(3*pi, l), np.true_divide(np.power(np.multiply(np.subtract(r, D), r), 3), np.multiply(2*E, h)))  #3*pi.*l .* (r-D.*r).^3./(2*E.*h)
    c0 = np.true_divide(np.multiply(E, h), rho*(np.multiply(np.subtract(r, D), r)))    #(E.*h./(rho*(r-D.*r))).^0.5
    c0 = np.sign(c0) * (np.abs(c0)) ** (1 / 2)
    R0 =  np.true_divide(rho*c0, np.power(pi*np.multiply(np.subtract(r, D), r), 2 ))     #rho*c0./(pi*(r-D.*r).^2)
    RLCtru[:, 3] = R0 *(1+G0)/(1-G0)
    np.savetxt("DB/RLCtru.txt", RLCtru,delimiter=",")


if __name__ == "__main__":
    import datetime
    stn_dat = {'0': None, '1': 3, '7': 4, '13':6, '3': 7, '11': 20, '10': 0, '51': 0, '46': 0,
               '74': 0, '56': None, '70': 0, '62': 0, '63': 0, '108': 0, '109': 0, \
               '102': 0, '107': 0, '96': 0, '92': 55}
    steno(**stn_dat)
