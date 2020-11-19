import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

def CanaleMeridiano(H, N):
    K = 2.294 / (H ** (3 / 4))
    De = 84.5 * (0.79 + 1.602 * K) * ((H ** 0.5) / N)     # diametro runner [m] (N in rpm)
    tau = 0.25 * De                                       # distanza pale distributrici e asse runner [m]
    Di = (0.25 + (0.0951 / K)) * De                       # diametro hub [m]
    A = 0.13 * De                                         # larghezza canale meridiano [m]
    return (K, De, tau, Di, A)
