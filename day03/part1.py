def find_largest_num(nums: str):
    combinations = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            combinations.append(int(nums[i] + nums[j]))

    return max(combinations)


def find_largest_num2(nums: str):
    nums = [int(n) for n in nums.strip()]

    index, largest_left = max(enumerate(nums[: len(nums) - 1]), key=lambda x: x[1])
    largest_right = max(nums[index + 1 :])
    return int(str(largest_left) + str(largest_right))


def main():
    with open("puzzle.txt", "r") as f:
        puzzle = f.readlines()

    result = 0
    for nums in puzzle:
        largest = find_largest_num2(nums)
        print(largest)
        result += largest

    print(result)


if __name__ == "__main__":
    main()
