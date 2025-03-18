def dijkstra(graph, start):
    # Inicializar distancias con infinito para todos los nodos excepto el inicio
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    # Inicializar el diccionario de predecesores
    predecessors = {node: None for node in graph}
    
    # Conjunto de nodos no visitados
    unvisited = list(graph.keys())
    
    while unvisited:
        # Encontrar el nodo no visitado con la distancia mínima
        current = min(unvisited, key=lambda node: distances[node])
        
        # Si la distancia es infinita, no hay camino a los nodos restantes
        if distances[current] == float('infinity'):
            break
        
        # Remover el nodo actual del conjunto de no visitados
        unvisited.remove(current)
        
        # Revisar todos los vecinos del nodo actual
        for neighbor, weight in graph[current].items():
            distance = distances[current] + weight
            
            # Si encontramos una distancia más corta, la actualizamos
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current
    
    return distances, predecessors

def get_shortest_path(predecessors, start, end):
    path = []
    current = end
    
    while current != start:
        path.append(current)
        current = predecessors[current]
        if current is None:
            return None  # No hay camino
    
    path.append(start)
    path.reverse()
    
    return path

# Definir el grafo basado en la imagen proporcionada
graph = {
    'A': {'B': 4, 'C': 8},
    'B': {'A': 4, 'H': 8, 'C': 11},
    'C': {'A': 8, 'B': 11, 'I': 7, 'G': 1},
    'D': {'H': 7, 'F': 14, 'E': 9},
    'E': {'D': 9, 'F': 10},
    'F': {'D': 14, 'E': 10, 'G': 2},
    'G': {'C': 1, 'F': 2, 'I': 6},
    'H': {'B': 8, 'D': 7, 'I': 2},
    'I': {'H': 2, 'C': 7, 'G': 6}
}

# Ejecutar el algoritmo de Dijkstra desde el nodo A
start_node = 'A'
distances, predecessors = dijkstra(graph, start_node)

# Mostrar las distancias más cortas desde A a todos los demás nodos en formato de tabla
print("Distancias más cortas desde", start_node)
print("=" * 40)
print("| Nodo | Distancia |")
print("|------|-----------|")
for node in sorted(graph.keys()):
    print(f"| {node}    | {distances[node]:<9} |")
print("=" * 40)

# Mostrar el camino más corto desde A hasta cada nodo en formato de tabla
print("\nCaminos más cortos desde", start_node)
print("=" * 60)
print("| Destino | Camino                  | Distancia |")
print("|---------|-------------------------|-----------|")
for node in sorted(graph.keys()):
    if node != start_node:
        path = get_shortest_path(predecessors, start_node, node)
        path_str = ' → '.join(path)
        print(f"| {node}       | {path_str:<23} | {distances[node]:<9} |")
print("=" * 60)