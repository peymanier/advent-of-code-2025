def valid_parentheses(s: str) -> bool:
    close_to_open = {")": "(", "}": "{", "]": "["}
    stack = []
    for char in s:
        if char in close_to_open.values():
            stack.append(char)
            continue

        popped = stack.pop()
        if popped != close_to_open[char]:
            return False

    return not stack


def main():
    s = "()"
    expected = True
    result = valid_parentheses(s)
    print("expected", expected, "got", result)

    s = "(){}[]"
    expected = True
    result = valid_parentheses(s)
    print("expected", expected, "got", result)

    s = "({[]})"
    expected = True
    result = valid_parentheses(s)
    print("expected", expected, "got", result)

    s = "({[])"
    expected = False
    result = valid_parentheses(s)
    print("expected", expected, "got", result)

    s = "({["
    expected = False
    result = valid_parentheses(s)
    print("expected", expected, "got", result)


if __name__ == "__main__":
    main()
