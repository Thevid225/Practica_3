class UnionFind:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return False

        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1

        return True


def kruskal_max_cost(graph):
    edges = []
    for u in graph:
        for v, weight in graph[u].items():
            edges.append((u, v, weight))

    edges.sort(key=lambda x: x[2], reverse=True)

    vertices = set(graph.keys())
    uf = UnionFind(vertices)
    max_cost_tree = []

    for u, v, weight in edges:
        if uf.union(u, v):
            max_cost_tree.append((u, v, weight))

    return max_cost_tree


def kruskal_min_cost(graph):
    edges = []
    for u in graph:
        for v, weight in graph[u].items():
            edges.append((u, v, weight))

    edges.sort(key=lambda x: x[2])

    vertices = set(graph.keys())
    uf = UnionFind(vertices)
    min_cost_tree = []

    for u, v, weight in edges:
        if uf.union(u, v):
            min_cost_tree.append((u, v, weight))

    return min_cost_tree


# Función para mostrar el árbol resultante
def print_tree(tree):
    for edge in tree:
        print(edge[0], "-", edge[1], ":", edge[2])


# Ejemplo de uso
graph = {
    'A': {'B': 2, 'D': 5},
    'B': {'A': 2, 'C': 3, 'D': 3, 'E': 4},
    'C': {'B': 3, 'E': 1},
    'D': {'A': 5, 'B': 3, 'E': 6},
    'E': {'B': 4, 'C': 1, 'D': 6}
}

print("Árbol de Máximo Costo (Kruskal):")
max_cost_tree = kruskal_max_cost(graph)
print_tree(max_cost_tree)

print("\nÁrbol de Mínimo Costo (Kruskal):")
min_cost_tree = kruskal_min_cost(graph)
print_tree(min_cost_tree)
