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
                    self.posicionInicio=f"fila: {i}, columna: {i}"
                    self.direccion="horizontal"
                    return True

        for col in range(columnas):
            for row in range(filas - 3):
                if len(set([lista[row + i][col] for i in range(4)])) == 1:
                    self.base_mutada=lista[row + i][col]
                    self.posicion_numero=col
                    self.posicionInicio=f"fila: {row}, columna: {col}"
                    self.direccion="vertical"
                    return True

        for row in range(filas - 3):
            for col in range(columnas - 3):
                if len(set([lista[row + i][col + i] for i in range(4)])) == 1:
                    self.base_mutada=fila[i]
                    self.posicionInicio=f"fila: {row}, columna: {col}" 
                    self.direccion="diagonal principal"
                    return True

        for row in range(filas - 3):
            for col in range(3, columnas): 
                if len(set([lista[row + i][col - i] for i in range(4)])) == 1:
                    self.base_mutada=fila[i]
                    self.posicionInicio=f"fila: {row}, columna: {col}" 
                    self.direccion="diagonal inversa"
                    return True

        return False
    
    
    def informacion_detectada(self):
        print(f"la mutación es de base: {self.base_mutada} y está sobre {self.posicionInicio} con dirección {self.direccion}")    
def completar_matriz(matriz):
    for i in range(6):
        adn = input(f"Ingrese una cadena de ADN de 6 letras para la fila {i+1}: ")
        while len(adn) != 6 or not all(c in "ACGT" for c in adn.upper()):
            print("Error: Debe ser una cadena de exactamente 6 letras (solo A, C, G, T).")
            adn = input(f"Ingrese una cadena de ADN de 6 letras para la fila {i+1}: ")
        
        print("Cadena correcta.")
        for j in range(6):
            matriz[i][j] = adn[j]
    return matriz

