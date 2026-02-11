def main():
    with open("puzzle.txt", "r") as f:
        puzzle = [list(line.strip()) for line in f.readlines()]

    row_len = len(puzzle)
    col_len = len(puzzle[0])

    count = 0
    for i in range(row_len):
        for j in range(col_len):
            if i - 1 >= 0 and puzzle[i - 1][j] in ("S", "|"):
                if puzzle[i][j] == "^":
                    if j - 1 >= 0:
                        puzzle[i][j - 1] = "|"

                    if j + 1 < col_len:
                        puzzle[i][j + 1] = "|"

                    count += 1
                else:
                    puzzle[i][j] = "|"

    for line in puzzle:
        print("".join(line))

    print(count)


if __name__ == "__main__":
    main()
