def max_subarray_of_length(nums: list[int], k: int) -> int:
    window = nums[0:k]
    result = sum(window)
    for right in range(k + 1, len(nums)):
        left = right - k
        window = nums[left:right]
        result = max(result, sum(window))

    return result


def max_subarray_of_length2(nums: list[int], k: int) -> int:
    window = nums[0:k]
    window_sum = sum(window)

    result = window_sum
    for right in range(k, len(nums)):
        left = right - k
        window_sum -= nums[left]
        window_sum += nums[right]
        result = max(result, window_sum)

    return result


def main():
    nums = [1, 2, 3, 7, 4, 1]
    k = 3

    # result = max_subarray_of_length(nums, k)
    # print(result)

    result = max_subarray_of_length2(nums, k)
    print(result)


if __name__ == "__main__":
    main()
