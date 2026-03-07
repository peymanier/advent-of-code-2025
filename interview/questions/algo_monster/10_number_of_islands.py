# DFS on Grids
def count_number_of_islands(grid: list[list[int]]) -> int:
    num_rows = len(grid)
    num_cols = len(grid[0])

    def get_neighbours(coord):
        result = []
        row, col = coord

        delta_row = [-1, 0, 1, 0]
        delta_col = [0, -1, 0, 1]
        for i in range(len(delta_row)):
            r = row + delta_row[i]
            c = col + delta_col[i]

            if 0 <= r < num_rows and 0 <= c < num_cols:
                result.append((r, c))

        return result

    def dfs(coord):
        r, c = coord
        if grid[r][c] == 0:
            return

        # we mark it visited by sinking it
        grid[r][c] = 0

        for neighbour in get_neighbours(coord):
            nr, nc = neighbour
            if grid[nr][nc] == 1:
                dfs(neighbour)

    count = 0
    for r in range(num_rows):
        for c in range(num_cols):
            if grid[r][c] == 1:
                dfs((r, c))
                count += 1

    return count



def main():
    grid = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1],
    ]
    result = count_number_of_islands(grid)
    print(result)

    grid = [
        [1, 1, 1, 1, 0],
        [1, 1, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    result = count_number_of_islands(grid)
    print(result)


if __name__ == "__main__":
    main()
