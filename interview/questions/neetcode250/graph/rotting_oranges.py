from collections import deque


def rotting_oranges(grid: list[list[int]]) -> int:
    num_rows = len(grid)
    num_cols = len(grid[0])

    fresh_count = 0
    rotten = []
    for i in range(num_rows):
        for j in range(num_cols):
            if grid[i][j] == 1:
                fresh_count += 1

            elif grid[i][j] == 2:
                rotten.append((i, j))

    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    minutes = 0
    que = deque(rotten)
    while que and fresh_count > 0:
        n = len(que)
        for _ in range(n):
            r, c = que.popleft()

            for dr, dc in directions:
                i, j = r + dr, c + dc
                if (
                    not (0 <= i < num_rows)
                    or not (0 <= j < num_cols)
                    or grid[i][j] != 1
                ):
                    continue

                grid[i][j] = 2
                fresh_count -= 1
                que.append((i, j))

        minutes += 1

    return minutes if fresh_count == 0 else -1


def main():
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    result = rotting_oranges(grid)
    val = 4
    print("passed:", result == val, "expected", val, "got", result)

    grid = [[2, 0, 1], [0, 1, 0], [0, 1, 1]]
    result = rotting_oranges(grid)
    val = -1
    print("passed:", result == val, "expected", val, "got", result)

    grid = [[2, 0, 0, 2], [1, 1, 1, 1], [0, 0, 1, 1], [0, 0, 0, 0]]
    result = rotting_oranges(grid)
    val = 3
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
