def contains_duplicate(nums: list[int]) -> bool:
    visited = set()

    for num in nums:
        if num in visited:
            return True

        visited.add(num)

    return False


def contains_duplicate_alt(nums: list[int]) -> bool:
    sorted_nums = sorted(nums)

    for i in range(1, len(sorted_nums)):
        if sorted_nums[i - 1] == sorted_nums[i]:
            return True

    return False


def main():
    nums = [1, 2, 3, 1]
    result = contains_duplicate(nums)
    print(result)

    result = contains_duplicate_alt(nums)
    print(result)

    nums = [1, 2, 3, 4]
    result = contains_duplicate(nums)
    print(result)

    result = contains_duplicate_alt(nums)
    print(result)


if __name__ == "__main__":
    main()
