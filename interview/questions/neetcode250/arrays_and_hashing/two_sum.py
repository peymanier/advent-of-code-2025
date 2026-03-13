def two_sum(nums, target) -> tuple[int, int] | None:
    nums_map = {}
    for i in range(len(nums)):
        nums_map[nums[i]] = i

        complement = target - nums[i]
        if complement in nums_map:
            return nums_map[complement], i

    return None


def main():
    nums = [7, 11, 2, 15]
    target = 9
    result = two_sum(nums, target)
    print("expected", (0, 2), "got", result)

    nums = [7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print("expected", None, "got", result)


if __name__ == "__main__":
    main()
