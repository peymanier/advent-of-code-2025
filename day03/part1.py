def find_largest_num(nums: str):
    combinations = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            combinations.append(int(nums[i] + nums[j]))

    return max(combinations)


def main():
    with open("test_puzzle.txt", "r") as f:
        puzzle = f.readlines()

    result = 0
    for nums in puzzle:
        largest = find_largest_num(nums)
        print(largest)
        result += largest

    print(result)


if __name__ == "__main__":
    main()
