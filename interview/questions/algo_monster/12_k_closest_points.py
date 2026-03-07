import heapq


# Priority Queues
# repeatedly extract the largest/smallest elements
def k_closest_points(points: list[list[int]], k: int) -> list[list[int]]:
    heap = []
    for x, y in points:
        heapq.heappush(heap, (x**2 + y**2, [x, y]))

    result = []
    for _ in range(k):
        result.append(heapq.heappop(heap)[1])

    return result


def main():
    points = [[3, 3], [5, -1], [-2, 4], [0, 6]]
    k = 2
    result = k_closest_points(points, k)
    print(result)


if __name__ == "__main__":
    main()
