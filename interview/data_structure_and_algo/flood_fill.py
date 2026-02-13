from collections import deque


def flood_fill(
    r: int, c: int, replacement: int, image: list[list[int]]
) -> list[list[int]]:
    num_rows, num_cols = len(image), len(image[0])

    def get_neighbours(coord, color):
        row, col = coord

        delta_row = [-1, 0, 1, 0]
        delta_col = [0, 1, 0, -1]
        for i in range(len(delta_row)):
            neighbour_row = row + delta_row[i]
            neighbour_col = col + delta_col[i]

            if 0 <= neighbour_row < num_rows and 0 <= neighbour_col < num_cols:
                if image[neighbour_row][neighbour_col] == color:
                    yield neighbour_row, neighbour_col

    def bfs(root):
        queue = deque([root])
        visited = [[False for _ in range(num_cols)] for _ in range(num_rows)]

        i, j = root
        color = image[i][j]
        image[i][j] = replacement
        visited[i][j] = True
        while queue:
            node = queue.popleft()
            for neighbour in get_neighbours(node, color):
                i, j = neighbour
                if visited[i][j]:
                    continue

                image[i][j] = replacement
                queue.append(neighbour)
                visited[i][j] = True

    bfs((r, c))
    return image


def main():
    image = [
        [0, 1, 3, 4, 1],
        [3, 8, 8, 3, 3],
        [6, 7, 8, 8, 3],
        [12, 2, 8, 9, 1],
        [12, 3, 1, 3, 2],
    ]
    result = flood_fill(2, 2, 9, image)
    for row in result:
        print(row)


if __name__ == "__main__":
    main()
