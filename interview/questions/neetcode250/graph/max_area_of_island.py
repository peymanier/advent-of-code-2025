def max_area_of_island(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    def get_neighbors(coord):
        delta_rows = [-1, 0, 1, 0]
        delta_cols = [0, 1, 0, -1]

        res = []
        for i in range(len(delta_rows)):
            r = coord[0] + delta_rows[i]
            c = coord[1] + delta_cols[i]

            if 0 <= r < num_rows and 0 <= c < num_cols:
                res.append((r, c))

        return res

    result = 0
    area = 0

    def dfs(coord):
        i, j = coord
        if matrix[i][j] == 0:
            return

        nonlocal area
        area += 1
        matrix[i][j] = 0

        for nei in get_neighbors(coord):
            if matrix[nei[0]][nei[1]] == 1:
                dfs(nei)

        return

    for i in range(num_rows):
        for j in range(num_cols):
            if matrix[i][j] == 1:
                area = 0
                dfs((i, j))
                result = max(result, area)

    return result


def main():
    matrix = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ]
    result = max_area_of_island(matrix)
    val = 6
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
