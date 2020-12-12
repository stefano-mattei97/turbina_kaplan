import numpy as np
import pandas as pd
import math

def Prestazioni (WE,He, Q, rho, g, omega, H, Cu1, r, Wm, betam, t, chord, CL, CD ):

    torque = Q * rho * Cu1 * r

    shaft_power = torque * omega

    runner_power = WE * rho  * Q

    etam = shaft_power / runner_power          #efficienza meccanica

    etah = (He) / H                         #efficienza idraulica

    etao = etam * etah                         #efficienza totale

    L = 0.5 * rho * chord * CL * Wm**2

    D = 0.5 * rho * chord * CD * Wm**2

    Ft = L * np.cos(math.radians(betam)) + D * np.sen(math.radians(betam))

    WE_real = Ft * r * omega / rho * Q

    efficiency_real = WE_real / WE






    data = {'torque': torque,
            'etah': etah,
            'etam': etam,
            'shaft_power': shaft_power,
            'runner_power': runner_power,
            'etao': etao,
            'L' : L,
            'D': D,
            'Ft' : Ft,
            'WE_real' : WE_real,
            'efficiency_real' : efficiency_real
            }
    Prestazionidb = pd.DataFrame(data, columns=['torque', 'etah', 'etam', 'shaft_power', 'runner_power', 'etao', 'L','D', 'Ft', 'WE_real', 'efficiency_real'])
    return(Prestazionidb)


