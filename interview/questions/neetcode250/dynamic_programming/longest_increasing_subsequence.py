def longest_increasing_subsequence(nums: list[int]) -> int:
    def longest(index: int, count: int):
        candidates = []
        for i in range(index + 1, len(nums)):
            if nums[i] > nums[index]:
                candidates.append(longest(i, count + 1))

        if not candidates:
            return count

        return max(candidates)

    choices = []
    for j in range(len(nums)):
        choices.append(longest(j, 1))

    return max(choices)


def cache_longest_increasing_subsequence(func):
    cache = {}

    def wrapper(index, count):
        if index in cache:
            return cache[index] + count

        result = func(index, count)

        cache[index] = result - count
        return result

    return wrapper


def longest_increasing_subsequence_with_cache(nums: list[int]) -> int:
    @cache_longest_increasing_subsequence
    def longest(index: int, count: int):
        candidates = []
        for i in range(index + 1, len(nums)):
            if nums[i] > nums[index]:
                candidates.append(longest(i, count + 1))

        if not candidates:
            return count

        return max(candidates)

    choices = []
    for j in range(len(nums)):
        choices.append(longest(j, 1))

    return max(choices)


def main():
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    result = longest_increasing_subsequence(nums)
    val = 4
    print("passed:", result == val, "expected", val, "got", result)

    nums = [20, 1, 2, 1, 2, 5, 1]
    result = longest_increasing_subsequence(nums)
    val = 3
    print("passed:", result == val, "expected", val, "got", result)

    import time

    nums = [20, 1, 2, 1, 2, 5, 1] * 50
    start = time.perf_counter()
    result = longest_increasing_subsequence(nums)
    end = time.perf_counter()
    print("duration", f"{end - start:.4f} seconds")
    val = 4
    print("passed:", result == val, "expected", val, "got", result)

    nums = [20, 1, 2, 1, 2, 5, 1] * 50
    start = time.perf_counter()
    result = longest_increasing_subsequence_with_cache(nums)
    end = time.perf_counter()
    print("duration", f"{end - start:.4f} seconds")
    val = 4
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
