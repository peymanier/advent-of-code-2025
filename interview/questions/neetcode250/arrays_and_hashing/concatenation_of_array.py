# def concat_of_array(nums: list[int]) -> list[int]:
#     return nums + nums


# def concat_of_array(nums: list[int]) -> list[int]:
#     nums.extend(nums)
#     return nums


# def concat_of_array(nums: list[int]) -> list[int]:
#     result = []
#     for i in range(2):
#         for num in nums:
#             result.append(num)
#
#     return result


def concat_of_array(nums: list[int]) -> list[int]:
    for i in range(len(nums)):
        nums.append(nums[i])

    return nums


def main():
    nums = [1, 2, 1]
    result = concat_of_array(nums)
    print("expected", [1, 2, 1, 1, 2, 1], "got", result)


if __name__ == "__main__":
    main()
