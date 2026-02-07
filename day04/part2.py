def has_fewer_than_4_adjacent(puzzle: list[list[str]], i: int, j: int) -> bool:
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

            if adj == "@" or adj == "x":
                counter += 1

            if counter >= 4:
                return False

    return True


def mark_removals_and_has_any_removal(puzzle: list[list[str]]) -> bool:
    rows = len(puzzle)
    cols = len(puzzle[0])

    has_removals = False
    for i in range(rows):
        for j in range(cols):
            if puzzle[i][j] == "@" and has_fewer_than_4_adjacent(puzzle, i, j):
                puzzle[i][j] = "x"
                has_removals = True

    return has_removals


def clean_up_mark_removals(puzzle: list[list[str]]):
    rows = len(puzzle)
    cols = len(puzzle[0])

    counter = 0
    for i in range(rows):
        for j in range(cols):
            if puzzle[i][j] == "x":
                puzzle[i][j] = "."
                counter += 1

    return puzzle, counter


def main():
    with open("puzzle.txt", "r") as f:
        puzzle = f.readlines()
        puzzle = [list(line.strip()) for line in puzzle]

    result = 0
    while mark_removals_and_has_any_removal(puzzle):
        puzzle, count = clean_up_mark_removals(puzzle)
        result += count

    print(result)


if __name__ == "__main__":
    main()
