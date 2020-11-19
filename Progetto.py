import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd
from OperatingPoint import OperatingPoint
from CanaleMeridiano import CanaleMeridiano
from Girante import Girante
from TriangoliVelocita import TriangoliVelocita
from PlotVariabili import PlotVariabili

#INPUT
Q = 0.28                             #[m^3/s]
H = 4
Np = 4                            #numero poli
efficiency = 0.85

#COSTANTI
f = 50
rho = 998
g = 9.81
k1 = 4                     #costante Cu in ingresso
k2 = 1.5                   #costante Cu in uscita

#OPERATING POINT
N,omega,P,Ns,Nsd,omegas,Z = OperatingPoint(f, Np, rho, Q, g, H, efficiency)
#CANALE MERIDIANO
K,De,tau,Di,A = CanaleMeridiano(H, N)
#DISTRIBUTORE
Dgv = 1.24 * De                                           #diametro distributore [m]
Cr1 = Q/(math.pi * Dgv * A)                               #componenete radiale in uscita dal GV
Zgv = 16
tgv = (math.pi * Dgv) / Zgv                               #passo
#GIRANTE
data,Database,We = Girante(g, H, omega, Q, k1, k2, Di, De)
sezione=5
sezionemid = Database.iloc[sezione]
TriangoliVelocita(sezionemid,sezione)
sezione=0
sezionehub = Database.iloc[sezione]
TriangoliVelocita(sezionehub,sezione)
sezione=10
sezionetip = Database.iloc[sezione]
TriangoliVelocita(sezionetip,sezione)
PlotVariabili(Database)


