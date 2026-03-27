def generate_parentheses(n: int) -> list[str]:
    result = []

    def generate(s: str, open_count: int, close_count: int):
        if open_count > n:
            return

        if open_count - close_count < 0:
            return

        if open_count == n and close_count == n:
            result.append(s)
            return

        generate(s + ")", open_count, close_count + 1)
        generate(s + "(", open_count + 1, close_count)
        return

    generate("(", 1, 0)
    return result


def deep_cmp(l1: list[str], l2: list[str]):
    return sorted(l1) == sorted(l2)


def main():
    n = 3
    result = generate_parentheses(n)
    val = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    print("passed:", deep_cmp(result, val), "expected", val, "got", result)

    n = 1
    result = generate_parentheses(n)
    val = ["()"]
    print("passed:", result == val, "expected", val, "got", result)

    n = 5
    result = generate_parentheses(n)
    print(result)


if __name__ == "__main__":
    main()
