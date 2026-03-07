import heapq


# Priority Queue
def kth_largest_element(nums: list[int], k: int) -> int:
    return heapq.nlargest(k, nums)[-1]


def kth_largest_element2(nums: list[int], k: int) -> int:
    heap = []
    for num in nums:
        heapq.heappush(heap, num * -1)

    for _ in range(k - 1):
        heapq.heappop(heap)

    return heapq.heappop(heap) * -1


def kth_largest_element3(nums: list[int], k: int) -> int:
    heap = [-n for n in nums]
    heapq.heapify(heap)

    for _ in range(k - 1):
        heapq.heappop(heap)

    # return heapq.heappop(heap) * -1
    return -heap[0]


def main():
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    # result = kth_largest_element(nums, k)
    # result = kth_largest_element2(nums, k)
    result = kth_largest_element3(nums, k)
    print(result)

    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    # result = kth_largest_element(nums, k)
    # result = kth_largest_element2(nums, k)
    result = kth_largest_element3(nums, k)
    print(result)


if __name__ == "__main__":
    main()
