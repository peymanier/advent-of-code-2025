# def evaluate_reverse_polish_notation(tokens: list[str]) -> int:
#     def evaluate():
#         curr = tokens.pop()
#         if curr.isdigit():
#             return int(curr)
#
#         elif curr == "*":
#             op1 = evaluate()
#             op2 = evaluate()
#             return op2 * op1
#
#         elif curr == "/":
#             op1 = evaluate()
#             op2 = evaluate()
#             return int(op2 / op1)
#
#         elif curr == "+":
#             op1 = evaluate()
#             op2 = evaluate()
#             return op2 + op1
#
#         elif curr == "-":
#             op1 = evaluate()
#             op2 = evaluate()
#             return op2 - op1
#
#         else:
#             raise ValueError
#
#     return evaluate()


def evaluate_reverse_polish_notation(tokens: list[str]) -> int:
    stack = []
    for curr in tokens:
        if curr.isdigit():
            stack.append(int(curr))
        elif curr == "*":
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(op2 * op1)
        elif curr == "/":
            op1 = stack.pop()
            op2 = stack.pop()
            # int goes toward zero even for negative number unlike //
            stack.append(int(op2 / op1))
        elif curr == "+":
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(op2 + op1)
        elif curr == "-":
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(op2 - op1)
        else:
            raise ValueError

    return stack.pop()


def main():
    tokens = ["2", "1", "+", "3", "*"]
    result = evaluate_reverse_polish_notation(tokens)
    val = 9
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
