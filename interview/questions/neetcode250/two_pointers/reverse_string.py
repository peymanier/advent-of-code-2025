def reverse_string(s: list[str]) -> None:
    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


def reverse_string_alt(s: list[str]) -> list[str]:
    stack = []
    for char in s:
        stack.append(char)

    result = []
    while stack:
        char = stack.pop()
        result.append(char)

    return result


def main():
    s = ["h", "e", "1", "1", "о"]
    reverse_string(s)
    print("expected", ["o", "1", "1", "e", "h"], "got", s)

    s = ["h", "e", "1", "1", "о"]
    result = reverse_string_alt(s)
    print("expected", ["o", "1", "1", "e", "h"], "got", result)


if __name__ == "__main__":
    main()
