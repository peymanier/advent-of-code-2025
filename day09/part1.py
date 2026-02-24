import itertools


def calculate_distance(point1, point2):
    return (abs(point2[0] - point1[0]) + 1) * (abs(point2[1] - point1[1]) + 1)


def main():
    with open("puzzle.txt", "r") as f:
        puzzle = [line.strip() for line in f.readlines()]

    points = []
    for line in puzzle:
        col, row = line.split(",")
        col, row = int(col), int(row)
        points.append((row, col))

    distances = []
    for point1, point2 in itertools.combinations(points, 2):
        if point1 == point2:
            continue

        distance = calculate_distance(point1, point2)
        distances.append(distance)

    print(max(distances))


if __name__ == "__main__":
    main()
