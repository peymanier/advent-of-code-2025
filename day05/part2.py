# reddit
from collections import deque


def main():
    with open("puzzle.txt", "r") as f:
        puzzle = [line.rstrip("\n") for line in f.readlines()]

    ranges = []
    for line in puzzle:
        if line == "":
            break

        start, end = line.split("-")
        rng = (int(start), int(end))
        ranges.append(rng)

    ranges.sort()

    que_ranges = deque(ranges)
    que_merged = deque()

    while True:
        if len(que_ranges) == 1:
            que_merged.append(que_ranges.popleft())
            break

        a_min, a_max = que_ranges.popleft()
        b_min, b_max = que_ranges.popleft()

        if b_min > a_max:
            que_merged.appendleft((a_min, a_max))
            que_ranges.appendleft((b_min, b_max))
        else:
            que_ranges.appendleft((a_min, max(a_max, b_max)))

    result = 0
    for rng in que_merged:
        start, end = rng
        result += end - start + 1

    print(result)


if __name__ == "__main__":
    main()
