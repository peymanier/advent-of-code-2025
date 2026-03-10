def search_2d_matrix(matrix: list[list[int]], target: int) -> bool:
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    left = 0
    right = num_rows * num_cols - 1
    while left <= right:
        m = (left + right) // 2
        mid = matrix[m // num_cols][m % num_cols]
        if mid == target:
            return True

        if target < mid:
            right = m - 1
        else:
            left = m + 1

    return False


def search_2d_matrix_alt(matrix: list[list[int]], target: int) -> bool:
    left = 0
    right = len(matrix)

    row_index = None
    while left <= right:
        mid = (left + right) // 2
        low = matrix[mid][0]
        high = matrix[mid][-1]
        if low <= target <= high:
            row_index = mid
            break

        if target < matrix[mid][0]:
            right = mid - 1
        else:
            left = mid + 1

    if not row_index:
        return False

    row = matrix[row_index]
    left = 0
    right = len(row)
    while left <= right:
        mid = (left + right) // 2
        if row[mid] == target:
            return True

        if target < row[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return False


def main():
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 34
    result = search_2d_matrix(matrix, target)
    print("expected", True, end=" ")
    print("got", result)

    result = search_2d_matrix_alt(matrix, target)
    print("expected", True, end=" ")
    print("got", result)

    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 8
    result = search_2d_matrix(matrix, target)
    print("expected", False, end=" ")
    print("got", result)

    result = search_2d_matrix_alt(matrix, target)
    print("expected", False, end=" ")
    print("got", result)


if __name__ == "__main__":
    main()
