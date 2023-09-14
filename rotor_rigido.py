from math import *
import numpy as np
import matplotlib.pyplot as plt

def e_rot(m,I):
    '''
    Funcion que devuelve la energia rotacional

    Se ingresa los siguientes valores
    (m) que puede tomar valores desde 0, +-1, +-2, ...
    (I) momento de inercia [kg m**2]
        
    '''
    hb = 1.05457182*10**(-34)  # hbarra [(m**2 kg)/s]
    return (m**2 * hb**2)/(2*I)
'''
Ejemplo 

    La energia rotacional para la molecula metano puede 
    ser calculada usando I = 5*10**(-47)
'''
#print(e_rot(1,5.33*10**(-47)))
#Declaracion de funciones que devuelven la parte real 
#e imaginaria de la funcion de onda

f_real       = lambda m,phi: sqrt(1/2)*np.cos(m*phi) #parte real 
f_imaginaria = lambda m,phi: sqrt(1/2)*np.sin(m*phi) #parte imaginaria   

#----------------------------------------------

#Graficacion de la funcion de onda para distintos valores de m 

n = int(input("Ingresa el valor máximo de m: "))
ml = range(n)

for i in ml:    
    x  = np.arange(0,2*pi,0.01)
    y1 = f_real(i,x)    
    plt.plot(x,y1)

plt.title("Funcion de onda para distintos valores de m")
plt.grid()
plt.show()

