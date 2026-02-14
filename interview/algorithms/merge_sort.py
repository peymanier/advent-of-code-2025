def merge_sort(nums: list[int]) -> list[int]:
    if len(nums) < 2:
        return nums

    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)


def merge(first: list[int], second: list[int]) -> list[int]:
    result = []
    i, j = 0, 0
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            result.append(first[i])
            i += 1
        else:
            result.append(second[j])
            j += 1

    if i < len(first):
        result.extend(first[i:])

    if j < len(second):
        result.extend(second[j:])

    return result


def main():
    nums = [8, 2, 8, 1, 3, 9, 5]
    result = merge_sort(nums)
    print(result)


if __name__ == "__main__":
    main()
