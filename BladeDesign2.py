import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import math
from Girante import Girante
from XfoilBladeD import callXFBD


def BladeDesign2 (dato,g,H,efficiency,rho,Ns,lsezioni,Z,Di,str1,str2):


    C3 = 2                                                  #[m/s]  hip:pag 291 'Macchine Idrauliche' [1.5-2]
    Wm = (dato['W1'] +dato['W2'])/2
    Wmu = (dato['Wu1'] + dato['Wu2'])/2
    patm = 10.34528                                           #[m]
    Patm = 101324                                             #[Pa]
    Pv= 2985.7                                                #[Pa] pressione di vapore a T=24° (Rogers-Mayhew)
    pmin = 2.5                                              # pressione minima acqua [2-2.5] [m]
    K = 4                                                 # numero caratteristico del profilo [2.6-3]
    etas = 0.91                                              # efficienza di scambio energetico [0.88-0.91]
    betam = 90+math.degrees(np.arctan(Wmu/dato['Cm']))      # rispetto alla direzione periferica in gradi

    #step0 : Cavitazione

    Hn = H * efficiency                                            # carico idraulico netto
    Nqe = 2.294/(Hn**0.486)                                        # Specif speed (F. Schweiger - J. Gregory)
    thoma = 1.5241 * (Nqe**1.46) + (C3**2/(2*g*Hn))                # Coefficiente di Thoma
    Hs = ((Patm - Pv)/(rho*g)) + ((C3**2)/(2*g)) - (thoma*Hn)      # Maximun Suction Head


    #step1 : calcolo coefficiente di lift per ogni raggio cl

    cl = (dato['W2']**2 - Wm**2 + (2 * g * (patm - Hs - pmin - etas * ((dato['C2']**2 - C3**2)/(2*g))))) / (K * Wm**2)

    #step2 : Calcolo CL

    t=(math.pi*Di)/Z
    M=(dato['Cu1']-dato['Cu2'])/dato['Cm']
    data = pd.read_csv('pitchtochord.txt', delim_whitespace=True)
    pitchtochord= np.interp(M, data['M'], data['t/chord'])
    chord=t/pitchtochord
    Rer = (dato['C1'] * chord) / (1.05e-6)
    NACA = str1
    NNodes = '170'
    Re = str(Rer)
    iter = '500'
    inputFile = 'xfoilInput'
    nacaFile = 'nacaProfile'
    polarFile = str2
    AoAmin = '-10'
    AoAmax = '30'
    AoAdelta = '0.5'
    data2 = pd.read_csv('liftratio.txt', delim_whitespace=True)
    Xfoildb = callXFBD(NACA, NNodes, Re, iter, inputFile, nacaFile, polarFile, AoAmin, AoAmax, AoAdelta)
    liftratio = np.interp(pitchtochord, data2['t/chord'], data2['liftratio'])
    CL = cl / liftratio
    CLd=np.zeros(len(Xfoildb['CL']))
    CDd = np.zeros(len(CLd))
    CLd=Xfoildb['CL']
    CDd=Xfoildb['CD']
    xdelta=100
    for ii in range(len(CLd)):
        if abs(CL-CLd[ii])<xdelta:
            kk=ii
            xdelta=abs(CL-CLd[ii])
    CLd[kk]=CL
    CDd[kk]=np.nan
    Xfoildb['CL']=CLd
    Xfoildb['CD']=CDd
    Xfoildb=Xfoildb.interpolate()
    data3 = {'CL':Xfoildb['CL'],
            'CD': Xfoildb['CD'],
            'AoA': Xfoildb['AoA'],
            'chord':chord
             }
    Bladedesigndb = pd.DataFrame(data3, columns=['CL', 'CD', 'AoA','chord'])
    b=Bladedesigndb.iloc[kk]
    return (b)









