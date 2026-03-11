import heapq


def kth_largest_element(array: list[int], k: int) -> int:
    heap = []
    for num in array:
        heapq.heappush(heap, -1 * num)

    for _ in range(k - 1):
        heapq.heappop(heap)

    return -1 * heap[0]


def main():
    array = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    result = kth_largest_element(array, k)
    print("expected", 4, "got", result)


if __name__ == "__main__":
    main()
