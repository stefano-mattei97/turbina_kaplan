import numpy as np
import pandas as pd

def Prestazioni (WE, Q, rho, g, omega, H, C1d, C0d, Cu1, Di, r):

    torque = Q * rho * Cu1 * Di/2

    shaft_power = torque * omega

    runner_power = (WE / g) * rho * g * Q

    etam = shaft_power / runner_power          #efficienza meccanica

    #etah = (WE /g) / H                         #efficienza idraulica

    #etao = etam * etah                         #efficienza totale

    eta_distributore = C1d**2 / C0d**2

    eta_rotore = WE / (0.5 * C1d**2)

    etah = eta_distributore * eta_rotore

    data = {'torque': torque,
            'etah': etah,
            'eta_distributore': eta_distributore,
            'eta_rotore': eta_rotore,
            'shaft_power': shaft_power,
            'runner_power': runner_power,
            'etam': etam
            }
    Prestazionidb = pd.DataFrame(data, columns=['torque', 'etah', 'eta_rotore', 'eta_distributore', 'shaft_power', 'runner_power', 'etam'])
    return(Prestazionidb)