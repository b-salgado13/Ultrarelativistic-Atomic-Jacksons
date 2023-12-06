"""
Este archivo contiene las funciones correspondientes al momento angular. Algunas cosas que incluir:
  - Generador de matriz de momento angular.
  - Generador de eigenvalores.
  - Eigenfunciones 

Pendiente:
  -Añadir el caso de l semientero        [X]
  - Prácticamente todas las funciones evalúan si l es entero o semientero, se podría definir una función IsSemiInteger para simplificar.

  
"""

import numpy as np

#Funciones auxiliares
def ValoresM(j):
  if not EnteroSemienteroPositivoQ(j):
    raise ValueError("El momento angular debe ser entero o semientero positivo")
    
  return [i for i in range(-j, j+1, 1)]

def EnteroSemienteroPositivoQ(j):
  return j%(1/2) == 0 and j >= 0


#Generadores de matrices para operadores de momento angular

def MatrizJCuadrada(l):
    """
    Generador de la matriz de momento angular L^2 para valor de l.
    """
    #Primero evaluamos que el momento angular sea entero o semientero positivo. 
    if not EnteroSemienteroPositivoQ(l):
        raise ValueError("El momento angular debe ser entero o semientero positivo")
      
    m_total = int(2*l + 1)
    L2      = np.identity(m_total)
    return L2
  
def MatrizJz(l):
    """
    Generador de la matriz de momento angular de L_Z para valor de l.
    """
  
    #Primero evaluamos que el momento angular sea entero o semientero positivo. 
    if not EnteroSemienteroPositivoQ(l):
        raise ValueError("El momento angular debe ser entero o semientero positivo")
      
    m_valores = ValoresM(l)
    m_total   = int(2*l + 1)
    Lz        = np.zeros((m_total, m_total))

    for i in range(m_total):
        Lz[i, i] = m_valores[i]

    return Lz
  
def MatrizJMasMenos(l, p=True):
    """
    Generador de la matriz de subida/bajada de momento angular L_+/L_-
    """
    
    #Primero evaluamos que el momento angular sea entero o semientero positivo. 
    if not EnteroSemienteroPositivoQ(l):
        raise ValueError("El momento angular debe ser entero o semientero positivo")
        
    m_valores = ValoresM(l)
    eigenvalores_mas_menos = np.zeros(len(m_valores))
    
    for j in range(len(m_valores)):
        #Se evalua si se requiere el operador J+ o J-
        if p is True:
            eigenvalores_mas_menos[j]= np.sqrt( l*(l+1)-m_valores[j]*(m_valores[j]+1) )
        else:
            eigenvalores_mas_menos[j]= np.sqrt( l*(l+1)-m_valores[j]*(m_valores[j]-1) )
        
    m_total   = int(2*l + 1)
    L_mas_menos = np.zeros((m_total, m_total))

    for i in range(m_total-1):
        #Nuevamente se evalua si se requiere el operador J+ o J-
        if p is True:
            L_mas_menos[i, i+1] = eigenvalores_mas_menos[i]
        else:
            L_mas_menos[i+1, i] = eigenvalores_mas_menos[i+1]
            
    return L_mas_menos
            
def MatrizJx(l):
    """
    Generador de matriz Jx en base a los operadores escalera
    """
    return (MatrizJMasMenos(l) + MatrizJMasMenos(l,False))/2

def MatrizJy(l):
    """
    Generador de matriz Jy en base a los operadores escalera
    """
    return complex(0,-1)*(MatrizJMasMenos(l) - MatrizJMasMenos(l,False))/2

# En base a las funciones generadoras de matrices, podemos definir las matrices de Pauli
pauli_x = 2*MatrizJx(1/2)
pauli_y = 2*MatrizJy(1/2)
pauli_z = 2*MatrizJz(1/2)
