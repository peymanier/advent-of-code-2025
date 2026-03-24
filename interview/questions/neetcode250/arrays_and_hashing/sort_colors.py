def sort_colors(nums: list[int]) -> list[int]:
    buckets = [0 for _ in range(len(nums))]
    for n in nums:
        buckets[n] += 1

    k = 0
    for i in range(len(buckets)):
        for _ in range(buckets[i]):
            nums[k] = i
            k += 1

    return nums


def sort_colors2(nums: list[int]) -> list[int]:
    left = 0
    right = len(nums) - 1
    i = 0
    while i <= right:
        if nums[i] == 0:
            nums[left], nums[i] = nums[i], nums[left]
            left += 1

        elif nums[i] == 2:
            nums[right], nums[i] = nums[i], nums[right]
            right -= 1
            i -= 1

        i += 1

    return nums


def main():
    nums = [2, 0, 2, 1, 1, 0]
    result = sort_colors(nums)
    val = [0, 0, 1, 1, 2, 2]
    print("passed:", result == val, "expected", val, "got", result)

    nums = [2, 0, 1]
    result = sort_colors(nums)
    val = [0, 1, 2]
    print("passed:", result == val, "expected", val, "got", result)

    nums = [2, 0, 2, 1, 1, 0]
    result = sort_colors2(nums)
    val = [0, 0, 1, 1, 2, 2]
    print("passed:", result == val, "expected", val, "got", result)

    nums = [2, 0, 1]
    result = sort_colors2(nums)
    val = [0, 1, 2]
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
