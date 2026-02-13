def max_subarray_of_length(nums: list[int], k: int) -> int:
    window = nums[0:k]
    result = sum(window)
    for right in range(k, len(nums)):
        left = right - k
        window = nums[left:right]
        result = max(result, sum(window))

    return result


def main():
    nums = [1, 2, 3, 7, 4, 1]
    k = 3
    result = max_subarray_of_length(nums, k)
    print(result)


if __name__ == "__main__":
    main()
