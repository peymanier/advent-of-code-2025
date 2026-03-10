def baseball_game(ops: list[str]) -> int:
    stack = []
    for op in ops:
        if op == "+":
            stack.append(stack[-1] + stack[-2])
        elif op == "D":
            stack.append(stack[-1] * 2)
        elif op == "C":
            stack.pop()
        elif op.isdigit():
            stack.append(int(op))
        else:
            raise Exception("unexpected op")

    return sum(stack)


def main():
    ops = ["5", "2", "C", "D", "+"]
    expected = 30
    result = baseball_game(ops)
    print("expected", expected, "got", result)


if __name__ == "__main__":
    main()
