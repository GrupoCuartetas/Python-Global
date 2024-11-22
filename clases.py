import random
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#


class Detector():
    def __init__(self):
        self.direccion=None
        self.posicionInicio=None
        self.base_mutada=None

    
    def detectar_mutante(self, lista):
        filas = len(lista)
        columnas = len(lista[0])

        for fila in lista:
            for i in range(columnas - 3):
                if len(set(fila[i:i+4])) == 1:
                    self.base_mutada=fila[i]
                    self.posicionInicio=f"fila: {i+1}, columna: {i+1}"
                    self.direccion="radiación"
                    return True

        for col in range(columnas):
            for row in range(filas - 3):
                if len(set([lista[row + i][col] for i in range(4)])) == 1:
                    self.base_mutada=lista[row + i][col]
                    self.posicion_numero=col
                    self.posicionInicio=f"fila: {row+1}, columna: {col+1}"
                    self.direccion="radiación"
                    return True

        for row in range(filas - 3):
            for col in range(columnas - 3):
                if len(set([lista[row + i][col + i] for i in range(4)])) == 1:
                    self.base_mutada=fila[i]
                    self.posicionInicio=f"fila: {row+1}, columna: {col+1}" 
                    self.direccion="virus"
                    return True

        for row in range(filas - 3):
            for col in range(3, columnas): 
                if len(set([lista[row + i][col - i] for i in range(4)])) == 1:
                    self.base_mutada=fila[i]
                    self.posicionInicio=f"fila: {row+1}, columna: {col+1}" 
                    self.direccion="virus"
                    return True

        return False
    
    
    def informacion_detectada(self):
        print(f"la mutación es de base: {self.base_mutada} y está sobre {self.posicionInicio}, infeccion de tipo: {self.direccion}")  


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#         


class Sanador: 
  def __init__(self, matriz_ADN, esMutante): 
    self.matriz_ADN = matriz_ADN; 
    self.esMutante = esMutante; 
  # Genera una nueva matriz de ADN de 6 x 6, que se va a utilizar en caso de que el adn de la def sanar_mutantes detecte una matriz infectada 
  def nueva_matriz(self): 
    nueva_matrizADN = []
    
    for i in range(6): # Nos da las filas de la matriz 
        aleatorio_ADN = "".join(random.choices("ATGC",k=6)) # Genera string aleatorio, recibe como param las letras que quiero que contenga, y la longitud del string a crear 
        nueva_matrizADN.append(list(aleatorio_ADN)) 
                        

    return nueva_matrizADN         
  # Funcion que verifica el adn ,si esta infectado, genera un adn nuevo sin mutaciones, sino, devuelve el adn 
  def sanar_mutantes(self): 
    if self.esMutante: 
      nuevaMatriz=self.nueva_matriz() 
      # Verifica la matriz creada, si esta infectada genera otra hasta que genere una que no este infectada 
      while Detector().detectar_mutante(nuevaMatriz): 
        nuevaMatriz=self.nueva_matriz() 
      return nuevaMatriz
    else: 
      return self.matriz_ADN
    

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#


def completar_matriz(matriz):
    for i in range(6):
        adn = input(f"Ingrese una cadena de ADN de 6 letras para la fila {i+1}: ").upper()
        while len(adn) != 6 or not all(c in "ACGT" for c in adn.upper()):
            print("Error: Debe ser una cadena de exactamente 6 letras (solo A, C, G, T).")
            adn = input(f"Ingrese una cadena de ADN de 6 letras para la fila {i+1}: ").upper()
        
        print("Cadena correcta.")
        for j in range(6):
            matriz[i][j] = adn[j]
    return matriz

class Mutador:
    def __init__(self, base_nitrogenada, tipo_mutacion, size_mutacion=4):
        
        self.base_nitrogenada = base_nitrogenada
        self.tipo_mutacion = tipo_mutacion
        self.size_mutacion = size_mutacion

    def crear_mutante(self):
        
        pass


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#

class Radiacion(Mutador):
    def __init__(self, base_nitrogenada, size_mutacion):
        super().__init__(base_nitrogenada, "horizontal/vertical", size_mutacion)

    def crear_mutante(self, matriz, posicion, orientacion):
        fila, columna = posicion
        if orientacion not in ["H", "V"]:
            raise ValueError("La orientacion debe ser H o V")
        if orientacion == "H":
            try:
                matriz[fila][columna + self.size_mutacion]=matriz[fila][columna + self.size_mutacion]
                for i in range(columna, columna + self.size_mutacion):
                    matriz[fila][i] = self.base_nitrogenada        
            except IndexError:
                for i in range(columna, columna - self.size_mutacion, -1):
                    matriz[fila][i] = self.base_nitrogenada


        elif orientacion == "V":
            try:
                matriz[fila+self.size_mutacion][columna] = matriz[fila+self.size_mutacion][columna]
                for i in range(fila, fila + self.size_mutacion):
                    matriz[i][columna] = self.base_nitrogenada
            except IndexError:    
                
                for i in range(fila, fila - self.size_mutacion, -1):
                    matriz[i][columna] = self.base_nitrogenada       
            
        
        return matriz


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#


class Virus(Mutador):
    def __init__(self, base_nitrogenada, size_mutacion, tipo_diagonal):
        super().__init__(base_nitrogenada, "diagonal", size_mutacion)
        self.tipo_diagonal = tipo_diagonal

    def crear_mutante(self, matriz, posicion_inicial):
        try:
            fila, columna = posicion_inicial
            if self.tipo_diagonal == "principal":
                try:
                    try:
                        for i in range(self.size_mutacion):
                            matriz[fila + i][columna + i] = self.base_nitrogenada
                    except IndexError:
                        for i in range(self.size_mutacion):
                            matriz[fila - i][columna - i] = self.base_nitrogenada
                except IndexError:
                    print("Espacio no valido en el ADN")

            elif self.tipo_diagonal == "inversa":
                try:
                    try:
                        for i in range(self.size_mutacion):
                            matriz[fila + i][columna - i] = self.base_nitrogenada
                    except IndexError:
                        for i in range(self.size_mutacion):
                            matriz[fila - i][columna + i] = self.base_nitrogenada
                except IndexError:
                    print("Espacio no valido en el ADN")
            else:
                raise ValueError("Tipo de diagonal no válido")
            # for i in range(6):
            #     for j in range(6):
            #         if (i, j) not in [(fila + k, columna + k) for k in range(self.size_mutacion)] and (i, j) not in [(fila + k, columna - k) for k in range(self.size_mutacion)]:
            #             matriz[i][j] = random.choice("ACGT")

            return matriz
        except Exception as e:
            print(f"Error: {e}")
            return None
