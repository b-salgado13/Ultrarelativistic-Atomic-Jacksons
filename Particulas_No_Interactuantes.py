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

"""def encontrar_configuraciones_menor_energia(m1, m2, m3, rango_n, num_configuraciones):
    configuraciones = []

    # Probar todas las posibles configuraciones de energía para cada n de cada partícula
    for n1 in rango_n:
        for n2 in rango_n:
            for n3 in rango_n:
                # Calcular la energía total para esta configuración
                E1 = (n1 ** 2) / m1
                E2 = (n2 ** 2) / m2
                E3 = (n3 ** 2) / m3
                energia_total = E1 + E2 + E3

                # Almacenar la configuración y su energía total
                configuracion = (n1, n2, n3)
                
                # Comprobar que una configuración no tenga una energía duplicada
                if not any(energia_total in nested_list for nested_list in configuraciones):
                    configuraciones.append((configuracion, energia_total))

    # Ordenar las configuraciones por energía total
    configuraciones.sort(key=lambda x: x[1])

    # Seleccionar las primeras N configuraciones
    mejores_configuraciones = configuraciones[:num_configuraciones]

    return mejores_configuraciones

# Valores iniciales (m = masa | n = num. cuant. princ. | 
#  rango = valores que puede tomar n | num_configuraciones = primeros n niveles de energía)
m1 = 9
m2 = 5
m3 = 5
n1 = n2 = n3 = 1
rango_n = range(1, 6)  # Por ejemplo, valores de n de 1 a 5
num_configuraciones = 5  # Obtener las primeras 3 configuraciones de menor energía

resultados = encontrar_configuraciones_menor_energia(m1, m2, m3, rango_n, num_configuraciones)
print(resultados)"""
