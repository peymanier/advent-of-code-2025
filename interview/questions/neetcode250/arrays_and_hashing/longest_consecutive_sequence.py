def longest_consecutive_sequence(nums: list[int]) -> list[int]:
    sorted_nums = sorted(nums)
    left = 0
    result = []
    for right in range(1, len(sorted_nums)):
        if sorted_nums[right] - sorted_nums[right - 1] == 1:
            if (right - left + 1) > len(result):
                result = sorted_nums[left : right + 1]
        else:
            left = right

    return result


def main():
    nums = [100, 4, 200, 1, 3, 2]
    result = longest_consecutive_sequence(nums)
    val = [1, 2, 3, 4]
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
