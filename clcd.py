import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from xfoil import callXF

def clcd (Rer):
    NACA = '6412'
    NNodes = '170'
    Re = str(Rer)
    iter = '500'
    inputFile = 'xfoilInput'
    nacaFile = 'nacaProfile'
    polarFile = 'polarNaca6412'
    AoAmin = '-10'
    AoAmax = '30'
    AoAdelta = '0.5'

    cl, cd = callXF(NACA, NNodes, Re, iter, inputFile, nacaFile, polarFile, AoAmin, AoAmax, AoAdelta)

    ClMax = 0

    for i in range(len(cl.x)):
        if cl.y[i] > ClMax:
            ClMax = cl.y[i]
            alphamax = cl.x[i]

    fig11 = plt.figure()
    plt.subplot(111)
    plt.title('Cl-Cd')
    plt.xlabel('alpha0')
    plt.plot(cl.x, cl.y)
    plt.plot(alphamax, ClMax, marker='o', color='black')
    plt.plot(cd.x, cd.y)
    plt.legend(['Cl', 'Cd'], prop={'size': 8}, loc='upper left')
    plt.show()

    return(alphamax)