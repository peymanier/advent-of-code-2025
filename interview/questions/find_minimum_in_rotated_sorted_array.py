def find_minimum_in_rotated_sorted_array(arr: list[int]) -> int:
    left, right = 0, len(arr) - 1

    while left <= right:
        if arr[left] <= arr[right]:
            return left

        mid = (left + right) // 2
        if arr[mid] >= arr[left]:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def main():
    arr = [30, 40, 50, 10, 20]
    result = find_minimum_in_rotated_sorted_array(arr)
    print(result)

    arr = [3, 5, 7, 11, 13, 17, 19, 2]
    result = find_minimum_in_rotated_sorted_array(arr)
    print(result)

    arr = [2, 3, 5, 7, 11, 13, 17, 19]
    result = find_minimum_in_rotated_sorted_array(arr)
    print(result)


if __name__ == "__main__":
    main()
