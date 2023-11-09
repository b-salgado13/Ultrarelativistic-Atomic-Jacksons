"""
Este archivo sirve para encontrar las representaciones Irreducibles del Grupo de Simetria:
  - C2v 
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

  
C2v_num = np.array([[1, 1, 1, 1],
[1, 1, -1, -1],
[1, -1, 1, -1],
[1, -1, -1, 1]])

C2v_op = np.array([1, 1, 1, 1])

C2v_nom = np.array(["A1", "A2", "B1", "B2"])
Gamma_orb = np.array([10, 0, 2, 4])
h = np.sum(C2v_op)
print("** REPRESENTACIONES IRREDUCIBLES, GRUPO C2v ** \n")
print("--> h = %i \n"%h)
print("---> Gamma_orb = ", Gamma_orb)

a_Gamma_orb = a(h,C2v_op, Gamma_orb, C2v_num)
Imprimir_a(a_Gamma_orb, C2v_nom, h, "Gamma_orb")

