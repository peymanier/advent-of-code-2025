# def majority_element(nums: list[int]) -> int | None:
#     freq = {}
#     for n in nums:
#         freq[n] = 1 + freq.get(n, 0)
#         if freq[n] > len(nums) // 2:
#             return n
#
#     return None


def majority_element(nums: list[int]) -> int | None:
    count = 0
    result = None
    for n in nums:
        if count == 0:
            result = n

        if n == result:
            count += 1
        else:
            count -= 1

    return result


def main():
    nums = [3, 2, 3]
    result = majority_element(nums)
    val = 3
    print("passed:", result == val, "expected", val, "got", result)

    nums = [2, 2, 1, 1, 1, 2, 2]
    result = majority_element(nums)
    val = 2
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
