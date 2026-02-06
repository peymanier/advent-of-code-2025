def has_bigger_after(num: int, nums_after: list[int]) -> bool:
    for n in nums_after:
        if n > num:
            return True

    return False


def find_largest_num(nums: str):
    nums = nums.strip()
    nums = [int(n) for n in nums]

    index, largest_left = max(enumerate(nums[: len(nums) - 11]), key=lambda x: x[1])

    result = [largest_left]
    deletable_count = (len(nums) - 1 - index) - 11

    curr = index + 1
    while deletable_count > 0 and curr < len(nums) and len(result) < 12:
        if has_bigger_after(nums[curr], nums[curr + 1 : curr + 1 + deletable_count]):
            deletable_count -= 1
            curr += 1
            continue

        result.append(nums[curr])
        curr += 1

    if len(result) < 12 and curr < len(nums):
        result = [*result, *nums[curr:]][:12]

    return int("".join([str(n) for n in result]))


def main():
    with open("puzzle.txt", "r") as f:
        puzzle = f.readlines()

    result = 0
    for nums in puzzle:
        largest = find_largest_num(nums)
        result += largest

    print(result)


if __name__ == "__main__":
    main()
