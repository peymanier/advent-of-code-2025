def combination_sum_not_distinct(nums: list[int], target: int) -> int:
    result = []

    curr = []

    def dfs(i: int, curr_sum: int):
        if curr_sum == target:
            result.append(curr.copy())
            return

        if i >= len(nums) or curr_sum > target:
            return

        curr.append(nums[i])
        dfs(i + 1, curr_sum + nums[i])
        curr.pop()
        dfs(i + 1, curr_sum)

        return

    dfs(0, 0)
    result = set([tuple(sorted(comb)) for comb in result])
    print(result)
    return len(result)


def main():
    nums = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    result = combination_sum_not_distinct(nums, target)
    val = 4
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
