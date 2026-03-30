def longest_turbulent_subarray(nums: list[int]) -> int:
    l, r = 0, 1
    result = 0
    prev = ""
    while r < len(nums):
        if nums[r - 1] < nums[r] and prev != "<":
            result = max(result, r - l + 1)
            r += 1
            prev = "<"
        elif nums[r - 1] > nums[r] and prev != ">":
            result = max(result, r - l + 1)
            r += 1
            prev = ">"
        else:
            r = r + 1 if nums[r - 1] == nums[r] else r
            l = r - 1
            prev = ""

    return result


def main():
    nums = [9, 4, 2, 10, 7, 8, 8, 1, 9]
    result = longest_turbulent_subarray(nums)
    val = 5
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
