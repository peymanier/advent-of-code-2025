def quick_sort(nums: list[int]) -> None:
    def quick(low, high):
        if low >= high:
            return

        p = partition(nums, low, high)
        quick(low, p - 1)
        quick(p + 1, high)

    return quick(0, len(nums) - 1)


def partition(nums, low, high):
    pivot = nums[high]
    i = low

    for j in range(low, high):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

    nums[i], nums[high] = nums[high], nums[i]
    return i


def main():
    nums = [8, 2, 8, 1, 3, 9, 5]
    quick_sort(nums)
    print(nums)


if __name__ == "__main__":
    main()
