# DISTANCIA INTERATOMICA APARTIR DE FRECUENCIA DE ABSORCION

N_A = 6.022e23 # Numero de Avogadro
import math
import pandas as pd

import Base.Constantes as const
import Base.TablaPeriodica as elementos

def iniciar(Simbolos, Masas_Atomicas):
  print("---------------------------------------")
  print("--- DISTANCIA INTER ATÓMICA ---\n--- A PARTIR DE FRENCUENCIA DE ABSORCION---")
  print("---------------------------------------")
  Elemento_1 = input("--> Elemento 1: ")
  E1 = elementos.Atomo[Elemento_1]
  isotopos_1 = pd.DataFrame(E1).iloc[:, 0:len(E1)-1]*const.electron_uma
  print("Isótopos disponibles:")
  print(isotopos_1)
  I1 = input("-->Isotopo: ")
  M1 = elementos.Atomo[Elemento_1][int(I1)]['masa']*const.electron_uma

  Elemento_2 = input("--> Elemento 2: ")
  E2 = elementos.Atomo[Elemento_2]
  isotopos_2 = pd.DataFrame(E2).iloc[:, 0:len(E2)-1]*const.electron_uma
  print("Isótopos disponibles:")
  print(isotopos_2)
  I2 = input("-->Isotopo: ")
  M2 = elementos.Atomo[Elemento_2][int(I2)]['masa']*const.electron_uma
  print("--> Masa de {:} = {:} g/mol".format(Elemento_1, M1))
  print("--> Masa de {:} = {:} g/mol".format(Elemento_2, M2))
  print("---------------------------------------")
  nu =  float(input("--> La frecuencia de absorción en Hz: "))
  J =  float(input("--> El nível energético J: "))
  print("---------------------------------------")
  return M1, M2, nu, J

def d(nu, mu, J):
  hbar = 1.0545771e-34 # H barra
  J_F = (J*(J+1))
  if J == 0:
    J_F = 1
  h = 6.626070e-34 #Cte de Planck
  d = math.sqrt( (J_F*(hbar**2 ) )/(2 * mu* h * nu))
  print("--> d = {:.8} Armstrongs".format(d *10e9))
  print("---------------------------------------")
  return d

M1, M2, nu, J = iniciar(Simbolos, Masas_Atomicas)
mu = (M1/N_A) * (M2/N_A) / ((M2/N_A) + (M1/N_A)) / 1000 #Mu o Masa reducida
d = d(nu, mu, J)
