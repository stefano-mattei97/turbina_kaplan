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
from BladeDesign import BladeDesign


#INPUT
Q = 48.11                          #[m^3/s]
H = 15
Np = 40                           #numero poli con moltiplicatore
efficiency = 0.85


#COSTANTI
f = 50
rho = 998
g = 9.81


#OPERATING POINT
N,omega,P,Ns,Nsd,omegas,Z = OperatingPoint(f, Np, rho, Q, g, H, efficiency)

#CANALE MERIDIANO
K,De,tau,Di,A,chord = CanaleMeridiano(H,N,efficiency)

#DISTRIBUTORE
Dgv,Vgv,Cr1,Re,Kug,Kfg = Distributore(H, g, N, Q, A, P,chord)


#GIRANTE
data,Database,We,Cu1 = Girante(g, H, omega, Q, Di, De)
sezioni=[0,5,10]
for jj in range(len(sezioni)):
    girsez=Database.iloc[sezioni[jj]]
    TriangoliVelocita(girsez,sezioni[jj])
PlotVariabili(Database)

#CANALE TOROIDALE
Cut, Delta = CanaleToroidale(Di, De, Dgv, Cu1)

#XFOIL
alphamax = clcd(Re)

#TRIANGOLI DI VELOCITA' DISTRIBUTORE

alpha1d = (np.arctan(Cut / Cr1)) / (2 * 3.14) * 360
deflessione = alpha1d - alphamax
for kk in range(len(sezioni)):
    TriangoliVelocitaDistributore(Cr1, Vgv, Cut, sezioni[kk], chord, alphamax)

#BLADE DESIGN
slip=np.zeros(5)
alpha=np.zeros(5)
slipp=[]
deltaa=[]
slipstimato=[]
listafilecdcl = ['410_CL_CD.txt','410_CL_CD.txt','410_CL_CD.txt','423_CL_CD.txt','444_CL_CD.txt']
listafilealpha = ['410_CL_alpha.txt','410_CL_alpha.txt','410_CL_alpha.txt','423_CL_alpha.txt','444_CL_alpha.txt']
lsezioni = [1,3,5,7,10]
for ii in range(len(listafilecdcl)):
    sez=Database.iloc[lsezioni[ii]]
    str = listafilecdcl[ii]
    stralpha=listafilealpha[ii]
    slip[ii],alpha[ii]= BladeDesign(sez,g,H,efficiency,rho,str,stralpha,Ns,ii)






















