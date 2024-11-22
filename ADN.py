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
        print("¿Qué tipo de mutación desea realizar?")
        print("1. Radiación")
        print("2. Virus")
        tipo_mutacion = int(input())
        if tipo_mutacion == 1:
            print("Ingrese la base nitrogenada que desea mutar (A, C, G o T):")
            base_nitrogenada = input().upper()
            print("Ingrese la posición inicial de la mutacion (fila y columna):")
            fila = int(input()) - 1
            columna = int(input()) - 1
            print("Ingrese la orientación de la mutación (H o V):")
            orientacion = input().upper()
            radiacion = clases.Radiacion(base_nitrogenada, 4)
            matriz = radiacion.crear_mutante(matriz, (fila, columna), orientacion)
        elif tipo_mutacion == 2:
            print("Ingrese la base nitrogenada que desea mutar (A, C, G o T):")
            base_nitrogenada = input().upper()
            print("Ingrese la posición inicial de la mutación (fila y columna):")
            fila = int(input()) - 1
            columna = int(input()) - 1
            print("Ingrese el tipo de diagonal que desea mutar (principal o inversa):")
            tipo_diagonal = input().lower()
            virus = clases.Virus(base_nitrogenada, 4, tipo_diagonal)
            matriz = virus.crear_mutante(matriz, (fila, columna))
        else:
            print("Opción inválida. Intente de nuevo.")
    elif respuesta == 3:
        print("Función sanar ADN no implementada aún.")
    elif respuesta == 4:
        print("Saliendo...")
        break
    else:
        print("Opción inválida. Intente de nuevo.")
