import numpy as np

global tcr

def Ecal(EEE,ZZZ,vol) :
    global tcr
    EcalR = EEE* np.exp(vol/ZZZ)
    return EcalR

def Lvecal():
    global Elva, Elvb
    global elv, tcr
    global tee, FL
    tcal = tcr

    if tcal <= tee :
        elv = FL * Elva * 0.5 * (1.0 - np.cos(3.1415926 * tcal / tee)) + Elvb / FL
    else:
        if tcal <= 1.5 * tee :
            elv = FL * Elva * 0.5 * (1.0 + np.cos(3.1415926 * (tcal - tee) / (0.5 * tee))) + Elvb / FL
        else:
            elv = Elvb / FL


def rvecal() :
    global tcal
    global erv
    tcal = tcr
    if tcal <= tee :
        erv = FR1*Erva*0.5*(1.0-cos(3.1415926*tcal/tee))+Ervb/FR1
    else :
        if tcal <= 1.5*tee :
            erv = FR1*Erva*0.5*(1.0+cos(2.0*3.1415926*(tcal-tee)/tee))+Ervb/FR1
        else :
            erv = Ervb/FR1

def raecal() :

    global tcal,teer
    global tar,tac
    global era
    global eec
    eec = tar - tac
    teer = teec
    tcal = tcr

    tap = tar + teer - Tduration

    if 0 <= tcal <= tap:
        era = Eraa * 0.5 * (1.0 + cos(3.1415926 * (tcal + Tduration - tar) / teer)) + Erab

    if tap < tcal <= tac:
        era = Erab

    if (tcal > tac and tcal <= tar) :
        era = Eraa * 0.5 * (1.0 - cos(3.1415926 * (tcal - tac) / teec)) + Erab

    if (tcal > tar and tcal <= Tduration) :
        era = Eraa * 0.5 * (1.0 + cos(3.1415926 * (tcal - tar) / teer)) + Erab



def Laecal():
    global tcr
    global teec
    global teer
    global tcal

    tcal = tcr
    teec = tar - tac
    teer = teec
    tap = tar + teer - Tduration

    if (tcal >= 0.0 and tcal <= tap) :
        ela = Elaa * 0.5 * (1.0 + cos(3.1415926 * (tcal + Tduration - tar) / teer)) + Elab

    if (tcal > tap and tcal <= tac) :
        ela = Elab

    if (tcal > tac and tcal <= tar) :
        ela = Elaa * 0.5 * (1.0 - cos(3.1415926 * (tcal - tac) / teec)) + Elab

    # c if (tcal > tar. and.tcal <= (tar+teer)) then
    if (tcal > tar and tcal <= Tduration) :
        ela = Elaa * 0.5 * (1.0 + cos(3.1415926 * (tcal - tar) / teer)) + Elab


def AAtv() :
    intee = era * v(3) - prv
    if (intee > 0.0) :
        AAtv = 4.0
    else :
        AAtv = 0.0

    return AAtv

def AApv() :
    intee = prv - Epua * Zpua

    if (intee > 0.0) :
        AApv = 4.0
    else :
        AApv = 0.0

    return AApv

def AAmv() :
    intee = ela * v(10) - plv
    if (intee > 0.0) :
        AAmv = 4.0
    else :
        AAmv = 0.0

