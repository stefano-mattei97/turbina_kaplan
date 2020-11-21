import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd


def PlotVariabili(dato):
    fig = plt.figure()

    plt.subplot(211)
    plt.title('Andamento delle Velocità')
    plt.xlabel('m/s')
    plt.ylabel('R%')
    plt.plot(dato['U'],dato['R%'])
    plt.plot(dato['Cm'], dato['R%'])
    plt.plot(dato['Cu1'], dato['R%'])
    plt.plot(dato['Cu2'], dato['R%'])
    plt.legend(['U', 'Cm', 'Cu1', 'Cu2'], prop={'size': 6}, loc='center')

    plt.subplot(212)
    plt.title('Andamento lavoro di Eulero')
    plt.ylabel('R%')
    plt.xlabel('')
    plt.plot(dato['WE'], dato['R%'])
    plt.legend(['WE'], prop={'size': 6}, loc='upper left')
    plt.show()

    fig1=plt.figure()

    plt.subplot(211)
    plt.title('Andamento degli angoli Beta')
    plt.ylabel('R%')
    plt.xlabel('°')
    plt.plot(dato['beta1'], dato['R%'])
    plt.plot(dato['beta2'], dato['R%'])
    plt.legend(['beta1', 'beta2'], prop={'size': 6}, loc='upper left')

    plt.subplot(212)
    plt.title('Andamento degli angoli Alpha')
    plt.ylabel('R%')
    plt.xlabel('°')
    plt.plot(dato['alpha1'], dato['R%'])
    plt.plot(dato['alpha2'], dato['R%'])
    plt.legend(['alpha1', 'alpha2'], prop={'size': 6}, loc='upper left')
    plt.show()
    return()