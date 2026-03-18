from collections import deque


def island_perimeter(grid: list[list[int]]) -> int:
    num_rows = len(grid)
    num_cols = len(grid[0])

    def get_neighbors(coord: tuple[int, int]):
        delta_row = [0, 1, 0, -1]
        delta_cols = [1, 0, -1, 0]

        result = []
        for i in range(len(delta_row)):
            r = coord[0] + delta_row[i]
            c = coord[1] + delta_cols[i]

            if 0 <= r < num_rows and 0 <= c < num_cols:
                result.append((r, c))

        return result

    def calc_perimeter(coord):
        score = 4
        for nei in get_neighbors(coord):
            if grid[nei[0]][nei[1]] == 1:
                score -= 1

        return score

    visited = [[False for _ in range(num_cols)] for _ in range(num_rows)]
    result = 0

    def dfs(coord: tuple[int, int]):
        i, j = coord
        if visited[i][j] or grid[i][j] == 0:
            return

        nonlocal result
        result += calc_perimeter(coord)

        visited[i][j] = True

        for nei in get_neighbors(coord):
            if grid[nei[0]][nei[1]] == 1:
                dfs(nei)

        return

    for i in range(num_rows):
        for j in range(num_cols):
            if grid[i][j] == 1:
                dfs((i, j))
                break
        else:
            continue

        break

    return result


def main():
    grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    result = island_perimeter(grid)
    val = 16
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
