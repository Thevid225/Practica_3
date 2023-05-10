import sys

def dijkstra(graph, start):
    # Inicializar distancias con infinito para todos los nodos, excepto el inicio
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Mantener un seguimiento de los nodos visitados
    visited = set()

    while visited != set(graph):
        # Encontrar el nodo con la distancia mínima no visitado
        min_node = None
        for node in graph:
            if node not in visited and (min_node is None or distances[node] < distances[min_node]):
                min_node = node

        # Marcar el nodo mínimo como visitado
        visited.add(min_node)

        # Actualizar las distancias de los nodos vecinos no visitados
        for neighbor, distance in graph[min_node].items():
            if neighbor not in visited:
                new_distance = distances[min_node] + distance
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

    return distances


# Ejemplo de uso
graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'A': 2, 'C': 1, 'D': 7},
    'C': {'A': 4, 'B': 1, 'D': 3},
    'D': {'B': 7, 'C': 3}
}

start_node = 'A'
distances = dijkstra(graph, start_node)

print("Distancias mínimas desde el nodo de inicio (" + start_node + "):")
for node, distance in distances.items():
    print("Nodo:", node, "- Distancia:", distance)
