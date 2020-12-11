import numpy as np
import pandas as pd

def Prestazioni (WE,He, Q, rho, g, omega, H, C1d, C0d, Cu1, r):

    torque = Q * rho * Cu1 * r

    shaft_power = torque * omega

    runner_power = WE * rho  * Q

    etam = shaft_power / runner_power          #efficienza meccanica

    etah = (He) / H                         #efficienza idraulica

    etao = etam * etah                         #efficienza totale

    eta_distributore = C1d ** 2 / C0d ** 2

    eta_rotore = WE / (0.5 * C1d ** 2)

    etaH = eta_distributore * eta_rotore

    data = {'torque': torque,
            'etah': etah,
            'etam': etam,
            'shaft_power': shaft_power,
            'runner_power': runner_power,
            'etao': etao,
            'eta_distributore':eta_distributore,
            'eta_rotore':eta_rotore,
            'etaH':etaH
            }
    Prestazionidb = pd.DataFrame(data, columns=['torque', 'etah', 'etam', 'shaft_power', 'runner_power', 'etao','eta_distributore','eta_rotore','etaH'])
    return(Prestazionidb)


