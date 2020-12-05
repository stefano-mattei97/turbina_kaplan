import numpy as np
import pandas as pd
import math
from TriangoliVelocitaDistributore import TriangoliVelocitaDistributore

def Distributore2(H, g, Q, chord,De):
    R = 0.7                                         #grado di reazione
    Dgv = 1.1 * De
    AltezzaDistributore = 0.5
    C0 = (2*g*(1-R)*H)**0.5
    Cr1 = Q/AltezzaDistributore/math.pi/Dgv
    Re = (C0 * chord) / (1.05e-6)

    return(Re,C0,Cr1,AltezzaDistributore,Dgv)