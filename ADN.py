import clases

matriz = [[None for _ in range(6)] for _ in range(6)]
matriz = clases.completar_matriz(matriz)

print("Así quedaría la matriz:")
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
while respuesta != 4:
    print(menu)
    try:
        respuesta = int(input())
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue
    if respuesta == 1:
        detector = clases.Detector()
        hay_mutacion = detector.detectar_mutante(matriz)
        if hay_mutacion:
            print("La matriz está infectada.")
            detector.informacion_detectada()
        else:
            print("La matriz no está infectada.")
    elif respuesta == 2:
        print("Función mutar ADN no implementada aún.")
    elif respuesta == 3:
        print("Función sanar ADN no implementada aún.")
    elif respuesta == 4:
        print("Saliendo...")
        break
    else:
        print("Opción inválida. Intente de nuevo.")
