def main():
    with open("puzzle.txt", "r") as f:
        puzzle = f.readlines()

    result = 0
    pointer = 50
    for line in puzzle:
        direction = line[0]
        distance = int(line[1:])

        if direction == "L":
            distance *= -1

        while distance:
            if distance > 0:
                distance -= 1
                pointer += 1
                pointer %= 100
            else:
                distance += 1
                pointer -= 1
                pointer %= 100

            if pointer == 0:
                result += 1

    print(result)


if __name__ == "__main__":
    main()
