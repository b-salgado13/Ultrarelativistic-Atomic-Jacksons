""" Este programa es para graficar los orbitales de un átomo de Hidrogeno 
apartir de los armonicos esfericos """

from numpy import sin, cos, pi, sqrt, shape, linspace, meshgrid, zeros, array
from math import factorial
import matplotlib.pyplot as plt
import numpy as np

""" Definimos funciones"""

def EsfericosaCartesianas(r,theta,phi):

    x = r*sin(theta)*cos(phi)
    y = r*sin(theta)*sin(phi)
    z = r*cos(theta)
    
    return x, y, z

def PolinomioLegendre(l,m,x):
    pmm = 1.0
    if m > 0:
        sign = 1.0 if m % 2 == 0 else -1.0
        pmm = sign*pow(factorial(2*m-1)*(1.0-x*x),((m/2)))

    if l == m:
        return pmm

    pmm1 = x*(2*m+1)*pmm
    if l == m+1:
        return pmm1

    for n in range(m+2,l+1):
        pmn = (x*(2*n-1)*pmm1-(n+m-1)*pmm)/(n-m)
        pmm = pmm1
        pmm1 = pmn

    return pmm1

def GraficarOrbital(X, Y, Z, l, m, a, b):
  fig = plt.figure(f'Armónico {l},{m}')
  ax = fig.add_subplot(b, 1, a, projection='3d')

  ax.plot_surface(x,y,z, cmap = 'RdYlBu')

  ax.set_title(f'Armónico Esferico l = {l}, m = {m}')
  ax.set_xlabel('X', fontweight = 'bold')
  ax.set_ylabel('Y', fontweight = 'bold')
  ax.set_zlabel('Z', fontweight = 'bold')



""" Definimos los numeros cuanticos azimutales"""

L =[1,2,3]

for i in range(0, len(L)):

    l = L[i]
    print('Número cuántico azimutal l: ', l)

    if l < 0:
      zprint('l no puede ser negativo')

      """ Definimos los numeros cuanticos magneticos"""
    M = np.arange(-l, l+1, 1)
    print('Números cuánticos magneticos m: ', M)

    for i in range(0, len(M)):
        m = M[i]
        A = sqrt(((2*l+1)*factorial(l-abs(m)))/(4*pi*factorial(l+abs(m)))) # Constante de normalización

        phi = linspace(0,2*pi,181)
        theta = linspace(0,pi,91)

        Phi,Theta = array(meshgrid(phi,theta))

        if m>0:
                
            rho = pow(abs(sqrt(2)*A*cos(m*Phi)*PolinomioLegendre(l,m,cos(Theta))),2)
                
        elif m < 0:
                
            rho = pow(abs(sqrt(2)*A*sin(abs(m)*Phi)*PolinomioLegendre(l,abs(m),cos(Theta))),2)
                
        else:
                
            rho = pow(abs(A*PolinomioLegendre(l,0,cos(Theta))),2)

        x,y,z = EsfericosaCartesianas(abs(rho),Theta,Phi)
        
        GraficarOrbital(x, y, z, l, m, i+1, len(M))
    plt.show()


