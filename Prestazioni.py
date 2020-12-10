import numpy as np
import pandas as pd

def Prestazioni (WE,He, Q, rho, g, omega, H, C1d, C0d, Cu1, r):


    torque = Q * rho * Cu1 * r

    shaft_power = torque * omega

    runner_power = WE * rho * Q

    etam = shaft_power / runner_power          #efficienza meccanica

    etah = (He) / H                         #efficienza idraulica

    etao = etam * etah                         #efficienza totale


    data = {'torque': torque,
            'etah': etah,
            'etam': etam,
            'shaft_power': shaft_power,
            'runner_power': runner_power,
            'etao': etao
            }
    Prestazionidb = pd.DataFrame(data, columns=['torque', 'etah', 'etam', 'shaft_power', 'runner_power', 'etao'])
    return(Prestazionidb)


