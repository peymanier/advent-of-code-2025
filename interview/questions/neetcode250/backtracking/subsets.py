from interview.questions.neetcode250.two_pointers.three_sum import deep_nested_cmp


def subsets(nums: list[int]) -> list[list[int]]:
    result = []

    def dfs(sub, i):
        if i == len(nums):
            result.append(sub)
            return

        dfs([*sub, nums[i]], i + 1)
        dfs(sub, i + 1)
        return

    dfs([], 0)
    return result


def subsets2(nums: list[int]) -> list[list[int]]:
    result = []

    subset = []

    def dfs(i):
        if i >= len(nums):
            result.append(subset.copy())
            return

        subset.append(nums[i])
        dfs(i + 1)

        subset.pop()
        dfs(i + 1)

        return

    dfs(0)
    return result


def main():
    nums = [1, 2, 3]
    result = subsets(nums)
    val = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    print("passed:", deep_nested_cmp(result, val), "expected", val, "got", result)

    nums = [1, 2, 3]
    result = subsets2(nums)
    val = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    print("passed:", deep_nested_cmp(result, val), "expected", val, "got", result)


if __name__ == "__main__":
    main()
