def crear_matriz_ciudades():
    # Inicializar matriz con ceros
    ciudades = ['Guadalajara', 'Tlaquepaque', 'Zapopan', 'Tonalá', 'Tlajomulco']
    n = len(ciudades)
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    
    # Llenar la matriz con las distancias
    # Guadalajara (0) conexiones
    matriz[0][1] = matriz[1][0] = 7  # Guadalajara - Tlaquepaque
    matriz[0][2] = matriz[2][0] = 5  # Guadalajara - Zapopan
    matriz[0][3] = matriz[3][0] = 3  # Guadalajara - Tonalá
    
    # Tlaquepaque (1) conexiones
    matriz[1][2] = matriz[2][1] = 6  # Tlaquepaque - Zapopan
    matriz[1][3] = matriz[3][1] = 2  # Tlaquepaque - Tonalá
    matriz[1][4] = matriz[4][1] = 1  # Tlaquepaque - Tlajomulco
    
    # Zapopan (2) conexiones
    matriz[2][3] = matriz[3][2] = 5  # Zapopan - Tonalá
    
    # Tonalá (3) conexiones
    matriz[3][4] = matriz[4][3] = 3  # Tonalá - Tlajomulco
    
    return matriz, ciudades

def mostrar_matriz(matriz, etiquetas=None):
    n = len(matriz)
    # Mostrar encabezado de columnas si hay etiquetas
    if etiquetas:
        print("\n    ", end="")
        for i in range(n):
            print(f"{etiquetas[i][:4]:6}", end="")
        print()
        print("    " + "------" * n)
    
    # Mostrar matriz
    for i in range(n):
        if etiquetas:
            print(f"{etiquetas[i][:4]:4}", end="")
        else:
            print(f"{i:4}", end="")
        
        for j in range(n):
            print(f"{matriz[i][j]:6}", end="")
        print()

def main():
    # Ejercicio 1: Matriz de ciudades
    print("\nEjercicio 1: Matriz de adyacencia de distancias entre ciudades")
    matriz_ciudades, nombres_ciudades = crear_matriz_ciudades()
    mostrar_matriz(matriz_ciudades, nombres_ciudades)
    
    # Ejercicio 2: Matriz dada
    print("\nEjercicio 2: Matriz de adyacencia dada")
    matriz_2 = [
        [0, 1, 1, 1, 0],
        [1, 0, 1, 0, 1],
        [1, 1, 0, 1, 1],
        [0, 1, 1, 0, 1],
        [0, 1, 1, 0, 0]
    ]
    vertices = ['A', 'B', 'C', 'D', 'E']
    mostrar_matriz(matriz_2, vertices)

if __name__ == "__main__":
    main()