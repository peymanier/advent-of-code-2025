import heapq


class KthLargest:
    def __init__(self, k, elements):
        self.k = k
        self.heap = []
        for elem in elements:
            heapq.heappush(self.heap, elem)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        return heapq.nlargest(self.k, self.heap)[-1]


class KthLargestAlt:
    def __init__(self, k, elements):
        self.k = k
        self.heap = []

        for elem in elements:
            self._append(elem)

    def _append(self, val: int) -> None:
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        self._append(val)
        return self.heap[0]


def main():
    # kth_largest = KthLargest(3, [4, 5, 8, 2])
    kth_largest = KthLargestAlt(3, [4, 5, 8, 2])

    result = kth_largest.add(3)
    print("expected", 4, "got", result)

    result = kth_largest.add(5)
    print("expected", 5, "got", result)

    result = kth_largest.add(10)
    print("expected", 5, "got", result)

    result = kth_largest.add(9)
    print("expected", 8, "got", result)

    result = kth_largest.add(4)
    print("expected", 8, "got", result)


if __name__ == "__main__":
    main()
