def search_insert_position(nums: list[int], target: int) -> int:
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

    return left


def main():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    result = search_insert_position(nums, target)
    print(result)

    nums = [-1, 0, 3, 5, 9, 12]
    target = 8
    result = search_insert_position(nums, target)
    print(result)

    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    result = search_insert_position(nums, target)
    print(result)

    nums = [1, 3, 5, 6]
    target = 2
    result = search_insert_position(nums, target)
    print(result)

    nums = [1]
    target = 2
    result = search_insert_position(nums, target)
    print(result)

    nums = [1]
    target = 0
    result = search_insert_position(nums, target)
    print(result)


if __name__ == "__main__":
    main()
