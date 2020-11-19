import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd


def PlotVariabili(dato):
    fig = plt.figure()
    ax = plt.subplot(111)

    plt.plot(dato['U'],dato['R%'])
    plt.plot(dato['beta1'], dato['R%'])
    plt.plot(dato['beta2'], dato['R%'])
    plt.plot(dato['Cm'], dato['R%'])
    plt.plot(dato['Cu1'], dato['R%'])
    plt.plot(dato['Cu2'], dato['R%'])
    plt.legend(['U', 'beta1', 'beta2', 'Cm', 'Cu1', 'Cu2'], prop={'size': 6}, loc='upper left')

    return()