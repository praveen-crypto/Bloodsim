import numpy as np

dqv = np.divide(np.subtract(np.add(np.divide(Vv, Cv),np.multiply(Sv, v[0])),np.subtract(np.multiply(Rv,q[0]),(Vvc/Cvc)), np.multiply(Sv,v[0])),Lv)
dqvc = np.divide( np.subtract(np.subtract(np.add(np.divide(Vvc, Cvc),np.multiply(Svc,v[1])),np.multiply(Rvc, q[1])), np.subtract(np.subtract(np.multiply(eRA,Vra),np.multiply(Sra, v[2])), np.subtract(Ppl, Ppc)),Lvc))
dqmv = np.divide(np.muliply(np.add(np.multiply(np.subtract(np.multiply( np.subtract(np.multiply(np.subtract(np.subtract(np.multiply(ela, Vla), Plv), Rmv), q[12]), Bmv), np.mutliply(q[12], np.mod(q[12]))), Slv), DVLV), Sla),v[7]), Lmv)
dqpv = np.divide(np.add(np.multiply(np.add(np.multiply(np.subtract(np.multiply(np.subtract(np.multiply(np.subtract(np.multiply(np.subtract(Prv, Epua), Zpua), Rpv), q[12]), Bpv), np.multiply(q[12], np.mod(q[12]))), Srv), v[3]), Spua), v[4]), Ppc), Lpv)
dqpua = np.divide(np.subtract(np.add(np.multiply(Epua, Zpua) , np.multiply(Spua, v[4])),   np.multiply( np.subtract( np.multiply(np.subtract(np.multiply(Rpua, q[4]), Epuc), Zpuc) ,Spuc ), v[5])), Lpua)
dqpuc = np.divide(np.add(np.multiply(np.subtract(np.multiply(np.subtract(np.multiply(np.subtract(np.multiply(np.add( np.multiply(Epuc, Zpuc),Spuc), v[5]), Rpuc), q[5]), Epuv), Zpuv), Spuv), v[6]), Ppc), Lpuc)
dqpuv = np.divide(np.multiply(np.subtract(np.multiply(np.subtract(np.multiply(np.subtract(np.multiply(np.add(np.multiply(Epuv, Zpuv), Spuv), v[6]), Rpuv), q[6]), ela), Vla), Sla), v[7]), Lpuv)
dqtv = np.divide(np.multiply(np.add(np.multiply(np.subtract(np.multiply(np.subtract(np.multiply(np.subtract(np.subtract(np.multiply(era, Vra), Prv),Rtv), Qtv), Btv), np.multiply(Qtv,np.mod(Qtv))),Srv),v[3]),Sra),v[2]), Ltv)
dqav = np.multiply(np.subtract(np.subtract(np.multiply(np.subtract(np.multiply(np.subtract(np.multiply(np.add(Plv, Slv), v[8]), Rpv), q[12]), Bpv), np.multiply(Qtv, np.mod(Qtv))),(Vao/Cao)),Sao), v[9])
dqao = np.divide(np.multiply(np.subtract(np.subtract(np.multiply(np.subtract(np.multiply(np.add((Vao/Cao), Sao),v[9]),Rao), q[9]), (Vart/Cart)), Sart), v[10]), Lao)
dqart = np.divide(np.multiply(np.subtract(np.subtract(np.multiply(np.subtract(np.multiply(np.add((Vart, Cart), Sart),v[10]), Rart), q[10]), (Vcap/Ccap)), Scap), v[11]), Lart)
dqcap = np.divide(np.multiply(np.subtract(np.subtract(np.multiply(np.subtract(np.multiply(np.add((Vcap/Ccap), Scap), v[11]), Rcap), q[11]), (Vv/Cv)), Sv), v[0]), Lart)
