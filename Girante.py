import numpy as np
import pandas as pd

def Girante(g,H,omega,Q,k1,k2,Di,De):
    We = g * H                                         # lavoro di Eulero

    step = 11
    mid = 6
    r = np.linspace(Di, De, step, endpoint=True)
    U = omega * r                                       # blade speed
    phi = Q / (omega * (2 * r) ** 3)                    # flow coefficient

    # Free vortex: Cm costante

    Cm = phi[mid] * U[mid]                              # componente assiale velocità assoluta (midspan)

    # Prova eq.Radiale

    Cu1 = k1 / r
    Cu2 = k2 / r

    # Triangoli di velocità

    alpha1 = (np.arctan(k1 / (r * Cm)) / (2 * 3.14)) * 360  # gli angoli sono espressi in gradi
    alpha2 = (np.arctan(k2 / (r * Cm)) / (2 * 3.14)) * 360
    beta1 = (np.arctan((U / Cm) - (k1 / (r * Cm)))) / (2 * 3.14) * 360
    Wu1 = U - Cu1
    Wu2 = U - Cu2
    data = {'U': U,
            'Cm': Cm,
            'Cu1': Cu1,
            'Cu2': Cu2,
            'Wu1': Wu1,
            'Wu2': Wu2,
            'beta1': beta1,
            'alpha1': alpha1,
            'alpha2': alpha2}
    Database = pd.DataFrame(data, columns=['U', 'Wu1', 'Wu2', 'Cm', 'Cu1', 'Cu2', 'beta1', 'alpha1', 'alpha2'])
    return(data,Database,mid)