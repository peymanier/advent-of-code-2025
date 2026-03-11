import heapq


def k_closest_points_to_origin(points: list[list[int]], k: int) -> list[list[int]]:
    distance_heap = []
    for point in points:
        heapq.heappush(distance_heap, (point[0] ** 2 + point[1] ** 2, point))

    result = []
    for _ in range(k):
        result.append(heapq.heappop(distance_heap)[1])

    return result


def main():
    points = [[1, 3], [-2, 2]]
    k = 1
    result = k_closest_points_to_origin(points, k)
    print("expected", [[-2, 2]], "got", result)


if __name__ == "__main__":
    main()
