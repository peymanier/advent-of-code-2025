def remove_duplicates_from_sorted_array(nums: list[int]) -> int:
    if len(nums) <= 1:
        return len(nums)

    k = 1
    for i in range(1, len(nums)):
        if nums[i - 1] != nums[i]:
            nums[k] = nums[i]
            k += 1

    return k


def main():
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    result = remove_duplicates_from_sorted_array(nums)
    val = 5
    print("passed:", result == val, "expected", val, "got", result)
    result = nums[:result]
    val = [0, 1, 2, 3, 4]
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
