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
from Distributore2 import Distributore2
from TriangoliVelocitaDistributore2 import TriangoliVelocitaDistributore2
from clcd import clcd
from BladeDesign import BladeDesign
from Drafttube import Drafttube


#INPUT
Q = 48.11                          #[m^3/s]
H = 15
Np = 40                           #numero poli con moltiplicatore
efficiency = 0.85
data0 = {'Q': Q,
         'H': H,
         'Np': Np,
         'efficiency':efficiency
         }
Inputdb = pd.DataFrame(data0, columns=['Q', 'H', 'Np','efficiency'],index=[0])


#COSTANTI
f = 50
rho = 998
g = 9.81
data00 = {'f': f,
         'rho': rho,
         'g': g,
         }
Costantidb = pd.DataFrame(data00, columns=['f','rho','g'],index=[0])

#OPERATING POINT
N,omega,P,Ns,Nsd,omegas,Z,OperatingPointdb = OperatingPoint(f,Np,rho,Q,g,H,efficiency)

#CANALE MERIDIANO
K,De,tau,Di,A,chord,CanaleMeridianodb = CanaleMeridiano(H,N,efficiency)





#GIRANTE
data,Database,We,Cu1 = Girante(g, H, omega, Q, Di, De)
sezioni=[0,5,10]
for jj in range(len(sezioni)):
    girsez=Database.iloc[sezioni[jj]]
    TriangoliVelocita(girsez,sezioni[jj])
PlotVariabili(Database)



#DISTRIBUTORE
#Dgv,Vgv,Cr1,Re,Kug,Kfg,Cr0,AltezzaDistributore = Distributore(H, g, N, Q, P, chord)
Cr0,Cr1,AltezzaDistributore,Dgv,Distributoredb = Distributore2(H, g, Q, chord,De)
#CANALE TOROIDALE
Cut, Delta,CanaleToroidaledb= CanaleToroidale(Di,De,Dgv,Cu1)


#XFOIL
C1=(Cr1**2+Cut**2)**0.5
Re=(C1*chord)/(1.05e-6)
alphamax,clcddb = clcd(Re)

#TRIANGOLI DI VELOCITA' DISTRIBUTORE
alpha0 = math.radians(alphamax)
alpha1d = (np.arctan(Cut / Cr1)) / (2 * 3.14) * 360
deflessione = alpha1d - alphamax
for kk in range(len(sezioni)):
    TriangoliVelocitaDistributore2(Cr1, Cut, sezioni[kk], chord, alphamax,Cr0)

#BLADE DESIGN
slip=np.zeros(5)
alpha=np.zeros(5)
BladeDesigndb=[]
listafilecdcl = ['432_CL_CD.txt','432_CL_CD.txt','410_CL_CD.txt','423_CL_CD.txt','444_CL_CD.txt']
listafilealpha = ['432_CL_alpha.txt','432_CL_alpha.txt','410_CL_alpha.txt','423_CL_alpha.txt','444_CL_alpha.txt']
lsezioni = [0,2,5,8,10]
for ii in range(len(listafilecdcl)):
    sez=Database.iloc[lsezioni[ii]]
    str = listafilecdcl[ii]
    stralpha=listafilealpha[ii]
    slip[ii],alpha[ii],BladeDesigndb= BladeDesign(sez,g,H,efficiency,rho,str,stralpha,Ns,ii,lsezioni[ii])


thomacr,thoma,zsc,zscmax= Drafttube(Q,H,Ns,De,rho,g)
