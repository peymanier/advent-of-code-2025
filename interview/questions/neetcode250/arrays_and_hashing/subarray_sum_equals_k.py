# def subarray_sum_equals_k(nums: list[int], k: int) -> int:
#     def subarray(index: int, s: int):
#         if s == k:
#             return 1
#
#         if index >= len(nums):
#             return 0
#
#         return subarray(index + 1, s + nums[index])
#
#     choices = []
#     for i in range(len(nums)):
#         choices.append(subarray(i, 0))
#
#     return sum(choices)


# def subarray_sum_equals_k(nums: list[int], k: int) -> int:
#     result = 0
#     for i in range(len(nums)):
#         curr_sum = 0
#         for j in range(i, len(nums)):
#             curr_sum += nums[j]
#             if curr_sum == k:
#                 result += 1
#                 break
#
#     return result


def subarray_sum_equals_k(nums: list[int], k: int) -> int:
    prefix_sum_count = {0: 1}
    result = 0
    curr_sum = 0
    for n in nums:
        curr_sum += n
        diff = curr_sum - k
        result += prefix_sum_count.get(diff, 0)

        prefix_sum_count[curr_sum] = 1 + prefix_sum_count.get(curr_sum, 0)

    return result


def main():
    nums = [1, 1, 1]
    k = 2
    result = subarray_sum_equals_k(nums, k)
    val = 2
    print("passed:", result == val, "expected", val, "got", result)

    nums = [1, 2, 3]
    k = 3
    result = subarray_sum_equals_k(nums, k)
    val = 2
    print("passed:", result == val, "expected", val, "got", result)

    nums = [1, -1, 1, 1, 1, 1]
    k = 3
    result = subarray_sum_equals_k(nums, k)
    val = 4
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
