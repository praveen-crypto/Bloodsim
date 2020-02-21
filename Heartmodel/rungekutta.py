global valve,Aav,Amv,Apv,Atv,Gpw
global E_cardiopul,Elaa,Elab,Elva,Elvb,Eraa,Erab,Erva,Ervb,Epua,Epuc,Epuv,Epwa,Epwc,Epwv
global yL_cardiopul,yav,ymv,ypv,ytv,ypua,ypuc,ypuv,ypwa,ypwc,ypwv
global R_cardiopul,Ra,Raa,Rav,Rca,Rda,Rmv,Rpua,Rpuc,Rpuv,Rpv,Rpwa,Rpwc,Rpwv,Rtv,Rv,Rvc,bav,bmv,bpv,btv
global S_cardiopul,Spua,Spuc,Spuv,Spwa,Spwc,Spwv
global Z_cardiopul,Zpua,Zpuc,Zpuv,Zpwa,Zpwc,Zpwv
global C_peripheral,Caor,Cart,Ccap,Cven,Cvca
global yL_peripheral,yaor,yart,ycap,yven,yvca
global R_peripheral,Raor,Rart,Rcap,Rven,Rvca
global S_peripheral,Saor,Sart,Scap,Sven,Svca
global sdvsdqdvdq,dvq,P_0d
global dvdq_cardiopul,dv,v,dq,q
global cardiac_parameter,elv,ela,erv,era,cklr,ckrl,plv,prv,Sla,Slv,Sra,Srv,ppp,ppc,pit,qco,FL,FR1,STR
global R_cardiopulc,Rav0,Rmv0,Rpv0,Rtv0,bav0,bmv0,bpv0,btv0,Rav1,Rmv1,Rpv1,Rtv1,bav1,bmv1,bpv1,btv1
global Rav2,Rmv2,Rpv2,Rtv2,bav2,bmv2,bpv2,btv2,yav0,ymv0,ypv0,ytv0,yav1,ymv1,ypv1,ytv1,yav2,ymv2,ypv2,ytv2
global n_val,m_cvst,m_cvrg,n_vrg
global timestep,Tduration,ddt,tcr,tee,tac,tar,t

def rungekutta(subresultcr) :
    #call dvdqsdvsdq % == == == == == = make a note........................
    dvdqsdvsdq()
    dfl[1: 29] = dvq[1: 29]

    #do i = 0, 28
    #dfl(i) = dvq(i + 1)
    #end do

    dq[1: 7] = dfl[2: 2:14]
    dq[8: 15] = dfl[15: 2:29]

    dv[1: 7] = dfl[1: 2:13]
    dv[8: 14] = dfl[16: 2:28

    for nrk in np.arange(1, 4, 1):
        subrukruk[nrk, 1:29] = ddt * dfl[1:29]

        if nrk == 1 :
            Aav = AAav()
            Amv = AAmv()
            Apv = AApv()
            Atv = AAtv()

        if nrk < 4 :
            inter[1: 29] = 0.5 * (subrukuk[nrk, 1:29])
        else :
            inter[1:29] = subrukuk[nrk, 1:29]

    inter[1:29] = 0.5*(subrukuk[nrk,1:29])
    newpara[1:29] = subresultcr[1:29] + inter[1:29]4


    q[1:7] = newpara[2:2:14]
    q[8:15]= newpara[15:2:29]


    v[1:7] = newpara[1:2:13]
    v[8:14] = newpara[16:2:28]




