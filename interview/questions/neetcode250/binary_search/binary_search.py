def binary_search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        if target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def main():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    result = binary_search(nums, target)
    print(result)

    nums = [-1, 0, 3, 5, 9, 12]
    target = 12
    result = binary_search(nums, target)
    print(result)

    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    result = binary_search(nums, target)
    print(result)


if __name__ == "__main__":
    main()
