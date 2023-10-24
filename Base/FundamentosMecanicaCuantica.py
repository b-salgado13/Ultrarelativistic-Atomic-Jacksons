"""
Este módulo contiene funciones relacionadas con los fundamentos de mecánica cuántica:
  - Normalización
  - Valor esperado de una observable
  - Probabilidad
  - ?
"""

import numpy as np
import scipy.integrate as integrate

def Normalizacion(psi, a, b):
    """
    Se realiza la integral sobre un intervalo [a,b]
    """
    norm_constant = integrate.quad(psi*psi.conjugate(), a, b)
    return norm_constant

#Aun no queda jsjs
A = Normalizacion(lambda x: np.exp(-x^2/16),-np.inf, np.inf)
print(A)