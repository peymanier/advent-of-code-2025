def product_of_array_except_self(nums: list[int]) -> list[int]:
    left = [None for _ in range(len(nums))]
    product = 1
    for i in range(len(nums)):
        product *= nums[i]
        left[i] = product

    right = [None for _ in range(len(nums))]
    product = 1
    for j in range(len(nums) - 1, -1, -1):
        product *= nums[j]
        right[j] = product

    result = [None for _ in range(len(nums))]
    for i in range(len(nums)):
        if i - 1 >= 0:
            l = left[i - 1]
        else:
            l = 1

        try:
            r = right[i + 1]
        except IndexError:
            r = 1

        result[i] = l * r

    return result


def main():
    nums = [1, 2, 3, 4]
    result = product_of_array_except_self(nums)
    val = [24, 12, 8, 6]
    print("passed:", result == val, "expected", val, "got", result)

    nums = [-1, 1, 0, -3, 3]
    result = product_of_array_except_self(nums)
    val = [0, 0, 9, 0, 0]
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
