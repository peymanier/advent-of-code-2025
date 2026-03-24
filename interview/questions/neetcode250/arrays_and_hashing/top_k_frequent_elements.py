import heapq

# def top_k_frequent_elements(nums: list[int], k: int) -> list[int]:
#     counter = {}
#     for n in nums:
#         counter[n] = 1 + counter.get(n, 0)
#
#     heap = []
#     for num, freq in counter.items():
#         heapq.heappush(heap, (-1 * freq, num))
#
#     result = []
#     for _ in range(k):
#         result.append(heapq.heappop(heap)[1])
#
#     return result


def top_k_frequent_elements(nums: list[int], k: int) -> list[int]:
    counter_map = {}
    for n in nums:
        counter_map[n] = 1 + counter_map.get(n, 0)

    counter_list = [None for _ in range(len(nums) + 1)]
    for num, freq in counter_map.items():
        if counter_list[freq] is None:
            counter_list[freq] = []

        counter_list[freq].append(num)

    count = 0
    result = []
    for frequent_numbers in counter_list[::-1]:
        if frequent_numbers is None:
            continue

        for n in frequent_numbers:
            count += 1
            result.append(n)
            if count == k:
                return result

    return None


def main():
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    result = top_k_frequent_elements(nums, k)
    val = [1, 2]
    print("passed:", result == val, "expected", val, "got", result)

    nums = [1]
    k = 1
    result = top_k_frequent_elements(nums, k)
    val = [1]
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
