import numpy as np
import pandas as pd

def Girante(g, H, omega, Q, k1, k2, Di, De):
    We = g * H                                         # lavoro di Eulero

    step = 11
    mid = 5


    r = np.linspace(Di, De, step, endpoint=True)
    rNorm=np.linspace(0, 100, step, endpoint=True, dtype='int16')
    U = omega * r                                       # blade speed
    phi = Q / (omega * (2 * r) ** 3)                    # flow coefficient

    # Free vortex: Cm costante

    Cm = phi[mid] * U[mid]                              # componente assiale velocità assoluta (midspan)

    # Prova eq.Radiale

    Cu1 = k1 / r
    Cu2 = k2 / r

    # Triangoli di velocità mid

    alpha1 = (np.arctan(k1 / (r * Cm)) / (2 * 3.14)) * 360  # gli angoli sono espressi in gradi rispetto alla direzione assiale
    alpha2 = (np.arctan(k2 / (r * Cm)) / (2 * 3.14)) * 360
    beta1 = (np.arctan((U / Cm) - (k1 / (r * Cm)))) / (2 * 3.14) * 360
    Wu1 = U - Cu1
    Wu2 = U - Cu2
    W1 = (Wu1**2 + Cm**2)**0.5
    W2 = (Wu2**2 + Cm**2)**0.5
    beta2 = (np.arcsin(Wu2/W2)/ (2 * 3.14)) * 360
    WE = U*(Cu1 - Cu2)
    data = {'R%': rNorm,
            'U': U,
            'Cm': Cm,
            'Cu1': Cu1,
            'Cu2': Cu2,
            'Wu1': Wu1,
            'W1': W1,
            'Wu2': Wu2,
            'W2':W2,
            'WE':WE,
            'beta1': beta1,
            'beta2': beta2,
            'alpha1': alpha1,
            'alpha2': alpha2}
    Database = pd.DataFrame(data, columns=['R%','U', 'Wu1', 'W1', 'Wu2', 'W2', 'Cm', 'Cu1', 'Cu2', 'WE', 'beta1', 'beta2', 'alpha1', 'alpha2'])
    return(data,Database,We)
