class GraphMatrix:
    def __init__(self, num_vertices):
        self.graph = [[False for _ in range(num_vertices)] for _ in range(num_vertices)]

    def add_edge(self, u, v):
        if not (0 < u < len(self.graph)) or not (0 < v < len(self.graph)):
            raise ValueError("out of bounds")

        self.graph[u][v] = True
        self.graph[v][u] = True


class GraphAdjList:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = set()

        if v not in self.graph:
            self.graph[v] = set()

        self.graph[u].add(v)
        self.graph[v].add(u)
