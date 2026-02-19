import heapq
import itertools
import math


def main():
    with open("puzzle.txt", "r") as f:
        puzzle = [line.strip() for line in f.readlines()]

    points = []
    for line in puzzle:
        x, y, z = [int(i) for i in line.split(",")]
        points.append((x, y, z))

    distances = []
    for p1, p2 in itertools.combinations(points, 2):
        distance = math.dist(p1, p2)
        distances.append((distance, (p1, p2)))

    distances.sort()

    connections = 1000
    graph = {}
    for _, (p1, p2) in distances[:connections]:
        graph.setdefault(p1, set()).add(p2)
        graph.setdefault(p2, set()).add(p1)

    for p in points:
        graph.setdefault(p, set())

    visited = set()
    circuits = []
    for node in graph:
        if node in visited:
            continue

        stack = [node]
        current_circuit = []

        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                current_circuit.append(current)
                stack.extend(graph[current] - visited)

        circuits.append(current_circuit)

    circuits = [(len(c), circuits) for c in circuits]

    heapq.heapify(circuits)
    largest = heapq.nlargest(3, circuits)

    print(math.prod([l[0] for l in largest]))


if __name__ == "__main__":
    main()
