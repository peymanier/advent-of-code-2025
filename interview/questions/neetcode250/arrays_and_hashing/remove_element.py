# def remove_element(nums: list[int], val: int) -> int:
#     k = None
#     for i in range(len(nums)):
#         if nums[i] == val and not k:
#             k = i
#             continue
#
#         if nums[i] != val and k:
#             nums[k] = nums[i]
#             k += 1
#
#     return k


def remove_element(nums: list[int], val: int) -> int:
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1

    return k


def main():
    nums = [0, 1, 2, 2, 3, 0, 4, 2, 5, 6]
    result = remove_element(nums, 2)
    val = 7
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
