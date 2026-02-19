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

    def is_connected():
        node = next(iter(graph))
        stack = [node]
        visited = set()
        while stack:
            current = stack.pop()
            if current in visited:
                continue

            visited.add(current)
            stack.extend(graph[current] - visited)

        return len(visited) == len(points)

    result = None
    graph = {p: set() for p in points}
    for _, (p1, p2) in distances:
        graph[p1].add(p2)
        graph[p2].add(p1)

        if is_connected():
            result = (p1, p2)
            break

    print(result[0][0] * result[1][0])


if __name__ == "__main__":
    main()
