def dijkstra(graph, start):
    # Inicializar distancias con infinito
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    # Inicializar el conjunto de nodos visitados y no visitados
    unvisited = list(graph.keys())
    visited = []
    
    # Inicializar el registro de rutas
    previous_nodes = {node: None for node in graph}
    
    # Para registrar el proceso
    process = []
    
    iteration = 0
    while unvisited:
        iteration += 1
        
        # Encontrar el nodo no visitado con la distancia mínima
        current = min(unvisited, key=lambda node: distances[node])
        
        # Si la distancia es infinita, hemos terminado
        if distances[current] == float('infinity'):
            break
            
        # Registrar el estado actual
        current_state = {
            'Iteración': iteration,
            'Nodo actual': current,
            'Distancia actual': distances[current],
            'Nodos visitados': visited.copy(),
            'Distancias': distances.copy()
        }
        
        # Marcar el nodo como visitado
        unvisited.remove(current)
        visited.append(current)
        
        # Actualizar las distancias a los vecinos del nodo actual
        for neighbor, weight in graph[current].items():
            if neighbor not in visited:
                distance = distances[current] + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current
        
        # Añadir el estado después de actualizar
        current_state['Nodos visitados después'] = visited.copy()
        current_state['Distancias después'] = distances.copy()
        process.append(current_state)
    
    return distances, previous_nodes, process

def get_path(previous_nodes, start, end):
    path = []
    current = end
    
    while current != start:
        path.append(current)
        current = previous_nodes[current]
        if current is None:
            return None  # No hay camino posible
    
    path.append(start)
    path.reverse()  # Invertir el camino para que vaya de inicio a fin
    
    return path

def print_table(headers, rows):
    # Determinar el ancho de cada columna
    col_widths = [len(str(header)) for header in headers]
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))
    
    # Imprimir encabezados
    header_row = ' | '.join(str(header).ljust(col_widths[i]) for i, header in enumerate(headers))
    print(header_row)
    print('-' * len(header_row))
    
    # Imprimir filas
    for row in rows:
        row_str = ' | '.join(str(cell).ljust(col_widths[i]) for i, cell in enumerate(row))
        print(row_str)

# Definir el grafo según la imagen
graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'A': 5, 'C': 2, 'D': 3, 'F': 12},
    'C': {'A': 2, 'B': 2, 'D': 7, 'E': 20},
    'D': {'B': 3, 'C': 7, 'E': 9, 'F': 5},
    'E': {'C': 20, 'D': 9, 'F': 8, 'G': 1},
    'F': {'B': 12, 'D': 5, 'E': 8, 'G': 7},
    'G': {'E': 1, 'F': 7}
}

# Ejecutar el algoritmo desde el nodo inicial A
start_node = 'A'
distances, previous_nodes, process = dijkstra(graph, start_node)

# Mostrar el proceso paso a paso
print("PROCESO DEL ALGORITMO DE DIJKSTRA:")
for step in process:
    print(f"\nIteración {step['Iteración']}:")
    print(f"Nodo actual: {step['Nodo actual']} (distancia = {step['Distancia actual']})")
    print(f"Nodos visitados antes: {', '.join(step['Nodos visitados'])}")
    
    # Mostrar distancias después de actualizar
    dist_after = []
    for node in graph:
        value = step['Distancias después'][node]
        dist_after.append(f"{node}: {value if value != float('infinity') else '∞'}")
    print("Distancias después: " + ", ".join(dist_after))
    
    print(f"Nodos visitados después: {', '.join(step['Nodos visitados después'])}")

# Preparar los resultados para mostrarlos en forma de tabla
print("\nRESULTADOS DEL ALGORITMO DE DIJKSTRA:")
headers = ['Origen', 'Destino', 'Distancia', 'Ruta']
rows = []

for node in graph:
    if node != start_node:
        path = get_path(previous_nodes, start_node, node)
        path_str = ' → '.join(path) if path else "No hay camino"
        rows.append([start_node, node, distances[node], path_str])

# Imprimir la tabla de resultados
print_table(headers, rows)

# También mostrar las distancias en formato de matriz
print("\nMatriz de distancias desde el nodo", start_node)
dist_headers = [''] + list(graph.keys())
dist_row = [start_node]
for node in graph:
    dist = distances[node]
    dist_row.append(dist if dist != float('infinity') else '∞')

print_table(dist_headers, [dist_row])