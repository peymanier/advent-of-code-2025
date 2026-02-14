def two_sum(nums: list[int], target: int) -> tuple[int, int]:
    nums_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in nums_to_index:
            return nums_to_index[complement], i

        nums_to_index[num] = i

    return -1, -1


def main():
    nums = [2, 7, 11, 15]
    target = 9

    result = two_sum(nums, target)
    print(result)


if __name__ == "__main__":
    main()
