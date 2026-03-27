def sum_of_all_subsets_xor_totals(nums: list[int]) -> int:
    subsets = []

    def find_subsets(subset, i):
        if i == len(nums):
            subsets.append(subset)
            return

        include = [nums[i], *subset]
        not_include = [*subset]

        find_subsets(include, i + 1)
        find_subsets(not_include, i + 1)
        return

    find_subsets([], 0)

    result = 0
    for subset in subsets:
        xor_sum = 0
        for num in subset:
            xor_sum ^= num

        result += xor_sum

    return result


def main():
    nums = [5, 1, 6]
    result = sum_of_all_subsets_xor_totals(nums)
    val = 28
    print("passed:", result == val, "expected", val, "got", result)

    nums = [1, 3]
    result = sum_of_all_subsets_xor_totals(nums)
    val = 6
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
