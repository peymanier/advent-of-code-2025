import functools
from itertools import zip_longest


def is_column_empty(col: tuple[str]) -> bool:
    for ch in col:
        if ch != " ":
            return False

    return True


def calculate_column_group_result(numbers: list[int], operator: str) -> int:
    result = 0

    if operator == "+":
        result += sum(numbers)
    elif operator == "*":
        result += functools.reduce(lambda x, y: x * y, numbers, 1)
    else:
        raise Exception("not supported")

    return result


def main():
    with open("puzzle.txt", "r") as f:
        puzzle = [line.rstrip("\n") for line in f.readlines()]

    rows = []
    for line in puzzle:
        rows.append(list(line))

    result = 0
    numbers = []
    operator = None
    for col in zip_longest(*rows, fillvalue=" "):
        if operator is None:
            operator = col[-1]

        if is_column_empty(col):
            result += calculate_column_group_result(numbers, operator)
            numbers = []
            operator = None
            continue

        num_characters = col[:-1]
        number = "".join(num_characters)
        numbers.append(int(number))

    if numbers and operator:
        result += calculate_column_group_result(numbers, operator)

    print(result)


if __name__ == "__main__":
    main()
