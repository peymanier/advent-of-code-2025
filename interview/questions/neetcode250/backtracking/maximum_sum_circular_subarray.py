def maximum_sum_circular_subarray(nums: list[int]) -> int | None:
    result = float("-inf")

    def dfs(start: int, curr: int, curr_sum: int):
        nonlocal result
        result = max(result, curr_sum)

        nxt = (curr + 1) % len(nums)
        if start == nxt:
            return

        dfs(start, nxt, curr_sum + nums[curr])
        return

    for k in range(len(nums)):
        dfs(k, k, 0)

    return result if result != float("-inf") else None


def main():
    nums = [1, -2, 3, -2]
    result = maximum_sum_circular_subarray(nums)
    val = 3
    print("passed:", result == val, "expected", val, "got", result)

    nums = [5, -3, 5]
    result = maximum_sum_circular_subarray(nums)
    val = 10
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
