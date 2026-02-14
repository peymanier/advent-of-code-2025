def bubble_sort(nums: list[int]) -> list[int]:
    for k in range(len(nums)):
        for i in range(1, len(nums) - k):
            prev, curr = nums[i - 1], nums[i]
            if prev > curr:
                nums[i - 1], nums[i] = curr, prev

    return nums


def bubble_sort2(nums: list[int]) -> list[int]:
    swapping = True
    end = len(nums)
    while swapping:
        swapping = False
        for i in range(1, end):
            if nums[i - 1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                swapping = True

        end -= 1

    return nums


def main():
    nums = [8, 2, 8, 1, 3, 9, 5]
    # result = bubble_sort(nums)
    result = bubble_sort2(nums)
    print(result)


if __name__ == "__main__":
    main()
