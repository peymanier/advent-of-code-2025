def maximum_subarray(nums: list[int]) -> int:
    if not nums:
        return 0

    curr_sum = 0
    result = nums[0]
    for n in nums:
        curr_sum += n

        if n > curr_sum:
            curr_sum = n

        result = max(result, curr_sum)

    return result


def main():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = maximum_subarray(nums)
    val = 6
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
