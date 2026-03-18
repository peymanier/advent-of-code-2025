def find_town_judge(n: int, trust: list[list[int]]) -> int:
    incoming = {}
    outgoing = {}
    for a, b in trust:
        outgoing[a] = incoming.get(a, 0) + 1
        incoming[b] = incoming.get(b, 0) + 1

    for i in range(1, n + 1):
        if outgoing.get(i, 0) == 0 and incoming.get(i, 0) == n - 1:
            return i

    return -1


def main():
    n = 3
    trust = [[1, 3], [2, 3]]
    result = find_town_judge(n, trust)
    val = 3
    print("passed:", result == val, "expected", val, "got", result)

    n = 2
    trust = [[1, 2]]
    result = find_town_judge(n, trust)
    val = 2
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
