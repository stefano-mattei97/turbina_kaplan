import numpy as np
import pandas as pd
import math
from Girante import Girante



def BladeDesign (dato,g,H,efficiency,rho):


    C3 = 2                                                    #[m/s]  hip:pag 291 'Macchine Idrauliche' [1.5-2]
    Wm = (dato['W1'] +dato['W2'])/2
    Wmu = (dato['Wu1'] + dato['Wu2'])/2
    patm = 10.34528                                           #[m]
    Patm = 101324                                             #[Pa]
    Pv= 2985.7                                                #[Pa] pressione di vapore a T=24° (Rogers-Mayhew)
    pmin = 2.2                                                # pressione minima acqua [2-2.5] [m]
    K = 2.8                                                   # numero caratteristico del profilo [2.6-3]
    etas = 0.9                                                # efficienza di scambio energetico [0.88-0.91]
    betam = 90 + math.degrees(np.arctan(Wmu/dato['Cm']))              # rispetto alla direzione periferica in gradi

    #step0 : Cavitazione

    Hn = H * efficiency                                            # carico idraulico netto
    Nqe = 2.294/(Hn**0.486)                                        # Specif speed (F. Schweiger - J. Gregory)
    thoma = 1.5241 * (Nqe**1.46) + (C3**2/(2*g*Hn))                # Coefficiente di Thoma
    Hs = ((Patm - Pv)/(rho*g)) + ((C3**2)/(2*g)) - (thoma*Hn)      # Maximun Suction Head

    #step1 : calcolo coefficiente di lift per ogni raggio cl

    slip = np.linspace(2.5, 3, 6)               #stima dei valori dello slip
    cl = (dato['W2']**2 - Wm**2 + (2 * g * (patm - Hs - pmin - etas * ((dato['C2']**2 - C3**2)/(2*g))))) / (K * Wm**2)

    #step2 : stima slip angle [2.5°-3°]
    slipcorretto=0                              #valore dello slip corretto
    sliptru=np.zeros(6)                         #valore slip di confronto
    liftratio=np.zeros(6)
    CL=np.zeros(6)
    chordtopitch=np.zeros(6)
    pitchtochord=np.zeros(6)
    for j in range(len(slip)):
        #step3 : calcolo l/t

        chordtopitch[j] = (g * efficiency * H * dato['Cm'] * np.cos(math.radians(slip[j]))) / (Wm**2 * dato['U'] * cl * np.sin(math.radians(180 - betam - slip[j])))

        #step4 : calcolo coefficiente di lift cL

        data = pd.read_csv('liftratio.txt', delim_whitespace=True)
        pitchtochord[j]=(chordtopitch[j])**(-1)
        liftratio[j] = np.interp(pitchtochord[j], data['t/chord'], data['liftratio'])
        CL[j]=cl/liftratio[j]

        #step5 : calcolo coefficiente di drag cD

        CLCD = pd.read_csv('432_CL_CD.txt', delim_whitespace=True)
        CD = np.interp(CL[j],CLCD['CL'], CLCD['CD'])

        #step6 : calcolo angolo di slip

        sliptru[j] = math.degrees(np.arctan(CD/CL[j]))
        sliptru[j] = round(sliptru[j], 1)
        if sliptru[j]==slip[j]:
            slipcorretto=slip[j]

    return(slipcorretto,slip,sliptru,CL,liftratio,chordtopitch,pitchtochord,Nqe)








    #step7 : calcolo angolo di attacco delta








