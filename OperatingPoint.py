import math

def OperatingPoint( f, Np, rho, Q, g, H, efficiency):

    N = (120 * f) / Np                                              # condizione di sincronismo [rpm]
    omega = (2 * math.pi * N) / 60                                  # [rad/s]
    P = rho * Q * g * H * efficiency                                # potenza
    Ns = (omega * (P / rho) ** 0.5) / ((g * H) ** 1.25)             # numero di giri specifico adimensionale[rad]: 1.8<Ns<5
    Nsd = (N * (P / 1000) ** 0.5) / (H ** 1.25)                     # numero di giri dimensionale : 400<Nsd<900
    omegas = omega * (Q ** 0.5) / ((g * H) ** (3 / 4))              # velocità specifica
    Z = 5                                                           # pale runner
    return(N, omega, P, Ns, Nsd, omegas, Z)