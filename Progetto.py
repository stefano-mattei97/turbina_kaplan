import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd
from OperatingPoint import OperatingPoint
from CanaleMeridiano import CanaleMeridiano
from Girante import Girante
from TriangoliVelocita import TriangoliVelocita
from PlotVariabili import PlotVariabili
from CanaleToroidale import CanaleToroidale
from Distributore import Distributore
from TriangoliVelocitaDistributore import TriangoliVelocitaDistributore
from clcd import clcd

#INPUT
Q = 48.11                          #[m^3/s]
H = 15
Np = 40                            #numero poli con moltiplicatore
efficiency = 0.85


#COSTANTI
f = 50
rho = 998
g = 9.81


#OPERATING POINT
N,omega,P,Ns,Nsd,omegas,Z = OperatingPoint(f, Np, rho, Q, g, H, efficiency)
#CANALE MERIDIANO
K,De,tau,Di,A,chord = CanaleMeridiano(H, N)

#DISTRIBUTORE
Dgv,Vgv,Cr1,Re = Distributore(H, g, N, Q, A, P,chord)


#GIRANTE
data,Database,We,Cu1 = Girante(g, H, omega, Q, Di, De)
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


#CANALE TOROIDALE
Cut, Delta = CanaleToroidale(Di, De, Dgv, Cu1)


#XFOIL
alphamax = clcd()

#TRIANGOLI DI VELOCITA' DISTRIBUTORE


alpha1d = (np.arctan(Cut / Cr1)) / (2 * 3.14) * 360
step=0
TriangoliVelocitaDistributore(Cr1,Vgv,Cut,step,chord,alphamax)
step=5
TriangoliVelocitaDistributore(Cr1,Vgv,Cut,step,chord,alphamax)
step=10
TriangoliVelocitaDistributore(Cr1,Vgv,Cut,step,chord,alphamax)

















