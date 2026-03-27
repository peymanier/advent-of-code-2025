class MyQueue:
    def __init__(self):
        self.stack = []

    def push(self, val) -> None:
        return self.stack.append(val)

    def pop(self) -> int:
        stack = []
        for _ in range(len(self.stack)):
            stack.append(self.stack.pop())

        result = stack.pop()

        for _ in range(len(stack)):
            self.stack.append(stack.pop())

        return result

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0


def main():
    q = MyQueue()
    q.push(1)
    q.push(2)
    q.push(3)

    result = q.empty()
    val = False
    print("passed:", result == val, "expected", val, "got", result)

    result = q.peek()
    val = 1
    print("passed:", result == val, "expected", val, "got", result)

    result = q.pop()
    val = 1
    print("passed:", result == val, "expected", val, "got", result)

    result = q.pop()
    val = 2
    print("passed:", result == val, "expected", val, "got", result)

    result = q.pop()
    val = 3
    print("passed:", result == val, "expected", val, "got", result)

    result = q.empty()
    val = True
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
