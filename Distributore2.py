import numpy as np
import pandas as pd
import math


def Distributore2(H, g, Q, chord,De):
    Dgv = 1.1 * De
    Dgve = 4.5
    AltezzaDistributore = 0.5
    Cr0 = Q/(Dgv+2*chord)/math.pi/AltezzaDistributore
    Cr1 = Q/AltezzaDistributore/math.pi/Dgv
    data = {'Dgv': Dgv,
            'AltezzaDistributore': AltezzaDistributore,
            'Cr0': Cr0,
            'Cr1': Cr1}
    Distributoredb = pd.DataFrame(data, columns=['Dgv', 'AltezzaDistributore', 'Cr0', 'Cr1'], index=[0])

    return(Distributoredb)