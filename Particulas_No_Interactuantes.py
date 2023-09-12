""" Este programa es para hallar los niveles energéticos de un sistema con 
N partículas no interactuantes """
N, L= 0, 0.0
H = 6.626070e-34
HBAR = 1.0545771e-34
#Sección inicial
print("---------------------------------------")
print("--- PARTICULAS NO INTERACTUANTES EN ---\n--- UNA CAJA UNIDIMENSIONAL---")
print("---------------------------------------")
N = int(input("--> Ingrese el número de partículas no interactuantes: "))
print("---------------------------------------")
L =  float(input("--> Ingrese la longitud de la caja undimensional en m: "))

print("---------------------------------------")
#Sección para obtener las masas
masas = []
for i in range(0, N):
    mi = float(input(f"--> Ingrese la masa de la particula {i+1} en kg: "))
    masas.append(mi)
print("---> Masas = ", masas)
print("---------------------------------------")


def obtener_niveles(A):
    """Función que obtiene los valores de n para cada
    una de las N partículas"""
    n = list(int(num) for num in input("--> Ingrese Niveles a Obtener separados por espacios: ").strip().split())[:A]
    print("--->Niveles = ", n)
    print("---------------------------------------")
    return n


def energia(n, C, m):
    """Función que calcula la energía de cada una de las N partículas
    para el valor correspondiente de n, y las suma"""
    enn = []
    for j in range(0, len(n)):
        E = C * ((n[j]**2)/(m[j]))
        enn.append(E)
    en = sum(enn)
    energia_elecvolt = en * 6.242e18
    print("--> Energía = {:.3e} Joules, {:.2e} eV".format(en, energia_elecvolt))
    print("---------------------------------------")
    return en, energia_elecvolt


Cons = H**2 / (8 * L**2)
i = 0

iteraciones = int(input("--> ¿Cuantas iteraciones desea hacer? "))

for i in range(0,iteraciones):
    nivel = obtener_niveles(N)
    energia(nivel, Cons, masas)
    i = i +1
