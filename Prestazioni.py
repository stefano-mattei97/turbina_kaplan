import numpy as np
import pandas as pd
import math

def Prestazioni (WE,Q,rho,omega, Wm, betam,chord, b, CL, CD ,De, Di, Hn, g):
    r = np.linspace(Di/2,De/2,len(Wm),endpoint=True)
    We = Hn * g

    betam=(betam - 90)*(2*math.pi)/360

    L = 0.5 * rho * chord * b * CL * Wm**2

    D = 0.5 * rho * chord * b * CD * Wm**2

    Ft = L * np.cos(betam) + D * np.sin(betam)

    WE_real = Ft * r * omega/(rho * Q)

    ef_real = (WE_real / We)

    efficiency_real = np.mean(ef_real)



    data = {'L': L,
            'D': D,
            'Ft': Ft,
            'WE_real': WE_real,
            'efficiency_real': efficiency_real,
            'r': r
            }
    Prestazionidb = pd.DataFrame(data, columns=['L','D', 'Ft', 'WE_real', 'efficiency_real', 'r'])
    return(Prestazionidb)


