import random
import clases
matriz = [[None for _ in range(6)] for _ in range(6)]
matriz = clases.completar_matriz(matriz)
print("Asi quedaria")
for fila in matriz:
    print(" ".join(fila))
menu = """
====================================
              MENÚ
====================================
1. Detectar Mutaciones
2. Mutar ADN
3. Sanar ADN
4. Salir
====================================
Seleccione una opción: 
"""
respuesta = None
while respuesta !=4:
    print(menu) 
    respuesta=input()
    if respuesta==1:
        print("xd")
    if respuesta==2:
        print("xd")
    if respuesta==3:
        print("xd")
  