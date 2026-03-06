from collections import deque


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

    def bfs(self, v):
        visited = []

        q = deque([v])
        while q:
            vertex = q.popleft()
            if vertex in visited:
                continue

            visited.append(vertex)

            # python sets are stable only for integers, we use sorted to make the output deterministic
            for vx in sorted(self.graph[vertex]):
                q.append(vx)

        return visited


def main():
    graph = GraphAdjList()
    graph.add_edge("new york", "london")
    graph.add_edge("new york", "cairo")
    graph.add_edge("new york", "tokyo")
    graph.add_edge("london", "dubai")

    result = graph.bfs("new york")
    print(result)


if __name__ == "__main__":
    main()
