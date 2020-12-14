import numpy as np
import pandas as pd

def Girante(g, H, omega, Q, Di, De, rho):
    We = g * H                                         # lavoro di Eulero

    step = 11
    mid = 5


    r = np.linspace(Di/2, De/2, step, endpoint=True)
    rNorm=np.linspace(0, 100, step, endpoint=True, dtype='int16')
    U = omega * r                                       # blade speed
    phi = Q / (omega * (2 * r) ** 3)                    # flow coefficient


    Cu2 = 0                                             # condizione di axial leaving velocity

    # Free vortex: Cm costante

    Cm = phi[mid] * U[mid]                              # componente assiale velocità assoluta (midspan)

    # eq.Radiale

    Cu1 = We / U

    # Triangoli di velocità

    # gli angoli sono espressi in gradi rispetto alla direzione assiale
    alpha1 = -(np.arctan(Cu1 / Cm)) / (2 * 3.14) * 360
    alpha2 = (np.arctan(Cu2 / Cm)) / (2 * 3.14) * 360
    beta1 = (np.arctan((U / Cm) - (Cu1 / Cm))) / (2 * 3.14) * 360
    beta2 = (np.arctan(U / Cm) / (2 * 3.14)) * 360

    # gli angoli sono espressi in gradi rispetto alla direzione periferica
    alphap1 = 90 - alpha1
    alphap2 = 90 - alpha2
    betap1 = 90 - beta1
    betap2 = 90 - beta2

    Wu1 = U - Cu1
    Wu2 = U
    W1 = (Wu1**2 + Cm**2)**0.5
    W2 = (Cm**2 + Wu2**2)**0.5
    C1 = (Cm**2 + Cu1**2)**0.5
    C2 = (Cm**2 + Cu2**2)**0.5


    WE = U*(Cu1 - Cu2)

    torque = rho * Q * Cu1 * r


    data = {'R%': rNorm,
            'U': U,
            'Cm': Cm,
            'Cu1': Cu1,
            'Cu2': Cu2,
            'Wu1': Wu1,
            'W1': W1,
            'Wu2': Wu2,
            'W2':W2,
            'C1':C1,
            'C2':C2,
            'WE':WE,
            'beta1': beta1,
            'beta2': beta2,
            'alpha1': alpha1,
            'alpha2': alpha2,
            'torque': torque
            }
    Database = pd.DataFrame(data, columns=['R%','U', 'Wu1', 'W1', 'Wu2', 'W2', 'Cm', 'Cu1', 'Cu2', 'C1', 'C2', 'WE', 'beta1', 'beta2', 'alpha1', 'alpha2','torque'])
    return(Database,Cu1,WE,r)
