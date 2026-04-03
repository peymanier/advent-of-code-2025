def plus_one(nums: list[int]) -> list[int]:
    i = len(nums) - 1
    nums[i] += 1
    while nums[i] > 9:
        nums[i] = nums[i] % 10
        if i - 1 >= 0:
            nums[i - 1] += 1
        else:
            nums.insert(0, 1)
        i -= 1

    return nums


def main():
    nums = [1, 2, 3]
    result = plus_one(nums)
    val = [1, 2, 4]
    print("passed:", result == val, "expected", val, "got", result)

    nums = [4, 3, 2, 1]
    result = plus_one(nums)
    val = [4, 3, 2, 2]
    print("passed:", result == val, "expected", val, "got", result)

    nums = [9, 9, 9]
    result = plus_one(nums)
    val = [1, 0, 0, 0]
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
