"""
Este archivo contiene las funciones correspondientes al momento angular. Algunas cosas que incluir:
  - Generador de matriz de momento angular.
  - Generador de eigenvalores.
  - Eigenfunciones 

Pendiente:
  -Añadir el caso de l semientero
"""

import numpy as np

#Generadores de matrices para operadores de momento angular

def MatrizJCuadrada(l):
    """
    Generador de la matriz de momento angular L^2 para valor de l.

    TODO:
      Añadir error para que se evalue que l sea entero o semientero positivo. 
    """
    m_total = int(2*l + 1)
    L2 = np.identity(m_total)
    return L2
  
def MatrizJz(l):
    """
    Generador de la matriz de momento angular de L_Z para valor de l.

    TODO:
      Añadir error para que se evalue que l sea entero o semientero positivo. 
    """
    m_valores = [i for i in range(-l, l+1, 1) ]
    m_total   = 2*l + 1
    Lz = np.zeros((m_total, m_total))

    for i in range(m_total):
        Lz[i, i] = m_valores[i]

    return Lz
  
def MatrizJMasMenos(l,p=True):
    """
    Generador de la matriz de subida/bajada de momento angular L_+/L_-
    """
    m_valores = [i for i in range(-l, l+1, 1) ]
    eigenvalores_mas_menos = np.zeros(len(m_valores))

    for j in range(len(m_valores)):
        if p is True:
            eigenvalores_mas_menos[j]= np.sqrt(l*(l+1)-m_valores[j]*(m_valores[j]+1))
        else:
            eigenvalores_mas_menos[j]= np.sqrt(l*(l+1)-m_valores[j]*(m_valores[j]-1))
    m_total   = 2*l + 1
    L_mas_menos = np.zeros((m_total, m_total))

    for i in range(m_total-1):
        if p is True:
            L_mas_menos[i, i+1] = eigenvalores_mas_menos[i]
        else:
            L_mas_menos[i+1, i] = eigenvalores_mas_menos[i+1]
    return L_mas_menos
            
def MatrizLx(l):
    return (MatrizJMasMenos(l) + MatrizJMasMenos(l,False))/2

def MatrizLy(l):
    return complex(0,-1)*(MatrizJMasMenos(l) - MatrizJMasMenos(l,False))/2
