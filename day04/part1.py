def has_fewer_than_4_adjacent(puzzle: list[str], i: int, j: int) -> bool:
    rows = len(puzzle)
    cols = len(puzzle[0])

    counter = 0
    for m in [-1, 0, 1]:
        for n in [-1, 0, 1]:
            if m == 0 and n == 0:
                continue

            if i + m < 0 or j + n < 0 or i + m >= rows or j + n >= cols:
                continue

            adj = puzzle[i + m][j + n]

            if adj == "@":
                counter += 1

            if counter >= 4:
                return False

    return True


def main():
    with open("puzzle.txt", "r") as f:
        puzzle = f.readlines()
        puzzle = [line.strip() for line in puzzle]

    rows = len(puzzle)
    cols = len(puzzle[0])

    result = 0
    for i in range(rows):
        for j in range(cols):
            if puzzle[i][j] == "@" and has_fewer_than_4_adjacent(puzzle, i, j):
                result += 1

    print(result)


if __name__ == "__main__":
    main()
