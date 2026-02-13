# reddit
import functools


def main():
    with open("puzzle.txt", "r") as f:
        puzzle = [line.strip() for line in f.readlines()]

    row_len = len(puzzle)
    col_len = len(puzzle[0])

    @functools.cache
    def count_route(i, j) -> int:
        if i == row_len:
            return 1

        if puzzle[i][j] == "^":
            left_count = 0
            if j - 1 >= 0:
                left_count = count_route(i, j - 1)

            right_count = 0
            if j + 1 < col_len:
                right_count = count_route(i, j + 1)

            return left_count + right_count

        return count_route(i + 1, j)

    result = count_route(0, puzzle[0].find("S"))
    print(result)


if __name__ == "__main__":
    main()
