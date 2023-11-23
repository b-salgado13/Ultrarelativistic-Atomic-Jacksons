"""
Este archivo contiene las constantes físicas de mayor relevancia que se utilizan a lo largo de los diferentes módulos.
¿Se llaman vía scipy o no? SI

Propuestas de convenio para llamar constantes:
  1. Por su símbolo asociado.
  2. Por su nombre literal.  -> Propongo esta opción

  Ejemplo: velocidad de la luz:
    1. La variable se declararía como "c"
    2. La variable se declararía como "velocidad_luz" o "velocidad_de_la_luz" o "v_luz", etc.

Este módulo está basado en el diccionario de scipy.constants.physical_constants:

https://docs.scipy.org/doc/scipy/reference/constants.html#mathematical-constants
"""

from scipy.constants import physical_constants
from scipy.constants import pi
#Constantes matemáticas
pi = pi #xd

#Constantes universales bien perras importantes
hbarra         = physical_constants["reduced Planck constant"][0]
carga_electron = physical_constants["elementary charge"][0]


#Masas
masa_electron = physical_constants["electron mass"][0]
masa_proton   = physical_constants["proton mass"][0]
masa_neutron  = physical_constants["neutron mass"][0]

#Conversión
electron_uma = 5.485799*10**(-4)

