import re


def is_invalid_id(num: int):
    num_str = str(num)

    for i in range(1, int(len(num_str) / 2) + 1):
        matches = re.findall(num_str[:i], num_str)
        if "".join(matches) == num_str:
            return True

    return False


def main():
    with open("puzzle.txt", "r") as f:
        puzzle = f.read()

    result = 0
    ranges = puzzle.split(",")
    for r in ranges:
        start, end = r.split("-")
        start = int(start)
        end = int(end)

        for i in range(start, end + 1):
            if is_invalid_id(i):
                result += i

    print(result)


if __name__ == "__main__":
    main()
