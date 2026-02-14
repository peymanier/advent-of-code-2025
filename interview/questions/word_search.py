def exist(board: list[list[str]], word: str) -> bool:
    row_nums = len(board)
    col_nums = len(board[0])

    def dfs(i, j, word_i):
        if board[i][j] != word[word_i]:
            return False

        if word_i == len(word) - 1:
            return True

        char = board[i][j]
        # mark it visited by staring it
        board[i][j] = "*"

        delta_rows = [-1, 0, 1, 0]
        delta_cols = [0, 1, 0, -1]
        for k in range(len(delta_rows)):
            r = i + delta_rows[k]
            c = j + delta_cols[k]

            if 0 <= r < row_nums and 0 <= j < col_nums:
                if dfs(r, c, word_i + 1):
                    return True

        # clean up after word match fails for this path
        board[i][j] = char
        return False

    for i in range(row_nums):
        for j in range(col_nums):
            if dfs(i, j, 0):
                return True

    return False


def main():
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]
    word = "ABCCED"
    result = exist(board, word)
    print(result)

    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]
    word = "ABCB"
    result = exist(board, word)
    print(result)


if __name__ == "__main__":
    main()
