import numpy as np
import pandas as pd
import math
from TriangoliVelocitaDistributore import TriangoliVelocitaDistributore

def Distributore2(H, g, Q, chord,De):
    #R = 0.7                                         #grado di reazione
    Dgv = 1.1 * De
    AltezzaDistributore = 0.5
    #C0 = (2*g*(1-R)*H)**0.5
    Cr0=Q/(Dgv+2*chord)/math.pi/AltezzaDistributore
    Cr1 = Q/AltezzaDistributore/math.pi/Dgv
    #Re = (C0 * chord) / (1.05e-6)
    data = {'Dgv': Dgv,
            'AltezzaDistributore': AltezzaDistributore,
            'Cr0': Cr0,
            'Cr1': Cr1}
    Distributoredb = pd.DataFrame(data, columns=['Dgv', 'AltezzaDistributore', 'Cr0', 'Cr1'], index=[0])

    return(Cr0,Cr1,AltezzaDistributore,Dgv,Distributoredb)