def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    window = set()
    left = 0
    for right in range(len(nums)):
        if right - left > k:
            window.remove(nums[left])
            left += 1

        if nums[right] in window:
            return True

        window.add(nums[right])

    return False


def main():
    nums = [1, 2, 3, 1, 2, 3]
    k = 2
    result = contains_nearby_duplicate(nums, k)
    print(result)

    nums = [1, 2, 3, 1]
    k = 3
    result = contains_nearby_duplicate(nums, k)
    print(result)

    nums = [1, 0, 1, 1]
    k = 1
    result = contains_nearby_duplicate(nums, k)
    print(result)


if __name__ == "__main__":
    main()
