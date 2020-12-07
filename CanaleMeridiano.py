import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

def CanaleMeridiano(H, N, efficiency):
    Hn = H * efficiency                                   # carico idraulico netto
    K = 2.294 / (Hn ** (3 / 4))
    De = 84.5 * (0.79 + 1.602 * K) * ((Hn ** 0.5) / N)    # diametro runner [m] (N in rpm)
    tau = 0.25 * De                                       # distanza pale distributrici e asse runner [m]
    Di = (0.25 + (0.0951 / K)) * De                       # diametro hub [m]
    A = 0.13 * De                                         # larghezza canale meridiano [m]
    chord = (De - Di)/4                                   # corda distributore
    data = {'Hn': Hn,
            'K': K,
            'De': De,
            'tau': tau,
            'Di':Di ,
            'A': A,
            'chord': chord}
    CanaleMeridianodb = pd.DataFrame(data, columns=['Hn', 'K', 'De', 'tau', 'Di', 'A', 'chord'], index=[0])

    return (K, De, tau, Di, A, chord,CanaleMeridianodb)
