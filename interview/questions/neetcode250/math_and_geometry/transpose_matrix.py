def transpose_matrix(matrix: list[list[int]]) -> list[list[int]]:
    row_len = len(matrix)
    col_len = len(matrix[0])

    result = [[None for _ in range(row_len)] for _ in range(col_len)]
    for r in range(row_len):
        for c in range(col_len):
            result[c][r] = matrix[r][c]

    return result


def main():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = transpose_matrix(matrix)
    val = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    print("passed:", result == val, "expected", val, "got", result)

    matrix = [[1, 2, 3], [4, 5, 6]]
    result = transpose_matrix(matrix)
    val = [[1, 4], [2, 5], [3, 6]]
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
