from collections import deque


class MyStack:
    def __init__(self):
        self.que = deque()

    def push(self, val) -> None:
        return self.que.append(val)

    def pop(self) -> int:
        return self.que.pop()

    def top(self) -> int:
        return self.que[-1]

    def empty(self) -> bool:
        return len(self.que) == 0


def main():
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    result = stack.empty()
    val = False
    print("passed:", result == val, "expected", val, "got", result)

    result = stack.top()
    val = 3
    print("passed:", result == val, "expected", val, "got", result)

    result = stack.pop()
    val = 3
    print("passed:", result == val, "expected", val, "got", result)

    result = stack.pop()
    val = 2
    print("passed:", result == val, "expected", val, "got", result)

    result = stack.pop()
    val = 1
    print("passed:", result == val, "expected", val, "got", result)

    result = stack.empty()
    val = True
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
