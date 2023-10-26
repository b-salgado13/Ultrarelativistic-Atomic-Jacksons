def MatrizRotacion(angulo, eje):
    """
    Esta función calcula la matriz de rotación 3D alrededor de un eje (unitario) arbitrario cierto angulo
    
    Input:
        float angulo              -> Angulo en radianes
        array eje[ux, uy, uz]     -> eje de rotación (debe ser unitario)
        
    Output:
        
        array 3x3                 -> Matriz de rotación
    """
    coseno = np.cos(angulo)
    seno = np.sin(angulo)
    ux, uy, uz = eje
    
    matriz_rotacion = np.array([
        [coseno + ux**2*(1 - coseno),    ux*uy*(1 - coseno) - uz*seno,   ux*uz*(1 - coseno) + uy*seno],
        [uy*ux*(1 - coseno) + uz*seno,   coseno + uy**2*(1 - coseno),    uy*uz*(1 - coseno) - ux*seno],
        [uz*ux*(1 - coseno) - uy*seno,   uz*uy*(1 - coseno) + ux*seno,   coseno + uz**2*(1 - coseno)]
    ])
    
    return matriz_rotacion


class OperacionRotacion:
    
    def __init__(self, n, eje, sentido=True):
        """
        Inicialización del Operador de rotacion
        
        Input: 
            int n                  -> Tipo de rotación "n-fold", dada por 2pi/n
            eje[ux, uy, uz]        -> Eje de rotación (unitario) 
            base                   -> Base para representar la operacion
            sentido                -> Sentido de la rotación
                                        True: horario;  False: antihorario
                                       
        """
        self.eje     = eje
        self.n       = n
        self.sentido = sentido 
       
    
    def RepresentacionMatricial(self):
        """
        Obtiene la representación matricial del operador de rotación
        """
        angulo = 2*np.pi/self.n
        
        if self.sentido == False: angulo = - angulo
    
        return MatrizRotacion(angulo, self.eje)
    
    def Caracter(self):
        return np.trace(self.RepresentacionMatricial())
    
    #def Cambio de base
    


#class OperacionIdentidad:
    
    #def __init__(self, base):
     #   self.base = base
       
    #def RepresentacionMatricial(self):
    #    return np.identity( len(self.base) )
    
    #def Caracter(self):
    #    return np.trace(self.RepresentacionMatricial())
    
    #def Operar(self, element):
        #return element   
    
