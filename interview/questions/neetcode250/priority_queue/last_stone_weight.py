import heapq


def smash_stones(stones: list[int]) -> int:
    stones_heap = []
    for stone in stones:
        heapq.heappush(stones_heap, -1 * stone)

    while len(stones_heap) > 1:
        first = heapq.heappop(stones_heap)
        second = heapq.heappop(stones_heap)

        if first == second:
            continue

        heapq.heappush(stones_heap, -1 * ((-1 * first) - (-1 * second)))

    stones_heap.append(0)
    return -1 * stones_heap[0]


def main():
    stones = [2, 7, 4, 1, 8, 1]
    result = smash_stones(stones)
    print("expected", 1, "got", result)


if __name__ == "__main__":
    main()
