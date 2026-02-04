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
            first_half = str(i)[: int(len(str(i)) / 2)]
            second_half = str(i)[int(len(str(i)) / 2) :]

            if len(str(i)) % 2 == 0 and first_half == second_half:
                result += i

    print(result)


if __name__ == "__main__":
    main()
