def combination_sum(nums: list[int], target: int) -> int:
    result = []

    subset = []

    def dfs(curr_sum: int):
        if curr_sum > target:
            return

        if curr_sum == target:
            result.append(subset.copy())
            return

        for i in range(len(nums)):
            subset.append(nums[i])
            dfs(curr_sum + nums[i])
            subset.pop()

        return

    dfs(0)
    return len(set([tuple(sorted(comb)) for comb in result]))


def main():
    nums = [2, 3, 6, 7]
    target = 7
    result = combination_sum(nums, target)
    val = 2
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
