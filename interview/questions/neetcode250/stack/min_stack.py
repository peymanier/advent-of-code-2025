class MinStackNode:
    def __init__(self, val, current_min):
        self.val = val
        self.minimum = min(val, current_min if current_min else float("inf"))

    def __repr__(self):
        return f"{self.val=} {self.minimum=}"


class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        node = MinStackNode(val, self.get_min())
        self.stack.append(node)

    def pop(self):
        self.stack.pop()

    def top(self) -> MinStackNode | None:
        if not self.stack:
            return None

        return self.stack[-1]

    def get_min(self) -> int | None:
        top = self.top()
        if not top:
            return None

        return top.minimum


class MinStackAlt:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack:
            current_min = val
        else:
            current_min = min(self.min_stack[-1], val)

        self.min_stack.append(current_min)

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int | None:
        if not self.stack:
            return None

        return self.stack[-1]

    def get_min(self) -> int | None:
        if not self.min_stack:
            return None

        return self.min_stack[-1]


def main():
    # min_stack = MinStack()
    min_stack = MinStackAlt()

    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)

    result = min_stack.get_min()
    print("expected", -3, "got", result)

    min_stack.pop()

    result = min_stack.top()
    print("expected", 0, "got", result)

    result = min_stack.get_min()
    print("expected", -2, "got", result)


if __name__ == "__main__":
    main()
