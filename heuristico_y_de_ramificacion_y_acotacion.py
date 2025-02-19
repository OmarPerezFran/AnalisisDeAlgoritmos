from collections import namedtuple
import math

# Definición de la estructura de datos para los items
Item = namedtuple('Item', ['valor', 'peso', 'indice'])

class Nodo:
    def __init__(self, nivel, valor_utilizado, peso_utilizado, limite):
        self.nivel = nivel
        self.valor_utilizado = valor_utilizado
        self.peso_utilizado = peso_utilizado
        self.limite = limite

def calcular_limite(nodo, capacidad, items, n):
    """
    PROCESO 1: CÁLCULO DE LÍMITES
    Calcula el límite superior para un nodo dado usando aproximación fraccional.
    """
    print("\n--- PROCESO 1: Calculando límite superior ---")
    if nodo.peso_utilizado >= capacidad:
        print(f"Peso utilizado ({nodo.peso_utilizado}) excede capacidad ({capacidad})")
        return 0
    
    limite_valor = nodo.valor_utilizado
    limite_peso = nodo.peso_utilizado
    nivel = nodo.nivel
    
    print(f"Inicio: Valor={limite_valor}, Peso={limite_peso}, Nivel={nivel}")
    
    # Agregar items completos mientras quede espacio
    while nivel < n and limite_peso + items[nivel].peso <= capacidad:
        limite_peso += items[nivel].peso
        limite_valor += items[nivel].valor
        print(f"Agregando item completo: +{items[nivel].valor} valor, +{items[nivel].peso} peso")
        nivel += 1
    
    # Agregar fracción del siguiente item si es posible
    if nivel < n:
        peso_restante = capacidad - limite_peso
        fraccion = peso_restante / items[nivel].peso
        valor_adicional = items[nivel].valor * fraccion
        limite_valor += valor_adicional
        print(f"Agregando fracción de item: +{valor_adicional:.2f} valor")
    
    print(f"Límite superior calculado: {limite_valor:.2f}")
    return limite_valor

def ordenar_items(items):
    """
    PROCESO 2: ORDENAMIENTO
    Ordena los items por ratio valor/peso de forma descendente.
    """
    print("\n--- PROCESO 2: Ordenando items por valor/peso ---")
    for item in items:
        ratio = item.valor / item.peso
        print(f"Item {item.indice}: Valor={item.valor}, Peso={item.peso}, Ratio={ratio:.2f}")
    
    items_ordenados = sorted(items, key=lambda x: x.valor/x.peso, reverse=True)
    print("\nOrden final:")
    for item in items_ordenados:
        print(f"Item {item.indice}: Ratio={item.valor/item.peso:.2f}")
    return items_ordenados

def ramificar(nodo_actual, items, nivel_siguiente, capacidad, mejor_valor, n):
    """
    PROCESO 3: RAMIFICACIÓN
    Crea los nodos hijos (incluir/excluir item) para el nodo actual.
    """
    print(f"\n--- PROCESO 3: Ramificando nodo nivel {nodo_actual.nivel} ---")
    nodos_hijos = []
    
    # Intentar incluir el siguiente item
    if nivel_siguiente < n:
        peso_nuevo = nodo_actual.peso_utilizado + items[nivel_siguiente].peso
        if peso_nuevo <= capacidad:
            nodo_incluir = Nodo(
                nivel_siguiente + 1,
                nodo_actual.valor_utilizado + items[nivel_siguiente].valor,
                peso_nuevo,
                0
            )
            print(f"Creando nodo incluyendo item {items[nivel_siguiente].indice}")
            nodo_incluir.limite = calcular_limite(nodo_incluir, capacidad, items, n)
            if nodo_incluir.limite > mejor_valor:
                nodos_hijos.append(nodo_incluir)
                print("Nodo incluido aceptado")
            else:
                print("Nodo incluido podado por límite inferior")
    
    # Crear nodo excluyendo el siguiente item
    nodo_excluir = Nodo(
        nivel_siguiente + 1,
        nodo_actual.valor_utilizado,
        nodo_actual.peso_utilizado,
        0
    )
    print(f"Creando nodo excluyendo item {items[nivel_siguiente].indice}")
    nodo_excluir.limite = calcular_limite(nodo_excluir, capacidad, items, n)
    if nodo_excluir.limite > mejor_valor:
        nodos_hijos.append(nodo_excluir)
        print("Nodo excluido aceptado")
    else:
        print("Nodo excluido podado por límite inferior")
    
    return nodos_hijos

def mochila_ramificacion_acotacion(capacidad, items):
    """
    PROCESO 4: EXPLORACIÓN Y PODA
    Proceso principal que combina todos los procesos anteriores.
    """
    print("\n=== INICIO DEL ALGORITMO ===")
    n = len(items)
    print(f"Número de items: {n}, Capacidad de la mochila: {capacidad}")
    
    # Proceso 2: Ordenamiento
    items = ordenar_items(items)
    
    mejor_valor = 0
    cola = []
    
    # Crear nodo raíz
    raiz = Nodo(0, 0, 0, 0)
    raiz.limite = calcular_limite(raiz, capacidad, items, n)
    cola.append(raiz)
    
    print("\n--- PROCESO 4: Iniciando exploración y poda ---")
    while cola:
        nodo_actual = cola.pop(0)
        print(f"\nExplorando nodo nivel {nodo_actual.nivel}: " +
              f"Valor={nodo_actual.valor_utilizado}, " +
              f"Peso={nodo_actual.peso_utilizado}, " +
              f"Límite={nodo_actual.limite}")
        
        if nodo_actual.limite < mejor_valor:
            print("Podando rama por límite inferior")
            continue
        
        if nodo_actual.nivel == n:
            if nodo_actual.valor_utilizado > mejor_valor:
                mejor_valor = nodo_actual.valor_utilizado
                print(f"Nuevo mejor valor encontrado: {mejor_valor}")
            continue
        
        # Proceso 3: Ramificación
        nivel_siguiente = nodo_actual.nivel
        nodos_hijos = ramificar(nodo_actual, items, nivel_siguiente, capacidad, mejor_valor, n)
        cola.extend(nodos_hijos)
    
    print(f"\n=== FIN DEL ALGORITMO ===")
    print(f"Mejor valor encontrado: {mejor_valor}")
    return mejor_valor

# Ejemplo de uso
if __name__ == "__main__":
    items = [
        Item(60, 10, 0),   # valor=60, peso=10
        Item(100, 20, 1),  # valor=100, peso=20
        Item(120, 30, 2)   # valor=120, peso=30
    ]
    capacidad = 50
    resultado = mochila_ramificacion_acotacion(capacidad, items)