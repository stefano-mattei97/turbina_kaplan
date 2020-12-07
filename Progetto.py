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
Inputdb1 = pd.DataFrame(data0, columns=['Q', 'H', 'Np','efficiency'],index=[0])
Inputdb = Inputdb1.iloc[0]

#COSTANTI
f = 50
rho = 998
g = 9.81
data00 = {'f': f,
         'rho': rho,
         'g': g
         }
Costantidb1 = pd.DataFrame(data00, columns=['f','rho','g'],index=[0])
Costantidb=Costantidb1.iloc[0]


#OPERATING POINT
#N,omega,P,Ns,Nsd,omegas,Z,
OperatingPointdb1 = OperatingPoint(Costantidb['f'],Inputdb['Np'],Costantidb['rho'],
                                  Inputdb['Q'],Costantidb['g'],Inputdb['H'],
                                  Inputdb['efficiency'])

OperatingPointdb=OperatingPointdb1.iloc[0]

#CANALE MERIDIANO

CanaleMeridianodb1 = CanaleMeridiano(Inputdb['H'],OperatingPointdb['N'],Inputdb['efficiency'])
CanaleMeridianodb=CanaleMeridianodb1.iloc[0]




#GIRANTE
Database,Cu1 = Girante(Costantidb['g'],Inputdb['H'], OperatingPointdb['Omega'],Inputdb['Q'], CanaleMeridianodb['Di'], CanaleMeridianodb['De'])
sezioni=[0,5,10]
for jj in range(len(sezioni)):
    girsez=Database.iloc[sezioni[jj]]
    TriangoliVelocita(girsez,sezioni[jj])
PlotVariabili(Database)



#DISTRIBUTORE
#Dgv,Vgv,Cr1,Re,Kug,Kfg,Cr0,AltezzaDistributore = Distributore(H, g, N, Q, P, chord)

Distributoredb1 = Distributore2(Inputdb['H'],Costantidb['g'],Inputdb['Q'], CanaleMeridianodb['chord'],CanaleMeridianodb['De'])
Distributoredb=Distributoredb1.iloc[0]
#CANALE TOROIDALE
Cut, Delta,CanaleToroidaledb1= CanaleToroidale(CanaleMeridianodb['Di'],CanaleMeridianodb['De'],Distributoredb['Dgv'],Cu1)
CanaleToroidaledb=CanaleToroidaledb1.iloc[0]

#XFOIL
C1=(Distributoredb['Cr1']**2+Cut**2)**0.5
Re=(C1*CanaleMeridianodb['chord'])/(1.05e-6)
alphamax,clcddb = clcd(Re)

#TRIANGOLI DI VELOCITA' DISTRIBUTORE
alpha0 = math.radians(alphamax)
C0=(Distributoredb['Cr0']/np.cos(alpha0))
print('C0:',C0,'C1',C1)
alpha1d = (np.arctan(Cut / Distributoredb['Cr1'])) / (2 * 3.14) * 360
deflessione = alpha1d - alphamax
for kk in range(len(sezioni)):
    TriangoliVelocitaDistributore2(Distributoredb['Cr1'], Cut, sezioni[kk], CanaleMeridianodb['chord'], alphamax,Distributoredb['Cr0'])

#BLADE DESIGN
slip=np.zeros(5)
alpha=np.zeros(5)
BladeDesigndb=[]
listafilecdcl = ['432_CL_CD.txt','432_CL_CD.txt','410_CL_CD.txt','423_CL_CD.txt','444_CL_CD.txt']
listafilealpha = ['432_CL_alpha.txt','432_CL_alpha.txt','410_CL_alpha.txt','423_CL_alpha.txt','444_CL_alpha.txt']
lsezioni = [0,2,5,7,10]
for ii in range(len(listafilecdcl)):
    sez=Database.iloc[lsezioni[ii]]
    str = listafilecdcl[ii]
    stralpha=listafilealpha[ii]
    slip[ii],alpha[ii],BladeDesigndb= BladeDesign(sez,Costantidb['g'],Inputdb['H'],Inputdb['efficiency'],Costantidb['rho'],str,stralpha,OperatingPointdb['Ns'],ii,lsezioni[ii])


Drafttubedb= Drafttube(Inputdb['Q'],Inputdb['H'],OperatingPointdb['Ns'],CanaleMeridianodb['De'],Costantidb['rho'],Costantidb['g'])
