# def two_sum_sorted(nums: list[int], target: int) -> list[int]:
#     if len(nums) < 2:
#         return []
#
#     l = 0
#     end = len(nums) - 1
#     while l < len(nums):
#         r = l + 1
#         while l < r <= end:
#             if nums[l] + nums[r] == target:
#                 return [l + 1, r + 1]
#
#             if nums[l] + nums[r] > target:
#                 end -= end - r + 1
#
#             r += 1
#
#         l += 1
#
#     return []


def two_sum_sorted(nums: list[int], target: int) -> list[int]:
    if len(nums) < 2:
        return []

    l = 0
    r = len(nums) - 1
    while l < r:
        if nums[l] + nums[r] < target:
            l += 1
        elif nums[l] + nums[r] > target:
            r -= 1
        else:
            break

    return [l + 1, r + 1]


def main():
    nums = [1, 2, 3, 4, 7, 11, 15]
    target = 9
    result = two_sum_sorted(nums, target)
    val = [2, 5]
    print("passed:", result == val, "expected", val, "got", result)

    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum_sorted(nums, target)
    val = [1, 2]
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
