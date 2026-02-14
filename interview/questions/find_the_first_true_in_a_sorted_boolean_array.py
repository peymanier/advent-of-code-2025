def find_boundary(arr: list[bool]) -> int:
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid]:
            right = mid - 1
            result = mid
        else:
            left = mid + 1

    return result


def main():
    arr = [False, False, False, False, True, True]
    result = find_boundary(arr)
    print(result)

    arr = [False, False, True, True, True, True, True]
    result = find_boundary(arr)
    print(result)


if __name__ == "__main__":
    main()
