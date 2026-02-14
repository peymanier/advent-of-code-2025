def power_set(nums: list[int]) -> list[list[int]]:
    if not nums:
        return [[]]

    subsets = []
    first = nums[0]
    remaining = nums[1:]
    remaining_subsets = power_set(remaining)
    for subset in remaining_subsets:
        subsets.append([first, *subset])
        subsets.append(subset)

    return subsets


def main():
    nums = [1, 2, 3]
    result = power_set(nums)
    print(result)


if __name__ == "__main__":
    main()
