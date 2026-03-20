from functools import cache

# def rob_houses(nums: list[int]) -> int:
#     if not nums:
#         return 0
#
#     return max(nums[0] + rob_houses(nums[2:]), rob_houses(nums[1:]))


def rob_houses(nums: list[int]) -> int:
    @cache
    def rob(house: int):
        if house >= len(nums):
            return 0

        return max(nums[house] + rob(house + 2), rob(house + 1))

    return rob(0)


def main():
    nums = [1, 2, 3, 1]
    result = rob_houses(nums)
    val = 4
    print("passed:", result == val, "expected", val, "got", result)

    nums = [1, 2, 3, 1, 1, 5, 6] * 20
    result = rob_houses(nums)
    val = 201
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
