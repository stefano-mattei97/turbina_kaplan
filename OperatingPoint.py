import math
import pandas as pd

def OperatingPoint( f, Np, rho, Q, g, H, efficiency):

    N = (120 * f) / Np                                              # condizione di sincronismo [rpm]
    omega = (2 * math.pi * N) / 60                                  # [rad/s]
    P = rho * Q * g * H * efficiency                                # potenza
    Ns = (omega * (P / rho) ** 0.5) / ((g * H) ** 1.25)             # numero di giri specifico adimensionale[rad]: 1.8<Ns<5
    Nsd = (N * (P / 1000) ** 0.5) / (H ** 1.25)                     # numero di giri dimensionale : 400<Nsd<900
    omegas = omega * (Q ** 0.5) / ((g * H) ** (3 / 4))              # velocità specifica
    Z = 5                                                           # pale runner
    data = {'N': N,
            'Omega': omega,
            'P': P,
            'Ns': Ns,
            'Nsd': Nsd,
            'Omegas': omegas,
            'Z': Z}
    OperatingPointdb = pd.DataFrame(data, columns=['N','Omega','P','Ns','Nsd','Omegas','Z'],index=[0])


    return(OperatingPointdb)