import numpy as np
import pandas as pd
import math

def Prestazioni (WE,Q,rho,omega, Wm, betam,chord, CL, CD ,De,Di):
    r=np.linspace(Di/2,De/2,len(Wm),endpoint=True)
    We=WE[0]
    betam=(betam-90)*(2*math.pi)/360
    L = 0.5 * rho * chord * CL * Wm**2

    D = 0.5 * rho * chord * CD * Wm**2

    Ft = L * np.cos(betam) + D * np.sin(betam)

    FT = np.inner(Ft,r)

    WE_real = FT * ((Di+De)/2) * omega/ rho * Q

    efficiency_real = WE_real / We






    data = {'L': L,
            'D': D,
            'Ft': Ft,
            'WE_real': WE_real,
            'efficiency_real': efficiency_real
            }
    Prestazionidb = pd.DataFrame(data, columns=['L','D', 'Ft', 'WE_real', 'efficiency_real'])
    return(Prestazionidb)


