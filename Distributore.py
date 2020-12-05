import numpy as np
import pandas as pd
import math
from TriangoliVelocitaDistributore import TriangoliVelocitaDistributore

def Distributore(H, g, N, Q, P, chord):


    Specific_Speed = (N * (P*0.00135962)**0.5)/(H**1.25)
    data = pd.read_csv('Kug_Kfg.txt', delim_whitespace=True)
    Kug = np.interp(Specific_Speed, data['Specific_Speed'], data['Kug'])
    Dgv = (60 * Kug * (2 * g * H)**0.5) / (math.pi * N)                      # diametro distributore [m]
    Kfg = np.interp(Specific_Speed, data['Specific_Speed'], data['Kfg'])
    Vgv = Kfg * (2 * g * H)**0.5                     # velocità radiale uscita distributore
    AltezzaDistributore=Q/math.pi/Dgv/Vgv
    R=0.7
    Cr0 = Q/(Dgv+2*chord)/math.pi/AltezzaDistributore  #Vgv=Cr0
    Cr1 = Q / (math.pi * Dgv * AltezzaDistributore)          # componenete radiale in uscita dal Distributore
    Zgv = 16                                                                 # numero pale distributore
    tgv = (math.pi * Dgv) / Zgv                                              # passo
    Re = (Cr0 * chord)/(1.05e-6)
    print('Il valore di Cr1 è',Cr1,'Il Valore di Cr0 è',Cr0)
    return(Dgv,Vgv,Cr1,Re,Kug,Kfg,Cr0,AltezzaDistributore)




