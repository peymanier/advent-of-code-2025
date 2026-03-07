# Binary Search
def find_minimum_in_rotated_sorted_array(arr: list[int]) -> int:
    left, right = 0, len(arr) - 1

    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= arr[-1]:
            right = mid - 1
            result = mid
        else:
            left = mid + 1

    return result


def main():
    arr = [30, 40, 50, 10, 20]
    result = find_minimum_in_rotated_sorted_array(arr)
    print(result)

    arr = [3, 5, 7, 11, 13, 17, 19, 2]
    result = find_minimum_in_rotated_sorted_array(arr)
    print(result)

    arr = [20, 2, 3, 5, 7, 11, 13, 17, 19]
    result = find_minimum_in_rotated_sorted_array(arr)
    print(result)


if __name__ == "__main__":
    main()
