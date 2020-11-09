import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

#INPUT

Q = 9.5                               #[m^3/s]
H = 5.6
Np = 24
efficiency = 0.85

#COSTANTI
f = 50
rho = 1000
g = 9.81
k1 = 4                     #costante Cu in ingresso
k2 = 1.5                      #costante Cu in uscita



#OPERATING POINT

N = (120*f)/Np                             #condizione di sincronismo
omega = (2*math.pi*N)/60
P = rho * Q * g * H * efficiency           #potenza
Ns = (N * (P/rho)**0.5)/((g * H)**1.25)    #numero di giri specifico adimensionale
Nsd = (N * (P/1000)**0.5)/(H**1.25)        #numero di giri dimensionale
omegas = omega*(Q**0.5)/((g*H)**(3/4))     #velocità specifica
Z = 5                                      #pale runner


#CANALE MERIDIANO

K = 2.294/(H**(3/4))
De = 84.5 * (0.79 + 1.602*K) * ((H**0.5)/N)               #diametro runner [m]
tau = 0.25 * De                                           #distanza pale distributrici e asse runner [m]
Di = (0.25 + (0.0951/K)) * De                             #diametro hub [m]

#DISTRIBUTORE

Dgv = 1.24 * De                                           #diametro distributore [m]
A = 0.13 * De                                             #altezza [m]
Cr1 = Q/(math.pi * Dgv * A)                               #componenete radiale in uscita dal GV

Zgv = 16
tgv = (math.pi * Dgv) / Zgv                               #passo










#GIRANTE

We = g * H                              #lavoro di Eulero

step=200
r = np.linspace(Di,De,step)
#inizializzazione vettori velocità
U = np.zeros(len(r))
Cm = np.zeros(len(r))
Cu1 = np.zeros(len(r))
Cu2 = np.zeros(len(r))
Wu1 = np.zeros(len(r))
Wu2 = np.zeros(len(r))

U = omega * r                             #blade speed
phi = Q/(omega * (2 * r)**3)              #flow coefficient

#Free vortex: Cm costante

Cm = phi[100] * U[100]                    #componente assiale velocità assoluta (midspan)

#Prova eq.Radiale

Cu1 = k1/r
Cu2 = k2/r

#Triangoli di velocità

alpha1 = (np.arctan(k1/(r*Cm))/(2*3.14))*360                    #gli angoli sono espressi in gradi
alpha2 = (np.arctan(k2/(r*Cm))/(2*3.14))*360
beta1 = (np.arctan((U/Cm)-(k1/(r*Cm))))/(2*3.14)*360
Wu1 = U-Cu1
Wu2 = U+Cu2
data = {'U':U,
        'Cm':Cm,
        'Cu1':Cu1,
        'Cu2':Cu2,
        'Wu1':Wu1,
        'Wu2':Wu2,
        'beta1': beta1,
        'alpha1': alpha1,
        'alpha2':alpha2 }
Database = pd.DataFrame (data, columns = ['U','Wu1','Wu2','Cm','Cu1','Cu2','beta1','alpha1','alpha2'])

dato = Database.iloc[100]
fig = plt.figure()
ax = plt.subplot(111)
ax.set_aspect(1)

#IN

ax.arrow(dato['U'],dato['Cm'],-dato['U'],0,length_includes_head=True,width=0.5,facecolor='y')
ax.arrow(dato['U'],dato['Cm'],-dato['Cu1'],-dato['Cm'],length_includes_head=True,width=0.5,facecolor='b')
ax.arrow(0,dato['Cm'],dato['Wu1'],-dato['Cm'],length_includes_head=True,width=0.5,facecolor='g')
ax.annotate('U',(dato['U']*0.5, 1))
ax.annotate('C1',(dato['U'], 0.2))
ax.annotate('W1',(dato['U']/3.3, 0))
plt.show()

#OUT
dato = Database.iloc[100]
fig = plt.figure()
ax = plt.subplot(111)
ax.set_aspect(1)
ax.arrow(0,dato['Cm'],dato['Wu2'],-dato['Cm'],length_includes_head=True,width=0.5,facecolor='g')
ax.arrow(dato['Wu2'],0,-dato['U'],0,length_includes_head=True,width=0.5,facecolor='y')
ax.arrow(0,dato['Cm'],dato['Cu2'],-dato['Cm'],length_includes_head=True,width=0.5,facecolor='b')
ax.annotate('U',(dato['U']*0.5, 0))
ax.annotate('C2',(0, 0.2))
ax.annotate('W2',(dato['U']/2,1.2))
plt.show()
