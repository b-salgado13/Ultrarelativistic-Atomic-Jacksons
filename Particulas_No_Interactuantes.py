#PARTICIULAS NO INTERACTUANTES EN UNA CAJA UNIDIMENSIONAL

h = 6.626070e-34
hbar = 1.0545771e-34

def iniciar():
  print("---------------------------------------")
  print("--- PARTICULAS NO INTERACTUANTES EN ---\n--- UNA CAJA UNIDIMENSIONAL---")
  print("---------------------------------------")
  N = int(input("--> Ingrese el número de partículas no interactuantes: "))
  print("---------------------------------------")
  L =  float(input("--> Ingrese la longitud de la caja undimensional en m: "))
  print("---------------------------------------")
  return L, N


def Obtener_Masas(N):
  m = []
  for i in range(0, N):
    mi = float(input("--> Ingrese la masa de la particula %i en kg: "%(i+1)))
    m.append(mi)
  print("---> Masas = ", m)
  print("---------------------------------------")
  return m

def Obtener_Niveles(N):
  n = list(int(num) for num in input("--> Ingrese Niveles a Obtener separados por espacios: ").strip().split())[:N]
  print("--->Niveles = ", n)
  print("---------------------------------------")
  return n

def E(n, C, m):
  Enn = []
  for i in range(0, len(n)):
    E = C * ((n[i]**2)/(m[i]))
    Enn.append(E)
  En = sum(Enn)
  En_eV = En * 6.242e18
  print("--> Energía = {:.3e} Joules, {:.2e} eV".format(En, En_eV))
  print("---------------------------------------")
  return En, En_eV

L, N = iniciar()
m = Obtener_Masas(N)

C = h**2 / (8 * L**2)
i = 0

iter = int(input("--> ¿Cuantas iteraciones desea hacer? "))

for i in range(0,iter):
  n = Obtener_Niveles(N)
  E(n, C, m)
  i = i +1
