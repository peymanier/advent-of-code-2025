# def three_sum(nums: list[int]) -> list[list[int]]:
#     nums.sort()
#     result = []
#     for i in range(len(nums)):
#         prev = nums[i - 1] if i - 1 >= 0 else None
#         curr = nums[i]
#         if prev == curr:
#             continue
#
#         target = -curr
#         visited = set()
#         for j in range(i + 1, len(nums)):
#             diff = target - nums[j]
#             if diff in visited:
#                 result.append([nums[i], diff, nums[j]])
#
#             visited.add(nums[j])
#
#     return result


def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result = []
    for i in range(len(nums)):
        if i > 0 and nums[i - 1] == nums[i]:
            continue

        target = nums[i] * -1
        l = i + 1
        r = len(nums) - 1
        while l < r:
            if nums[l] + nums[r] > target:
                r -= 1
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                result.append([nums[i], nums[l], nums[r]])
                l += 1
                while nums[l - 1] == nums[l] and l < r:
                    l += 1

    return result


def deep_diff(l1: list[list], l2: list[list]):
    result1 = []
    for sublist in l1:
        result1.append(sorted(sublist))

    result2 = []
    for sublist in l2:
        result2.append(sorted(sublist))

    return sorted(result1) == sorted(result2)


def main():
    nums = [-3, 3, 4, -3, 1, 2]
    result = three_sum(nums)
    val = [[-3, 1, 2]]
    print("passed:", deep_diff(result, val), "expected", val, "got", result)

    nums = [-1, 0, 1, 2, -1, -4]
    result = three_sum(nums)
    val = [[-1, 0, 1], [-1, -1, 2]]
    print("passed:", deep_diff(result, val), "expected", val, "got", result)


if __name__ == "__main__":
    main()
