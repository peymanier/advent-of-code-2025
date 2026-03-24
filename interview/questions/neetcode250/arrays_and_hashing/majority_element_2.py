def majority_element_two(nums: list[int]) -> list[int]:
    freq = {}
    for n in nums:
        freq[n] = 1 + freq.get(n, 0)

    result = []
    for num, f in freq.items():
        if f > len(nums) // 3:
            result.append(num)

    return result


def majority_element_two_alt(nums: list[int]) -> list[int]:
    freq = {}
    for n in nums:
        freq[n] = 1 + freq.get(n, 0)
        if len(freq) <= 2:
            continue

        keys_to_delete = []
        for num in freq:
            freq[num] -= 1
            if freq[num] == 0:
                keys_to_delete.append(num)

        for key in keys_to_delete:
            del freq[key]

    result = []
    for n in freq.keys():
        if nums.count(n) > len(nums) // 3:
            result.append(n)

    return result


def main():
    nums = [3, 2, 3]
    result = majority_element_two(nums)
    val = [3]
    print("passed:", result == val, "expected", val, "got", result)

    nums = [1]
    result = majority_element_two(nums)
    val = [1]
    print("passed:", result == val, "expected", val, "got", result)

    nums = [1, 2]
    result = majority_element_two(nums)
    val = [1, 2]
    print("passed:", result == val, "expected", val, "got", result)

    nums = [1, 2, 3, 1, 2]
    result = majority_element_two(nums)
    val = [1, 2]
    print("passed:", result == val, "expected", val, "got", result)

    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    result = majority_element_two(nums)
    val = []
    print("passed:", result == val, "expected", val, "got", result)

    nums = [1, 2, 1, 2, 3, 4, 5]
    result = majority_element_two(nums)
    val = []
    print("passed:", result == val, "expected", val, "got", result)

    nums = [3, 2, 3]
    result = majority_element_two_alt(nums)
    val = [3]
    print("passed:", result == val, "expected", val, "got", result)

    nums = [1]
    result = majority_element_two_alt(nums)
    val = [1]
    print("passed:", result == val, "expected", val, "got", result)

    nums = [1, 2]
    result = majority_element_two_alt(nums)
    val = [1, 2]
    print("passed:", result == val, "expected", val, "got", result)

    nums = [1, 2, 3, 1, 2]
    result = majority_element_two_alt(nums)
    val = [1, 2]
    print("passed:", result == val, "expected", val, "got", result)

    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    result = majority_element_two_alt(nums)
    val = []
    print("passed:", result == val, "expected", val, "got", result)

    nums = [1, 2, 1, 2, 3, 4, 5]
    result = majority_element_two_alt(nums)
    val = []
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
