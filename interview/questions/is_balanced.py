def is_balanced(string: str) -> bool:
    stack = []
    for ch in string:
        if ch == "(":
            stack.append(ch)
        elif ch == ")":
            try:
                stack.pop()
            except IndexError:
                return False
        else:
            raise ValueError("invalid string")

    if stack:
        return False

    return True


def main():
    string = "(()(()))"
    print(is_balanced(string))

    string = "((()(()))"
    print(is_balanced(string))

    string = "("
    print(is_balanced(string))

    string = "())"
    print(is_balanced(string))


if __name__ == "__main__":
    main()
