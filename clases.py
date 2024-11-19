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