def insertion_sort(nums: list[int]) -> list[int]:
    for i in range(1, len(nums)):
        j = i
        while j > 0 and nums[j - 1] > nums[j]:
            nums[j - 1], nums[j] = nums[j], nums[j - 1]
            j -= 1

    return nums


def insertion_sort2(nums: list[int]) -> list[int]:
    for i in range(1, len(nums)):
        for j in range(i, 0, -1):
            if nums[j - 1] > nums[j]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]

    return nums


def main():
    nums = [8, 2, 8, 1, 3, 9, 5]
    result = insertion_sort(nums)
    print(result)

    result = insertion_sort2(nums)
    print(result)


if __name__ == "__main__":
    main()
