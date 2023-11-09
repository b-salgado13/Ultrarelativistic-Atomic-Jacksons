"""
Este archivo sirve para encontrar las representaciones Irreducibles del Grupo de Simetria:
  - D2h 
"""

import numpy as np

def a(h, Op, Gamma, Num):
  a = np.zeros((1,h))
  C = []
  for i in range(0, h-1):
    C = [0]
    for j in range(0, h-1):
      c = Op[j] * Gamma[j] * Num[i][j]
      C.append(c)
    a[0][i] = sum(C) / h 
  return a


def Imprimir_a(a, Nom, h, Gamma):
  print("\n-----> {} contiene las Siguientes Representaciones Irreducibles: ".format(Gamma))
  rep_irre=[]
  for i in range(0, h):
    if i < h:
      if a[0][i].is_integer():  
        if a[0][i] > 0:
          num = a[0][i]
          rep_irre.append(str(num) + ' ' + str(Nom[i]))
      else: 
        print("ERROR: a es un numero fraccionario, hay algun problema en Gamma")
  print("--->", rep_irre)

    

D2h_num = np.array([ [1,1,1,1,1,1,1,1],
[1, 1, -1, -1, 1, 1, -1, -1],
[1, -1, 1, -1, 1, -1, 1, -1],
[1, -1, -1, 1, 1, -1, -1, 1],
[1, 1, 1, 1, -1, -1, -1, -1],
[1, 1, -1, -1, -1, -1, 1, 1],
[1, -1, 1, -1, -1, 1, -1, 1],
[1, -1, -1, 1, -1,1,1, -1]])

D2h_op = np.array([1, 1, 1, 1, 1, 1, 1, 1])

D2h_nom = np.array(["Ag", "B1g", "B2g", "B3g", "Au", "B1u", "B2u", "B3u"])
Gamma_a = np.array([4, 0, 0, 0, 0, -4, 0, 0])
Gamma_b = np.array([4, 0, 0, 0, 0, -4, 0, 0])
Gamma_c = np.array([2, 0, 2, 0, 0, -2, 0, -2])
h = np.sum(D2h_op)
print("** REPRESENTACIONES IRREDUCIBLES, GRUPO D2h ** \n")
print("--> h = %i \n"%h)
print("---> Gamma_a = ", Gamma_a)
print("---> Gamma_b = ", Gamma_b)
print("---> Gamma_c = ", Gamma_c)

a_Gamma_a = a(h,D2h_op, Gamma_a, D2h_num)
Imprimir_a(a_Gamma_a, D2h_nom, h, "Gamma_a")
a_Gamma_b = a(h,D2h_op, Gamma_b, D2h_num)
Imprimir_a(a_Gamma_b, D2h_nom, h, "Gamma_b")
a_Gamma_c = a(h,D2h_op, Gamma_c, D2h_num)
Imprimir_a(a_Gamma_c, D2h_nom, h, "Gamma_c")

