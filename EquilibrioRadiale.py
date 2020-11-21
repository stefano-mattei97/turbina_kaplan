# importa math (nel modo sbagliato) e numpy per poter gestire le matrici
from math import *
import numpy as np


def radialSolution_UpWind(_Rc, _beta2, _omega, _Q):
    A = np.zeros((len(_Rc), len(_Rc)), dtype=float)
    B = np.zeros((len(_Rc)), dtype=float)

    A[len(_Rc) - 1, 0] = pi * (_Rc[1] ** 2 - _Rc[0] ** 2) / 2
    A[len(_Rc) - 1, len(_Rc) - 1] = pi * (_Rc[len(_Rc) - 1] ** 2 - _Rc[len(_Rc) - 2] ** 2) / 2

    B[len(_Rc) - 1] = _Q

    for i in range(0, len(_Rc) - 1):
        A[i, i] = (_Rc[i] * (tan(radians(_beta2[i]))) * ((tan(radians(_beta2[i + 1]))) - (tan(radians(_beta2[i])))) + (
                    (tan(radians(_beta2[i]))) ** 2) * (_Rc[i + 1] - _Rc[i]) - _Rc[i] * (
                               1 + (tan(radians(_beta2[i]))) ** 2)) / (_Rc[i] * (_Rc[i + 1] - _Rc[i]))
        A[i, i + 1] = (1 + (tan(radians(_beta2[i]))) ** 2) / ((_Rc[1 + i] - _Rc[i]))
        B[i] = 2 * _omega * tan(radians(_beta2[i]))

    for i in range(1, len(_Rc) - 1):
        A[len(_Rc) - 1, i] = pi * (_Rc[i + 1] ** 2 - _Rc[i - 1] ** 2) / 2

    # Soluzione del sistema

    invA = np.linalg.inv(A)
    Cx2 = np.dot(invA, B)

    _Qtot = 0

    for i in range(0, len(_Rc) - 1):
        _Qtot = _Qtot + pi * (_Rc[i + 1] ** 2 - _Rc[i] ** 2) * (Cx2[i + 1] + Cx2[i]) * 0.5
    return (Cx2, _Qtot)