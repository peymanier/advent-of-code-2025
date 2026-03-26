def minimum_size_subarray_sum(nums: list[int], target: int) -> int:
    l = 0
    result = float("inf")
    total = 0
    for r in range(len(nums)):
        total += nums[r]
        while total >= target:
            result = min(result, r - l + 1)
            total -= nums[l]
            l += 1

    return result if result != float("inf") else 0


def main():
    nums = [2, 3, 1, 2, 4, 3]
    target = 7
    result = minimum_size_subarray_sum(nums, target)
    val = 2
    print("passed:", result == val, "expected", val, "got", result)

    nums = [1, 4, 4]
    target = 4
    result = minimum_size_subarray_sum(nums, target)
    val = 1
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
