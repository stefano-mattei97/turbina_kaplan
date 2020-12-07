import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from Girante import Girante



def BladeDesign (dato,g,H,efficiency,rho,str,stralpha,Ns,plot,lsezioni):


    C3 = 2                                                   #[m/s]  hip:pag 291 'Macchine Idrauliche' [1.5-2]
    Wm = (dato['W1'] +dato['W2'])/2
    Wmu = (dato['Wu1'] + dato['Wu2'])/2
    patm = 10.34528                                           #[m]
    Patm = 101324                                             #[Pa]
    Pv= 2985.7                                                #[Pa] pressione di vapore a T=24° (Rogers-Mayhew)
    pmin = 2.5                                               # pressione minima acqua [2-2.5] [m]
    K = 3                                                   # numero caratteristico del profilo [2.6-3]
    etas = 0.91                                              # efficienza di scambio energetico [0.88-0.91]
    betam = 90 + math.degrees(np.arctan(Wmu/dato['Cm']))      # rispetto alla direzione periferica in gradi

    #step0 : Cavitazione

    Hn = H * efficiency                                            # carico idraulico netto
    Nqe = 2.294/(Hn**0.486)                                        # Specif speed (F. Schweiger - J. Gregory)
    thoma = 1.5241 * (Nqe**1.46) + (C3**2/(2*g*Hn))                # Coefficiente di Thoma
    Hs = ((Patm - Pv)/(rho*g)) + ((C3**2)/(2*g)) - (thoma*Hn)      # Maximun Suction Head

    #Grafico C.Thoma

    if plot==2:
        data2 = pd.read_csv('diagrammadiMoody.txt', delim_whitespace=True)
        fig = plt.figure()
        ax = plt.subplot(111)
        plt.title('Diagramma di Moody')
        ax.plot(data2['Ns'], data2['thoma'], color='k', ls='-')
        plt.plot(Ns, thoma, marker='o', color='red')
        ax.annotate('Zona Senza Cavitazione', (2,2),color='red')
        ax.annotate('Zona con Cavitazione',(4,0.5),color='red')
        ax.set_xlabel('Ns[rad]')
        ax.set_ylabel('thoma')
        plt.show()

    #step1 : calcolo coefficiente di lift per ogni raggio cl

    slip = np.linspace(2.5, 3, 50)               #stima dei valori dello slip
    cl = (dato['W2']**2 - Wm**2 + (2 * g * (patm - Hs - pmin - etas * ((dato['C2']**2 - C3**2)/(2*g))))) / (K * Wm**2)

    #step2 : stima slip angle [2.5°-3°]
    Slipc=0                                      #valore dello slip corretto
    sliptru=np.zeros(len(slip))                         #valore slip di confronto
    liftratio=np.zeros(len(slip))
    CL=np.zeros(len(slip))
    CD = np.zeros(len(slip))
    chordtopitch=np.zeros(len(slip))
    pitchtochord=np.zeros(len(slip))
    j=0
    deltatest = 99
    delta = np.zeros(len(slip))
    for j in range(len(slip)) :
        chordtopitch[j] = (g * efficiency * H * dato['Cm'] * np.cos(math.radians(slip[j]))) / (Wm**2 * dato['U'] * cl * np.sin(math.radians(betam - slip[j])))
        data = pd.read_csv('liftratio.txt', delim_whitespace=True)

        #step4  calcolo coefficiente di lift cL
        pitchtochord[j] = (chordtopitch[j])**(-1)
        liftratio[j] = np.interp(pitchtochord[j], data['t/chord'], data['liftratio'])
        CL[j] = cl/liftratio[j]

        #step5  calcolo coefficiente di drag cD
        CLCD = pd.read_csv(str, delim_whitespace=True)
        CD[j] = np.interp(CL[j],CLCD['CL'], CLCD['CD'])
        sliptru[j] = math.degrees(np.arctan(CD[j]/CL[j]))

        #step6  calcolo angolo di slip
        delta[j] = abs(slip[j] - sliptru[j])
        if delta[j]<deltatest:
            Slipc=slip[j]
            deltatest=delta[j]
            n=j

    #step 7: calcolo angolo di attacco
    dataalpha = pd.read_csv(stralpha, delim_whitespace=True)
    alpha = np.interp(CL[n], dataalpha['CL'], dataalpha['alpha'])

    data = {'C3': C3,
            'Wm': Wm,
            'Wmu': Wmu,
            'patm':patm,
            'Patm':Patm,
            'Pv':Pv,
            'pmin':pmin,
            'K':K,
            'etas':etas,
            'betam':betam,
            'Hn':Hn,
            'Nqe': Nqe,
            'thoma':thoma,
            'Hs':Hs,
            'Slipc':Slipc,
            'alpha':alpha,
            'chordtopitch':chordtopitch[n],
            'pitchtochord':pitchtochord[n],
            'CD':CD[n],
            'CL':CL[n]}

    BladeDesigndb = pd.DataFrame(data,columns=['C3', 'Wm', 'Wmu','patm','Patm','Pv','pmin','K','etas',
                                                'betam','Hn','Nqe','thoma','Hs','Slipc','alpha','chordtopitch',
                                                'pitchtochord','CD','CL'],index=[lsezioni])

    print('Valori Slip calcolati per la sezione:',lsezioni)
    print('sono:')
    print(sliptru)

    return(Slipc,alpha,BladeDesigndb)