import functools


def main():
    with open("puzzle.txt", "r") as f:
        puzzle = f.readlines()

    rows = []
    for line in puzzle:
        row = line.split()
        rows.append(row)

    result = 0
    for col in zip(*rows):
        operator = col[-1]
        numbers = col[:-1]
        if operator == "+":
            result += sum([int(n) for n in numbers])
        elif operator == "*":
            result += functools.reduce(lambda x, y: int(x) * int(y), numbers, 1)
        else:
            raise Exception("not supported")

    print(result)


if __name__ == "__main__":
    main()
