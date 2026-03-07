# Backtracking
def word_search(board: list[list[str]], word: str) -> bool:
    num_rows = len(board)
    num_cols = len(board[0])

    def get_neighbors(coord):
        result = []

        delta_row = [-1, 0, 1, 0]
        delta_col = [0, 1, 0, -1]
        for k in range(len(delta_row)):
            r = coord[0] + delta_row[k]
            c = coord[1] + delta_col[k]

            if 0 <= r < num_rows and 0 <= c < num_cols:
                result.append((r, c))

        return result

    def dfs(coord, i):
        r, c = coord
        if board[r][c] != word[i]:
            return False

        if i == len(word) - 1:
            return True

        char = board[r][c]
        # mark it visited by starring it
        board[r][c] = "*"

        for neighbor in get_neighbors(coord):
            if dfs(neighbor, i + 1):
                return True

        # backtrack if it is a wrong path
        board[r][c] = char
        return False

    for i in range(num_rows):
        for j in range(num_cols):
            if dfs((i, j), 0):
                return True

    return False


def main():
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]
    word = "ABCCED"
    result = word_search(board, word)
    print(result)

    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]
    word = "ABCB"
    result = word_search(board, word)
    print(result)


if __name__ == "__main__":
    main()
