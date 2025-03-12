def floyd_warshall(graph):
    """
    Algoritmo de Floyd-Warshall simplificado que devuelve las matrices
    de distancias y recorridos, tanto iniciales como finales.
    """
    n = len(graph)
    
    # 1. Matrices iniciales
    # Matriz de distancias inicial (copia de la matriz de adyacencia)
    dist_inicial = [[graph[i][j] for j in range(n)] for i in range(n)]
    
    # Matriz de recorridos inicial (todos los valores son '-')
    recorridos_inicial = [['-' for _ in range(n)] for _ in range(n)]
    
    # 2. Matrices que serán actualizadas
    dist = [[graph[i][j] for j in range(n)] for i in range(n)]
    recorridos = [['-' for _ in range(n)] for _ in range(n)]
    
    # 3. Algoritmo principal
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        recorridos[i][j] = f"v{k+1}"
    
    return dist_inicial, dist, recorridos_inicial, recorridos

# Representar el grafo del ejemplo
inf = float('inf')
grafo = [
    [0, 1, inf, 1, 5],    # Aristas desde v₁
    [9, 0, 3, inf, inf],  # Aristas desde v₂
    [inf, inf, 0, 4, inf], # Aristas desde v₃
    [inf, 2, 2, 0, 3],    # Aristas desde v₄
    [3, inf, inf, inf, 0]  # Aristas desde v₅
]

# Aplicar algoritmo y obtener las cuatro matrices
dist_inicial, dist_final, recorridos_inicial, recorridos_final = floyd_warshall(grafo)

# Función para imprimir matrices de forma legible
def imprimir_matriz(matriz, titulo, formato_valor=None):
    print(f"{titulo}:")
    print("    v₁  v₂  v₃  v₄  v₅")
    for i, fila in enumerate(matriz):
        if formato_valor:
            valores = [formato_valor(x) for x in fila]
        else:
            valores = [f"{x:>3}" for x in fila]
        print(f"v{i+1} | {' '.join(valores)}")
    print()

# Formato para valores numéricos (distancias)
def formato_distancia(x):
    return f"{x if x != float('inf') else '∞':>3}"

# Imprimir las cuatro matrices solicitadas
imprimir_matriz(dist_inicial, "1. Matriz de distancias inicial (D₀)", formato_distancia)
imprimir_matriz(dist_final, "2. Matriz de distancias final (D)", formato_distancia)
imprimir_matriz(recorridos_inicial, "3. Tabla de recorridos inicial (R₀)")
imprimir_matriz(recorridos_final, "4. Tabla de recorridos final (R)")