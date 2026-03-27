# class MyQueue:
#     def __init__(self):
#         self.stack = []
#
#     def push(self, val) -> None:
#         return self.stack.append(val)
#
#     def pop(self) -> int:
#         stack = []
#         for _ in range(len(self.stack)):
#             stack.append(self.stack.pop())
#
#         result = stack.pop()
#
#         for _ in range(len(stack)):
#             self.stack.append(stack.pop())
#
#         return result
#
#     def peek(self) -> int:
#         return self.stack[0]
#
#     def empty(self) -> bool:
#         return len(self.stack) == 0


class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, val) -> None:
        return self.stack1.append(val)

    def pop(self) -> int:
        for _ in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    def peek(self) -> int:
        for _ in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())

        result = self.stack2.pop()
        self.stack2.append(result)
        return result

    def empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0


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

    result = q.empty()
    val = False
    print("passed:", result == val, "expected", val, "got", result)

    q.push(10)
    q.push(11)

    result = q.peek()
    val = 10
    print("passed:", result == val, "expected", val, "got", result)

    result = q.pop()
    val = 10
    print("passed:", result == val, "expected", val, "got", result)

    result = q.pop()
    val = 11
    print("passed:", result == val, "expected", val, "got", result)

    result = q.pop()
    val = 3
    print("passed:", result == val, "expected", val, "got", result)

    result = q.empty()
    val = True
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
