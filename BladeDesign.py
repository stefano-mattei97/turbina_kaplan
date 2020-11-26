import numpy as np
import pandas as pd
import math
from Girante import Girante



def BladeDesign (W2,W1,Wu1,Wu2,g,H,efficiency,C2,Cm,U,rho):


    C3 = 2                                                    #[m/s]  hip:pag 291 'Macchine Idrauliche' [1.5-2]
    Wm = (W1 + W2)/2
    Wmu = (Wu1 + Wu2)/2
    patm = 10.34528                                           #[m]
    Patm = 101324                                             #[Pa]
    Pv= 2985.7                                                #[Pa] pressione di vapore a T=24° (Rogers-Mayhew)
    pmin = 2.2                                                # pressione minima acqua [2-2.5] [m]
    K = 2.8                                                   # numero caratteristico del profilo [2.6-3]
    etas = 0.9                                                # efficienza di scambio energetico [0.88-0.91]
    betam = 90 + math.degrees(np.arctan(Wmu/Cm))              # rispetto alla direzione periferica in gradi

    #step0 : Cavitazione

    Hn = H * efficiency                                            # carico idraulico netto
    Nqe = 2.294/(Hn**0.486)                                        # Specif speed (F. Schweiger - J. Gregory)
    thoma = 1.5241 * (Nqe**1.46) + (C3**2/(2*g*Hn))                # Coefficiente di Thoma
    Hs = ((Patm - Pv)/(rho*g)) + ((C3**2)/(2*g)) - (thoma*Hn)      # Maximun Suction Head

    #step1 : calcolo coefficiente di lift per ogni raggio cl

    cl = (W2**2 - Wm**2 + (2 * g * (patm - Hs - pmin - etas * ((C2**2 - C3**2)/(2*g)))) / (K * Wm**2))

    #step2 : stima slip angle [2.5°-3°]

    slip = 2.5    #gradi

    #step3 : calcolo l/t

    chordtopitch = (g * efficiency * H * Cm * np.cos(math.radians(slip))) / (Wm**2 * U * cl * np.sin(math.radians(180 - betam - slip)))

    #step4 : calcolo coefficiente di lift cL

    #step5 : calcolo coefficiente di drag cD

    #step6 : calcolo angolo di slip

    slip = np.arctan(cD/cL)

    #step7 : calcolo angolo di attacco delta









    return()