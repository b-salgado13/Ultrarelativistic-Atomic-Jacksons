"""
Este archivo contiene las funciones correspondientes al momento angular. Algunas cosas que incluir:
  - Generador de matriz de momento angular.
  - Generador de eigenvalores.
  - Eigenfunciones 
"""

import numpy as np

# Matrices de Pauli
pauli_x = np.array([[0, 1], [1, 0]])
pauli_y = np.array([[0, complex(0, -1)], [complex(0, 1), 0]])
pauli_z = np.array([[1, 0], [0, -1]])


#Generadores de matrices para operadores de momento angular

def MatrizJCuadrada(l):
  """
  Generador de la matriz de momento angular L^2 para valor de l.

  TODO:
    Añadir error para que se evalue que l sea entero o semientero positivo. 
  """
  m_total = int(2*l + 1)
  L2 = np.identity(m)
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
      Lz[i, i] = m[i]

  return Lz
  
    

def MatrizL2():

def MatrizLMasMenos():

            
